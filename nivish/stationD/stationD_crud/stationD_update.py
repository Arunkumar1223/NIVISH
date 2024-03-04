import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import UpdateStationDSerializers,GetStationDSerilizers
from ..models import *
from errormessage import Errormessage
from logs_data import logsFun
from Models_logs.stations_models_logs import StationDModel_Log

class StationDDetailsUpdate(generics.GenericAPIView):
    serializer_class = UpdateStationDSerializers

    def put(self, request, id):
        try:
            
            station_D_data = StationDModel.objects.get(id=id)
            station_D_logs = StationDModel_Log()

            logs_updated = logsFun(station_D_logs,station_D_data)

            station_D_data = GetStationDSerilizers(station_D_data,data=request.data, partial=True)
            station_D_data.is_valid(raise_exception=True)
            station_D_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_D_data.data
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