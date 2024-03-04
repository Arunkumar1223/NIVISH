from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import FinalStatusSerializers,GetFinalStatusSerializers
from ..models import FinalStatusModel
from errormessage import Errormessage





class FinalStatusPost(generics.GenericAPIView):
    serializer_class = FinalStatusSerializers

    def post(self, request, *args, **kwargs):
        try:

            InfoseekId = request.data.get('InfoseekId')

            final_status_data = FinalStatusModel.objects.filter(InfoseekId_id = InfoseekId)
            if final_status_data: 
                print("Data already exits")
                raise Exception('Data already exits')
            else:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = GetFinalStatusSerializers(user).data 
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
