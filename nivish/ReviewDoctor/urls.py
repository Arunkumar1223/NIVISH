from django.urls import path
from .views import *

urlpatterns = [
    path('FinalStatusPost/', FinalStatusPost.as_view(), name='FinalStatusPost'),
    path('GetAllInfoseekWNL/<int:HCID>/', GetAllInfoseekWNL.as_view(), name='GetAllInfoseekWNL'),
    path('GetAllInfoseekByReviewStatus/<str:Review_status>/<int:HCID>', GetAllInfoseekByReviewStatus.as_view(), name='GetAllInfoseekByReviewStatus'),
    path('UpdateFinalStatusRD/<str:UIN>', UpdateFinalStatusRD.as_view(), name='UpdateFinalStatusRD'),
    path('GetFinalStatusList/', GetFinalStatusList.as_view(), name='GetFinalStatusList'),
    path('GlobalSearch/<str:student>/', GlobalSearch.as_view(), name='GlobalSearch'),
    path("GetHcpId/<int:HCPID>/",GetByHcpId.as_view(),name = "GetHcpId"),
    path("AlertAPI/<int:HCID>/",AlertAPI.as_view(),name = "AlertAPI"),
    path("StationsFlagsPost/",StationsFlagsPost.as_view(),name = 'StationsFlagsPost'),
    path("GetObservations/<int:HCID>/<int:InfoseekId>/",GetObservations.as_view(),name = "GetObservations"),
    path('StationADetailsReviewUpdate/<int:id>/',UpdateRDstations.as_view(custom_property='RDUpdatestationA'), name='StationADetailsReviewUpdate'),
    path('StationBDetailsReviewUpdate/<int:id>/',UpdateRDstations.as_view(custom_property='RDUpdatestationB'), name='StationBDetailsReviewUpdate'),
    path('StationCDetailsReviewUpdate/<int:id>/',UpdateRDstations.as_view(custom_property='RDUpdatestationC'), name='StationCDetailsReviewUpdate'),
    path('StationDDetailsReviewUpdate/<int:id>/',UpdateRDstations.as_view(custom_property='RDUpdatestationD'), name='StationDDetailsReviewUpdate'),
    path('StationEDetailsReviewUpdate/<int:id>/',UpdateRDstations.as_view(custom_property='RDUpdatestationE'), name='StationEDetailsReviewUpdate'),
    path('StationFDetailsReviewUpdate/<int:id>/',UpdateRDstations.as_view(custom_property='RDUpdatestationF'), name='StationFDetailsReviewUpdate'),
    path('StationGDetailsReviewUpdate/<int:id>/',UpdateRDstations.as_view(custom_property='RDUpdatestationG'), name='StationGDetailsReviewUpdate'),
    path('StationHDetailsReviewUpdate/<int:id>/',UpdateRDstations.as_view(custom_property='RDUpdatestationH'), name='StationHDetailsReviewUpdate'),
    path('PostByHCID&UINDetails/',GetByHcidUINDetails.as_view(), name='GetByHcidUINDetails'),

    
]


