# leads/views.py

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from theme.models import ChatbotFlowStep
from .models import Lead, NewsletterSubscriber
from .serializers import LeadSerializer, NewsletterSubscriberSerializer

# --- 1. Lead ViewSet ---
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all().order_by("-created_at")
    serializer_class = LeadSerializer

# --- 2. Newsletter Subscriber ViewSet ---
class NewsletterSubscriberViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscriber.objects.all().order_by('-subscribed_at')
    serializer_class = NewsletterSubscriberSerializer

# --- 3. CHATBOT FLOW HANDLER (UPDATED) ---
@api_view(['POST'])
def chat_flow_handler(request):
    """
    Handles the sequential, CMS-configured chatbot flow.
    Saves answers in session, validates required fields, and generates a Lead at the end.
    """
    try:
        # Request se data nikalo
        current_field = request.data.get('current_field') # Jo sawal abhi poocha gaya tha (e.g., 'name')
        answer = request.data.get('answer')
        
        # Session se purana data nikalo (taaki conversation yaad rahe)
        flow_data = request.session.get('chatbot_flow_data', {})

        # --- STEP 1: VALIDATION (New Feature) ---
        # Check karo ki kya yeh field "Required" hai?
        if current_field:
            current_step_obj = ChatbotFlowStep.objects.filter(field_to_save=current_field).first()
            
            # Agar step required hai aur answer khali hai, to wahi sawal wapis bhejo
            if current_step_obj and current_step_obj.is_required and not answer:
                return Response({
                    "next_question": current_step_obj.question_text, # Same question repeat
                    "next_field": current_field,
                    "is_complete": False,
                    "error": "This field is required. Please provide an answer." # Frontend isse dikha sakta hai
                })

        # --- STEP 2: SAVE ANSWER ---
        if current_field and answer:
            flow_data[current_field] = answer
            request.session['chatbot_flow_data'] = flow_data # Session update karo
            
        # --- STEP 3: DETERMINE NEXT STEP ---
        last_order = 0
        if current_field:
            # Abhi jo field answer hua, uska order nikalo
            last_step = ChatbotFlowStep.objects.filter(field_to_save=current_field).first()
            if last_step:
                last_order = last_step.step_order
        
        # Us order ke baad wala agla step dhundo
        next_step = ChatbotFlowStep.objects.filter(step_order__gt=last_order).order_by('step_order').first()

        # --- STEP 4: RESPONSE OR LEAD GENERATION ---
        if next_step:
            # Agar agla sawal hai, to wo bhejo
            response_data = {
                "next_question": next_step.question_text,
                "next_field": next_step.field_to_save,
                "is_complete": False
            }
        else:
            # Agar koi sawal nahi bacha, iska matlab chat complete ho gayi
            
            # Session se sara data lekar Lead banao
            lead_name = flow_data.get('name', 'Unknown Chatbot Lead')
            lead_email = flow_data.get('email', '') # Email blank ho sakta hai agar nahi poocha
            
            Lead.objects.create(
                name=lead_name,
                email=lead_email,
                phone=flow_data.get('phone', ''),
                service=flow_data.get('service', 'General Inquiry'),
                message=flow_data.get('message', 'Flow completed successfully via Chatbot.'),
                source="chatbot"
            )
            
            # Session clear kar do taaki agli chat fresh start ho
            if 'chatbot_flow_data' in request.session:
                del request.session['chatbot_flow_data']
            
            response_data = {
                "next_question": f"Thank you, {lead_name}! We have received your details and will contact you shortly.",
                "next_field": None,
                "is_complete": True,
                "action": "lead_captured"
            }
        
        return Response(response_data)
        
    except Exception as e:
        # Agar koi error aaye to log karo aur chat restart karne ka option do
        print(f"Chatbot Flow Error: {e}")
        
        # Error hone par session clear kar do
        if 'chatbot_flow_data' in request.session:
            del request.session['chatbot_flow_data']
        
        # Pehla sawal wapis dhundo restart ke liye
        first_step = ChatbotFlowStep.objects.order_by('step_order').first()
        
        return Response({
            "error": "System encountered an error. Restarting chat...",
            "next_question": first_step.question_text if first_step else "Welcome to XpertAI. How can I help?",
            "next_field": first_step.field_to_save if first_step else "name",
            "is_complete": False
        })