import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import HcpRegistrationSerilizers,GetHcpRegistrationSerializers
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from ..models import *
from manage_urls import *

def experiencePost(hcpid,ProviderID):
    url = expirence_url  

    json_data = {
        'HCPID': hcpid,
        'ProviderID':ProviderID,
        'Total_Experience_Years' : None,
        'Total_Experience_Months' : None,
    }
    
    json_payload = json.dumps(json_data)
    print(json_payload,'satand')

    token = token1
    try:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'  # Replace with your token
        }

        response = requests.post(url, headers=headers, data=json_payload)
        print(response)
        result = True
        
    except requests.exceptions.RequestException as e:
        result = False
    return result


def hcpmasterpost(type,email,ProviderID,Registered_MobileNumber,Date_of_Birth,FullName,Gender):
    url = hcpmaster_url  

    json_data = {
                "FullName": FullName,
                "Gender": Gender,
                "Date_of_Birth": Date_of_Birth,
                "MobileNumber": Registered_MobileNumber,
                "Email": email,
                "Type": type
                }
    json_payload = json.dumps(json_data)
    print(json_payload,'satand')

    token = token1
    try:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'  # Replace with your token
        }

        response = requests.post(url, headers=headers, data=json_payload)
        print(response)
        result = True
    except:
        result = False
    return result

class HcpRegistrationPost(generics.GenericAPIView):
    serializer_class = HcpRegistrationSerilizers
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            type = request.data.get('Type')
            email = request.data.get('Registered_Email')
            ProviderID = request.data.get('ProviderID')
            Registered_MobileNumber = request.data.get('Registered_MobileNumber')
            Date_of_Birth = request.data.get('Date_of_Birth')
            FullName = request.data.get('FullName')
            Gender = request.data.get('Gender')
            # hcpmodel = HcpRegistrationModel.objects.filter(Registered_Email=email,Type=type,ProviderID=ProviderID,Registered_MobileNumber=Registered_MobileNumber,Date_of_Birth=Date_of_Birth,FullName=FullName)
            if HcpRegistrationModel.objects.filter(Registered_Email=email,Type=type,Registered_MobileNumber=Registered_MobileNumber,Date_of_Birth=Date_of_Birth,FullName=FullName):
                hcpmodel = HcpRegistrationModel.objects.filter(Registered_Email=email,Type=type,Registered_MobileNumber=Registered_MobileNumber,Date_of_Birth=Date_of_Birth,FullName=FullName)
                for i in hcpmodel:
                    user = i                
            else:
                if HcpRegistrationModel.objects.filter(Registered_Email=email):
                    raise Exception("This Email already exists")
                else:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    user = serializer.save()
                    
                    hcpid = user.HCPID
                    # print(user)
                    experiencePost(hcpid,ProviderID)

                    
                    hcp_master = HcpMasteModel.objects.filter(Email= email)
                    # print(hcp_master,"master")
                    if hcp_master:
                        # print("hcp_master",hcp_master)
                        pass
                    else:
                        hcp_master_post = hcpmasterpost(type,email,ProviderID,Registered_MobileNumber,Date_of_Birth,FullName,Gender)
                        hcp_master_data = HcpMasteModel.objects.get(FullName=FullName,Date_of_Birth=Date_of_Birth,Email=email)
                    
                        if hcp_master_data.Tag == None:
                            hcp_master_data.Tag = False
                            hcp_master_data.save()
        
                        print(hcp_master_post,'hcp_master_post')
                        if result == False:
                            raise Exception("Request Faild")



            print(user)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = GetHcpRegistrationSerializers(user).data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)