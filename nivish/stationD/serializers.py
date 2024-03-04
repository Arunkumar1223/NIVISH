from rest_framework import serializers
from .models import *
from datetime import date



class StationDSerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationDModel
        fields = ['HCID','HCPID','InfoseekId','EntryTime','Do_you_have_problem_inhearing_your_Teachers_Friends_Parents', 'Do_you_have_problem_inhearing_your_Teachers_Yes', 
                  'Does_any_fluid_come_out_of_your_ears', 'Does_any_fluid_come_out_of_your_ears_Yes']
        
    def create(self, validated_data):

        infoseek_data = validated_data['InfoseekId']
        today = date.today()
        age = today.year - infoseek_data.Student_DOB.year - ((today.month, today.day) < (infoseek_data.Student_DOB.month, infoseek_data.Student_DOB.day))
        print(age)

        # Do_you_have_problem_inhearing_your_Teachers_Friends_Parents
        if validated_data['Do_you_have_problem_inhearing_your_Teachers_Friends_Parents']:
            if validated_data['Do_you_have_problem_inhearing_your_Teachers_Friends_Parents'] == "Yes" or "No":
                if age < 2:
                    raise Exception("No need to enter Do_you_have_problem_inhearing_your_Teachers_Friends_Parents")
                
        # Does_any_fluid_come_out_of_your_ears
        if validated_data['Does_any_fluid_come_out_of_your_ears']:
            if validated_data['Does_any_fluid_come_out_of_your_ears'] == "Yes" or "No":
                if age < 2:
                    raise Exception("No need to enter Does_any_fluid_come_out_of_your_ears")

        user = StationDModel.objects.create(HCID=validated_data['HCID'],
                                       HCPID=validated_data['HCPID'],
                                       InfoseekId=validated_data['InfoseekId'],
                                       EntryTime = validated_data['EntryTime'],
                                       Do_you_have_problem_inhearing_your_Teachers_Friends_Parents = validated_data['Do_you_have_problem_inhearing_your_Teachers_Friends_Parents'],
                                       Do_you_have_problem_inhearing_your_Teachers_Yes = validated_data['Do_you_have_problem_inhearing_your_Teachers_Yes'],
                                       Does_any_fluid_come_out_of_your_ears = validated_data['Does_any_fluid_come_out_of_your_ears'],
                                       Does_any_fluid_come_out_of_your_ears_Yes = validated_data['Does_any_fluid_come_out_of_your_ears_Yes'],

                                        )
        user.save()
        return user       
    
class GetStationDPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationDModel
        fields = ['id','StationID','HCID','HCPID','InfoseekId','EntryTime','Do_you_have_problem_inhearing_your_Teachers_Friends_Parents', 'Do_you_have_problem_inhearing_your_Teachers_Yes', 
                  'Does_any_fluid_come_out_of_your_ears', 'Does_any_fluid_come_out_of_your_ears_Yes']


class UpdateStationDSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationDModel
        fields = ['HCID','HCPID','InfoseekId','Do_you_have_problem_inhearing_your_Teachers_Friends_Parents', 'Do_you_have_problem_inhearing_your_Teachers_Yes', 
                  'Does_any_fluid_come_out_of_your_ears', 'Does_any_fluid_come_out_of_your_ears_Yes','Reviewed_By','Reviewed_On']


class StationDSerializers2(serializers.ModelSerializer):
    class Meta:
        model = StationDModel
        fields = ['id','Visual_inspection_Right_Ear_Pinna','Visual_inspection_Right_Ear_Pinna_Abnormal','Visual_inspection_Right_Ear_EarCanal','Visual_inspection_Right_Ear_EarCanal_Abnormal',
                  'Visual_inspection_Left_Ear_Pinna','Visual_inspection_Left_Ear_Pinna_Abnormal','Visual_inspection_Left_Ear_EarCanal','Visual_inspection_Left_Ear_EarCanal_Abnormal','Any_other_related_findings','Reviewed_By','Reviewed_On']
        
class StationDSerializers3(serializers.ModelSerializer):
    class Meta:
        model = StationDModel
        fields = ['id','Pure_Tone_Audiometry_Right_Ear_500Hz_25dB','Pure_Tone_Audiometry_Right_Ear_500Hz_25dB_Refer','Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB','Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB_Refer','Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB','Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB_Refer',
                  'Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB','Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB_Refer','Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB','Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB_Refer','Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB','Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB_Refer',
                  
                  'Pure_Tone_Audiometry_Left_Ear_500Hz_25dB','Pure_Tone_Audiometry_Left_Ear_500Hz_25dB_Refer','Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB','Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB_Refer','Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB','Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB_Refer',
                  'Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB','Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB_Refer','Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB','Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB_Refer','Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB','Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB_Refer','Reviewed_By','Reviewed_On']

class StationDSerializersUpdateDoc(serializers.ModelSerializer):
    class Meta:
        model = StationDModel
        fields = ['id','Upload_Pure_Tone_Test_Results']

class UploadDocStationDSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationDModel_Doc
        fields = ['HCID','HCPID','InfoseekId','Upload_Pure_Tone_Test_Results']


class StationDSerializers4(serializers.ModelSerializer):
    class Meta:
        model = StationDModel
        fields = ['id','Other_Observations','Specialist_Referral_Needed','Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag','Other','Completed','Reviewed_By','Reviewed_On','EndTime']

class GetStationDSerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationDModel
        fields = ['id','StationID','HCID', 'HCPID', 'InfoseekId','EntryTime',
                  'Do_you_have_problem_inhearing_your_Teachers_Friends_Parents', 'Do_you_have_problem_inhearing_your_Teachers_Yes', 
                  'Does_any_fluid_come_out_of_your_ears', 'Does_any_fluid_come_out_of_your_ears_Yes',
                  
                  'Visual_inspection_Right_Ear_Pinna','Visual_inspection_Right_Ear_Pinna_Abnormal','Visual_inspection_Right_Ear_EarCanal','Visual_inspection_Right_Ear_EarCanal_Abnormal',
                  'Visual_inspection_Left_Ear_Pinna','Visual_inspection_Left_Ear_Pinna_Abnormal','Visual_inspection_Left_Ear_EarCanal','Visual_inspection_Left_Ear_EarCanal_Abnormal','Any_other_related_findings',

                  'Pure_Tone_Audiometry_Right_Ear_500Hz_25dB','Pure_Tone_Audiometry_Right_Ear_500Hz_25dB_Refer','Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB','Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB_Refer','Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB','Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB_Refer',
                  'Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB','Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB_Refer','Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB','Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB_Refer','Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB','Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB_Refer',
                  
                  'Pure_Tone_Audiometry_Left_Ear_500Hz_25dB','Pure_Tone_Audiometry_Left_Ear_500Hz_25dB_Refer','Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB','Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB_Refer','Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB','Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB_Refer',
                  'Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB','Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB_Refer','Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB','Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB_Refer','Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB','Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB_Refer','Upload_Pure_Tone_Test_Results',

                  'Other_Observations','Specialist_Referral_Needed','Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag','Other','Completed','Review_Status','Reviewed_By',
                  'Reviewed_On','Comments','EndTime']
        

