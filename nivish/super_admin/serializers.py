from rest_framework import serializers
from .models import *


class SuperAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = SuperAdminModel
        fields = ['Username','Password','MobileNumber','Email']


class GetSuperAdminSerializers(serializers.ModelSerializer):
    class Meta:
        model = SuperAdminModel
        fields = ['id','Username','Password','MobileNumber','Email']



class HealthCampTeamsSerializers(serializers.ModelSerializer):
    class Meta:
        model = HealthCampTeamsModel
        fields = ['TeamName']


class GetHealthCampTeamsSerializers(serializers.ModelSerializer):
    class Meta:
        model = HealthCampTeamsModel
        fields = ['id','TeamName']



class CampRegSerilizers(serializers.ModelSerializer):
    class Meta:
        model = HealthCampModel
        fields = ['SA_ID','Place', 'StartDate','EndDate','Health_Assessment_Name','Created_By','Updated_By',
                  'Number_of_Participant']




class GetCampRegSerializers(serializers.ModelSerializer):
    class Meta:
        model = HealthCampModel
        fields = ['HCID','SA_ID','Place','StartDate','EndDate','Health_Assessment_Name','Created_By','Updated_By',
                  'Number_of_Participant']


class StationSerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationNamesModel
        fields = ['Station_Names']




class GetStationSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationNamesModel
        fields = ['id', 'Station_Names']


class MailSerilizers(serializers.ModelSerializer):
    class Meta:
        model = MailModel
        fields = ['Email']


class HealthCampScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = HealthCampScheduleModel
        fields = ['HcID', 'Date','Scheduled_Start_Time','Scheduled_End_Time']


class UpdateHealthCampScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = HealthCampScheduleModel
        fields = ['Actual_End_Time', 'Actual_Start_Time',]