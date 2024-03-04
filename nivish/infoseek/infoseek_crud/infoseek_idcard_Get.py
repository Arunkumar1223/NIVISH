from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import InfoseekIdCardGetSerializer
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from ..models import InfoseekVerificationModel,NoteModel





class InfoseekIdCardGet(generics.GenericAPIView):
    """Here We can retrieve Note data based on 
       an InfoseekId from the "InfoseekNote" table"""
    serializer_class = InfoseekIdCardGetSerializer
    # permission_classes = (IsAuthenticated,)

    def get(self, request, InfoseekId=None):
        try:
            data = InfoseekVerificationModel.objects.get(InfoseekId=InfoseekId)

            serializer_class = InfoseekIdCardGetSerializer(data)
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