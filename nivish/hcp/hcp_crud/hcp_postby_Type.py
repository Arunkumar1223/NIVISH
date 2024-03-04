from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import HcpGetBy,GetHcpRegistrationSerializers
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from ..models import HcpRegistrationModel



class HcpGetbyType(generics.GenericAPIView):
    serializer_class = HcpGetBy
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            Type = request.data.get('Type')
            FullName = request.data.get('FullName')
            Registered_Email = request.data.get('Registered_Email')

            res = HcpRegistrationModel.objects.get(Type=Type,FullName=FullName,Registered_Email=Registered_Email)

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = GetHcpRegistrationSerializers(res).data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "HasError")
            response.Message = "This user doesn't exist"
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
