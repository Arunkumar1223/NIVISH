from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import Getobservationserializers
from stationA.models import StationAModel
from stationB.models import StationBModel
from stationC.models import StationCModel
from stationD.models import StationDModel
from stationE.models import StationEModel
from stationF.models import StationFModels
from stationG.models import StationGModel
from stationH.models import StationHModel
from errormessage import Errormessage


class GetObservations(generics.GenericAPIView):
    serializer_class = Getobservationserializers 


    def get(self,request,HCID,InfoseekId):
        try:
            response_data = []
            StationAdata = StationAModel.objects.filter(HCID=HCID,InfoseekId_id=InfoseekId)
            for Loop_StationA in StationAdata:
                response_data.append({"Other_Observations_A": Loop_StationA.Other_Observations})

            StationBdata = StationBModel.objects.filter(HCID=HCID,InfoseekId_id=InfoseekId)
            for Loop_StationB in StationBdata:
                response_data.append({"Other_Observations_B":  Loop_StationB.Other_Observations})

            StationCdata = StationCModel.objects.filter(HCID=HCID,InfoseekId_id=InfoseekId)
            for Loop_StationC in StationCdata:
                response_data.append({"Other_Observations_C":  Loop_StationC.Other_Observations})

            StationDdata = StationDModel.objects.filter(HCID=HCID,InfoseekId_id=InfoseekId)
            for Loop_StationD in StationDdata:
                response_data.append({"Other_Observations_D":  Loop_StationD.Other_Observations})

            StationEdata = StationEModel.objects.filter(HCID=HCID,InfoseekId_id=InfoseekId)
            for Loop_StationE in StationEdata:
                response_data.append({"Other_Observations_E":  Loop_StationE.Other_Observations})


            StationFdata = StationFModels.objects.filter(HCID=HCID,InfoseekId_id=InfoseekId)
            for Loop_StationF in StationFdata:
                response_data.append({"Other_Observations_F":  Loop_StationF.Other_Observations})

            StationGdata = StationGModel.objects.filter(HCID=HCID,InfoseekId_id=InfoseekId)
            for Loop_StationG in StationGdata:
                response_data.append({"Other_Observations_G":  Loop_StationG.Other_Observations})

            StationHdata = StationHModel.objects.filter(HCID=HCID,InfoseekId_id=InfoseekId)
            for Loop_StationH in StationHdata:
                response_data.append({"Other_Observations_H":  Loop_StationH.Other_Observations})

            
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
            


