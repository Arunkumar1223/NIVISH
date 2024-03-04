import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import UpdateStationASerilizers,GetStationASerilizers
from ..models import *
from errormessage import Errormessage

from logs_data import logsFun
from Models_logs.stations_models_logs import StationAModel_Log

class StationADetailsUpdate(generics.GenericAPIView):
    serializer_class = UpdateStationASerilizers

    def put(self, request, id):
        try:

            station_A_data = StationAModel.objects.get(id=id)
            station_A_logs = StationAModel_Log()

            logs_updated = logsFun(station_A_logs,station_A_data)

            station_A_data = GetStationASerilizers(station_A_data,data=request.data, partial=True)
            station_A_data.is_valid(raise_exception=True)
            station_A_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_A_data.data
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