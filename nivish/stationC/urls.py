from .views import *
from django.urls import path


urlpatterns = [

path('StationCDetailsCreate/',StationCDetailsCreate.as_view(), name='StationCDetailsCreate'),
path('StationCDetailsS2/<int:id>', StationCDetailsS2.as_view(custom_property='section2'), name = 'StationCDetailsS2'),
path('StationCDetailsS3/<int:id>', StationCDetailsS2.as_view(custom_property='section3'), name = 'StationCDetailsS3'),
path('StationCDetailsS4/<int:id>', StationCDetailsS2.as_view(custom_property='section4'), name = 'StationCDetailsS4'),
path('StationCDetailsS5/<int:id>', StationCDetailsS2.as_view(custom_property='section5'), name = 'StationCDetailsS5'),


path('StationCDetails/',StationCDetails.as_view(), name='StationCDetails'),
path('StationCDetails/<int:id>/',StationCDetails.as_view(), name='StationCDetails'),


path('StationCDetailsUpdate/<int:id>/',StationCDetailsUpdate.as_view(), name='StationCDetailsUpdate'),

]
