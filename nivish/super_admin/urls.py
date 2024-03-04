from .views import *
from django.urls import path


urlpatterns = [

path('SuperAdminPost/',SuperAdminPost.as_view(), name='SuperAdminPost'),
path('SuperAdminGetById/<int:id>/',SuperAdminGetById.as_view(), name='SuperAdminGetById'),
path('SuperAdminGetAll/',SuperAdminGetById.as_view(), name='SuperAdminGetAll'),
path('SuperAdminUpdate/<int:id>/',SuperAdminUpdate.as_view(), name='SuperAdminUpdate'),

path('HealthCampTeamsPost/',HealthCampTeamsPost.as_view(), name='HealthCampTeamsPost'),
path('HealthCampTeamsGetById/<int:id>/',HealthCampTeamsGet.as_view(), name='HealthCampTeamsGet'),
path('HealthCampTeamsGetAll/',HealthCampTeamsGet.as_view(), name='HealthCampTeamsGetall'),
path('HealthCampTeamsUpdate/<int:id>/',HealthCampTeamsUpdate.as_view(), name='HealthCampTeamsUpdate'),


path('CampRegPost/',CampRegPost.as_view(), name='CampRegPost'),
path('CampRegUpdate/<int:HCID>/', CampRegUpdate.as_view(), name='CampRegUpdate'),
path('CampRegGetById/<int:HCID>/', CampRegGetById.as_view(), name='CampRegGetbyid'),
path('CampRegGetall/', CampRegGetById.as_view(), name='CampRegGetall'),
path('StationPost/',StationPost.as_view(), name='StationPost'),
path('StationGetById/<int:id>/', StationGetById.as_view(), name='StationGetById'),
path('StationGetById/', StationGetById.as_view(), name='StationGetall'),
path('HealthCampSchedulePost/', HealthCampSchedulePost.as_view(), name='HealthCampSchedulePost'),
path('UpdateHealthCampSchedule/<int:HcID>/', UpdateHealthCampSchedule.as_view(), name='UpdateHealthCampSchedule'),
path('MailGeneration/', MailGeneration.as_view(), name='MailGeneration'),

]

