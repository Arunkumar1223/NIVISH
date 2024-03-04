from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import GetAbdominalSerializers
from ..models import AbdominalModel
from genericresponse import GenericResponse
from errormessage import Errormessage


class GetabdominalDetails(generics.GenericAPIView):
    serializer_class = GetAbdominalSerializers

    def get(self,request,InfoseekId):
        try:
            bp_data = AbdominalModel.objects.filter(InfoseekId=InfoseekId)
            serializer_class = GetAbdominalSerializers(bp_data,many=True)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = serializer_class.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)