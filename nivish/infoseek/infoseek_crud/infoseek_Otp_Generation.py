from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import InfoseekOtpSerializers,OtpGenerationSerializers,InfoseekUserSerializers
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from ..models import *
from django.core.mail import send_mail
from django.conf import settings
from services_otp_sendmail import Servicespost


    




class InfoseekOtpGeneration(generics.GenericAPIView):
    """Here We generate and send OTPs during the Infoseek Master Data upload.
        It validates student details provided in a POST request, generates an OTP, and sends it via email.
        The response confirms if the OTP was sent successfully or an error. 
        (Table_Name:'infoseek_OTP')"""
    
    serializer_class = InfoseekOtpSerializers
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            
            Student_FirstName = request.data.get('Student_FirstName')
            Student_DOB = request.data.get('Student_DOB')
            # Mothers_FullName = request.data.get('Mothers_FullName')
            email=request.data.get("Email")
            print(email)
            a = InfoseekMasterModel.objects.filter(Student_First_Name=Student_FirstName,Date_of_Birth=Student_DOB,Parent_Email= email)
            print(a)

            if InfoseekMasterModel.objects.filter(Student_First_Name=Student_FirstName,Date_of_Birth=Student_DOB,Parent_Email= email):
                # if InfoseekVerificationModel.objects.filter(Student_FirstName= Student_FirstName,Student_DOB=Student_DOB,Registered_EmailId=email):
                #     raise Exception("This User Already Exists, Please try with another details")
                pass
            else:
                raise Exception("Invalid Details")
            
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()


            Otp=user.Otp
            Email=user.Email

            infoseek_data = Servicespost(Otp,Email,Student_FirstName)
            print(infoseek_data)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "OTP Sent"
            response.Result = True
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