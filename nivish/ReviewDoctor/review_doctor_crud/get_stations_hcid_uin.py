import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from stationA.serializers import GetStationASerilizers
from stationB.serializers import GetStationBSerilizers
from stationC.serializers import GetStationCSerilizers
from stationD.serializers import GetStationDSerilizers
from stationE.serializers import GetStationESerializers
from stationF.serializers import GetStationFSerializers
from stationG.serializers import GetStationGSerializers
from stationH.serializers import GetStationHSerializers
from stationA.models import StationAModel
from stationB.models import StationBModel
from stationC.models import StationCModel
from stationD.models import StationDModel
from stationE.models import StationEModel
from stationF.models import StationFModels
from stationG.models import StationGModel
from stationH.models import StationHModel
from infoseek.models import InfoseekVerificationModel
from errormessage import Errormessage
from ..serializers import GetbyHcidUINSerializer

class GetByHcidUINDetails(generics.GenericAPIView):
    serializer_class = GetbyHcidUINSerializer

    def post(self, request, *args, **kwargs):
        try:
            hcid_string = request.data.get('HCID', '')
            hcid_list = list(map(int, hcid_string.split(','))) 
            UIN = request.data.get('UIN')
            StationName = request.data.get('StationName')
            infoseek_data = InfoseekVerificationModel.objects.get(UIN=UIN)
            combined_data = {}
            
            if StationName == 'StationA':            
                station_a_data = StationAModel.objects.filter(HCID__in=hcid_list, InfoseekId=infoseek_data.InfoseekId)
                serializer = GetStationASerilizers(station_a_data, many=True)

            elif StationName == 'StationB':
                station_b_data = StationBModel.objects.filter(HCID__in=hcid_list, InfoseekId=infoseek_data.InfoseekId)
                serializer = GetStationBSerilizers(station_b_data, many=True)

            elif StationName == 'StationC':
                station_c_data = StationCModel.objects.filter(HCID__in=hcid_list, InfoseekId=infoseek_data.InfoseekId)
                serializer = GetStationCSerilizers(station_c_data, many=True)

            elif StationName == 'StationD':
                station_d_data = StationDModel.objects.filter(HCID__in=hcid_list, InfoseekId=infoseek_data.InfoseekId)
                serializer = GetStationDSerilizers(station_d_data, many=True)
 
            elif StationName == 'StationE':
                station_e_data = StationEModel.objects.filter(HCID__in=hcid_list, InfoseekId=infoseek_data.InfoseekId)
                serializer = GetStationESerializers(station_e_data, many=True)

            elif StationName == 'StationF':
                station_f_data = StationFModels.objects.filter(HCID__in=hcid_list, InfoseekId=infoseek_data.InfoseekId)
                serializer = GetStationFSerializers(station_f_data, many=True)

            elif StationName == 'StationG':
                station_g_data = StationGModel.objects.filter(HCID__in=hcid_list, InfoseekId=infoseek_data.InfoseekId)
                serializer = GetStationGSerializers(station_g_data, many=True)

            elif StationName == 'StationH':
                station_h_data = StationHModel.objects.filter(HCID__in=hcid_list, InfoseekId=infoseek_data.InfoseekId)
                serializer = GetStationHSerializers(station_h_data, many=True)
            else:
                pass

            

            if serializer:
                combined_data[StationName] = serializer.data
            
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = combined_data
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
