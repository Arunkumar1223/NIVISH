from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import HcpLicenseDetailsSerilizers,GetHcpLicenseDetailsSerilizers
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from Validations.Hcp_Validations import *
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser





@parser_classes((MultiPartParser,))


class HcpLicenseDetailsPost(generics.GenericAPIView):
    serializer_class = HcpLicenseDetailsSerilizers
    

    def post(self, request, *args, **kwargs):
        try:

            check_Category(request)
            check_License_Authority(request)

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = GetHcpLicenseDetailsSerilizers(user).data
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

