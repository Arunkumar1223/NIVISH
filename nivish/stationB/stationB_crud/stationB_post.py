from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..models import *
from ..serializers import StationBSerilizers,GetStationBSerilizers
from errormessage import Errormessage
from Multiselect.multiselectFunction import *
from Multiselect.multiselectLists import *
from Validations.Specialist_Referral_Needed import check_SRN
from super_admin.models import StationNamesModel

class StationBDetailsCreate(generics.GenericAPIView):
    serializer_class = StationBSerilizers

    def post(self, request, *args, **kwargs):
        try:
            hcid = request.data.get('HCID')
            infoseekid = request.data.get('InfoseekId')
            if StationBModel.objects.filter(HCID=hcid, InfoseekId=infoseekid):
                raise Exception("This HCID already exits with InfoseekId")
            else:

                data = request.data
                check_SRN(request)
                field_lists ={
                        'Specialist_Referral_Needed_Type': Specialist_Referral_Needed_Type
                    }
                
                validation_result = multiselect.check_field_lists(data, field_lists)
                if validation_result is not None:
                    return validation_result
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                station_instance = StationNamesModel.objects.get(id=2)
                serializer.validated_data['StationID'] = station_instance
                user = serializer.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = GetStationBSerilizers(user).data
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
