from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from hcp.serializers import GetHcpRegistrationSerializers,GetHcpLicenseDetailsSerilizers,GetHcpEducationSerializers,GetExperienceSerializers
from hcp.models import HcpRegistrationModel,Hcp_License_Details_Model,HcpEducationModel,ExperienceModel
from genericresponse import GenericResponse
from errormessage import Errormessage


class GetByHcpId(generics.GenericAPIView):
    serializer_class = GetHcpRegistrationSerializers 

    def get(self,request,HCPID):
        try:
            hcp_data = HcpRegistrationModel.objects.filter(HCPID=HCPID)
            serializer_class = GetHcpRegistrationSerializers(hcp_data, many=True)

            license_data = Hcp_License_Details_Model.objects.filter(HCPID=HCPID)
            serializer_class2 = GetHcpLicenseDetailsSerilizers(license_data,many=True)

            education_data = HcpEducationModel.objects.filter(HCPID=HCPID)
            education_serializer = GetHcpEducationSerializers(education_data, many=True)

            experince_data = ExperienceModel.objects.filter(HCPID=HCPID)
            experince_serializer = GetExperienceSerializers(experince_data,many=True)


            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = {'HCP' : serializer_class.data,
                               'License':serializer_class2.data,
                               'Education':education_serializer.data,
                               'Experince':experince_serializer.data},

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


