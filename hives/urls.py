from django.urls import path
from . import views


urlpatterns = [
    path('hive/<apiary_id>/', views.hive, name='hive'),
    path('addHive/<apiary_id>/', views.addHive, name='addHive'),
    path('deleteHive/<apiaryID>/<pk>/', views.deleteHive, name='deleteHive'),
    path('editHive/<apiaryID>/<pk>/', views.editHive, name='editHive')
]
