
from django.core.files.base import ContentFile
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser

from genericresponse import GenericResponse
from ..serializers import UpdateInfoseekVerificationSerializers
from ..models import InfoseekVerificationModel
from errormessage import Errormessage

@parser_classes((MultiPartParser,))
class InfoseekPhotoUploadUpdate(generics.GenericAPIView):
    """Here We're updating the Photo Upload based on InfoseekId
                (Table_Name:'Infoseek')"""
    serializer_class = UpdateInfoseekVerificationSerializers

    def put(self, request, InfoseekId):
        
        try:
            r = InfoseekVerificationModel.objects.get(InfoseekId=InfoseekId)
            s = UpdateInfoseekVerificationSerializers(r,data=request.data, partial=True)
            s.is_valid(raise_exception=True)
            s.save()
            Image = s.data
            image = Image

            a = ('\n'.join("{}: {}".format(k, v) for k, v in image.items()))
            partitioned_string = a.partition('?')
            before_first_period = partitioned_string[0]
            key = before_first_period.split(': ')
          
            s = key[1]
            data = s.split('/')
            # img = data[3].split('%20')
            dictionary = {}
            # dictionary['id'] = str(user.id)
            dictionary['upload_photo'] = data[4]

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = dictionary
            response.Status = status.HTTP_200_OK
            response.HasError = False
            return Response(response.__dict__, status=status.HTTP_200_OK)
        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = str(e)  # Change this to handle errors appropriately
            response.Result = False
            response.Status = status.HTTP_400_BAD_REQUEST
            response.HasError = True
            return Response(response.__dict__, status=status.HTTP_400_BAD_REQUEST)
