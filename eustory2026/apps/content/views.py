from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import ContentBlock, Source

# Create your views here.
class ContentBlockViewSet(ModelViewSet):
    def get_queryset(self):
        section_id = self.request.query_params.get('section')
        queryset = ContentBlock.objects.all()

        if section_id:
            queryset = queryset.filter(section_id=section_id)
        
        return queryset

class SourceViewSet(ModelViewSet):
    def get_queryset(self):
        block_id = self.request.query_params.get('content_block')
        queryset = Source.objects.all()

        if block_id:
            queryset = queryset.filter(content_block_id=block_id)
        
        return queryset