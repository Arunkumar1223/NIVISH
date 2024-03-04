import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import StationDSerializers2, StationDSerializers3, StationDSerializers4
from ..models import *
from errormessage import Errormessage
from Multiselect.multiselectLists import *
from Multiselect.multiselectFunction import *
from Validations.Specialist_Referral_Needed import check_SRN
from Validations.StationD_Validations import *
from logs_data import logsFun
from Models_logs.stations_models_logs import StationDModel_Log

class DynamicSerializerMixin:
    def get_serializer_class(self):
        # Implement your logic to determine the serializer class dynamically
             
        if self.custom_property == "section2":
            return StationDSerializers2
        elif self.custom_property == "section3":
            return StationDSerializers3
        elif self.custom_property == "section4":
            return StationDSerializers4

class StationDDetailsS2(DynamicSerializerMixin, generics.GenericAPIView):
    #serializer_class = StationCSerializers2
    custom_property = None
    def __init__(self, *args, **kwargs):
        # Capture any custom keyword arguments passed during instantiation
        self.custom_property = kwargs.pop('custom_property', None)
        super().__init__(*args, **kwargs)

    def put(self, request, id):
        print("put")
        print(self.request.path_info)
        try:
            station_D_data = StationDModel.objects.get(id=id)
            station_D_logs = StationDModel_Log()

            logs_updated = logsFun(station_D_logs,station_D_data)
            data=request.data
            field_lists = {}
            if self.custom_property == "section2":
                check_Visual_inspection_Right_Ear_Pinna(request)
                check_Visual_inspection_Right_Ear_EarCanal(request)
                check_Visual_inspection_Left_Ear_Pinna(request)
                check_Visual_inspection_Left_Ear_EarCanal(request)

                serializer_class = StationDSerializers2
            elif self.custom_property == "section3":
                check_Pure_Tone_Audiometry_Right_Ear_500Hz_25dB(request)
                check_Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB(request)
                check_Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB(request)
                check_Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB(request)
                check_Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB(request)
                check_Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB(request)

                check_Pure_Tone_Audiometry_Left_Ear_500Hz_25dB(request)
                check_Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB(request)
                check_Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB(request)
                check_Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB(request)
                check_Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB(request)
                check_Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB(request)

                serializer_class = StationDSerializers3
            
            elif self.custom_property == "section4":
                check_SRN(request)
                field_lists ={
                    'Specialist_Referral_Needed_Type': Specialist_Referral_Needed_Type
                }
                serializer_class = StationDSerializers4

            
            validation_result = multiselect.check_field_lists(data, field_lists)
            if validation_result is not None:
                return validation_result
          
            station_D_data = serializer_class(station_D_data, data=data, partial=True)
            station_D_data.is_valid(raise_exception=True)
            station_D_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_D_data.data
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