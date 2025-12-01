from rest_framework import serializers
from .models import CareersPage, Benefit, JobOpening, JobApplication

class CareersPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareersPage
        fields = '__all__'

class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'

class JobOpeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobOpening
        fields = '__all__'

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'