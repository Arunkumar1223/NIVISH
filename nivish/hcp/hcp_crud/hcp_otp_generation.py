# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.utils import json
# from genericresponse import GenericResponse
# from ..serializers import HcpOtpSerializers
# from errormessage import Errormessage
# from rest_framework.permissions import IsAuthenticated
# from ..models import *
# from django.core.mail import send_mail
# from django.conf import settings




# class HcpOtpGeneration(generics.GenericAPIView):
#     serializer_class = HcpOtpSerializers
#     # permission_classes = (IsAuthenticated,)

#     def post(self, request, *args, **kwargs):
#         try:
            

#             name = request.data.get('Name')
#             Date_of_Birth = request.data.get('Date_of_Birth')
#             email=request.data.get("Email")

           
#             if HcpMasteModel.objects.filter(FullName=name,Date_of_Birth=Date_of_Birth,Email=email):
#                 if HcpRegistrationModel.objects.filter(FullName=name,Date_of_Birth=Date_of_Birth,Registered_Email=email):
#                     raise Exception("This User Already Exists, Please try with another details")                    
#             else:
#                 raise Exception("Invalid Details")
                
#             serializer = self.get_serializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             user = serializer.save()
#             response = GenericResponse("Message", "Result", "Status", "HasError")
#             response.Message = "OTP Sent"
#             response.Result = True
#             response.Status = 200
#             response.HasError = False
#             jsonStr = json.dumps(response.__dict__)
#             return Response(json.loads(jsonStr), status=200)
#         except Exception as e:
#             response = GenericResponse("message", "result", "status", "has_error")
#             response.Message = Errormessage(e)
#             response.Result = False
#             response.Status = 400
#             response.HasError = True
#             jsonStr = json.dumps(response.__dict__)
#             return Response(json.loads(jsonStr), status=400)


from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import HcpOtpSerializers
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from ..models import *
from django.core.mail import send_mail
from django.conf import settings
from services_otp_sendmail import Servicespost



class HcpOtpGeneration(generics.GenericAPIView):
    serializer_class = HcpOtpSerializers
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            
            name = request.data.get('Name')
            Date_of_Birth = request.data.get('Date_of_Birth')
            email=request.data.get("Email")

            if name and Date_of_Birth and email is not None: 

           
                if HcpMasteModel.objects.filter(FullName=name,Date_of_Birth=Date_of_Birth,Email=email):
                    pass                  
                else:
                    raise Exception("Invalid Details")
                    
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            Otp=user.Otp
            Email=user.Email
            hcp_data = Servicespost(Otp,Email,name)
            print(hcp_data,"hcp_data")

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