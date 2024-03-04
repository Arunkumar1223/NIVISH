import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import UpdateStationCSerilizers,GetStationCSerilizers
from ..models import *
from errormessage import Errormessage
from logs_data import logsFun
from Models_logs.stations_models_logs import StationCModel_Log


class StationCDetailsUpdate(generics.GenericAPIView):
    serializer_class = UpdateStationCSerilizers

    def put(self, request, id):
        try:
            
            station_C_data = StationCModel.objects.get(id=id)
            station_C_logs = StationCModel_Log()

            logs_updated = logsFun(station_C_logs,station_C_data)

            station_C_data = GetStationCSerilizers(station_C_data,data=request.data, partial=True)
            station_C_data.is_valid(raise_exception=True)
            station_C_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_C_data.data
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