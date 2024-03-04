from .views import *
from django.urls import path


urlpatterns = [

# path('HealthCampTeamsGetTeamName/<str:TeamName>/',HealthCampTeamsGetTeamName.as_view(), name='HealthCampTeamsGetTeamName'),
path('CampStationsStatus/',CampStationsStatus.as_view(), name='CampStationsStatus'),

]