from .views import *
from django.urls import path


urlpatterns = [

    path('StationHDetailsCreate/', StationHDetailsCreate.as_view(), name= 'StationHDetailsCreate'),
    path('StationHDetailsS2/<int:id>', StationHDetailsS2.as_view(custom_property='section2'), name = 'StationHDetailsS2'),
    path('StationHDetailsS3/<int:id>', StationHDetailsS2.as_view(custom_property='section3'), name = 'StationHDetailsS3'),
    path('StationHDetailsS4/<int:id>', StationHDetailsS2.as_view(custom_property='section4'), name = 'StationHDetailsS4'),
    path('StationHDetailsS5/<int:id>', StationHDetailsS2.as_view(custom_property='section5'), name = 'StationHDetailsS5'),
    path('StationHDetailsS6/<int:id>', StationHDetailsS2.as_view(custom_property='section6'), name = 'StationHDetailsS6'),
    


    path('StationHDetails/<int:id>/', StationHDetails.as_view(), name= 'StationHDetails'),
    path('StationHDetails/', StationHDetails.as_view(), name= 'StationHDetails'),

    path('StationHDetailsUpdate/<int:id>/', StationHDetailsUpdate.as_view(), name= 'StationHDetailsUpdate'),
    


]