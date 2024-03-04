import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import StationCSerializers2, StationCSerializers3, StationCSerializers4, StationCSerializers5
from ..models import *
from errormessage import Errormessage
from Multiselect.multiselectLists import *
from Multiselect.multiselectFunction import *
from Validations.StationC_Validations import *
from Validations.Specialist_Referral_Needed import check_SRN
from logs_data import logsFun


class DynamicSerializerMixin:
    def get_serializer_class(self):
        # Implement your logic to determine the serializer class dynamically
             
        if self.custom_property == "section2":
            return StationCSerializers2
        elif self.custom_property == "section3":
            return StationCSerializers3
        elif self.custom_property == "section4":
            return StationCSerializers4
        elif self.custom_property == "section5":
            return StationCSerializers5

class StationCDetailsS2(DynamicSerializerMixin, generics.GenericAPIView):
    #serializer_class = StationCSerializers2
    custom_property = None
    def __init__(self, *args, **kwargs):
        # Capture any custom keyword arguments passed during instantiation
        self.custom_property = kwargs.pop('custom_property', None)
        super().__init__(*args, **kwargs)

    def put(self, request, id):
        print(id,"put")
        print(self.request.path_info)
        try:
            station_C_data = StationCModel.objects.get(id=id)
          
            station_C_logs = StationCModel_Log()

            logs_updated = logsFun(station_C_logs,station_C_data)

            
            data=request.data
            field_lists = {}
            if self.custom_property == "section2":
                serializer_class = StationCSerializers2
                
            elif self.custom_property == "section3":
                check_Visually_Challenged(request)
                field_lists ={
                    'Visually_Challenged_Right_Eye_Enucleation_Why_removed' : Visually_Challenged_Right_Eye_Enucleation_list,
                    'Visually_Challenged_Left_Eye_Enucleation_Why_removed': Visually_Challenged_Right_Eye_Enucleation_list,
                    'Visually_Challenged_Right_Eye_Enucleation_No': Eye_Enucleation_No_list,
                    'Visually_Challenged_Left_Eye_Enucleation_No': Eye_Enucleation_No_list,
                  }                     
                serializer_class = StationCSerializers3
            elif self.custom_property == "section4":
                check_Visual_Acuity_Color_Blindness(request)
                serializer_class = StationCSerializers4
            elif self.custom_property == "section5":
                check_SRN(request)
                field_lists ={
                    'Specialist_Referral_Needed_Type': Specialist_Referral_Needed_Type
                }
                serializer_class = StationCSerializers5

            
            validation_result = multiselect.check_field_lists(data, field_lists)
            if validation_result is not None:
                return validation_result
          
            station_C_data = serializer_class(station_C_data, data=data, partial=True)
            station_C_data.is_valid(raise_exception=True)
            station_C_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_C_data.data
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