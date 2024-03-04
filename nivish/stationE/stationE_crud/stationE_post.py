from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..models import *
from ..serializers import StationESerilizers, GetStationEPostSerializers
from errormessage import Errormessage
from Multiselect.multiselectLists import *
from Multiselect.multiselectFunction import *
from Validations.StationE_Validations import *
from super_admin.models import StationNamesModel

class StationEDetailsCreate(generics.GenericAPIView):
    serializer_class = StationESerilizers

    def post(self, request, *args, **kwargs):
        try:

            hcid = request.data.get('HCID')
            infoseekid = request.data.get('InfoseekId')
            if StationEModel.objects.filter(HCID=hcid, InfoseekId=infoseekid):
                raise Exception("This HCID already exits with InfoseekId")
            else:
                data = request.data
                check_Child_Mobility(request)
                check_Student_Ambulant(request)
                check_Gait(request)
                check_Wear_Brace_Support(request)
                check_Prosthesis(request)
                check_Spine_Appearance(request)
                check_Shoulder_Griddle_Appearance(request)
                check_Spine_Mobility(request)
                check_Neck_Mobility(request)

                field_lists = {
                    'Wear_Brace_Support_Yes': Wear_Brace_Support_Yes_list,
                    'Prosthesis_Yes': Prosthesis_Yes_list,
                    'Shoulder_Griddle_Appearance_Abnormal': Shoulder_Griddle_Appearance_Abnormal_list,
                }

                validation_result = multiselect.check_field_lists(data, field_lists)
                if validation_result is not None:
                    return validation_result
                
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                station_instance = StationNamesModel.objects.get(id=5)
                serializer.validated_data['StationID'] = station_instance
                user = serializer.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = GetStationEPostSerializers(user).data
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
