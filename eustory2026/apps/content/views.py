from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import ContentBlock, Source
from .serializers import ContentBlockSerializer, SourceSerializer

# Create your views here.
class ContentBlockViewSet(ModelViewSet):
    serializer_class = ContentBlockSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        section_id = self.request.query_params.get('section')
        queryset = ContentBlock.objects.all()

        if section_id:
            queryset = queryset.filter(section_id=section_id)
        
        return queryset
    
    def perform_create(self, serializer):
        # Automatically set the author to the current user
        serializer.save(author=self.request.user)

class SourceViewSet(ModelViewSet):
    serializer_class = SourceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        block_id = self.request.query_params.get('content_block')
        queryset = Source.objects.all()

        if block_id:
            queryset = queryset.filter(content_block_id=block_id)
        
        return queryset