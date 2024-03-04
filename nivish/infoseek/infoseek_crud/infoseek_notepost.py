from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import *
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from Validations.Hcp_Validations import *
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
import json
from io import BytesIO
import qrcode

@parser_classes((MultiPartParser,))



class NotePost(generics.GenericAPIView):
    """Here We can post the Note Data based on InfoseekId
          (Table_Name:'InfoseekNote')"""

    serializer_class = InfoseekNoteSerializers

    def generate_qrcode(self, data):
        qr_data = json.dumps(data)
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        return buffer.getvalue()
    
    def post(self, request, *args, **kwargs):
        try:
            InfoseekId = request.data.get('InfoseekId')
            r = InfoseekVerificationModel.objects.get(InfoseekId=InfoseekId)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            # Update InfoseekVerificationModel instance
            uin = r.UIN
            if uin is None:
                random_number = str(r.InfoseekId) + str(random.randint(1, 99999999999))
                print(random_number)
                r.UIN = random_number
                r.save()

            qr_data = f"UIN: {r.UIN}"
            qr_code_image = self.generate_qrcode(qr_data)
            
            # Update qrcode_image in InfoseekVerificationModel instance
            r.qrcode_image.save(f'qrcode_{InfoseekId}.png', ContentFile(qr_code_image), save=False)
            r.save()

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = InfoseekGetNoteSerializers(user).data
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