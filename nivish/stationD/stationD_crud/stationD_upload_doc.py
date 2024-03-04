import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import UploadDocStationDSerializers
from ..models import *
from errormessage import Errormessage
from rest_framework.decorators import parser_classes
from rest_framework.parsers import MultiPartParser
from super_admin.models import StationNamesModel

@parser_classes((MultiPartParser,))
class UpdateDocStationD(generics.GenericAPIView):
    serializer_class = UploadDocStationDSerializers

    def post(self, request, *args, **kwargs):
        try:
            # Create a list to store instances of the uploaded images
            uploaded_images = []

            for image_file in request.FILES.getlist('Upload_Pure_Tone_Test_Results'):
                

                # Create a serializer instance for each image file
                serializer_data = {
                    'Upload_Pure_Tone_Test_Results': image_file
                }
                print(serializer_data,"data")
                serializer = self.get_serializer(data=serializer_data)
                serializer.is_valid(raise_exception=True)
                # print("idd")
                station_instance = StationNamesModel.objects.get(id=4)
                serializer.validated_data['StationID'] = station_instance
                print(serializer,"id")

                user = serializer.save()
                uploaded_images.append(UploadDocStationDSerializers(user).data)
                print(uploaded_images,"image")

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = uploaded_images
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
