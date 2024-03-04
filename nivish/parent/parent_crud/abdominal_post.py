from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from ..models import BPModel
from infoseek .models import *
from ..serializers import GetAbdominalSerializers
from genericresponse import GenericResponse
from errormessage import Errormessage
import requests


class AbdominalVerification(generics.GenericAPIView):
    serializer_class = GetAbdominalSerializers 

    def post(self,request):
        InfoseekId=request.data.get("InfoseekId")
        
        
        try:
            if InfoseekVerificationModel.objects.filter(InfoseekId=InfoseekId):
                a = GetAbdominalSerializers(data=request.data)
                a.is_valid(raise_exception=True)
                b = a.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = GetAbdominalSerializers(b).data
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message ="Invalid Id"
                response.Result = False
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)

            
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message =Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
       
