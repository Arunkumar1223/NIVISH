from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..models import *
from ..serializers import StationASerilizers, GetStationASerilizers
from errormessage import Errormessage
from Multiselect.multiselectFunction import *
from Multiselect.multiselectLists import *
from Validations.Specialist_Referral_Needed import *
from super_admin.models import StationNamesModel
from super_admin.models import HealthCampTeamsModel
from hcp.models import AssignmentModel

class StationADetailsCreate(generics.GenericAPIView):
    serializer_class = StationASerilizers

    def post(self, request, *args, **kwargs):
        try:
            hcid = request.data.get('HCID')
            infoseekid = request.data.get('InfoseekId')
            hcpid = request.data.get('HCPID')
      
            if StationAModel.objects.filter(HCID=hcid, InfoseekId=infoseekid):
                raise Exception("This HCID already exists with InfoseekId")

            data = request.data
            check_SRN(request)
            field_lists = {
                'Specialist_Referral_Needed_Type': Specialist_Referral_Needed_Type
            }

            validation_result = multiselect.check_field_lists(data, field_lists)
            if validation_result is not None:
                return validation_result

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            assignment_instance = AssignmentModel.objects.filter(HCID=hcid, HCPID=hcpid).first() 

            if assignment_instance:
                serializer.validated_data['HCP_TeamId'] = assignment_instance.TeamId
            else:             
                serializer.validated_data['HCP_TeamId'] = None

            
            station_instance = StationNamesModel.objects.get(id=1)
            serializer.validated_data['StationID'] = station_instance

            user = serializer.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = GetStationASerilizers(user).data
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


