from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..models import *
from ..serializers import StationDSerilizers,GetStationDPostSerializers
from errormessage import Errormessage
from Validations.StationD_Validations import *
from super_admin.models import StationNamesModel


class StationDDetailsCreate(generics.GenericAPIView):
    serializer_class = StationDSerilizers

    def post(self, request, *args, **kwargs):
        try:

            hcid = request.data.get('HCID')
            infoseekid = request.data.get('InfoseekId')
            if StationDModel.objects.filter(HCID=hcid, InfoseekId=infoseekid):
                raise Exception("This HCID already exits with InfoseekId")
            else:

                check_Do_you_have_problem_inhearing_your_Teachers_Friends_Parents(request)
                check_Does_any_fluid_come_out_of_your_ears(request)
                
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                station_instance = StationNamesModel.objects.get(id=4)
                serializer.validated_data['StationID'] = station_instance
                user = serializer.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = GetStationDPostSerializers(user).data
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
