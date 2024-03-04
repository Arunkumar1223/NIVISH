from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import GetHcpLicenseDetailsSerilizers
from ..models import Hcp_License_Details_Model
from genericresponse import GenericResponse
from errormessage import Errormessage

class GetHcpLicenseDetails(generics.GenericAPIView):
    serializer_class = GetHcpLicenseDetailsSerilizers
    # permission_classes = (IsAuthenticated,)

    def get(self, request,HCPID = None):
        try:
            if HCPID == None:
                data = Hcp_License_Details_Model.objects.all()
            else:
                data = Hcp_License_Details_Model.objects.filter(HCPID=HCPID)

            serializer_class = GetHcpLicenseDetailsSerilizers(data, many=True)
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