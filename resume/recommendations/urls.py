from django.urls import path
from . import views

urlpatterns = [
    path('recommendations/',views.rec,name='rec'),
    
]