from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import GetbyHcidUINSerializers,GetStationASerilizers
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from ..models import StationAModel
from  infoseek.models import InfoseekVerificationModel
from stationB.models import StationBModel
from stationB.serializers import GetStationBSerilizers
from stationC.models import StationCModel
from stationC.serializers import GetStationCSerilizers
from stationD.serializers import GetStationDSerilizers
from stationE.serializers import GetStationESerializers
from stationF.serializers import GetStationFSerializers
from stationG.serializers import GetStationGSerializers
from stationH.serializers import GetStationHSerializers
from stationD.models import StationDModel
from stationE.models import StationEModel
from stationF.models import StationFModels
from stationG.models import StationGModel
from stationH.models import StationHModel

class StationDetails(generics.GenericAPIView):
    serializer_class = GetbyHcidUINSerializers
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):

        try:
            UIN = request.data.get('UIN')
            HCID = request.data.get('HCID')
            StationName = request.data.get('StationName')
            infoseek_data = InfoseekVerificationModel.objects.filter(UIN=UIN)
            if infoseek_data:
                for i in infoseek_data:
                    infoseekid = i.InfoseekId

                if StationName == 'StationA':            
                    stationA_data = StationAModel.objects.filter(HCID=HCID, InfoseekId=infoseekid)
                    serializer = GetStationASerilizers(stationA_data, many=True)
                elif StationName == 'StationB':            
                    stationB_data = StationBModel.objects.filter(HCID=HCID, InfoseekId=infoseekid)
                    serializer = GetStationBSerilizers(stationB_data, many=True)
                elif StationName == 'StationC':            
                    stationC_data = StationCModel.objects.filter(HCID=HCID, InfoseekId=infoseekid)
                    serializer = GetStationCSerilizers(stationC_data, many=True)
                elif StationName == 'StationD':            
                    stationD_data = StationDModel.objects.filter(HCID=HCID, InfoseekId=infoseekid)
                    serializer = GetStationDSerilizers(stationD_data, many=True)
                elif StationName == 'StationE':            
                    stationE_data = StationEModel.objects.filter(HCID=HCID, InfoseekId=infoseekid)
                    serializer = GetStationESerializers(stationE_data, many=True)
                elif StationName == 'StationF':            
                    stationF_data = StationFModels.objects.filter(HCID=HCID, InfoseekId=infoseekid)
                    serializer = GetStationFSerializers(stationF_data, many=True)
                elif StationName == 'StationG':            
                    stationG_data = StationGModel.objects.filter(HCID=HCID, InfoseekId=infoseekid)
                    serializer = GetStationGSerializers(stationG_data, many=True)
                elif StationName == 'StationH':            
                    stationH_data = StationHModel.objects.filter(HCID=HCID, InfoseekId=infoseekid)
                    serializer = GetStationHSerializers(stationH_data, many=True)

                else: 
                    serializer = None
                    
                if serializer:
                    serializer = serializer.data
                else:
                    serializer = None
            else:
                serializer = None
                
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = serializer
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