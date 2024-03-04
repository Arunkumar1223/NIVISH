from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import ProviderOtpSerializers
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from ..models import *
from django.core.mail import send_mail
from django.conf import settings
from services_otp_sendmail import Servicespost



class ProviderOtpGeneration(generics.GenericAPIView):
    serializer_class = ProviderOtpSerializers
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            # email=request.data.get("Registered_Email")
            email=request.data.get("Email")
            print(email,'email')
            name = request.data.get('Name')

            # if HcpRegistrationModel.objects.filter(Registered_Email= email):
            if ProviderRegistrationModel.objects.filter(Email= email):
                
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                
                Otp=user.Otp
                Email=user.Email
                Provider_data = Servicespost(Otp,Email,name)
                print(Provider_data,"Provider")
                # OtpModel.objects.create(Email=Email, Otp=Otp)
                # message = "This is Ypur OTP for Your Verification",Otp
                # message = "This is Your OTP for Your Verification: {}".format(Otp)

                # subject = 'OTP Verification'
                # sender = settings.FROM_EMAIL
                # recipient = [Email]            

                # send_mail(subject, message, sender, recipient)

                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "OTP Sent"
                response.Result = True
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            else:
                raise Exception("Invalid Details")
            
            
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)