"""resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('daniel/',include('base.urls')),
    path('daniel/',include('education.urls')),
    path('daniel/',include('certification.urls')),
    path('daniel/',include('experience.urls')),
    path('daniel/',include('skills.urls')),
    path('daniel/',include('projects.urls')),
    path('daniel/',include('recommendations.urls')),
    path('', include('register.urls') ),
    path('',include('django.contrib.auth.urls'))

]

urlpatterns+=staticfiles_urlpatterns()
