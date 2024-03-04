from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import GetFinalStatusSerializers
from ..models import FinalStatusModel
from genericresponse import GenericResponse
from errormessage import Errormessage



class GetAllInfoseekWNL(generics.GenericAPIView):
    """Here We can get all the Infoseek UIN Which is having WNL for Flag field  { Collection:'Review_Doctor' }"""
    serializer_class = GetFinalStatusSerializers

   
    def get(self, request,HCID):


        try:
            
            RD_data = FinalStatusModel.objects.filter(Final_Flag_status = 'WNL',HCID=HCID).exclude(Review_status = "Review Completed") 

            UIN_List = []
            
            for i in RD_data:
                UIN_List.append(i.UIN)
                
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = UIN_List
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
            