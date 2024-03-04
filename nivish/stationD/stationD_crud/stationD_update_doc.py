import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import StationDSerializersUpdateDoc,GetStationDSerilizers
from ..models import *
from errormessage import Errormessage
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser



@parser_classes((MultiPartParser,))
class StationDUpdateDoc(generics.GenericAPIView):
    serializer_class = StationDSerializersUpdateDoc

    def put(self, request, id):
        try:
            
            r = StationDModel.objects.get(id=id)
            s = StationDSerializersUpdateDoc(r,data=request.data, partial=True)
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