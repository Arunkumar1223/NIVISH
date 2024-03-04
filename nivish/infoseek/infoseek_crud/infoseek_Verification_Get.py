from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from ..serializers import GetAllInfoseekSerializers
from ..models import InfoseekVerificationModel
from genericresponse import GenericResponse
from errormessage import Errormessage

class InfoseekVerficationDetails(generics.GenericAPIView):
    """Here We can get the Infoseek Verification details based on InfoseekId and 
        Get All The Infoseek Verification Details
         Table_Name:'Infoseek')"""
    serializer_class = GetAllInfoseekSerializers

    def get(self, request,InfoseekId = None):
        try:
            if InfoseekId == None:
                
                data = InfoseekVerificationModel.objects.all()
            else:
                data = InfoseekVerificationModel.objects.filter(InfoseekId=InfoseekId)

            

            serializer_class = GetAllInfoseekSerializers(data, many=True)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = serializer_class.data
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