import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import NIVSerializer,GetNIVSerializer
from ..models import *
from errormessage import Errormessage
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile


class nivupdate(generics.GenericAPIView):
    serializer_class = NIVSerializer

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
        img.save(buffer, format="PNG")  # Specify format to ensure proper saving
        buffer.seek(0)

        return buffer.getvalue()

    def post(self, request):
        try:
            HCPID = request.data.get('HCPID')

            a = HcpRegistrationModel.objects.get(HCPID=HCPID)
            if a.NIV is None:
                random_number = str(a.HCPID) + str(random.randint(1, 99999999999))
                a.NIV = random_number
                a.save()

                # Generate and save QR code
                qr_data = {
                    "NIV": a.NIV
                }
                qr_code_image = self.generate_qrcode(qr_data)
                qr_code_file = InMemoryUploadedFile(
                    ContentFile(qr_code_image),
                    None,
                    f'qrcode_{a.HCPID}.png',
                    'image/png',
                    len(qr_code_image),
                    None
                )
                a.Hcp_qrcode.save(qr_code_file.name, qr_code_file, save=True)
                a.save()

                response_message = 'Successful'
            else:
                response_message = "NIV is already updated"

            serializer = GetNIVSerializer(a)
            response_data = serializer.data

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = response_message
            response.Result = response_data
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


