import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import updatechestserializers,GetChestSerializers
from ..models import ChestModel
from errormessage import Errormessage


class ChestUpdate(generics.GenericAPIView):
    serializer_class = updatechestserializers

    def put(self, request, InfoseekId):
        try:
            
            r = ChestModel.objects.get(InfoseekId=InfoseekId)
            
            s = GetChestSerializers(r,data=request.data, partial=True)
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