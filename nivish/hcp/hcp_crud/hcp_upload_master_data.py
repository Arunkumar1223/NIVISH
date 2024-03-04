from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import HcpFileUploadSerializer
from ..models import HcpMasteModel
from errormessage import Errormessage
import pandas as pd
import requests
from datetime import datetime
from manage_urls import *

def api(file):
    df = pd.read_csv(file)
    length = len(df)
    success_message = "Data already exists"
    has_error = False

    for id_value in range(1, length + 1):
        filtered_data = df[df['S.No'] == id_value]

        FullName = filtered_data['FullName'].iloc[0]
        Gender = filtered_data['Gender'].iloc[0]
        Date_of_Birth_str = filtered_data['Date_of_Birth'].iloc[0]
        Date_of_Birth_obj = datetime.strptime(Date_of_Birth_str, '%d-%m-%Y')
        Date_of_Birth_formatted = Date_of_Birth_obj.strftime('%Y-%m-%d')
        MobileNumber = str(filtered_data['MobileNumber'].iloc[0])
        Email = filtered_data['Email'].iloc[0]
        Type = filtered_data['Type'].iloc[0]

        existing_data = HcpMasteModel.objects.filter(Email=Email, Type=Type)

        json_data = {
            'FullName': FullName,
            'Gender': Gender,
            'Date_of_Birth': Date_of_Birth_formatted,
            'MobileNumber': MobileNumber,
            'Email': Email,
            'Type': Type,
            'Tag': None,
        }

        if not existing_data:
            success_message = "New data uploaded successfully"
            has_error = True

            url = hcpmaster_url
            token = token1
            headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {token}'
            }

            response = requests.post(url, headers=headers, json=json_data)

    return success_message, has_error

from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes

@parser_classes((MultiPartParser,))
class HcpUploadExcel(generics.GenericAPIView):
    serializer_class = HcpFileUploadSerializer

    def post(self, request, *args, **kwargs):
        try:
            file = request.data.get('file')
            success_message, has_error = api(file)

            response = GenericResponse("Message", "Result", "Status", "HasError")

            if has_error:
                response.Message = success_message
                response.Status = 200
                response.HasError = False
            else:
                response.Message = success_message
                response.Status = 400
                response.HasError = True

            return Response(response.__dict__, status=response.Status)

        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            return Response(response.__dict__, status=400)