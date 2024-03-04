import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import UpdateHcpRegistrationSerializers,UpdateResponseHcpRegistrationSerializers
from ..models import *
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated


class HcpRegistrationUpdate(generics.GenericAPIView):
    serializer_class = UpdateHcpRegistrationSerializers
    # permission_classes = (IsAuthenticated,)

    def put(self, request, HCPID):
        try:
            
            r = HcpRegistrationModel.objects.get(HCPID=HCPID)
            FullName = request.data.get('FullName')
            Gender = request.data.get('Gender')
            Date_of_Birth = request.data.get('Date_of_Birth')
            Registered_Email = request.data.get('Registered_Email')
            Registered_MobileNumber = request.data.get('Registered_MobileNumber')
   
  
            s = UpdateResponseHcpRegistrationSerializers(r,data=request.data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            hcp_master_data = HcpMasteModel.objects.get(Email= Registered_Email)

            hcp_master_data.FullName = FullName
            hcp_master_data.Gender = Gender
            hcp_master_data.Date_of_Birth = Date_of_Birth
            hcp_master_data.MobileNumber = Registered_MobileNumber
            hcp_master_data.save()

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