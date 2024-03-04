import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import UpdateStationBSerilizers,GetStationBSerilizers
from ..models import *
from errormessage import Errormessage
from logs_data import logsFun
from Models_logs.stations_models_logs import StationBModel_Log

class StationBDetailsUpdate(generics.GenericAPIView):
    serializer_class = UpdateStationBSerilizers

    def put(self, request, id):
        try:
            
            station_B_data = StationBModel.objects.get(id=id)
            station_B_logs = StationBModel_Log()

            logs_updated = logsFun(station_B_logs,station_B_data)

            station_B_data = GetStationBSerilizers(station_B_data,data=request.data, partial=True)
            station_B_data.is_valid(raise_exception=True)
            station_B_data.save()   
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_B_data.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)