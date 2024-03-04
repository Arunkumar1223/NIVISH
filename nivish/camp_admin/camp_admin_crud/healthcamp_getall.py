from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from genericresponse import GenericResponse
from errormessage import Errormessage

from ..serializers import CampStationsStatusSerializers

from stationA.models import StationAModel
from stationB.models import StationBModel
from stationC.models import StationCModel
from stationD.models import StationDModel
from stationE.models import StationEModel
from stationF.models import StationFModels
from stationG.models import StationGModel
from stationH.models import StationHModel
from hcp.models import AssignmentModel,RegistrationDeskModel


def process_station_data(data):
    Emergency_list = [item for item in data if item.Specialist_Referral_Needed_Flag == 'Emergency']
    Non_Urgent_list = [item for item in data if item.Specialist_Referral_Needed_Flag == 'Non-Urgent']
    Urgent_list = [item for item in data if item.Specialist_Referral_Needed_Flag == 'Urgent']
    station_specilist = [item for item in data if item.Specialist_Referral_Needed == "No"]

    return {
        "Completed": len(data),
        "Emergency": len(Emergency_list),
        "Urgent": len(Urgent_list),
        "Non-Urgent": len(Non_Urgent_list),
        "WNL": len(station_specilist)
    }


class CampStationsStatus(generics.GenericAPIView):
    serializer_class = CampStationsStatusSerializers
    # permission_classes = (IsAuthenticated,)

    def post(self, request,HCID=None,):

        try:
            TeamId = request.data.get('TeamId')
            HCID = request.data.get('HCID')
            Date = request.data.get('Date')
            
            if TeamId is None and Date is None:
                data_stationA = StationAModel.objects.filter(HCID=HCID, Completed="Yes")
                stationA = process_station_data(data_stationA)

                data_stationB = StationBModel.objects.filter(HCID=HCID, Completed="Yes")
                stationB = process_station_data(data_stationB)

                data_stationC = StationCModel.objects.filter(HCID=HCID,Completed="Yes")
                stationC = process_station_data(data_stationC)

    
                data_stationD = StationDModel.objects.filter(HCID=HCID,Completed="Yes")
                stationD = process_station_data(data_stationD)


                
                data_stationE = StationEModel.objects.filter(HCID=HCID,Completed="Yes")
                stationE = process_station_data(data_stationE)

    
                data_stationF = StationFModels.objects.filter(HCID=HCID,Completed="Yes")
                stationF = process_station_data(data_stationF)

            

                data_stationG = StationGModel.objects.filter(HCID=HCID,Completed="Yes")
                stationG = process_station_data(data_stationG)


                data_stationH = StationHModel.objects.filter(HCID=HCID,Completed="Yes")
                stationH = process_station_data(data_stationH)

                result = {"StationA": stationA,
                               "StationB": stationB,
                               "StationC": stationC,
                               "StationD": stationD,
                               "StationE": stationE,
                               "StationF": stationF,
                               "StationG": stationG,
                               "StationH": stationH,
                               
                               }
            elif TeamId == 4:

                print(TeamId)
                
                Team_O_Assignments = AssignmentModel.objects.filter(HCID=HCID,TeamId=int(TeamId))
                
                Ass_Register_desk_user = []
                Ass_Exit_desk_user = []
                
                for Team_O_Assignments_loop in Team_O_Assignments:
                    stationid = Team_O_Assignments_loop.StationID
                    stationid = stationid.id
                    if stationid == 101:
                        Ass_Register_desk_user.append(Team_O_Assignments_loop)
                    elif stationid == 102:
                        Ass_Exit_desk_user.append(Team_O_Assignments_loop)

                if Ass_Register_desk_user:
                    for Ass_Register_desk_user_loop in Ass_Register_desk_user:
                        Reg_desk = RegistrationDeskModel.objects.filter(RegisteredBy=Ass_Register_desk_user_loop.HCPID_id)
                        len_of_Reg_desk = len(Reg_desk)
                        break
                else:
                  len_of_Reg_desk = []

                   
                if Ass_Exit_desk_user:
                    for Ass_Exit_desk_user_loop in Ass_Exit_desk_user:
                        Exit_desk = RegistrationDeskModel.objects.filter(ExitedBy=Ass_Exit_desk_user_loop.HCPID_id)
                        len_of_Exit_desk = len(Exit_desk)
                        break
                else:
                  len_of_Exit_desk = []


                result = {
                    'Registrations' : len_of_Reg_desk,
                        'Exit' : len_of_Exit_desk
                    }

            else:

                Assaigments = AssignmentModel.objects.filter(HCID=HCID,TeamId=int(TeamId))
                hcid_list = []

                if Assaigments:
                    for Assaigments_loop in Assaigments:
                        hcpid = Assaigments_loop.HCPID
                        hcpid = hcpid.HCPID
                        hcid_list.append(hcpid)

                print(hcid_list,"hcid_list")
                


                data_stationA = StationAModel.objects.filter(HCID=HCID,HCPID__in = hcid_list, Completed="Yes")
                stationA = process_station_data(data_stationA)


                data_stationB = StationBModel.objects.filter(HCID=HCID,HCPID__in = hcid_list, Completed="Yes")
                stationB = process_station_data(data_stationB)

                data_stationC = StationCModel.objects.filter(HCID=HCID,HCPID__in = hcid_list,Completed="Yes")
                stationC = process_station_data(data_stationC)

    
                data_stationD = StationDModel.objects.filter(HCID=HCID,HCPID__in = hcid_list,Completed="Yes")
                stationD = process_station_data(data_stationD)


                
                data_stationE = StationEModel.objects.filter(HCID=HCID,HCPID__in = hcid_list,Completed="Yes")
                stationE = process_station_data(data_stationE)

    
                data_stationF = StationFModels.objects.filter(HCID=HCID,HCPID__in = hcid_list,Completed="Yes")
                stationF = process_station_data(data_stationF)

            

                data_stationG = StationGModel.objects.filter(HCID=HCID,HCPID__in = hcid_list,Completed="Yes")
                stationG = process_station_data(data_stationG)


                data_stationH = StationHModel.objects.filter(HCID=HCID,HCPID__in = hcid_list,Completed="Yes")
                stationH = process_station_data(data_stationH)

                result = {"StationA": stationA,
                               "StationB": stationB,
                               "StationC": stationC,
                               "StationD": stationD,
                               "StationE": stationE,
                               "StationF": stationF,
                               "StationG": stationG,
                               "StationH": stationH,
                               
                               }



            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = result
            
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