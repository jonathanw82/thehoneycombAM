from django.urls import path
from . import views

urlpatterns = [
    path('beeMedical/', views.beeMedical, name='beeMedical'),
]
