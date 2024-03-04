from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..models import *
from ..serializers import StationGSerializers,GetStationGPostSerializers
from errormessage import Errormessage
from Multiselect.multiselectLists import *
from Multiselect.multiselectFunction import *
from Validations.StationG_Validations import *
from super_admin.models import StationNamesModel


class StationGDetailsCreate(generics.GenericAPIView):
    serializer_class = StationGSerializers

    def post(self, request, *args, **kwargs):
        try:

            hcid = request.data.get('HCID')
            infoseekid = request.data.get('InfoseekId')
            if StationGModel.objects.filter(HCID=hcid, InfoseekId=infoseekid):
                raise Exception("This HCID already exits with InfoseekId")
            else:
                data = request.data
                check_CNS_Speech(request)
                check_CNS_History_of_Headache(request)
                check_CNS_History_of_Dizziness(request)

                field_lists = {
                    'CNS_History_of_Headache_yes_Associated_With': Associated_With_list,
                    'CNS_History_of_Headache_yes_Associated_With_Occurrence' : History_of_Headache_yes_Associated_With_Occurrence_list,
                    'CNS_History_of_Dizziness_yes_Associated_With' : Associated_With_list,
                    'CNS_History_of_Dizziness_yes_Associated_With_Occurrence' : History_of_Headache_yes_Associated_With_Occurrence_list
                }
                
                validation_result = multiselect.check_field_lists(data, field_lists)
                if validation_result is not None:
                    return validation_result
            

                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                station_instance = StationNamesModel.objects.get(id=7)
                serializer.validated_data['StationID'] = station_instance
                user = serializer.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = GetStationGPostSerializers(user).data
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
