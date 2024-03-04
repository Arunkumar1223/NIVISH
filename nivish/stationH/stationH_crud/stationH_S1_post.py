from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..models import *
from ..serializers import StationHSerializers,GetStationHPostSerializers
from errormessage import Errormessage
from Multiselect.multiselectLists import *
from Multiselect.multiselectFunction import *
from Validations.StationH_Validations import *
from super_admin.models import StationNamesModel



class StationHDetailsCreate(generics.GenericAPIView):
    serializer_class = StationHSerializers
    
    def post(self, request, *args, **kwargs):

        try: 

            hcid = request.data.get('HCID')
            infoseekid = request.data.get('InfoseekId')
            if StationHModel.objects.filter(HCID=hcid, InfoseekId=infoseekid):
                raise Exception("This HCID already exits with InfoseekId")
            else:
                data = request.data
                check_Upper_Permanent(request)
                check_Upper_Deciduous(request)
                check_Lower_Deciduous(request)
                check_Lower_Permanent(request)
                
                field_lists = {
                    'Upper_Permanent' : Permanent_List,
                    'Upper_Deciduous' : Permanent_List,
                    'Lower_Deciduous' : Permanent_List,
                    'Lower_Permanent' : Permanent_List,

                    'Upper_Permanent_Decayed' : Upper_Permanent_list,
                    'Upper_Permanent_Missing' : Upper_Permanent_list,
                    'Upper_Permanent_Filled'  : Upper_Permanent_list,
                    'Upper_Permanent_Prosthesis' :Upper_Permanent_list,
                    'Upper_Permanent_Restoration_done' :Upper_Permanent_list,

                    'Upper_Deciduous_Decayed' : Upper_Deciduous_List,
                    'Upper_Deciduous_Missing' : Upper_Deciduous_List,
                    'Upper_Deciduous_Filled' : Upper_Deciduous_List,
                    'Upper_Deciduous_Prosthesis' :Upper_Deciduous_List,
                    'Upper_Deciduous_Restoration_done' : Upper_Deciduous_List,

                    'Lower_Deciduous_Decayed' : Lower_Deciduous_List,
                    'Lower_Deciduous_Missing' : Lower_Deciduous_List,
                    'Lower_Deciduous_Filled'  : Lower_Deciduous_List,
                    'Lower_Deciduous_Prosthesis' : Lower_Deciduous_List,
                    'Lower_Deciduous_Restoration_done' : Lower_Deciduous_List,

                    'Lower_Permanent_Decayed' : Lower_Permanent_list,
                    'Lower_Permanent_Missing' : Lower_Permanent_list,
                    'Lower_Permanent_Filled' : Lower_Permanent_list,
                    'Lower_Permanent_Prosthesis' : Lower_Permanent_list,
                    'Lower_Permanent_Restoration_done' : Lower_Permanent_list
                }

                validation_result = multiselect.check_field_lists(data, field_lists)
                if validation_result is not None:
                    return validation_result  
                        
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True) 
                station_instance = StationNamesModel.objects.get(id=8)
                serializer.validated_data['StationID'] = station_instance 
                user = serializer.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = GetStationHPostSerializers(user).data
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
