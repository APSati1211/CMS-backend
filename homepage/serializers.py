from rest_framework import serializers
from .models import HeroSection, Stat, Feature, BottomCTA

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = '__all__'

class BottomCTASerializer(serializers.ModelSerializer):
    class Meta:
        model = BottomCTA
        fields = '__all__'