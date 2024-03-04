from .views import *
from django.urls import path


urlpatterns = [

    path('StationBDetailsCreate/',StationBDetailsCreate.as_view(), name='StationBDetailsCreate'),


    path('StationBDetailsUpdate/<int:id>/',StationBDetailsUpdate.as_view(), name='StationBDetailsUpdate'),


    path('StationBDetails/<int:id>/',StationBDetails.as_view(), name='StationBDetails'),
    path('StationBDetails/',StationBDetails.as_view(), name='StationBDetails'),
   
]