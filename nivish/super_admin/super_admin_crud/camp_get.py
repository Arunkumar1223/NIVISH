from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import GetCampRegSerializers
from ..models import HealthCampModel
from genericresponse import GenericResponse
from errormessage import Errormessage

class CampRegGetById(generics.GenericAPIView):
    serializer_class = GetCampRegSerializers
    # permission_classes = (IsAuthenticated,)

    def get(self, request,HCID = None):
        try:
            if HCID == None:
                data = HealthCampModel.objects.all()

            else:
                data = HealthCampModel.objects.filter(HCID=HCID)

        
            serializer_class = GetCampRegSerializers(data, many=True)
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