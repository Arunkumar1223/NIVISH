
from .views import *
from django.urls import path


urlpatterns = [

path('StationADetailsCreate/',StationADetailsCreate.as_view(), name='StationADetailsCreate'),

path('StationADetailsUpdate/<int:id>/',StationADetailsUpdate.as_view(), name='StationADetailsUpdate'),

path('StationADetails/<int:id>/',StationADetails.as_view(), name='StationADetails'),
path('StationADetails/',StationADetails.as_view(), name='StationADetails'),
path('StationDetails/',StationDetails.as_view(), name='StationDetails'),


]
