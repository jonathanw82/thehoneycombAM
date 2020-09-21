from django.urls import path
from . import views


urlpatterns = [
    path('setup/', views.setup, name='setup'),
    path('addApiary/', views.addApiary, name='addApiary'),
    path('apiary/', views.apiary, name="apiary"),
    path('editApiary/<pk>', views.editApiary, name="editApiary"),
    path('deleteApiary/<pk>', views.deleteApiary, name="deleteApiary")
]
