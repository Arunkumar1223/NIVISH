from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from ..serializers import GetHcpIdCardSerializers
from genericresponse import GenericResponse
from errormessage import Errormessage
from ..models import HcpRegistrationModel

class HcpIdCardGetById(generics.GenericAPIView):
    serializer_class = GetHcpIdCardSerializers
    # permission_classes = (IsAuthenticated,)

    def get(self, request, HCPID=None):
        try:
          
            hcp_data = HcpRegistrationModel.objects.filter(HCPID=HCPID)
            hcp_serializers = GetHcpIdCardSerializers(hcp_data, many=True)        
            # note_data = NoteModel.objects.filter(HCPID=HCPID)
            # note_serializers = GetHcpNoteIdCardSerializers(note_data, many=True)

            combined_data = {
                'FullName': hcp_serializers.data[0]['FullName'],
                'Gender': hcp_serializers.data[0]['Gender'],
                'Date_of_Birth': hcp_serializers.data[0]['Date_of_Birth'],
                'Registered_MobileNumber': hcp_serializers.data[0]['Registered_MobileNumber'],
                'Registered_Email': hcp_serializers.data[0]['Registered_Email'],
                'Upload_Your_Photo': hcp_serializers.data[0]['Upload_Your_Photo'],
                'NIV': hcp_serializers.data[0]['NIV'],
                'Hcp_qrcode': hcp_serializers.data[0]['Hcp_qrcode'],
            }

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = combined_data
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
