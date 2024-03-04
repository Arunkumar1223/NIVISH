import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import InfoseekUserSerializers,GetInfoseekUserSerializers
from ..models import *
from errormessage import Errormessage
from logs_data import logsFun
from Models_logs.infoseek_models_logs import InfoseekVerificationModel_Log

class InfoseekVerficationUpdate(generics.GenericAPIView):
    """Here We're updating the Infoseek Verification details based on InfoseekId
            (Here InfoseekId is nothing but Student Registration id)
                (Table_Name:'Infoseek')"""
    serializer_class = InfoseekUserSerializers
   
    def put(self, request, InfoseekId):

        try:

            infoseek_verification_data = InfoseekVerificationModel.objects.get(InfoseekId=InfoseekId)
            infoseek_verification_data_logs = InfoseekVerificationModel_Log()

            logs_updated = logsFun(infoseek_verification_data_logs,infoseek_verification_data)
            
            r = InfoseekVerificationModel.objects.get(InfoseekId=InfoseekId)
        
            
            s = GetInfoseekUserSerializers(r,data=request.data, partial=True)
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