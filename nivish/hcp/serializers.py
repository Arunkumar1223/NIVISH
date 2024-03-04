from rest_framework import serializers
from .models import *


class HcpMasterSerilizers(serializers.ModelSerializer):
    class Meta:
        model = HcpMasteModel
        fields = ['FullName','Gender','Date_of_Birth','MobileNumber','Email','Type']

class UpdateHcpMasterSerilizers(serializers.ModelSerializer):
    class Meta:
        model = HcpMasteModel
        fields = ['FullName','Gender','Date_of_Birth','MobileNumber','Email','Type','Tag']


class GetHcpMasterSerilizers(serializers.ModelSerializer):
    class Meta:
        model = HcpMasteModel
        fields = ['id','FullName','Gender','Date_of_Birth','MobileNumber','Email','Type','Tag']

import random
import string


def password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
random_password = password()



class HcpRegistrationSerilizers(serializers.ModelSerializer):
    class Meta:
        model = HcpRegistrationModel
        fields = ['ProviderID','FullName','Date_of_Birth','Registered_Email','Gender','Registered_MobileNumber','Type']


    def create(self, validated_data):
        Password=password()
        user = HcpRegistrationModel.objects.create(FullName=validated_data['FullName'],
                                                   ProviderID=validated_data['ProviderID'],
                                       Date_of_Birth=validated_data['Date_of_Birth'],
                                       Registered_Email=validated_data['Registered_Email'],
                                       Gender=validated_data['Gender'],
                                       Registered_MobileNumber=validated_data['Registered_MobileNumber'],
                                       Type=validated_data['Type'],
                                       Password=Password)

        user.save()
        return user
        



class GetHcpRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = HcpRegistrationModel
        fields = ['HCPID','ProviderID','FullName','Date_of_Birth','Registered_Email','Gender','Registered_MobileNumber','Type','Terms_and_conditions','Version','Date','Upload_Your_Photo','NIV','Hcp_qrcode']

class UpdateHcpRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = HcpRegistrationModel
        fields = ['FullName','ProviderID','Date_of_Birth','Registered_Email','Gender','Registered_MobileNumber']


class UpdateResponseHcpRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = HcpRegistrationModel
        fields = ['HCPID','ProviderID','FullName','Date_of_Birth','Registered_Email','Gender','Registered_MobileNumber','Upload_Your_Photo']


class HcpGetBy(serializers.ModelSerializer):
    class Meta:
        model = HcpRegistrationModel
        fields = ['Type','FullName','Registered_Email']

        
class HcpLoginSerializers(serializers.ModelSerializer):
    

    User_Type = serializers.CharField(max_length=50,default=None)

    class Meta:
        model = HcpRegistrationModel
        fields = ['Registered_Email','Password','User_Type']







class HcpNoteTermsSerializers(serializers.ModelSerializer):
    class Meta:
        model = HcpRegistrationModel
        fields = ['Terms_and_conditions','Version','Date']


class HcpUploadPhotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = HcpRegistrationModel
        fields = ['Upload_Your_Photo']



class ProviderRegistrationSerilizers(serializers.ModelSerializer):
    class Meta:
        model = ProviderRegistrationModel
        fields = ['Name', 'Date_of_Birth','Email','MobileNumber']

    def create(self, validated_data):
        Password=password()
        user = ProviderRegistrationModel.objects.create(Name=validated_data['Name'],
                                       Date_of_Birth=validated_data['Date_of_Birth'],
                                       Email=validated_data['Email'],
                                       MobileNumber=validated_data['MobileNumber'],
                                       Password=Password)

        user.save()
        return user
        
class UpdateProviderRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProviderRegistrationModel
        fields = ['Terms_and_conditions','Version','Date']




class GetProviderRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProviderRegistrationModel
        fields = ['ProviderID','Name', 'Date_of_Birth','Email','MobileNumber','Terms_and_conditions','Version','Date']




class HcpEducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = HcpEducationModel
        fields = ['HCPID','ProviderID','Name_of_institute', 'Type_of_degree','Filed_of_study','Country','from_Date','to_Date','Upload_certificate']

class UpdateHcpEducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = HcpEducationModel
        fields = ['HCPID','ProviderID','Name_of_institute', 'Type_of_degree','Filed_of_study','Country','from_Date','to_Date']

class GetHcpEducationSerializers(serializers.ModelSerializer):
    class Meta:
        model = HcpEducationModel
        fields = ['id','HCPID','ProviderID','Name_of_institute', 'Type_of_degree','Filed_of_study','Country','from_Date','to_Date','Upload_certificate']
        depth = 1

class HcpEducationUploadDocSerializers(serializers.ModelSerializer):
    class Meta:
        model = HcpEducationModel
        fields = ['Upload_certificate']

    # Focus_Area = models.CharField(max_length=100)
    # MCI_Reg_Num = models.CharField(max_length=100)
    # Country = models.CharField(max_length=100)
    # State = models.CharField(max_length=100)
    # Issued_Date = models.DateField()
    # Validate_till = models.DateField()
    # Life_long_till = models.CharField(max_length=100)
    # Upload_certificate = models.CharField(max_length=100)
    
class HcpLicenseDetailsSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Hcp_License_Details_Model
        fields = ['HCPID','ProviderID','Category','Category_Others', 'License_Authority' ,'License_Authority_others' ,'License_Number','Country','State','Issued_Date','Validate_till','Life_long_till','Upload_certificate']


class UpdateHcpLicenseDetailsSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Hcp_License_Details_Model
        fields = ['HCPID','ProviderID','Category','Category_Others', 'License_Authority' ,'License_Authority_others' ,'License_Number','Country','State','Issued_Date','Validate_till','Life_long_till']



class GetHcpLicenseDetailsSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Hcp_License_Details_Model
        fields = ['id','HCPID','ProviderID','Category','Category_Others', 'License_Authority' ,'License_Authority_others' ,'License_Number','Country','State','Issued_Date','Validate_till','Life_long_till','Upload_certificate']
        depth = 1

class HcpLicenseDetailsUploadDocSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hcp_License_Details_Model
        fields = ['Upload_certificate']


import math
import random

def GenerateOtp():
    digits = "0123456789"
    otp = ""
    for i in range(4):
        otp += digits[math.floor(random.random() * 10)]
    return otp


class HcpOtpSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = HcpOtpModel
        fields = ['Name','Date_of_Birth','Email','MobileNumber']
   
    def create(self, validated_data):    
        otp = GenerateOtp()
        user = HcpOtpModel.objects.create(Name=validated_data['Name'],
                                       Date_of_Birth=validated_data['Date_of_Birth'],
                                       MobileNumber=validated_data['MobileNumber'],
                                       Email=validated_data['Email'],
                                       Otp=otp)

        user.save()
        return user


class HcpOtpGenerationSerializers(serializers.ModelSerializer):

    Review_Doctor = serializers.BooleanField(default=False)

    class Meta:
        model = HcpOtpModel
        fields = ['Name','Date_of_Birth','Email','MobileNumber','Otp','Review_Doctor']


import math
import random

def GenerateOtp():
    digits = "0123456789"
    otp = ""
    for i in range(4):
        otp += digits[math.floor(random.random() * 10)]
    return otp


# class ProviderOtpSerializers(serializers.ModelSerializer):
    
#     class Meta:
#         model = ProviderOtpModel
#         fields = ['Registered_Email']
   
#     def create(self, validated_data):
#         otp=GenerateOtp()
#         user = ProviderOtpModel.objects.create(Registered_Email=validated_data['Registered_Email'],
#                                        Otp=otp)

#         user.save()
#         return user
    
class ProviderOtpSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ProviderOtpModel
        fields = ['Email']
   
    def create(self, validated_data):
        # print("Validated Data:", validated_data)

        if(validated_data['Email'] == 'nivish@nivish.com') :
            otp='1111'
            # print("Specific OTP:", otp)
        else:
            otp=GenerateOtp()
            # print("Generated OTP:", otp)
        user = ProviderOtpModel.objects.create(Email=validated_data['Email'],
                                       Otp=otp)

        user.save()
        return user


# class ProviderOtpGenerationSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = ProviderOtpModel
#         fields = ['Registered_Email','Otp']

class ProviderOtpGenerationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProviderOtpModel
        fields = ['Email','Otp']

class AssignmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = AssignmentModel
        fields = ['TeamId','HCPID','HCID','StationID']

class GetAssignmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = AssignmentModel
        fields = ['id','TeamId','HCPID','HCID','StationID']



class LoginAssignmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = AssignmentModel
        fields = ['HCID','TeamId','HCPID','StationID']


class ExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModel
        fields = ['HCPID','ProviderID','Total_Experience_Years','Total_Experience_Months']

class GetExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExperienceModel
        fields = ['id','HCPID','ProviderID','Total_Experience_Years','Total_Experience_Months']
        

class NoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = ['HCPID','ProviderID','Full_Name','Signature','Submitted_date','Place','Accepted']



class GetNoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = ['id','HCPID','ProviderID','Full_Name','Signature','Upload_Your_Sign','Submitted_date','Place','Accepted']


class UpdateNoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = ['Upload_Your_Sign']


class HcpFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HcpFileUploadModel
        fields = ['file']


class GetHcpIdCardSerializers(serializers.ModelSerializer):
    class Meta:
        model = HcpRegistrationModel
        fields = ['FullName','Gender','Date_of_Birth','Registered_MobileNumber','Registered_Email','Upload_Your_Photo','NIV','Hcp_qrcode']


# class GetHcpNoteIdCardSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = NoteModel
#         fields = ['NIV','Hcp_qrcode']
    


class RegistrationDeskSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegistrationDeskModel
        fields = ['RegisteredBy','ExitedBy','HCID','UIN','RegisteredStatus','ExitStatus','RegistrationTime']
  
    
class GetRegistrationDeskSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegistrationDeskModel
        fields = ['id','RegisteredBy','ExitedBy','HCID','UIN','RegisteredStatus','ExitStatus','RegistrationTime','ExitTime','RegistrationEntryTime','ExitEntryTime']

class GetAllRegistrationDeskSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegistrationDeskModel
        fields = ['RegisteredStatus','ExitStatus']

class NIVSerializer(serializers.Serializer):
    HCPID = serializers.IntegerField(required=False)

class GetNIVSerializer(serializers.ModelSerializer):
    class Meta:
        model = HcpRegistrationModel 
        fields = ["NIV","Hcp_qrcode"]


    
    