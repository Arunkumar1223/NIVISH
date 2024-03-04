import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import UpdateStationHSerializers,GetStationHSerializers
from ..models import *
from errormessage import Errormessage

from logs_data import logsFun
from Models_logs.stations_models_logs import StationHModel_Log

class StationHDetailsUpdate(generics.GenericAPIView):
    serializer_class = UpdateStationHSerializers

    def put(self, request, id):
        try:

            station_H_data = StationHModel.objects.get(id=id)
            station_H_logs = StationHModel_Log()

            logs_updated = logsFun(station_H_logs,station_H_data)

            station_H_data = GetStationHSerializers(station_H_data,data=request.data, partial=True)
            station_H_data.is_valid(raise_exception=True)
            station_H_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_H_data.data
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