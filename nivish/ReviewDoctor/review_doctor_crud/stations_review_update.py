import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from stationA.models import StationAModel
from stationB.models import StationBModel
from stationC.models import StationCModel
from stationD.models import StationDModel
from stationE.models import StationEModel
from stationF.models import StationFModels
from stationG.models import StationGModel
from stationH.models import StationHModel
from ..serializers import UpdateStationAReviewDoctorSerializers,UpdateStationBReviewDoctorSerializers,UpdateStationCReviewDoctorSerializers,UpdateStationDReviewDoctorSerializers,UpdateStationEReviewDoctorSerializers,UpdateStationFReviewDoctorSerializers,UpdateStationFReviewDoctorSerializers,UpdateStationGReviewDoctorSerializers,UpdateStationHReviewDoctorSerializers
from errormessage import Errormessage



class DynamicSerializerMixin:
    def get_serializer_class(self):
        if self.custom_property == "RDUpdatestationA":
            return UpdateStationAReviewDoctorSerializers
        elif self.custom_property == "RDUpdatestationB":
            return UpdateStationBReviewDoctorSerializers
        elif self.custom_property == "RDUpdatestationC":
            return UpdateStationCReviewDoctorSerializers
        elif self.custom_property == "RDUpdatestationD":
            return UpdateStationDReviewDoctorSerializers
        elif self.custom_property == "RDUpdatestationE":
            return UpdateStationEReviewDoctorSerializers
        elif self.custom_property == "RDUpdatestationF":
            return UpdateStationFReviewDoctorSerializers
        elif self.custom_property == "RDUpdatestationG":
            return UpdateStationGReviewDoctorSerializers
        elif self.custom_property == "RDUpdatestationH":
            return UpdateStationHReviewDoctorSerializers
        
        
        



class UpdateRDstations(DynamicSerializerMixin, generics.GenericAPIView):
    custom_property = None
    def __init__(self, *args, **kwargs):
        self.custom_property = kwargs.pop('custom_property', None)
        super().__init__(*args, **kwargs)

    def put(self, request, id):
        print("put")
        print(self.request.path_info)
        try:
            data = request.data
            if self.custom_property == "RDUpdatestationA":
                serializer_class = UpdateStationAReviewDoctorSerializers
                r = StationAModel.objects.get(id=id)
                
            elif self.custom_property == "RDUpdatestationB":
                serializer_class = UpdateStationBReviewDoctorSerializers
                r = StationBModel.objects.get(id=id)
            
            elif self.custom_property == "RDUpdatestationC":
                serializer_class = UpdateStationCReviewDoctorSerializers
                r = StationCModel.objects.get(id=id)

            elif self.custom_property == "RDUpdatestationD":
                serializer_class = UpdateStationDReviewDoctorSerializers
                r = StationDModel.objects.get(id=id)
            
            elif self.custom_property == "RDUpdatestationE":
                serializer_class = UpdateStationEReviewDoctorSerializers
                r = StationEModel.objects.get(id=id)
            

            elif self.custom_property == "RDUpdatestationF":
                serializer_class = UpdateStationFReviewDoctorSerializers
                r = StationFModels.objects.get(id=id)
            

            elif self.custom_property == "RDUpdatestationG":
                serializer_class = UpdateStationGReviewDoctorSerializers
                r = StationGModel.objects.get(id=id)
            

            elif self.custom_property == "RDUpdatestationH":
                serializer_class = UpdateStationHReviewDoctorSerializers
                r = StationHModel.objects.get(id=id)
            
            
            serializer = serializer_class(r, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = serializer.data
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






