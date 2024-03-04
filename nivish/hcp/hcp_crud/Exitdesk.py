from rest_framework.views import APIView
from rest_framework.response import Response
from genericresponse import GenericResponse
from errormessage import Errormessage
from infoseek.models import InfoseekVerificationModel
from stationA.models import StationAModel
from stationB.models import StationBModel
from stationC.models import StationCModel
from stationD.models import StationDModel
from stationE.models import StationEModel
from stationF.models import StationFModels
from stationG.models import StationGModel
from stationH.models import StationHModel
from infoseek.serializers import GetAllInfoseekSerializers
from stationA.serializers import GetStationASerilizers
from stationB.serializers import GetStationBSerilizers
from stationC.serializers import GetStationCSerilizers
from stationD.serializers import GetStationDSerilizers
from stationE.serializers import GetStationESerializers
from stationF.serializers import GetStationFSerializers
from stationG.serializers import GetStationGSerializers
from stationH.serializers import GetStationHSerializers
from rest_framework.utils import json

class ExitdeskGet(APIView):

    serializer_class_infoseek = GetAllInfoseekSerializers
    serializer_class_station_a = GetStationASerilizers
    serializer_class_station_b = GetStationBSerilizers
    serializer_class_station_c = GetStationCSerilizers
    serializer_class_station_d = GetStationDSerilizers
    serializer_class_station_e = GetStationESerializers
    serializer_class_station_f = GetStationFSerializers
    serializer_class_station_g = GetStationGSerializers
    serializer_class_station_h = GetStationHSerializers

    def get(self, request, HCID, UIN):
        try:
            data_infoseek = InfoseekVerificationModel.objects.filter(UIN=UIN)

            if data_infoseek:
                for i in data_infoseek:
                    b = i.InfoseekId
                    break
                b = b
                # print(b,"b")
            else:
                return Response({"message": "No Infoseek data found for UIN {}".format(UIN)})

            station_models = [
                StationAModel, StationBModel, StationCModel,
                StationDModel, StationEModel, StationFModels,
                StationGModel, StationHModel
            ]
            print(len(station_models),'len')
            # print(station_models,"station_models")

            stations_status = []
            count = 1

            for  model, serializer_class in zip(station_models, [self.serializer_class_station_a, self.serializer_class_station_b, self.serializer_class_station_c, self.serializer_class_station_d, self.serializer_class_station_e, self.serializer_class_station_f, self.serializer_class_station_g, self.serializer_class_station_h]):
                data_station = model.objects.filter(HCID=HCID, InfoseekId=b)

                if data_station:
                    for station_data in data_station:
                        check = station_data.Completed
                        serializer = serializer_class(station_data)
                        station_info = {
                            'StationID': serializer.data.get('StationID'),
                            'Completed': check
                        }
                        stations_status.append(station_info)
                else:
                    print(model,"model")
                    station_info = {
                            'StationID': count,
                            'Completed': 'No'
                        }
                    stations_status.append(station_info)
                count = count + 1
            response_data = {
                "StationsStatus": stations_status
            }

            # print(response_data,"response_data")

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = response_data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)           
        except Exception as e:
            response = GenericResponse("message", "result", "status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)