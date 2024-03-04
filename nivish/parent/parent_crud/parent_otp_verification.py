from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from ..serializers import ParentOtpGenerationSerializers  
from ..models import ParentOtpModel
from genericresponse import GenericResponse
from errormessage import Errormessage
import requests
from datetime import datetime, timezone, timedelta
from infoseek.models import InfoseekVerificationModel

class ParentOtpVerification(generics.GenericAPIView):
    serializer_class = ParentOtpGenerationSerializers

    
    def post(self, request):
        try:
            mobilenumber = request.data.get("MobileNumber")
            otp = request.data.get("Otp")

            otpdata = ParentOtpModel.objects.get(MobileNumber=mobilenumber, Otp=otp)
            infoseekdata = InfoseekVerificationModel.objects.filter(Primary_Contact=mobilenumber)

            if infoseekdata:
                user = infoseekdata[0].InfoseekId
            else:
                serializer = ParentOtpGenerationSerializers(otpdata)
                result = serializer.data['Result']  

                user = result['InfoseekId']

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = {'InfoseekId': user}
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


