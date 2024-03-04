from .views import *
from django.urls import path


urlpatterns = [

path('StationDDetailsCreate/',StationDDetailsCreate.as_view(), name='StationDDetailsCreate'),
path('StationDDetailsS2/<int:id>', StationDDetailsS2.as_view(custom_property='section2'), name = 'StationDDetailsS2'),
path('StationDDetailsS3/<int:id>', StationDDetailsS2.as_view(custom_property='section3'), name = 'StationDDetailsS3'),
path('StationDDetailsS4/<int:id>', StationDDetailsS2.as_view(custom_property='section4'), name = 'StationDDetailsS4'),


path('StationDDetails/',StationDDetails.as_view(), name='StationDDetails'),
path('StationDDetails/<int:id>/',StationDDetails.as_view(), name='StationDDetails'),


path('StationDDetailsUpdate/<int:id>/',StationDDetailsUpdate.as_view(), name='StationDDetailsUpdate'),

path('StationDDetailsUploadDocs/<int:id>/',StationDUpdateDoc.as_view(), name='StationDUpdateDoc'),

path('UploadDocsStationDDetails/',UpdateDocStationD.as_view(), name='UpdateDocStationD'),

]
