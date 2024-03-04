from .views import *
from django.urls import path


urlpatterns = [

    path('StationEDetailsCreate/', StationEDetailsCreate.as_view(), name = 'StationEDetailsCreate'),
    path('StationEDetailsS2/<int:id>', StationEDetailsS2.as_view(custom_property='section2'), name = 'StationEDetailsS2'),
    path('StationEDetailsS3/<int:id>', StationEDetailsS2.as_view(custom_property='section3'), name = 'StationEDetailsS3'),
    path('StationEDetailsS4/<int:id>', StationEDetailsS2.as_view(custom_property='section4'), name = 'StationEDetailsS4'),
    path('StationEDetailsS5/<int:id>', StationEDetailsS2.as_view(custom_property='section5'), name = 'StationEDetailsS5'),


    path('StationEDetails/<int:id>/', StationEDetails.as_view(), name = 'StationEDetails'),
    path('StationEDetails/', StationEDetails.as_view(), name = 'StationEDetails'),


    path('StationEDetailsUpdate/<int:id>/', StationEDetailsUpdate.as_view(), name = 'StationEDetailsUpdate'),
   
]



