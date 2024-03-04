import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import StationGSerializersS2,StationGSerializersS3,StationGSerializersS4,StationGSerializersS5,StationGSerializersS6A,StationGSerializersS6B,StationGSerializersS7,StationGSerializersS8,StationGSerializersS9
from ..models import *
from errormessage import Errormessage
from Multiselect.multiselectLists import *
from Multiselect.multiselectFunction import *
from Validations.Specialist_Referral_Needed import check_SRN
from Validations.StationG_Validations import *
from logs_data import logsFun
from Models_logs.stations_models_logs import StationGModel_Log
  

class DynamicSerializerMixin:
    def get_serializer_class(self):
        # Implement your logic to determine the serializer class dynamically
        if self.custom_property == "section2":
            return StationGSerializersS2
        elif self.custom_property == "section3":
            return StationGSerializersS3
        elif self.custom_property == "section4":
            return StationGSerializersS4
        elif self.custom_property == "section5":
            return StationGSerializersS5
        elif self.custom_property == "section6A":
            return StationGSerializersS6A
        elif self.custom_property == "section6B":
            return StationGSerializersS6B
        elif self.custom_property == "section7":
            return StationGSerializersS7
        elif self.custom_property == "section8":
            return StationGSerializersS8
        elif self.custom_property == "section9":
            return StationGSerializersS9
        
        

