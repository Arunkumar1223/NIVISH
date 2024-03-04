from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from ..serializers import GetStationASerilizers
from ..models import StationAModel
from genericresponse import GenericResponse
from errormessage import Errormessage

class StationADetails(generics.GenericAPIView):
    serializer_class = GetStationASerilizers

    def get(self, request,id = None):
        try:

            if id == None:
                
                data = StationAModel.objects.all()
            else:

                data = StationAModel.objects.filter(id=id)

            serializer_class = GetStationASerilizers(data, many=True)
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