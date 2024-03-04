import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import UpdateFinalStatusSerializers,GetFinalStatusSerializers
from ..models import *
from errormessage import Errormessage


class UpdateFinalStatusRD(generics.GenericAPIView):
    serializer_class = UpdateFinalStatusSerializers

    def put(self, request, UIN):
        try:
            
            r = FinalStatusModel.objects.get(UIN=UIN)
            Reviewed_by = request.data.get('Reviewed_by')
            print(Reviewed_by,'Reviewed_by')

            s = UpdateFinalStatusSerializers(r,data=request.data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = s.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)