from django.urls import path
from . import views

urlpatterns = [
    path('certification/',views.cet,name='cet'),
    
]