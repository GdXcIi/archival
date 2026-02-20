from django.urls import path
from .views import dashboard, login, subtheme

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', login, name='login'),
    path('subtheme/<int:id>/', subtheme, name='subtheme'),
]