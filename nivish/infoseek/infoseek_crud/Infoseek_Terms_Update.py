import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import InfoseekTermsSerializers
from ..models import *
from errormessage import Errormessage


class InfoseekTermsUpdate(generics.GenericAPIView):
    """Here We're updating the Terms and Conditions based on InfoseekId
                (Table_Name:'Infoseek')"""
    serializer_class = InfoseekTermsSerializers

    def put(self, request, InfoseekId):
        try:
            
            r = InfoseekVerificationModel.objects.get(InfoseekId=InfoseekId)
            
            s = InfoseekTermsSerializers(r,data=request.data, partial=True)
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