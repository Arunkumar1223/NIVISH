import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import InfoseekMasterSerilizers
from ..models import *
from errormessage import Errormessage
from logs_data import logsFun
from Models_logs.infoseek_models_logs import InfoseekMasterModel_Log


class InfoseekUpdate(generics.GenericAPIView):
    """Here We're updating Master Data of the Infoseek 
                (Table_Name:'Infoseek_Master')"""
    serializer_class = InfoseekMasterSerilizers

    def put(self, request, id):
        try:
            infoseek_master_data = InfoseekMasterModel.objects.get(id=id)
            infoseek_master_data_logs = InfoseekMasterModel_Log()

            logs_updated = logsFun(infoseek_master_data_logs,infoseek_master_data)

            r = InfoseekMasterModel.objects.get(id=id)
            
            s = InfoseekMasterSerilizers(r,data=request.data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = s.data
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