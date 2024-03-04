from rest_framework import serializers
from .models import *
from datetime import date
import datetime
# from django.contrib.auth.hashers import make_password

class StationBSerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationBModel
        fields = ['HCID','HCPID','InfoseekId','EntryTime','Blood_Pressure_Position', 'Blood_Pressure_Type_of_Instrument', 'Blood_Pressure_Systolic_BP', 'Blood_Pressure_Diastolic_BP',
                   'Respiration','Heart_Rate',"Temprature_Measurement_Site","Temprature_Measurement_Instrument","Temprature" ,'Oxygen_Saturation_SpO2','Other_Observations','Specialist_Referral_Needed',
                  'Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag','Other','Completed','EndTime']
        
    def create(self, validated_data):

        infoseek_data = validated_data['InfoseekId']
        today = date.today()
        age = today.year - infoseek_data.Student_DOB.year - ((today.month, today.day) < (infoseek_data.Student_DOB.month, infoseek_data.Student_DOB.day))
        print(age)

        # Temprature
        if validated_data['Temprature_Measurement_Site']:
            if validated_data['Temprature_Measurement_Site'] == "Anal":
                if age > 2:
                    raise Exception("No need to enter Temprature_Measurement_Site")
        

        user = StationBModel.objects.create(HCID=validated_data['HCID'],
                                       HCPID=validated_data['HCPID'],
                                       InfoseekId=validated_data['InfoseekId'],
                                       EntryTime = validated_data['EntryTime'],
                                       Blood_Pressure_Position = validated_data['Blood_Pressure_Position'],
                                       Blood_Pressure_Type_of_Instrument = validated_data['Blood_Pressure_Type_of_Instrument'],
                                       Blood_Pressure_Systolic_BP = validated_data['Blood_Pressure_Systolic_BP'],
                                       Respiration = validated_data['Respiration'],
                                       Heart_Rate = validated_data['Heart_Rate'],
                                       Temprature_Measurement_Site = validated_data['Temprature_Measurement_Site'],
                                       Temprature_Measurement_Instrument = validated_data['Temprature_Measurement_Instrument'],
                                       Temprature = validated_data['Temprature'],
                                       Oxygen_Saturation_SpO2 = validated_data['Oxygen_Saturation_SpO2'],
                                       Other_Observations = validated_data['Other_Observations'],
                                       Specialist_Referral_Needed = validated_data['Specialist_Referral_Needed'],
                                       Specialist_Referral_Needed_Type = validated_data['Specialist_Referral_Needed_Type'],
                                       Specialist_Referral_Needed_Flag = validated_data['Specialist_Referral_Needed_Flag'],
                                       Other = validated_data['Other'],
                                       Completed = validated_data['Completed'],
                                       EndTime = validated_data['EndTime'],
                                        )
        user.save()
        return user

        
class GetStationBSerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationBModel
        fields = ['id','StationID','HCID','HCPID','InfoseekId','EntryTime','Blood_Pressure_Position', 'Blood_Pressure_Type_of_Instrument', 'Blood_Pressure_Systolic_BP', 'Blood_Pressure_Diastolic_BP',
                   'Respiration','Heart_Rate',"Temprature_Measurement_Site","Temprature_Measurement_Instrument","Temprature" ,'Oxygen_Saturation_SpO2','Other_Observations','Specialist_Referral_Needed',
                  'Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag','Other','Completed','Review_Status','Reviewed_By',
                  'Reviewed_On','Comments','EndTime']
        
        
class UpdateStationBSerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationBModel
        fields = ['HCID','HCPID','InfoseekId','Blood_Pressure_Position', 'Blood_Pressure_Type_of_Instrument', 'Blood_Pressure_Systolic_BP', 'Blood_Pressure_Diastolic_BP',
                   'Respiration','Heart_Rate',"Temprature_Measurement_Site","Temprature_Measurement_Instrument","Temprature" ,'Oxygen_Saturation_SpO2','Other_Observations','Specialist_Referral_Needed',
                  'Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag','Other','Completed','Reviewed_By','Reviewed_On']
        

