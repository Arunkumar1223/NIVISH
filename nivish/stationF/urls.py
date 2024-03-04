from .views import *
from django.urls import path

urlpatterns = [
    path('StationFDetailsCreate/', StationFDetailsCreate.as_view(), name='StationFDetailsCreate'),
    path('StationFDetailsS2/<int:id>', StationFDetailsS2.as_view(custom_property='section2'), name = 'StationFDetailsS2'),
    path('StationFDetailsS3/<int:id>', StationFDetailsS2.as_view(custom_property='section3'), name = 'StationFDetailsS3'),
    path('StationFDetailsS4/<int:id>', StationFDetailsS2.as_view(custom_property='section4'), name = 'StationFDetailsS4'),
    path('StationFDetailsS5/<int:id>', StationFDetailsS2.as_view(custom_property='section5'), name = 'StationFDetailsS5'),
    path('StationFDetailsS6/<int:id>', StationFDetailsS2.as_view(custom_property='section6'), name = 'StationFDetailsS6'),
    path('StationFDetailsS7/<int:id>', StationFDetailsS2.as_view(custom_property='section7'), name = 'StationFDetailsS7'),
    path('StationFDetailsS8/<int:id>', StationFDetailsS2.as_view(custom_property='section8'), name = 'StationFDetailsS8'),
    path('StationFDetailsS9/<int:id>', StationFDetailsS2.as_view(custom_property='section9'), name = 'StationFDetailsS9'),
    path('StationFDetailsS10/<int:id>', StationFDetailsS2.as_view(custom_property='section10'), name = 'StationFDetailsS10'),

    path('StationFDetails/<int:id>/', StationFDetails.as_view(), name='StationFDetails'),
    path('StationFDetails/', StationFDetails.as_view(), name='StationFDetails'),


    path('StationFDetailsUpdate/<int:id>/', StationFDetailsUpdate.as_view(), name='StationFDetailsUpdate'),
    
]



