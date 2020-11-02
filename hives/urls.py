from django.urls import path
from . import views


urlpatterns = [
    path('hive/<apiary_id>/', views.hive, name='hive'),
    path('addHive/<apiary_id>/', views.addHive, name='addHive'),
    path('deleteHive/<apiaryID>/<pk>/', views.deleteHive, name='deleteHive'),
    path('editHive/<apiaryID>/<pk>/', views.editHive, name='editHive'),
    path('hiveDocs/<pk>/', views.hiveDocs, name='hiveDocs'),
    path('addhiveDoc/<pk>/', views.addhiveDoc, name='addhiveDoc'),
    path('editHiveDoc/<hive_id>/<pk>/', views.editHiveDoc, name='editHiveDoc'),
    path('deleteHivedoc/<hive_id>/<pk>/', views.deleteHivedoc,
         name='deleteHivedoc')
]
