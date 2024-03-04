import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import StationFSerializers2,StationFSerializers3,StationFSerializers4,StationFSerializers5,StationFSerializers6,StationFSerializers7,StationFSerializers8,StationFSerializers9,StationFSerializers10
from ..models import *
from errormessage import Errormessage
from Multiselect.multiselectLists import *
from Multiselect.multiselectFunction import *
from Validations.StationF_Validations import *
from Validations.Specialist_Referral_Needed import *
from logs_data import logsFun
from Models_logs.stations_models_logs import StationFModel_Log


class DynamicSerializerMixin:
    def get_serializer_class(self):
        # Implement your logic to determine the serializer class dynamically
        if self.custom_property == "section2":
            return StationFSerializers2
        elif self.custom_property == "section3":
            return StationFSerializers3
        elif self.custom_property == "section4":
            return StationFSerializers4
        elif self.custom_property == "section5":
            return StationFSerializers5
        elif self.custom_property == "section6":
            return StationFSerializers6
        elif self.custom_property == "section7":
            return StationFSerializers7
        elif self.custom_property == "section8":
            return StationFSerializers8
        elif self.custom_property == "section9":
            return StationFSerializers9
        elif self.custom_property == "section10":
            return StationFSerializers10
        
        

class StationFDetailsS2(DynamicSerializerMixin, generics.GenericAPIView):
    
    custom_property = None
    def __init__(self, *args, **kwargs):
        # Capture any custom keyword arguments passed during instantiation
        self.custom_property = kwargs.pop('custom_property', None)
        super().__init__(*args, **kwargs)

    def put(self, request, id):
        print("put")
        print(self.request.path_info)
        try:
            
            station_F_data = StationFModels.objects.get(id=id)
            station_F_logs = StationFModel_Log()

            logs_updated = logsFun(station_F_logs,station_F_data)
            data = request.data
            field_lists = {}
            if self.custom_property == "section2":
                check_Nails_Shape(request)
                check_Nails_Deformity(request)
                field_lists = {
                    'Nails_Shape_Abnormal': Nails_Shape_Abnormal_list,
                    'Nails_Deformity_Yes': Nails_Deformity_Yes_list,
                    }
                serializer_class = StationFSerializers2
            elif self.custom_property == "section3":
                check_Head_Skull_Fontanelle(request)
                check_Head_Hair_Appearance(request)
                check_Head_Scalp(request)
                check_Head_Parasites(request)
                check_Head_Hair_Loss(request)
                field_lists = {
                    'Head_Skull_Fontanelle_Open' : Head_Skull_Fontanelle_Open_list,
                    'Head_Skull_Fontanelle_Open_Fontanella' : Fontanelle_list,
                    'Head_Skull_Fontanelle_Open_Occipital' : Fontanelle_list,
                    'Head_Hair_Appearance_Abnormal' : Head_Hair_Appearance_Abnormal_list,
                    'Head_Scalp_Abnormal' : Head_Scalp_Abnormal_list,
                    'Head_Parasites_Yes' : Head_Parasites_Yes_list,
                    'Head_Hair_Loss_Yes' : Head_Hair_Loss_Yes_list,
                    }
                serializer_class = StationFSerializers3
            elif self.custom_property == "section4":
                check_Thyroid_Lymph_Cervical_LN(request)
                check_Thyroid_Lymph_Thyroid_Gland(request)
                check_Thyroid_Lymph_Supraclavicular_LN(request)
                check_Thyroid_Lymph_Axillary_LN(request)
                check_Thyroid_Lymph_Supratrochlear_LN(request)
                check_Thyroid_Lymph_Inguinal_LN(request)
                field_lists = {
                    'Thyroid_Lymph_Cervical_LN_Palpable' : Thyroid_Lymph_Cervical_LN_Palpable_list,
                    'Thyroid_Lymph_Supraclavicular_LN_Palpable': LN_Palpable_list,
                    'Thyroid_Lymph_Axillary_LN_Palpable': LN_Palpable_list,
                    'Thyroid_Lymph_Supratrochlear_LN_Palpable': LN_Palpable_list,
                    'Thyroid_Lymph_Inguinal_LN_Palpable': LN_Palpable_list,
                    }
                serializer_class = StationFSerializers4
            elif self.custom_property == "section5": 
                check_Eyes_Discharge(request)
                field_lists = {
                    'Eyes_Discharge_Yes': Discharge_Yes_list,
                    }
                serializer_class = StationFSerializers5
            elif self.custom_property == "section6":
                Ears_Hearing(request)
                check_Ears_Discharge(request)
                check_Ear_Wax(request)
                check_Ear_Eardrum(request)
                field_lists = {
                    'Ears_Hearing_Abnormal': Ears_Hearing_Abnormal_list,
                    'Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes': LN_Palpable_list,
                    'Ears_Discharge_Yes': Ears_Discharge_Yes_list,
                    'Ear_Wax_Present': LN_Palpable_list,
                    'Ear_Eardrum_Abnormal': Ears_Discharge_Yes_list,
                    }
                serializer_class = StationFSerializers6
            elif self.custom_property == "section7":
                check_Nose_Discharge(request)
                check_Nose_Dryness(request)
                check_Nose_Crusting(request)
                check_Nose_Polyps(request)
                field_lists = {
                    'Nose_Discharge_Yes': Nose_Discharge_Yes_list,
                    }
                serializer_class = StationFSerializers7
            elif self.custom_property == "section8":
                check_Mouth_Throat_Mucosa(request)
                check_Mouth_Throat_Tongue(request)
                check_Mouth_Tonsils(request)
                check_Mouth_Uvula(request)
                check_Mouth_Palate(request)
            
                field_lists = {
                    'Mouth_Throat_Mucosa_Abnormal': Mouth_Throat_Mucosa_Abnormal_list,
                    'Mouth_Throat_Tongue_Abnormal':Mouth_Throat_Tongue_Abnormal_list,
                    'Mouth_Tonsils_Abnormal': Mouth_Tonsils_Abnormal_list,
                    }
                serializer_class = StationFSerializers8
            elif self.custom_property == "section9":
                serializer_class = StationFSerializers9
            elif self.custom_property == "section10":
                check_SRN(request)
                
                field_lists ={
                    'Specialist_Referral_Needed_Type': Specialist_Referral_Needed_Type
                }
                serializer_class = StationFSerializers10

            validation_result = multiselect.check_field_lists(data, field_lists)
            if validation_result is not None:
                return validation_result
        
            
            station_F_data = serializer_class(station_F_data, data=data, partial=True)
            station_F_data.is_valid(raise_exception=True)
            station_F_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_F_data.data
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