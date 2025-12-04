from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, ClientProfile, ProfessionalProfile, TrainingProfile

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.CharField(write_only=True)  # Frontend se role aayega

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        
        # 1. User Create karo
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        # 2. UserProfile update karo (Signal se already ban chuka hoga)
        # Hum bas Role update kar rahe hain
        if hasattr(user, 'profile'):
            profile = user.profile
            profile.role = role
            profile.save()

        # 3. Role ke hisaab se Specific Profile banao (Empty for now)
        if role == 'client':
            ClientProfile.objects.create(user=user)
        
        elif role in ['professional', 'freelancer']:
            # Professional aur Freelancer dono ke liye ProfessionalProfile use karenge
            # Freelancers ke liye hum baad mein 'is_agency=False' set kar sakte hain
            is_agency = True if role == 'professional' else False
            ProfessionalProfile.objects.create(user=user, is_agency=is_agency)
            
        elif role == 'trainer':
            TrainingProfile.objects.create(user=user)
        
        return user