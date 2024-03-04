from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import GetFinalStatusSerializers
from ..models import FinalStatusModel
from infoseek.models import InfoseekVerificationModel
from genericresponse import GenericResponse
from errormessage import Errormessage
from django.db.models import Q
import re



class GlobalSearch(generics.GenericAPIView):
    """Global Search"""
    serializer_class = GetFinalStatusSerializers

   
    def get(self, request,student):


        try:
            
            # name_regex = re.compile(fr'{student}', re.IGNORECASE)
            # query["Name"] = {"$regex": name_regex}
            
            infoseek_data = InfoseekVerificationModel.objects.filter(Q(UIN=student) | Q(Student_FirstName=student))

            if infoseek_data:
                infosekId_list = []
                for i in infoseek_data:
                    print(i.InfoseekId,"info")
                    infoseekId = i.InfoseekId   
                    infosekId_list.append(infoseekId)
                rd_data = FinalStatusModel.objects.filter(InfoseekId__in = infosekId_list)
                if rd_data:
                    pass
                else:
                    raise Exception("There is no data for this User")
            else:
                rd_data = FinalStatusModel.objects.filter(Final_Flag_status = student)
                if rd_data:
                    pass
                else:
                    raise Exception("There is no data for this user")
            

            final_data = GetFinalStatusSerializers(rd_data, many=True)

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = final_data.data
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
            