from django.urls import path
from . import views


urlpatterns = [
    path('hive/<apiary_id>', views.hive, name='hive'),
    path('addHive/<apiaryID>', views.addHive, name='addHive'),
    path('deleteHive/<pk><apiary_id>', views.deleteHive, name='deleteHive')
]
