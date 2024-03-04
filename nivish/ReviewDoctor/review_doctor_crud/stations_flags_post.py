from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import FlagsSerializers,GetFlagsSerializers
from ..models import AllStationsFlags
from errormessage import Errormessage



class StationsFlagsPost(generics.GenericAPIView):
    serializer_class = FlagsSerializers 

    def post(self, request, *args, **kwargs):
        try:
            InfoseekId = request.data.get('InfoseekId')
            Hcid = request.data.get("HCID")
            if AllStationsFlags.objects.filter(HCID=Hcid, InfoseekId=InfoseekId):
                raise Exception("This Infoseek already exists with Hcid")
            

            else:   
                stationsflags = FlagsSerializers(data=request.data)
                stationsflags.is_valid(raise_exception=True)
                user = stationsflags.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = GetFlagsSerializers(user).data
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
                 

