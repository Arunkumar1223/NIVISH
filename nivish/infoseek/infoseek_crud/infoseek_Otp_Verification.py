# def userVerificationPost(Student_FirstName,Student_DOB,Mothers_FullName,email):
#     url = 'http://127.0.0.1:8000/Infoseek/InfoseekUserVerification/'  # Example POST URL

#     a = InfoseekMasterModel.objects.filter(Student_First_Name=Student_FirstName,Date_of_Birth=Student_DOB,Mothers_First_Name=Mothers_FullName,Parent_Email= email)
#     print(a,"aaaaaaaaaaa")
#     for i in a:
        
#         Student_MiddleName1 = i.Student_Middle_Name_1
#         print(Student_MiddleName1)
#         Student_MiddleName2 = i.Student_Middle_Name_2
#         print(Student_MiddleName2)
#         gender = i.Gender
#         print(gender)
#         Mothers_MiddleName1 = i.Mothers_Middle_Name
#         print(Mothers_MiddleName1)
#         Mothers_MiddleName2 = i.Mothers_Middle_Name
#         print(Mothers_MiddleName2)
#         Mothers_LastName = i.Mothers_Last_Name
#         print(Mothers_LastName)
#         Fathers_FirstName = i.Fathers_First_Name
#         print(Fathers_FirstName)
#         Fathers_MiddleName1 = i.Fathers_Middle_Name
#         print(Fathers_MiddleName1)
#         Fathers_MiddleName2 = i.Fathers_Middle_Name
#         print(Fathers_MiddleName2)
#         Fathers_LastName = i.Fathers_Last_Name
#         print(Fathers_LastName)
#         BloodGroup = i.Blood_Group
#         print(BloodGroup)
#         # Rh_Factor = i.RH_Factor
#         Building_Name = i.Address_Building
#         print(Building_Name)
#         Street_No = i.Adress_Street
#         print(Street_No)
#         country = 1
#         print(country)
#         state = 1
#         print(state)
#         city = 1
#         print(city)
#         Zip_Code = i.Zip
#         print(Zip_Code)

#     print(Student_FirstName,Student_DOB,Mothers_FullName,email)
  
#     json_data = {
#     'Student_FirstName': Student_FirstName,
#     'Student_DOB': Student_DOB,
#     'Mothers_FullName': Mothers_FullName,
#     'Registered_EmailId': email,

#     'Student_MiddleName1': Student_MiddleName1,
#     'Student_MiddleName2' : Student_MiddleName2,
#     'Gender' : gender,
#     'Mothers_MiddleName1': Mothers_MiddleName1,
#     'Mothers_MiddleName2': Mothers_MiddleName2,
#     'Mothers_LastName': Mothers_LastName,
#     'Fathers_FirstName': Fathers_FirstName,
#     'Fathers_MiddleName1': Fathers_MiddleName1,
#     'Fathers_MiddleName2': Fathers_MiddleName2,
#     'Fathers_LastName': Fathers_LastName,
#     'BloodGroup': BloodGroup,
#     # 'Rh_Factor': None,
#     'Building_Name': Building_Name,
#     'Street_No': Street_No,
#     'Country': country,
#     'State': state,
#     'City':city,
#     'Zip_Code': Zip_Code,
    
#     }
from rest_framework.utils import json
from rest_framework import generics
from rest_framework.response import Response
from ..serializers import OtpGenerationSerializers,GetAllInfoseekSerializers
from ..models import OtpModel,InfoseekMasterModel,InfoseekVerificationModel
from genericresponse import GenericResponse
from errormessage import Errormessage
import requests
from datetime import datetime, timezone, timedelta
from manage_urls import *

