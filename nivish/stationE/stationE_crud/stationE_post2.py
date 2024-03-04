import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import StationESerilizers2, StationESerilizers3, StationESerializers4,StationESerializers5
from ..models import *
from errormessage import Errormessage
from Multiselect.multiselectLists import *
from Multiselect.multiselectFunction import *
from Validations.Specialist_Referral_Needed import check_SRN
from Validations.StationE_Validations import *
from logs_data import logsFun
from Models_logs.stations_models_logs import StationEModel_Log


class DynamicSerializerMixin:
    def get_serializer_class(self):
        # Implement your logic to determine the serializer class dynamically
        if self.custom_property == "section2":
            return StationESerilizers2
        elif self.custom_property == "section3":
            return StationESerilizers3
        elif self.custom_property == "section4":
            return StationESerializers4
        elif self.custom_property == "section5":
            return StationESerializers5
        

class StationEDetailsS2(DynamicSerializerMixin, generics.GenericAPIView):
    
    custom_property = None
    def __init__(self, *args, **kwargs):
        # Capture any custom keyword arguments passed during instantiation
        self.custom_property = kwargs.pop('custom_property', None)
        super().__init__(*args, **kwargs)

    def put(self, request, id):
        print("put")
        print(self.request.path_info)
        try:
            station_E_data = StationEModel.objects.get(id=id)
            station_E_logs = StationEModel_Log()

            logs_updated = logsFun(station_E_logs,station_E_data)
            data = request.data
            field_lists = {}
            if self.custom_property == "section2":
                serializer_class = StationESerilizers2
            elif self.custom_property == "section3":
                check_UL_Right_Appearance(request)
                check_UL_Right_Motor_Function_Range_of_Movement(request)
                check_UL_Right_Deep_Tendon_Reflexes_Biceps(request)
                check_UL_Right_Deep_Tendon_Reflexes_Radial(request)
                check_UL_Right_Deep_Tendon_Reflexes_Sensory_Function(request)

                check_UL_Left_Appearance(request)
                check_UL_Left_Deep_Tendon_Reflexes_Biceps(request)
                check_UL_Left_Deep_Tendon_Reflexes_Radial(request)
                check_UL_Left_Motor_Function_Range_of_Movement(request)
                check_UL_Left_Deep_Tendon_Reflexes_Sensory_Function(request)


                field_lists = {
                    'UL_Right_Appearance_Abnormal': Appearance_Abnormal_list,
                    'UL_Left_Appearance_Abnormal': Appearance_Abnormal_list,
                    'UL_Right_MF_RM_Abnormal_Hyper_Flexible': MF_RM_Abnormal_Hyper_Flexible_list,
                    'UL_Left_MF_RM_Abnormal_Hyper_Flexible': MF_RM_Abnormal_Hyper_Flexible_list,
                    'UL_Right_DTR_SF_Abnormal': DTR_SF_Abnormal_list,
                    'UL_Left_DTR_SF_Abnormal': DTR_SF_Abnormal_list,
                    }
                serializer_class = StationESerilizers3

            elif self.custom_property == "section4": 
                check_LL_Right_Appearance(request)
                check_LL_Right_Motor_Function_Knee(request)
                check_LL_Right_Deep_Tendon_Reflexes_Sensory_Function(request)

                check_LL_Left_Appearance(request)
                check_LL_Left_Motor_Function_Knee(request)
                check_LL_Left_Deep_Tendon_Reflexes_Sensory_Function(request)

                field_lists = {
                    'LL_Right_Appearance_Abnormal': Appearance_Abnormal_list,
                    'LL_Left_Appearance_Abnormal': Appearance_Abnormal_list,
                    'LL_Right_DTR_SF_Abnormal': DTR_SF_Abnormal_list,
                    'LL_Left_DTR_SF_Abnormal': DTR_SF_Abnormal_list,
                    }
                serializer_class = StationESerializers4
                
            elif self.custom_property == "section5":
                check_SRN(request)
                field_lists ={
                    'Specialist_Referral_Needed_Type': Specialist_Referral_Needed_Type
                }
                serializer_class = StationESerializers5
            
            validation_result = multiselect.check_field_lists(data, field_lists)
            if validation_result is not None:
                return validation_result
                    
            station_E_data = serializer_class(station_E_data, data=data, partial=True)
            station_E_data.is_valid(raise_exception=True)
            station_E_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_E_data.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)