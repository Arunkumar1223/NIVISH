from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import RegistrationDeskSerializers,GetRegistrationDeskSerializers
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from ..models import RegistrationDeskModel



class RegistrationDeskPost(generics.GenericAPIView):
    serializer_class = RegistrationDeskSerializers
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            hcid = request.data.get('HCID')
            uin = request.data.get('UIN')

            deskpost = RegistrationDeskModel.objects.filter(HCID=hcid,UIN=uin)
            print(deskpost,"post")
            if deskpost:
                for i in deskpost:                
                    user = i
                    print(user,"user")

            else:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                user = serializer.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = GetRegistrationDeskSerializers(user).data
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
