from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from super_admin.serializers import GetHealthCampTeamsSerializers
from super_admin.models import HealthCampTeamsModel,HcIdTeamIdModel,HcpIdTeamIdModel
from genericresponse import GenericResponse
from errormessage import Errormessage
from stationA.models import StationAModel
from stationA.serializers import GetStationASerilizers
from stationB.models import StationBModel
from stationB.serializers import GetStationBSerilizers

class HealthCampTeamsGetTeamName(generics.GenericAPIView):
    serializer_class = GetHealthCampTeamsSerializers
    # permission_classes = (IsAuthenticated,)

    def get(self, request,TeamName = None):
        try:
            team_data = HealthCampTeamsModel.objects.filter(TeamName=TeamName)

            for i in team_data:
                teamid = i.id

            hcpid_data = HcpIdTeamIdModel.objects.filter(TeamId=teamid)


            hcpids = []
            for j in hcpid_data:
                hcpid_data = j.HCPID
                hcpid = (j.HCPID_id)
                hcpids.append(hcpid)
            
            
            hcid_data = HcIdTeamIdModel.objects.filter(TeamId=teamid)
            for a in hcid_data:
                hcid_data = a.HCID
                hcid = (a.HCID_id)
                
            stationA_data_list = []
            for k in hcpids:
                stationA_data = StationAModel.objects.filter(HCPID=k,HCID=hcid)
                if stationA_data:
                    
                    serialized_data = GetStationASerilizers(stationA_data, many=True).data
                    stationA_data_list.append(serialized_data)
                    # print(stationA_data,"data")
          
            stationB_data_list = []
            for s in hcpids:
                stationB_data = StationBModel.objects.filter(HCPID=s,HCID=hcid)
                if stationB_data:
                    serializer = GetStationBSerilizers(stationB_data,many=True).data
                    stationB_data_list.append(serializer)


            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"           
            response.Result = {"StationA":stationA_data_list,"StationB":stationB_data_list}           
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
        
