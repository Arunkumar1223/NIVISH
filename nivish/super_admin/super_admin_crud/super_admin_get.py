from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import GetSuperAdminSerializers
from ..models import SuperAdminModel
from genericresponse import GenericResponse
from errormessage import Errormessage

class SuperAdminGetById(generics.GenericAPIView):
    serializer_class = GetSuperAdminSerializers
    # permission_classes = (IsAuthenticated,)

    def get(self, request,id = None):
        try:
            if id == None:
                data = SuperAdminModel.objects.all()

            else:
                data = SuperAdminModel.objects.filter(id=id)

        
            serializer_class = GetSuperAdminSerializers(data, many=True)
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
        
