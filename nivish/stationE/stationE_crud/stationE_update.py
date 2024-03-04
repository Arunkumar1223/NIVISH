import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import UpdateStationESerializers,GetStationESerializers
from ..models import *
from errormessage import Errormessage

from logs_data import logsFun
from Models_logs.stations_models_logs import StationEModel_Log

class StationEDetailsUpdate(generics.GenericAPIView):
    serializer_class = UpdateStationESerializers

    def put(self, request, id):
        try:

            station_E_data = StationEModel.objects.get(id=id)
            station_E_logs = StationEModel_Log()

            logs_updated = logsFun(station_E_logs,station_E_data)

            station_E_data = GetStationESerializers(station_E_data,data=request.data, partial=True)
            station_E_data.is_valid(raise_exception=True)
            station_E_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_E_data.data
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