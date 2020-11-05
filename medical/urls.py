from django.urls import path
from . import views

urlpatterns = [
    path('beeMedical/', views.beeMedical, name='beeMedical'),
    path('addMedicine/', views.addMedicine, name='addMedicine'),
    path('editMedicine/<pk>/', views.editMedicine, name='editMedicine'),
    path('deleteMedicine/<pk>/', views.deleteMedicine, name='deleteMedicine'),
    path('hiveMedicalHistory/<pk>/', views.hiveMedicalHistory,
         name='hiveMedicalHistory'),
    path('addMedicalRecord/<pk>/', views.addMedicalRecord,
         name='addMedicalRecord'),
    path('editMedicalRecord/<hiveinst_id>/<pk>/', views.editMedicalRecord,
         name='editMedicalRecord'),
    path('deleteMedicalRecord/<hiveinst_id>/<pk>/', views.deleteMedicalRecord,
         name='deleteMedicalRecord'),
]
