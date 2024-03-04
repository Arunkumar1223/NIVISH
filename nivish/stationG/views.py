from django.shortcuts import render

# Create your views here.
from stationG.stationG_crud.stationG_S1_post import StationGDetailsCreate
from stationG.stationG_crud.stationG_S2_to_S9_post import StationGDetailsS2
from stationG.stationG_crud.stationG_update import StationGDetailsUpdate
from stationG.stationG_crud.stationG_Details import StationGDetails


StationGDetailsCreate()
StationGDetailsS2()
StationGDetailsUpdate()
StationGDetails()
