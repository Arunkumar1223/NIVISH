from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json

from genericresponse import GenericResponse
from errormessage import Errormessage

from stationA.models import StationAModel
from stationB.models import StationBModel
from stationC.models import StationCModel
from stationD.models import StationDModel
from stationE.models import StationEModel
from stationF.models import StationFModels
from stationG.models import StationGModel
from stationH.models import StationHModel
from infoseek.models import InfoseekVerificationModel
from infoseek.serializers import GetAllInfoseekSerializers

from stationA.serializers import GetStationASerilizers
from stationB.serializers import GetStationBSerilizers
from stationC.serializers import GetStationCSerilizers
from stationD.serializers import GetStationDSerilizers
from stationE.serializers import GetStationESerializers
from stationF.serializers import GetStationFSerializers
from stationG.serializers import GetStationGSerializers
from stationH.serializers import GetStationHSerializers

class ReviewdoctorGet(generics.GenericAPIView):
    serializer_classes = {
        StationAModel: GetStationASerilizers,
        StationBModel: GetStationBSerilizers,
        StationCModel: GetStationCSerilizers,
        StationDModel: GetStationDSerilizers,
        StationEModel: GetStationESerializers,
        StationFModels: GetStationFSerializers,
        StationGModel: GetStationGSerializers,
        StationHModel: GetStationHSerializers,
    }

    def get(self, request, HCID):
        """Here we are getting Infoseek data by using HCID-"""
        try:
            infoseek_ids = set()

            for model, serializer_class in self.serializer_classes.items():
                data_station = model.objects.filter(HCID=HCID)
                if data_station:
                    for station_data in data_station:
                        serializer = serializer_class(station_data)
                        infoseek_ids.add(serializer.data.get('InfoseekId'))

            infoseek_ids_list = list(infoseek_ids)
            final_infoseek_data = []
            for id in infoseek_ids_list:
                infoseek_data = InfoseekVerificationModel.objects.get(InfoseekId = int(id))
                final_infoseek_data.append(infoseek_data)
            

            
            print(final_infoseek_data)
            response_data = {
                "Infoseek_Data": GetAllInfoseekSerializers(final_infoseek_data,many=True).data
            }

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = response_data
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