def userVerificationPost(Student_FirstName,Student_DOB,Mothers_FullName,email):
    url = infoseek_url
  

    print(Student_FirstName,Student_DOB,Mothers_FullName,email)

    master_data = InfoseekMasterModel.objects.filter(Student_First_Name=Student_FirstName,Date_of_Birth=Student_DOB,Parent_Email= email)

    for i in master_data:
        
        Student_MiddleName1 = i.Student_Middle_Name_1
        Student_MiddleName2 = i.Student_Middle_Name_2
        Student_LastName = i.Student_Last_Name
        gender = i.Gender
        class_name = i.Student_Class
        print(class_name,"class")
        section_name = i.Student_Section
        print(section_name,"section")
        Mothers_FirstName = i.Mothers_First_Name
        print(Mothers_FirstName,"Mother")
        Mothers_MiddleName1 = i.Mothers_Middle_Name
        Mothers_MiddleName2 = i.Mothers_Middle_Name
        Mothers_LastName = i.Mothers_Last_Name
        Fathers_FirstName = i.Fathers_First_Name
        Fathers_MiddleName1 = i.Fathers_Middle_Name
        Fathers_MiddleName2 = i.Fathers_Middle_Name
        Fathers_LastName = i.Fathers_Last_Name
        BloodGroup = i.Blood_Group
        Rh_Factor = i.RH_Factor
        Building_Name = i.Address_Building
        Street_No = i.Adress_Street
        Zip_Code = i.Zip
        Email_Registered_With_School = email
        print(Email_Registered_With_School)
        print(Zip_Code,'Zip')

        # country = 1
        # state = 1
        # city = 1

    json_data = {
                "Student_FirstName": Student_FirstName,
                "Student_DOB": Student_DOB,
                "Mothers_FullName": Mothers_FullName,
                "Registered_EmailId": email,
                    'Student_MiddleName1': str(Student_MiddleName1),
                    'Student_MiddleName2': str(Student_MiddleName2),
                    'Student_LastName': str(Student_LastName),
                    'class_name' : str(class_name),
                    'section_name' : str(section_name),
                    'Gender': str(gender),
                    'Mothers_FirstName': str(Mothers_FirstName),
                    'Mothers_MiddleName1': str(Mothers_MiddleName1),
                    'Mothers_MiddleName2': str(Mothers_MiddleName2),
                    'Mothers_LastName': str(Mothers_LastName),
                    'Fathers_FirstName': str(Fathers_FirstName),
                    'Fathers_MiddleName1': str(Fathers_MiddleName1),
                    'Fathers_MiddleName2': str(Fathers_MiddleName2),
                    'Fathers_LastName': str(Fathers_LastName),
                    'BloodGroup': str(BloodGroup),
                    'Rh_Factor' : str(Rh_Factor),
                    'Building_Name': str(Building_Name),
                    'Street_No': str(Street_No),
                    'Zip_Code': str(Zip_Code),
                    'Email_Registered_With_School' : Email_Registered_With_School,
                    

                }

    print(json_data,"json_data")

    
    json_payload = json.dumps(json_data)
    token = token1
    # print(token)
  
    try:
        headers = {
                                'Accept': 'application/json',
                                'Content-Type': 'application/json',
                                'Authorization': f'Bearer {token}'  # Replace with your token
                        }
        
        response = requests.post(url, headers=headers, data=json_payload)

        # print(response)

        if response.status_code == 200:
            data = response.json()
            print(data)
            result = data
        else:
            result = False
    except requests.exceptions.RequestException as e:
        result = f"Request failed: {e}"
    return result



class InfoseekOtpVerfication(generics.GenericAPIView):
    """Here We Verifying OTP
        (Table_Name:'infoseek_OTP')"""
    serializer_class = OtpGenerationSerializers

    def post(self, request):
        try:

            Student_FirstName = request.data.get('Student_FirstName')
            Student_DOB = request.data.get('Student_DOB')
            Mothers_FullName = request.data.get('Mothers_FullName')


            email=request.data.get("Email")
            otp=request.data.get("Otp")

            if OtpModel.objects.get(Student_FirstName=Student_FirstName,Student_DOB=Student_DOB,Email=email,Otp=otp):
                otpdata = OtpModel.objects.get(Student_FirstName=Student_FirstName,Student_DOB=Student_DOB,Email=email,Otp=otp)

                created_date = otpdata.CreatedOn
                Created_date_only = created_date.date()
                Created_time_only = created_date.time()

                current_datetime = datetime.now()
                current_date_only = current_datetime.date()
                current_time_only = current_datetime.time()

                if Created_date_only == current_date_only:

                    time_difference = datetime.combine(current_date_only, current_time_only) - datetime.combine(Created_date_only, Created_time_only)

                    if time_difference.total_seconds() < 600:

                        infoseek_data = InfoseekVerificationModel.objects.filter(Student_FirstName= Student_FirstName,Student_DOB=Student_DOB,Registered_EmailId=email)

                        if infoseek_data:
                            
                            for i in infoseek_data:
                                b = i.InfoseekId
                                break

                            # b = GetAllInfoseekSerializers(infoseek_data,many=True)
                            # b = b.data

                                
                        else:
                            userverify_data = userVerificationPost(Student_FirstName,Student_DOB,Mothers_FullName,email)

                            print(userverify_data,'userverify_data')

                            result = userverify_data['Result']

                            print(result,'result')
                            b = result['InfoseekId']

                        InfoseekMaster = InfoseekMasterModel.objects.get(Student_First_Name=Student_FirstName,Date_of_Birth=Student_DOB,Parent_Email = email)
                        masterid = InfoseekMaster.id

                        # b['InfoseekMasterId'] = masterid


                        # deleteotp = otpdelete(email,otp)
                        otpdata.delete()

                        # a = OtpModel.objects.get(Email=email,Otp=otp)
                        # serializer_class = True

                        response = GenericResponse("Message", "Result", "Status", "HasError")
                        response.Message = "Successful"
                        response.Result = {'InfoseekId':b}
                        response.InfoseekMasterId = masterid
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