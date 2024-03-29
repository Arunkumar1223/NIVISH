"""nivish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import *

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# from rest_framework.schemas import get_schema_view, openapi
from django.views.generic import TemplateView
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions


schema_view = get_schema_view(
openapi.Info(
    title="Nivish_Staging",
    default_version='v1.0.0-Staging',
    name='openapi-schema',
),


public=True,
permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('Api/token/',
          jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('Api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
        
    path('admin/', admin.site.urls),
    path('StationA/', include('stationA.urls')),
    path('StationB/', include('stationB.urls')),
    path('StationC/', include('stationC.urls')),
    path('StationE/', include('stationE.urls')),
    path('Infoseek/', include('infoseek.urls')),
    path('Hcp/', include('hcp.urls')),
    # path('Camp/', include('camp.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('Redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('StationF/', include('stationF.urls')),
    path('StationG/', include('stationG.urls')),
    path('StationH/', include('stationH.urls')),
    path('StationD/', include('stationD.urls')),
    path('Parent/', include('parent.urls')),
    path('CampAdmin/', include('camp_admin.urls')),
    path('SuperAdmin/', include('super_admin.urls')),
    path('ReviewDoctor/', include('ReviewDoctor.urls')),

    
]

