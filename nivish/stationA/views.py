from django.shortcuts import render

# Create your views here.
from .stationA_crud.stationA_post import StationADetailsCreate
from .stationA_crud.stationA_update import StationADetailsUpdate
from .stationA_crud.stationA_Get_by_id import StationADetails
from .stationA_crud.stationA_Get_by_hcid_infoseekid import StationDetails





StationADetailsCreate()
StationADetailsUpdate()
StationADetails()
StationDetails()

