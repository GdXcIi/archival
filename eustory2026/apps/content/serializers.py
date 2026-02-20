from rest_framework import serializers
from .models import ContentBlock, Source

class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = '__all__'
    
    def validate(self, data):
        if data["content_type"] == "image":
            if not self.instance or not self.instance.source.exists():
                raise serializers.ValidationError(
                    "Une image doit obligatoirement avoir une source."
                )
    
class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'