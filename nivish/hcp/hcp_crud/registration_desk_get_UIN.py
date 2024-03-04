from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import GetAllRegistrationDeskSerializers
from ..models import RegistrationDeskModel
from genericresponse import GenericResponse
from errormessage import Errormessage
import requests
import json


def HealthcampDetails(HCID,UIN):
    url = "http://65.1.50.165:8000/Hcp/AllStationsStatus/"
    token ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE1NTgwODk0LCJpYXQiOjE3MDc4MDQ4OTQsImp0aSI6IjllNDExYzgxNDM2MTQ3YmQ5OGZjODY0OGI0MjIwNjI4IiwidXNlcl9pZCI6MTJ9.do35is8zRhHbU1wrBHslXhKfLF9u6r4cOkRc1LT2_R8'

    healthcamp_url = f"{url}{HCID}/{UIN}/"
    # print(healthcamp_url, "Full URL")

    try:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'  
        }

        response = requests.get(healthcamp_url, headers=headers)
        # print(response, "response")

        if response.status_code == 200:
            data = response.json()
            result = data
        else:
            result = False
    except requests.exceptions.RequestException as e:
        result = False
        print(result,"result")

    return result




class RegistrationDeskDetails(generics.GenericAPIView):
    serializer_class = GetAllRegistrationDeskSerializers
    # permission_classes = (IsAuthenticated,)


    def get(self, request,UIN,HCID):

        '''For UIN here we can check Registerd or Not to start his Stations'''

        try:
            register_data = RegistrationDeskModel.objects.filter(UIN=UIN,HCID=HCID)
            if register_data:
                serializer_class = GetAllRegistrationDeskSerializers(register_data, many=True)

                health_camp_details = HealthcampDetails(UIN=UIN,HCID=HCID)
                result = health_camp_details['Result']

                for i in result:
                    Status = i['Status']
                    
                Status_data = serializer_class.data
                # print(Status_data,"Status_data")
                Registration_status = Status_data[0].get("RegisteredStatus", "")
                Exit_status = Status_data[0].get("ExitStatus", "")
                Regis_desk_data =         {
                            "RegisteredStatus": Registration_status,
                            "ExitStatus": Exit_status,
                            "Status":   Status,
                            }
            else:
                Regis_desk_data = {
                    "RegisteredStatus": None,
                    "ExitStatus": None,
                    "Status":   None,
                    }

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = Regis_desk_data
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