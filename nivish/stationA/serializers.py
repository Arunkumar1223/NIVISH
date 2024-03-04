

from rest_framework import serializers
from .models import *
from datetime import date
import datetime


class StationASerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationAModel
        fields = ['HCID','HCPID','InfoseekId','EntryTime','Height', 'Length', 'Weight', 'Calculated_BMI', 'Triceps_Skin_Fold','Subscapular_Skinfold','Arm_Circumference','Head_Circumference','Abdominal_Girth',
                  'Abdominal_Girth_to_Hight_Ratio','Other_Observations', 'Specialist_Referral_Needed','Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag','Other','Completed','EndTime']

    def create(self, validated_data):

        infoseek_data = validated_data['InfoseekId']
        today = date.today()
        age = today.year - infoseek_data.Student_DOB.year - ((today.month, today.day) < (infoseek_data.Student_DOB.month, infoseek_data.Student_DOB.day))
        print(age)

        
        # Height
        if validated_data['Height']:
            if age < 2:
                raise Exception("No need to enter Height")
        else:
            if age > 2:
                raise Exception("please enter height")
        # Length    
        if validated_data['Length']:
            if age > 2:
                raise Exception("No need to enter Length")
        else:
            if age < 2:
                raise Exception("please enter Length")
        # Subscapular_Skinfold
        if validated_data['Subscapular_Skinfold']:
            if age > 5:
                raise Exception("No need to enter Subscapular_Skinfold")
        else:
            if age < 5:
                raise Exception("please enter Subscapular_Skinfold")
        # Arm_Circumference
        if validated_data['Arm_Circumference']:

            if age > 5:
                raise Exception("No need to enter Arm_Circumference")
        else:
            if age < 5:
                raise Exception("please enter Arm_Circumference")
        # Head_Circumference
        if validated_data['Head_Circumference']:
            if age > 5:
                raise Exception("No need to enter Head_Circumference")
        else:
            if age < 5:
                raise Exception("please enter Head_Circumference")

        user = StationAModel.objects.create(HCID=validated_data['HCID'],
                                       HCPID=validated_data['HCPID'],
                                       InfoseekId=validated_data['InfoseekId'],
                                       EntryTime = validated_data['EntryTime'],
                                       Height = validated_data['Height'],
                                       Length = validated_data['Length'],
                                       Weight = validated_data['Weight'],
                                       Calculated_BMI = validated_data['Calculated_BMI'],
                                       Triceps_Skin_Fold = validated_data['Triceps_Skin_Fold'],
                                       Subscapular_Skinfold = validated_data['Subscapular_Skinfold'],
                                       Head_Circumference = validated_data['Head_Circumference'],
                                       Abdominal_Girth = validated_data['Abdominal_Girth'],
                                       Abdominal_Girth_to_Hight_Ratio = validated_data['Abdominal_Girth_to_Hight_Ratio'],
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



class GetStationASerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationAModel
        fields = ['id','StationID','HCID','HCPID','InfoseekId','HCP_TeamId','EntryTime','Height', 'Length', 'Weight', 'Calculated_BMI', 'Triceps_Skin_Fold','Subscapular_Skinfold','Arm_Circumference','Head_Circumference','Abdominal_Girth',
                  'Abdominal_Girth_to_Hight_Ratio','Other_Observations', 'Specialist_Referral_Needed','Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag','Other','Completed','Review_Status','Reviewed_By',
                  'Reviewed_On','Comments','EndTime']


class UpdateStationASerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationAModel
        fields = ['HCID','HCPID','InfoseekId','Height', 'Length', 'Weight', 'Calculated_BMI', 'Triceps_Skin_Fold','Subscapular_Skinfold','Arm_Circumference','Head_Circumference','Abdominal_Girth',
                  'Abdominal_Girth_to_Hight_Ratio','Other_Observations', 'Specialist_Referral_Needed','Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag','Other','Completed','Reviewed_By','Reviewed_On']



class GetbyHcidUINSerializers(serializers.Serializer):
    
    StationName = serializers.CharField(required=False,default='StationA')
    UIN = serializers.CharField(required=False)
    HCID = serializers.IntegerField(required=False)