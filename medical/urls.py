from django.urls import path
from . import views

urlpatterns = [
    path('beeMedical/', views.beeMedical, name='beeMedical'),
    path('addMedicine/', views.addMedicine, name='addMedicine'),
    path('editMedicine/<pk>/', views.editMedicine, name='editMedicine'),
    path('deleteMedicine/<pk>/', views.deleteMedicine, name='deleteMedicine'),
    path('hiveMedicalHistory/<apiaryPK>/<pk>/', views.hiveMedicalHistory,
         name='hiveMedicalHistory'),
    path('addMedicalRecord/<apiaryID>/<pk>/', views.addMedicalRecord,
         name='addMedicalRecord'),
    path('editMedicalRecord/<apiaryID>/<hiveinst_id>/<pk>/', views.editMedicalRecord,
         name='editMedicalRecord'),
    path('deleteMedicalRecord/<apiaryPK>/<hiveinst_id>/<pk>/', views.deleteMedicalRecord,
         name='deleteMedicalRecord'),
]
