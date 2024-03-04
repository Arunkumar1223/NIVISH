import datetime
import json
from django.test import RequestFactory
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import StationHSerializers2,StationHSerializers3,StationHSerializers4,StationHSerializers5,StationHSerializers6
from ..models import *
from errormessage import Errormessage
from Multiselect.multiselectLists import *
from Multiselect.multiselectFunction import *
from Validations.StationH_Validations import *
from Validations.Specialist_Referral_Needed import check_SRN
from logs_data import logsFun
from Models_logs.stations_models_logs import StationHModel_Log


class DynamicSerializerMixin:
    def get_serializer_class(self):
        # Implement your logic to determine the serializer class dynamically
        
        
        if self.custom_property == "section2":
          return StationHSerializers2
        elif self.custom_property == "section3":
            return StationHSerializers3
        elif self.custom_property == "section4":
            return StationHSerializers4
        elif self.custom_property == "section5":
            return StationHSerializers5
        elif self.custom_property == "section6":
            return StationHSerializers6
        
        
        

class StationHDetailsS2(DynamicSerializerMixin, generics.GenericAPIView):
    
    custom_property = None
    def __init__(self, *args, **kwargs):
        # Capture any custom keyword arguments passed during instantiation
        self.custom_property = kwargs.pop('custom_property', None)
        super().__init__(*args, **kwargs)

    def put(self, request, id):
        print("put")
        print(self.request.path_info)
        try:
            station_H_data = StationHModel.objects.get(id=id)
            station_H_logs = StationHModel_Log()

            logs_updated = logsFun(station_H_logs,station_H_data)
            data=request.data
            field_lists = {}
            if self.custom_property == "section2": 
                serializer_class = StationHSerializers2

            elif self.custom_property == "section3":
                check_Braces(request)
                check_Bridges(request)
                check_Dentures(request)
                field_lists ={
                  'Braces_Yes' : Braces_list,
                  'Bridges_Yes' : Braces_list,
                  'Dentures_Yes' : Dentures_List, 
                  }                     
                serializer_class = StationHSerializers3

            elif self.custom_property == "section4":
                check_Soft_Tissue_Pathology(request)
                check_Treatment_Needed(request)
                field_lists ={
                  'Soft_Tissue_Pathology_Yes' : Soft_Tissue_Pathology,
                  'Treatment_Needed_Yes' : Treatment_Needed, 
                  }                     
                
                serializer_class = StationHSerializers4
            elif self.custom_property == "section5":
                check_SRNDental(request)
                serializer_class = StationHSerializers5
            elif self.custom_property == "section6":
                check_SRN(request)
                field_lists ={
                    'Specialist_Referral_Needed_Type': Specialist_Referral_Needed_Type
                }
                serializer_class = StationHSerializers6

            validation_result = multiselect.check_field_lists(data, field_lists)
            if validation_result is not None:
                return validation_result 
        
            
            station_H_data = serializer_class(station_H_data, data=data, partial=True)
            station_H_data.is_valid(raise_exception=True)
            station_H_data.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = station_H_data.data
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