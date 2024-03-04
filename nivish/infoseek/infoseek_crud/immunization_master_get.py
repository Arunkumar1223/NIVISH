from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from ..serializers import GetImmunizationMasterSerializer
from ..models import ImmunizationModel
from genericresponse import GenericResponse
from errormessage import Errormessage

class ImmunizationGet(generics.GenericAPIView):
    """Here We can get all the Immunization Master Data based on ImmunizationId        
         Table_Name:'Immunization_Master')"""
    serializer_class = GetImmunizationMasterSerializer

    def get(self, request,ImmunizationId = None):

        try:
            data = ImmunizationModel.objects.filter(ImmunizationId=ImmunizationId)
            serializer_class = GetImmunizationMasterSerializer(data, many=True)
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