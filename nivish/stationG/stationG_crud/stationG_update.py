import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import UpdateStationGSerializers,GetStationGSerializers
from ..models import *
from errormessage import Errormessage
from logs_data import logsFun
from Models_logs.stations_models_logs import StationGModel_Log

class StationGDetailsUpdate(generics.GenericAPIView):
    serializer_class = UpdateStationGSerializers

    def put(self, request, id):
        try:
            station_G_data = StationGModel.objects.get(id=id)
            station_G_logs = StationGModel_Log()

            logs_updated = logsFun(station_G_logs,station_G_data)

            station_G_data = GetStationGSerializers(station_G_data,data=request.data, partial=True)
            station_G_data.is_valid(raise_exception=True)
            station_G_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_G_data.data
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