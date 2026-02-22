from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import SubTheme, Section
from .serializers import SubThemeSerializer, SectionSerializer

# Create your views here.
class SubThemeViewSet(ModelViewSet):
    queryset = SubTheme.objects.all()
    serializer_class = SubThemeSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def lock(self, request, pk=None):
        subtheme = self.get_object()

        if request.user.role not in ['admin', 'teacher']:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        subtheme.is_locked = True
        subtheme.save()
        
        return Response({'status': 'locked'})
    
    @action(detail=True, methods=['get'])
    def progress(self, request, pk=None):
        subtheme = self.get_object()
        
        return Response({'progress': subtheme.progress()})
    
class SectionViewSet(ModelViewSet):
    serializer_class = SectionSerializer
    
    def get_queryset(self):
        subtheme_id = self.request.query_params.get('subtheme')
        queryset = Section.objects.all()

        if subtheme_id:
            queryset = queryset.filter(subtheme_id=subtheme_id)

        return queryset