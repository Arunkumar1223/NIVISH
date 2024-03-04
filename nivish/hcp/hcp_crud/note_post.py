from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import *
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from Validations.Hcp_Validations import *
# from rest_framework.decorators import parser_classes
# from rest_framework.parsers import MultiPartParser
# @parser_classes((MultiPartParser,))

import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
import requests
import json
from manage_urls import *

def Nivupdate(HCPID):
    url = niv_url

    json_data = {
        'HCPID': HCPID
    }

    json_payload = json.dumps(json_data)
    print(json_payload,'satand')

    token = token1
    try:
        print("try")
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'  # Replace with your token
        }

        response = requests.post(url, headers=headers, data=json_payload)
        print(response,"response")
        if response.status_code == 200:
            data = response.json()
            result = data
            
            # result = True
        else:
            # result_data = []
            result = False
    except requests.exceptions.RequestException as e:
        result = False
        # result_data = []
    return result


class NotePost(generics.GenericAPIView):
    serializer_class = NoteSerializers
       
    def post(self, request, *args, **kwargs):
        try:
            HCPID = request.data.get('HCPID')
          
            accepted = request.data.get('Accepted', False)
            if not accepted:
                raise ValueError("Note cannot be posted without Accepted being True.")
            
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            niv=Nivupdate(HCPID)
            print(niv,"niv")
            user.NIV = niv['Result']['NIV']

            print(user.NIV)
            user.save()
            # print(niv.Result.NIV)

            qr_data = {              
                "NIV": niv['Result']['NIV'],
                 "Hcp_qrcode":niv['Result']['Hcp_qrcode']
                }

           
            hcp_data = HcpRegistrationModel.objects.get(HCPID=HCPID)
            hcp_email = hcp_data.Registered_Email
            hcp_master_data = HcpMasteModel.objects.get(Email=hcp_email)
            
            if hcp_master_data.Tag == False:
                hcp_master_data.Tag = True
                hcp_master_data.save()
        
            
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = GetNoteSerializers(user).data
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
