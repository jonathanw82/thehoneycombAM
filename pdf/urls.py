from django.urls import path
from . import views


urlpatterns = [
    path('hive_record_pdf_view/<pk>/', views.hive_record_pdf_view, name='hive_record_pdf_view'),
]
