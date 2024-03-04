from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..models import *
from ..serializers import StationFSerializers,GetStationFPostSerializers
from errormessage import Errormessage
from Multiselect.multiselectLists import *
from Multiselect.multiselectFunction import *
from Validations.StationF_Validations import *
from super_admin.models import StationNamesModel


class StationFDetailsCreate(generics.GenericAPIView):
    serializer_class = StationFSerializers

    def post(self, request, *args, **kwargs):
        try:

            hcid = request.data.get('HCID')
            infoseekid = request.data.get('InfoseekId')
            if StationFModels.objects.filter(HCID=hcid, InfoseekId=infoseekid):
                raise Exception("This HCID already exits with InfoseekId")
            else:
                data = request.data
                check_Skin_colour_Tone(request)
                check_Skin_Texture_of_Skin(request)
                check_skin_Rash(request)
                check_Other_Skin_lesions(request)
                check_skin_Acne(request)

                field_lists = {
                    'Skin_Texture_of_Skin_Abnormal': Skin_Texture_of_Skin_Abnormal_list,
                    'skin_Rash_Present': skin_Rash_Present_list,
                    'skin_Rash_Present_Face': Rash_Present_list,
                    'skin_Rash_Present_Neck': Rash_Present_list,
                    'skin_Rash_Present_Chest': Rash_Present_list,
                    'skin_Rash_Present_Abdomen': Rash_Present_list,
                    'skin_Rash_Present_Groin': Rash_Present_list,
                    'skin_Rash_Present_Back': Rash_Present_list,
                    'skin_Rash_Present_Arms': Rash_Present_list,
                    'skin_Rash_Present_Hands': Rash_Present_list,
                    'skin_Rash_Present_Legs': Rash_Present_list,
                    'skin_Rash_Present_Feet': Rash_Present_list,
                    'Other_Skin_lesions_Yes': Other_Skin_lesions_Yes_list,
                    'Other_Skin_lesions_Yes_Birth_marks' : Other_Skin_lesions_Yes_Birth_marks_list,
                }

                validation_result = multiselect.check_field_lists(data, field_lists)
                if validation_result is not None:
                    return validation_result
                
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                station_instance = StationNamesModel.objects.get(id=6)
                serializer.validated_data['StationID'] = station_instance
                user = serializer.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = GetStationFPostSerializers(user).data
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
