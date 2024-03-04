from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import GetRegistrationDeskSerializers
from ..models import RegistrationDeskModel
from genericresponse import GenericResponse
from errormessage import Errormessage
from .Exitdesk import ExitdeskGet  


class AllStationsStatus(generics.GenericAPIView):
    serializer_class = GetRegistrationDeskSerializers
    # permission_classes = (IsAuthenticated,)

    def get_exitdesk_response(self, HCID, UIN):
        try:
            print("Mani")
            exitdesk_instance = ExitdeskGet()
            print("exitdesk_instance",exitdesk_instance)
            exitdesk_response = exitdesk_instance.get(request=None, HCID=HCID, UIN=UIN)
            exitdesk_result = exitdesk_response.data.get("Result", {})

            return exitdesk_result

        except Exception as e:
            error_message = f"Error in get_exitdesk_response: {str(e)}"
            return {"error_message": error_message}

    def get_station_status(self, exitdesk_result):
        if not exitdesk_result:
            return "Not Started"
        
        if all(station.get("Completed", "") == "No" for station in exitdesk_result["StationsStatus"]):
            return "Not Started"

        if any(station.get("Completed", "") == "No" for station in exitdesk_result["StationsStatus"]):
            return "In Progress"

        if all(station.get("Completed", "") == "Yes" for station in exitdesk_result["StationsStatus"]):
            return "Completed"

    def get(self, request, HCID=None, UIN=None):
        try:
            data = RegistrationDeskModel.objects.filter(HCID=HCID, UIN=UIN)
            if data:

                serializer_class = GetRegistrationDeskSerializers(data, many=True)
                stations_status = self.get_exitdesk_response(HCID=HCID, UIN=UIN)
                overall_status = self.get_station_status(stations_status)
                final_response = serializer_class.data[0]
                final_response['All_Stations_Status'] = stations_status['StationsStatus']
                final_response['Status'] = overall_status


                # Count completed stations
                count_completed = sum(1 for station in stations_status["StationsStatus"] if station.get("Completed") == "Yes")
                final_response['Count'] = count_completed #if overall_status == "Completed" else None

            else:
                final_response = {
                "id": None,
                "RegisteredBy": None,
                "ExitedBy": None,
                "HCID": None,
                "UIN": None,
                "RegisteredStatus": None,
                "ExitStatus": None,
                "RegistrationTime": None,
                "ExitTime": None,
                "RegistrationEntryTime": None,
                "ExitEntryTime": None,
                "All_Stations_Status": [
                    {
                    "StationID": None,
                    "Completed": None
                    },
                    {
                    "StationID": None,
                    "Completed": None
                    },
                    {
                    "StationID": None,
                    "Completed": None
                    },
                    {
                    "StationID": None,
                    "Completed": None
                    },
                    {
                    "StationID": None,
                    "Completed": None
                    },
                    {
                    "StationID": None,
                    "Completed": None
                    },
                    {
                    "StationID": None,
                    "Completed": None
                    },
                    {
                    "StationID": None,
                    "Completed": None
                    }
                ],
                "Status": None
                }

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"

            response.Result = final_response,
            response.Status = 200
            response.HasError = False
            json_str = json.dumps(response.__dict__)
            return Response(json.loads(json_str), status=200)

        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            json_str = json.dumps(response.__dict__)
            return Response(json.loads(json_str), status=400)
