from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from infoseek.models import InfoseekMasterModel
from ..serializers import MailSerilizers
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from ..models import *
from django.core.mail import send_mail
from django.conf import settings
import json

class MailGeneration(generics.GenericAPIView):
    # serializer_class = MailSerilizers
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            
            # registered_emails = InfoseekMasterModel.objects.values_list('Parent_Email', flat=True)
            # print(registered_emails,"mail")

            # for email in registered_emails:
            #     print(email,"emails")

                # if "@nivish.com" not in email:
            email = 'devteam-nivish@vivifyhealthcare.com'
            message = "Infoseek On boarding http://65.1.50.165:4204/login"
            subject = 'Registration'
            sender = settings.FROM_EMAIL
            recipient = [email]

            send_mail(subject, message, sender, recipient)
            # print(send_mail,"sendemail")

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Mails Sent"
            response.Result = True
            response.Status = 200
            response.HasError = False
            json_str = json.dumps(response.__dict__)
            return Response(json.loads(json_str), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = str(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            json_str = json.dumps(response.__dict__)
            return Response(json.loads(json_str), status=400)
