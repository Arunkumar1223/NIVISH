from .views import *
from django.urls import path

urlpatterns = [
    path('StationGDetailsCreate/', StationGDetailsCreate.as_view(), name='StationFDetailsCreate'),

    path('StationGDetailsS2/<int:id>', StationGDetailsS2.as_view(custom_property='section2'), name = 'StationGDetailsS2'),
    path('StationGDetailsS3/<int:id>', StationGDetailsS2.as_view(custom_property='section3'), name = 'StationGDetailsS3'),
    path('StationGDetailsS4/<int:id>', StationGDetailsS2.as_view(custom_property='section4'), name = 'StationGDetailsS4'),
    path('StationGDetailsS5/<int:id>', StationGDetailsS2.as_view(custom_property='section5'), name = 'StationGDetailsS5'),
    path('StationGDetailsS6A/<int:id>', StationGDetailsS2.as_view(custom_property='section6A'), name = 'StationGDetailsS6A'),
    path('StationGDetailsS6B/<int:id>', StationGDetailsS2.as_view(custom_property='section6B'), name = 'StationGDetailsS6B'),
    path('StationGDetailsS7/<int:id>', StationGDetailsS2.as_view(custom_property='section7'), name = 'StationGDetailsS7'),
    path('StationGDetailsS8/<int:id>', StationGDetailsS2.as_view(custom_property='section8'), name = 'StationGDetailsS8'),
    path('StationGDetailsS9/<int:id>', StationGDetailsS2.as_view(custom_property='section9'), name = 'StationGDetailsS9'),

    path('StationGDetailsUpdate/<int:id>', StationGDetailsUpdate.as_view(), name = 'StationGDetailsUpdate'),

    path('StationGDetails/<int:id>/', StationGDetails.as_view(), name='StationGDetails'),
    path('StationGDetails/', StationGDetails.as_view(), name='StationGDetails'),
    

]