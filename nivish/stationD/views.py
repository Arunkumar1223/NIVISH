from django.shortcuts import render

# Create your views here.
from stationD.stationD_crud.stationD_post import StationDDetailsCreate
from stationD.stationD_crud.stationD_post2 import StationDDetailsS2
from stationD.stationD_crud.stationD_update import StationDDetailsUpdate
from stationD.stationD_crud.stationD_GetbyID import StationDDetails
from stationD.stationD_crud.stationD_update_doc import StationDUpdateDoc
from stationD.stationD_crud.stationD_upload_doc import UpdateDocStationD

StationDDetailsCreate()
StationDDetailsS2()
StationDDetailsUpdate()
StationDDetails()
StationDUpdateDoc()
UpdateDocStationD()





