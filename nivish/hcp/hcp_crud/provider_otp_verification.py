from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from ..serializers import ProviderOtpGenerationSerializers,GetHcpRegistrationSerializers
from ..models import *
from genericresponse import GenericResponse
from errormessage import Errormessage
import requests
from datetime import datetime, timezone, timedelta
from manage_urls import *

def ProviderVerificationPost(email):
    url = provider_url

    print(email)
  
    json_data = {
    'Email': email,
    'Name': None,
    'Date_of_Birth': None,
    'MobileNumber': None,
    }
    json_payload = json.dumps(json_data)
    token = token1
    # print(token,"token")
    try:
        headers = {
                                'Accept': 'application/json',
                                'Content-Type': 'application/json',
                                'Authorization': f'Bearer {token}'  # Replace with your token
                        }
        
        response = requests.post(url , headers=headers , data=json_payload)

        # print(response)

        if response.status_code == 200:
            data = response.json()
            print(data)
            result = data
        else:
            result = False
    except requests.exceptions.RequestException as e:
        result = f"Request failed: {e}"
    return result



class ProviderOtpVerfication(generics.GenericAPIView):
    serializer_class = ProviderOtpGenerationSerializers

    def post(self, request):
        try:
            # email=request.data.get("Registered_Email")
            email=request.data.get("Email")
            otp=request.data.get("Otp")

            # if ProviderOtpModel.objects.get(Registered_Email=email,Otp=otp):
            #     otpdata = ProviderOtpModel.objects.get(Registered_Email=email,Otp=otp)

            if ProviderOtpModel.objects.get(Email=email,Otp=otp):
                otpdata = ProviderOtpModel.objects.get(Email=email,Otp=otp)

                created_date = otpdata.CreatedOn
                Created_date_only = created_date.date()
                Created_time_only = created_date.time()

                current_datetime = datetime.now()
                current_date_only = current_datetime.date()
                current_time_only = current_datetime.time()

                if Created_date_only == current_date_only:

                    time_difference = datetime.combine(current_date_only, current_time_only) - datetime.combine(Created_date_only, Created_time_only)

                    if time_difference.total_seconds() < 600:

                        # provider_data = HcpRegistrationModel.objects.filter(Registered_Email= email)

                        # if provider_data:

                        #     b = GetHcpRegistrationSerializers(provider_data,many=True)
                        #     b = b.data
                        # else:
                        #     raise Exception("Invalid Details")
                        b = ProviderVerificationPost(email)
                        # print(b,"bbbbbbbbbbbbbb")

                        # # deleteotp = otpdelete(email,otp)
                        otpdata.delete()

                        # a = OtpModel.objects.get(Email=email,Otp=otp)
                        # serializer_class = True

                        response = GenericResponse("Message", "Result", "Status", "HasError")
                        response.Message = "Successful"
                        response.Result = b
                        response.Status = 200
                        response.HasError = False
                        jsonStr = json.dumps(response.__dict__)
                        return Response(json.loads(jsonStr), status=200)
                    else:
                            otpdata.delete()
                            print("Fail")
                            raise Exception("Your OTP has been Expired")

                else:
                    otpdata.delete()
                    print("Fail")
                    raise Exception("Your OTP has been Expired")
            else:
                raise Exception("Please Enter Valid OTP")
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)