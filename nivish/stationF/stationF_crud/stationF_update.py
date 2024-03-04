import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import UpdateStationFSerializers,GetStationFSerializers
from ..models import *
from errormessage import Errormessage

from logs_data import logsFun
from Models_logs.stations_models_logs import StationFModel_Log

class StationFDetailsUpdate(generics.GenericAPIView):
    serializer_class = UpdateStationFSerializers

    def put(self, request, id):
        try:

            station_F_data = StationFModels.objects.get(id=id)
            station_F_logs = StationFModel_Log()

            logs_updated = logsFun(station_F_logs,station_F_data)

            station_F_data = GetStationFSerializers(station_F_data,data=request.data, partial=True)
            station_F_data.is_valid(raise_exception=True)
            station_F_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_F_data.data
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