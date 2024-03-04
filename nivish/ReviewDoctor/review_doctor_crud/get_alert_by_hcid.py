from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from ReviewDoctor.serializers import AlertSerializer
from ReviewDoctor.models import FinalStatusModel 
from genericresponse import GenericResponse
from errormessage import Errormessage

class AlertAPI(generics.GenericAPIView):
    serializer_class = AlertSerializer 


    def get(self,request,HCID):
        try:
            HCIDdata = FinalStatusModel.objects.filter(HCID=HCID).exclude(Review_status="Review Completed")
            HCID_Serializer = AlertSerializer(HCIDdata, many=True)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = HCID_Serializer.data
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
            

