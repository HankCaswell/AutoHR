"""
URL configuration for autoHR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as auth_views
from equipmentmanagement.views import PDFTextView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token-auth/', auth_views.obtain_auth_token, name = 'obtain-token'),
    path('api/pdf-text/', PDFTextView.as_view(), name='pdf-text'),
    # path('api/unit/', include('unit.urls')),
    path('api/', include('equipmentmanagement.urls')),
    path('api/user/', include('equipmentmanagement.urls')),
#     path('api/equipment/', include('equipment.urls')),
#     path('api/transaction/', include('transaction.urls')),
]