class StationGDetailsS2(DynamicSerializerMixin, generics.GenericAPIView):
    
    custom_property = None
    def __init__(self, *args, **kwargs):
        # Capture any custom keyword arguments passed during instantiation
        self.custom_property = kwargs.pop('custom_property', None)
        super().__init__(*args, **kwargs)

    def put(self, request, id):
        print("put")
        print(self.request.path_info)
        try:
            station_G_data = StationGModel.objects.get(id=id)
            station_G_logs = StationGModel_Log()

            logs_updated = logsFun(station_G_logs,station_G_data)
            data = request.data
            field_lists = {}
            if self.custom_property == "section2":
                check_RS_Shape_of_Chest(request)
                check_RS_Type_of_Respiration_Label(request)

                serializer_class = StationGSerializersS2
            elif self.custom_property == "section3":
                check_RL_Breath_Sounds(request)
                check_RL_Rales_Crepts(request)
                check_RL_Rhonchi_Wheezing(request)
                check_RL_Added_Sounds(request)
                check_RL_Added_Zone_of_Concern(request)
                check_LL_Breath_Sounds(request)
                check_LL_Rales_Crepts(request)
                check_LL_Rhonchi_Wheezing(request)
                check_LL_Added_Sounds(request)
                check_LL_Added_Zone_of_Concern(request)
                field_lists ={
                     'RL_Breath_Sounds_Abnormal' : Abnormal_list,
                     'RL_Rales_Crepts_Present' : Abnormal_list, 
                     'RL_Added_Zone_of_Concern_Abnormal' : Abnormal_list,
                     'LL_Breath_Sounds_Abnormal': Abnormal_list,
                     'LL_Rales_Crepts_Present': Abnormal_list,
                     'LL_Added_Zone_of_Concern_Abnormal' : Abnormal_list,
                }
                serializer_class = StationGSerializersS3
            elif self.custom_property == "section4":
                check_CVS_Jugular_Pulsations(request)
                check_CVS_Suprasternal_Pulsations(request)
                check_CVS_Peripheral_Pulsations_Radial(request)
                check_CVS_Peripheral_Pulsations_Dorsalis_Pedis(request)
                check_CVS_Murmur(request)
                check_CVS_Click(request)
                check_CVS_Apex_Beat(request)
                field_lists ={
                    'CVS_Jugular_Pulsations_Visible_Abnormal' : CVS_Jugular_Pulsations_Visible_Abnormal_list,
                     'CVS_Suprasternal_Pulsations_Present' : CVS_Suprasternal_Pulsations_Present_list, 
                     'CVS_Peripheral_Pulsations_Radial_Present_Abnormal' : Present_Abnormal_list,
                     'CVS_Peripheral_Pulsations_Dorsalis_Pedis_Abnormal': Present_Abnormal_list,
                     'CVS_Murmur_Present' : CVS_Murmur_Present_list,    
                }
                serializer_class = StationGSerializersS4
            elif self.custom_property == "section5":
                check_AUS_Cleft_Lip(request)
                check_AUS_Cleft_Palate(request)
                check_AUS_Right_Hypochondrium_Pain(request)
                check_AUS_RH_Tenderness(request)
                check_AUS_RH_Swelling_Lumps(request)
                check_AUS_RH_Liver(request)
                check_AUS_RH_Gall_Bladder(request)
                check_AUS_Right_Lumbar_Pain(request)
                check_AUS_RL_Tenderness(request)
                check_AUS_RL_Swelling_Lumps(request)
                check_AUS_RL_Right_Kidney(request)
                check_AUS_Right_Iliac_Pain(request)
                check_AUS_RI_MBP(request)
                check_AUS_RI_Tenderness(request)
                check_AUS_RI_Swelling_Lumps(request)
                check_AUS_Epigastric_Pain(request)
                check_AUS_E_Tenderness(request)
                check_AUS_E_Swelling_Lumps(request)
                check_AUS_Umbilical_Pain(request)
                check_AUS_U_Tenderness(request)
                check_AUS_U_Swelling_Lumps(request)
                check_AUS_Suprapubic_Pain(request)
                check_AUS_S_Tenderness(request)
                check_AUS_S_Swelling_Lumps(request)
                check_AUS_S_Uterus(request)
                check_AUS_Left_Hypochondrium_Pain(request)
                check_AUS_LH_Tenderness(request)
                check_AUS_LH_Swelling_Lumps(request)
                check_AUS_LH_Spleen(request)
                check_AUS_Left_Lumbar_Pain(request)
                check_AUS_LL_Tenderness(request)
                check_AUS_LL_Swelling_Lumps(request)
                check_AUS_LL_Left_Kidney(request)
                check_AUS_Left_Iliac_Pain(request)
                check_AUS_LI_Tenderness(request)
                check_AUS_LI_Swelling_Lumps(request)
                check_AUS_Hernia(request)
                check_AUS_Urinary_Bladder(request)

                field_lists ={
                    'AUS_Hernia_Present' : AUS_Hernia_list,
                }
                serializer_class = StationGSerializersS5
            elif self.custom_property == "section6A":
                check_Pubertal_Girls(request)
                check_Years_Menarche_Attained(request)
                check_PAG_during_menses(request)
                check_Pubertal_Girls_Behaviour(request)
                check_PAG_Abnormal_finding(request)

                field_lists ={
                    'PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes' : PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_list,
                    'PAG_Change_behaviour_Yes' : Change_behaviour_Yes_list,
                }
                serializer_class = StationGSerializersS6A
            elif self.custom_property == "section6B":
                check_Pubertal_Boys(request)
                check_Pubertal_Behaviour(request)
                check_Abnormal_finding(request)

                field_lists ={
                    'PAB_Change_behaviour_Yes' : Change_behaviour_Yes_list,
                }
                serializer_class = StationGSerializersS6B
            elif self.custom_property == "section7":
                check_History_medication(request)
                serializer_class = StationGSerializersS7
            elif self.custom_property == "section8":
                serializer_class = StationGSerializersS8
            elif self.custom_property == "section9":
                check_SRN(request)
                field_lists ={
                    'Specialist_Referral_Needed_Type': Specialist_Referral_Needed_Type
                }
                serializer_class = StationGSerializersS9
                
            validation_result = multiselect.check_field_lists(data, field_lists)
            if validation_result is not None:
                return validation_result
           
        
            
            station_G_data = serializer_class(station_G_data, data=data, partial=True)
            station_G_data.is_valid(raise_exception=True)
            station_G_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_G_data.data
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