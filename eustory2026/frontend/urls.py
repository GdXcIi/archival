from django.urls import path
from .views import dashboard, login, subtheme, subtheme_old

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', login, name='login'),
    path('subthemeold/<int:id>/', subtheme_old, name='subthemeold'),
    path('subtheme/<int:id>/', subtheme, name='subtheme'),
]