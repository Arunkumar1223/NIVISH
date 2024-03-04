from django.shortcuts import render

# Create your views here.
from stationE.stationE_crud.stationE_post import StationEDetailsCreate
from stationE.stationE_crud.stationE_post2 import StationEDetailsS2

from stationE.stationE_crud.stationE_Get_by_id import StationEDetails
from stationE.stationE_crud.stationE_update import StationEDetailsUpdate

StationEDetailsCreate()
StationEDetailsS2()

StationEDetails()
StationEDetailsUpdate()


