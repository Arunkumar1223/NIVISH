from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from ..serializers import GetAllInfoseekSerializers
from ..models import InfoseekVerificationModel
from genericresponse import GenericResponse
from errormessage import Errormessage

class UINInfoseekGet(generics.GenericAPIView):
    """Here We can get all the Infoseek data based on UIN number
        (Here UIN is nothing but Student UIN number)      
         Table_Name:'Infoseek')"""
    serializer_class = GetAllInfoseekSerializers

    def get(self, request,UIN = None):

        try:
            data = InfoseekVerificationModel.objects.filter(UIN=UIN)
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