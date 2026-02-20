from rest_framework import serializers
from .models import SubTheme, Section

class SubThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTheme
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'