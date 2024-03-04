from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import GetHcpEducationSerializers
from ..models import HcpEducationModel
from genericresponse import GenericResponse
from errormessage import Errormessage

class GetByHcpEducation(generics.GenericAPIView):
    serializer_class = GetHcpEducationSerializers
    # permission_classes = (IsAuthenticated,)

    def get(self, request,EducationId = None):
        try:
           
            data = HcpEducationModel.objects.filter(id=EducationId)    
            serializer_class = GetHcpEducationSerializers(data, many=True)
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