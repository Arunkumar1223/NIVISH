from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from ..serializers import HcpOtpGenerationSerializers,LoginAssignmentSerializers,GetHcpRegistrationSerializers
from ..models import *
from genericresponse import GenericResponse
from errormessage import Errormessage
import requests
from datetime import datetime, timezone, timedelta
from tokengeneration import *
from manage_urls import *


def userVerificationPost(FullName, Date_of_Birth, email, MobileNumber):
    url = hcp_url  
  
    hcp_masterdata = HcpMasteModel.objects.filter(FullName=FullName, Date_of_Birth=Date_of_Birth, Email=email, MobileNumber=MobileNumber)  

    for i in hcp_masterdata:
        gender = i.Gender

    json_data = {
        'ProviderID': None,
        'FullName': FullName,
        'Date_of_Birth': Date_of_Birth,
        'Registered_Email': email,
        'Registered_MobileNumber': MobileNumber,
        'Type': 'HCP',
        'Gender': str(gender),
        'Upload_Your_Photo': None
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
        

        if response.status_code == 200:
            data = response.json()
            print(data)
            result = data
            # result = True
        else:
            # result_data = []
            result = False
            # print(result, "result")
    except requests.exceptions.RequestException as e:
        result = False
        # result_data = []
    return result




class HcpOtpVerfication(generics.GenericAPIView):
    serializer_class = HcpOtpGenerationSerializers

    def post(self, request):
        try:

            name = request.data.get('Name')
            Date_of_Birth = request.data.get('Date_of_Birth')
            email=request.data.get("Email")
            MobileNumber=request.data.get("MobileNumber")
            otp=request.data.get("Otp")
            

            if name and Date_of_Birth and email is not None: 
                if HcpOtpModel.objects.filter(Name=name,Date_of_Birth=Date_of_Birth,Email=email,Otp=otp):
                    otpdata = HcpOtpModel.objects.get(Name=name,Date_of_Birth=Date_of_Birth,Email=email,Otp=otp)

                    created_date = otpdata.CreatedOn
                    Created_date_only = created_date.date()
                    Created_time_only = created_date.time()

                    current_datetime = datetime.now()
                    current_date_only = current_datetime.date()
                    current_time_only = current_datetime.time()

                    if Created_date_only == current_date_only:

                        time_difference = datetime.combine(current_date_only, current_time_only) - datetime.combine(Created_date_only, Created_time_only)

                        if time_difference.total_seconds() < 600:

                            registered_data = HcpRegistrationModel.objects.filter(FullName=name,Date_of_Birth=Date_of_Birth,Registered_Email=email)
                            if registered_data:
                                b = GetHcpRegistrationSerializers(registered_data, many=True)
                                b = b.data
                                # print(b[0],"existing")

                                otpdata.delete()
                                # print(b["Result"])
                                # b = b["Result"]

                                print("Success")
                                response = GenericResponse("Message", "Result", "Status", "HasError")
                                response.Message = "Successful"
                                response.Result = b[0]
                                response.Status = 200
                                response.HasError = False
                                jsonStr = json.dumps(response.__dict__)
                                return Response(json.loads(jsonStr), status=200)
                            
                            else:
                                b = userVerificationPost(name,Date_of_Birth,email,MobileNumber)

                                hcp_master_data = HcpMasteModel.objects.get(FullName=name,Date_of_Birth=Date_of_Birth,Email=email)
                                if hcp_master_data.Tag == None:
                                    hcp_master_data.Tag = False
                                    hcp_master_data.save()

                                if b != False:

                                    otpdata.delete()
                                    # print(b["Result"])
                                    b = b["Result"]

                                    # print("Success")
                                    response = GenericResponse("Message", "Result", "Status", "HasError")
                                    response.Message = "Successful"
                                    response.Result = b
                                    response.Status = 200
                                    response.HasError = False
                                    jsonStr = json.dumps(response.__dict__)
                                    return Response(json.loads(jsonStr), status=200)
                                else:
                                    raise Exception("Request Failed")
                        else:
                            otpdata.delete()
                            print("Fail")
                            raise Exception("Your OTP has been Expired")

                    else:
                        otpdata.delete()
                        print("Fail")
                        raise Exception("Your OTP has been Expired")
                else:
                    raise Exception("Please Enter Valid OTP")
            else:
                if  HcpOtpModel.objects.filter(Email=email,Otp=otp):
                    otpdata = HcpOtpModel.objects.get(Email=email,Otp=otp)

                    hcpdata = HcpRegistrationModel.objects.get(Registered_Email=email)
                    hcpassesment = AssignmentModel.objects.filter(HCPID=hcpdata.HCPID)

                    created_date = otpdata.CreatedOn
                    Created_date_only = created_date.date()
                    Created_time_only = created_date.time()

                    current_datetime = datetime.now()
                    current_date_only = current_datetime.date()
                    current_time_only = current_datetime.time()

                    if Created_date_only == current_date_only:

                        time_difference = datetime.combine(current_date_only, current_time_only) - datetime.combine(Created_date_only, Created_time_only)

                        if time_difference.total_seconds() < 100:
                            otpdata.delete()

                            if hcpassesment:
                                asss = LoginAssignmentSerializers(hcpassesment, many=True)
                                hcp_data = GetHcpRegistrationSerializers(hcpdata)
                                a=logintoken()
                                bearer_token=a['access']

                                assement = asss.data
                                data = hcp_data.data
                                data['Stations'] = assement
                                data['Token'] = bearer_token
                                
                            else:
                                hcp_data = GetHcpRegistrationSerializers(hcpdata)

                                a=logintoken()
                                bearer_token=a['access']
                                data = hcp_data.data
                                data['Stations'] = []
                                data['Token'] = bearer_token

                            # otpdata.delete()
                            response = GenericResponse("Message", "Result", "Status", "HasError")
                            response.Message = "Successfully logged In"
                            response.Result = data
                            response.Status = 200
                            response.HasError = False
                            jsonStr = json.dumps(response.__dict__)
                            return Response(json.loads(jsonStr), status=200)

                        else:
                            otpdata.delete()
                            print("Fail")
                            raise Exception("Your OTP has been Expired")
                    
                    else:
                        otpdata.delete()
                        print("Fail")
                        raise Exception("Your OTP has been Expired")


                    
                else:
                    raise Exception("Please Enter Valid OTP")

        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
