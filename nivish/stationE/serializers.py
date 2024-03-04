

from rest_framework import serializers
from .models import *
from datetime import date


    #  = models.ForeignKey("stationA.YesOrNoMasterModel",related_name='Wear_Brace_Support_YN',on_delete=models.CASCADE,null=True)
    #  = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Neck, Shoulders, Back, Chest, Right Upper Limb, Left Upper Limb, Right Lower Limb, Left Lower Limb)

    # Prosthesis = models.ForeignKey("stationA.YesOrNoMasterModel",related_name='Prosthesis_YN',on_delete=models.CASCADE,null=True)
    # Prosthesis_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Knee, Hip, Spine, Hip, Right Upper Limb, Left Upper Limb, Right Lower Limb, Left Lower Limb, Right shoulder, Left shoulder,Others)
    # Prosthesis_Yes_other = models.TextField(null=True, blank=True)


class StationESerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationEModel
        fields = ['HCID','HCPID', 'InfoseekId','EntryTime','Child_Mobility','Child_Mobility_Can_not_Walk',
                  'Child_Mobility_Can_not_Walk_other' ,'Student_Ambulant','Student_Ambulant_No',
                    'Gait', 'Gait_Abnormal', 'Gait_Abnormal_Limp', 'Gait_Abnormal_Limp_other'
                ]
    def create(self, validated_data):

        infoseek_data = validated_data['InfoseekId']
        today = date.today()
        age = today.year - infoseek_data.Student_DOB.year - ((today.month, today.day) < (infoseek_data.Student_DOB.month, infoseek_data.Student_DOB.day))
        print(age)

        # Child_Mobility
        if validated_data['Child_Mobility']:
            if validated_data['Child_Mobility'] == "Can Walk" or "Can not Walk":
                if age > 2:
                    raise Exception("No need to enter Child_Mobility")
                
        # Student_Ambulant
        if validated_data['Student_Ambulant']:
            if validated_data['Student_Ambulant'] == "Yes" or "No":
                if age < 2:
                    raise Exception("No need to enter Student_Ambulant")

        user = StationEModel.objects.create(HCID=validated_data['HCID'],
                                       HCPID=validated_data['HCPID'],
                                       InfoseekId=validated_data['InfoseekId'],
                                       EntryTime = validated_data['EntryTime'],
                                       Child_Mobility = validated_data['Child_Mobility'],
                                       Child_Mobility_Can_not_Walk = validated_data['Child_Mobility_Can_not_Walk'],
                                       Child_Mobility_Can_not_Walk_other = validated_data['Child_Mobility_Can_not_Walk_other'],
                                       Student_Ambulant = validated_data['Student_Ambulant'],
                                       Student_Ambulant_No = validated_data['Student_Ambulant_No'],
                                       Gait = validated_data['Gait'],
                                       Gait_Abnormal = validated_data['Gait_Abnormal'],
                                       Gait_Abnormal_Limp = validated_data['Gait_Abnormal_Limp'],
                                       Gait_Abnormal_Limp_other = validated_data['Gait_Abnormal_Limp_other'],
                                    
                                        )
        user.save()
        return user    

class GetStationEPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationEModel
        fields = ['id','StationID','HCID','HCPID', 'InfoseekId','EntryTime','Child_Mobility',
                  'Child_Mobility_Can_not_Walk','Child_Mobility_Can_not_Walk_other',
                  'Student_Ambulant','Student_Ambulant_No', 'Gait', 'Gait_Abnormal', 'Gait_Abnormal_Limp', 'Gait_Abnormal_Limp_other'
                  ]


class UpdateStationESerializers(serializers.ModelSerializer):
    class Meta:
        model = StationEModel
        fields = ['HCID','HCPID', 'InfoseekId','Child_Mobility','Child_Mobility_Can_not_Walk','Child_Mobility_Can_not_Walk_other' ,'Student_Ambulant','Student_Ambulant_No', 
                  'Gait', 'Gait_Abnormal', 'Gait_Abnormal_Limp', 'Gait_Abnormal_Limp_other','Reviewed_By','Reviewed_On']


class StationESerilizers2(serializers.ModelSerializer):
    class Meta:
        model = StationEModel
        fields = ['Wear_Brace_Support', 'Wear_Brace_Support_Yes','Prosthesis','Prosthesis_Yes', 'Prosthesis_Yes_other',
                  'Spine_Appearance','Spine_Appearance_Abnormal','Spine_Appearance_Abnormal_Other','Shoulder_Griddle_Appearance','Shoulder_Griddle_Appearance_Abnormal',
                  'Shoulder_Griddle_Appearance_Abnormal_Other','Spine_Mobility','Spine_Mobility_Restricted_movement','Neck_Mobility','Neck_Mobility_Restricted_movement','Reviewed_By','Reviewed_On']
        
    # def create(self, validated_data):

    #     infoseek_data = validated_data['InfoseekId']
    #     today = date.today()
    #     age = today.year - infoseek_data.Student_DOB.year - ((today.month, today.day) < (infoseek_data.Student_DOB.month, infoseek_data.Student_DOB.day))
    #     print(age)

    #     # Child_Mobility
    #     if validated_data['Child_Mobility']:
    #         if validated_data['Child_Mobility'] == "Can Walk" or "Can not Walk":
    #             if age > 2:
    #                 raise Exception("No need to enter Child_Mobility")
                
    #     # Student_Ambulant
    #     if validated_data['Student_Ambulant']:
    #         if validated_data['Student_Ambulant'] == "Yes" or "No":
    #             if age < 2:
    #                 raise Exception("No need to enter Student_Ambulant")

    #     user = StationEModel.objects.create(HCID=validated_data['HCID'],
    #                                    HCPID=validated_data['HCPID'],
    #                                    InfoseekId=validated_data['InfoseekId'],
    #                                    EntryTime = validated_data['EntryTime'],
    #                                    Child_Mobility = validated_data['Child_Mobility'],
    #                                    Child_Mobility_Can_not_Walk = validated_data['Child_Mobility_Can_not_Walk'],
    #                                    Child_Mobility_Can_not_Walk_other = validated_data['Child_Mobility_Can_not_Walk_other'],
    #                                    Student_Ambulant = validated_data['Student_Ambulant'],
    #                                    Student_Ambulant_No = validated_data['Student_Ambulant_No'],
    #                                    Gait = validated_data['Gait'],
    #                                    Gait_Abnormal = validated_data['Gait_Abnormal'],
    #                                    Gait_Abnormal_Limp = validated_data['Gait_Abnormal_Limp'],
    #                                    Gait_Abnormal_Limp_other = validated_data['Gait_Abnormal_Limp_other'],
                                    
    #                                     )
    #     user.save()
    #     return user 


class StationESerilizers3(serializers.ModelSerializer):
    class Meta:
        model = StationEModel
        fields = ['UL_Right_Appearance', 'UL_Right_Appearance_Abnormal','UL_Right_Motor_Function_Tone','UL_Right_Motor_Function_Range_of_Movement','UL_Right_MF_RM_Abnormal', 'UL_Right_MF_RM_Abnormal_Hyper_Flexible',
                  'UL_Right_MF_RM_Abnormal_Restricted','UL_Right_Motor_Function_Strength','UL_Right_Deep_Tendon_Reflexes_Biceps',
                  'UL_Right_DTR_Biceps_Abnormal','UL_Right_Deep_Tendon_Reflexes_Radial','UL_Right_DTR_Radial_Abnormal',
                  'UL_Right_Deep_Tendon_Reflexes_Sensory_Function', 'UL_Right_DTR_SF_Abnormal','UL_Right_DTR_SF_Abnormal_Touch',
                  'UL_Right_DTR_SF_Abnormal_Pain_Present','UL_Right_DTR_SF_Abnormal_Pressure_Abnormal',
                  'UL_Right_DTR_SF_Abnormal_Tenderness_Present','UL_Left_Appearance','UL_Left_Appearance_Abnormal',
                  'UL_Left_Motor_Function_Tone','UL_Left_Motor_Function_Range_of_Movement', 'UL_left_MF_RM_Abnormal' ,'UL_Left_MF_RM_Abnormal_Hyper_Flexible',
                  'UL_Left_MF_RM_Abnormal_Restricted','UL_Left_Motor_Function_Strength','UL_Left_Deep_Tendon_Reflexes_Biceps',
                  'UL_Left_DTR_Biceps_Abnormal','UL_Left_Deep_Tendon_Reflexes_Radial','UL_Left_DTR_Radial_Abnormal',
                  'UL_Left_Deep_Tendon_Reflexes_Sensory_Function', 'UL_Left_DTR_SF_Abnormal','UL_Left_DTR_SF_Abnormal_Touch',
                  'UL_Left_DTR_SF_Abnormal_Pain_Present','UL_Left_DTR_SF_Abnormal_Pressure_Abnormal',
                  'UL_Left_DTR_SF_Abnormal_Tenderness_Present','Reviewed_By','Reviewed_On']
        


class StationESerializers4(serializers.ModelSerializer):
    class Meta:
        model = StationEModel
        fields = ['LL_Right_Appearance','LL_Right_Appearance_Abnormal','LL_Right_Motor_Function_Tone','LL_Right_Motor_Function_Range_of_Movement',
                  'LL_Right_Motor_Function_Strength','LL_Right_Motor_Function_Knee','LL_Right_Motor_Function_Knee_Abnormal',
                  'LL_Right_Deep_Tendon_Reflexes_Sensory_Function', 'LL_Right_DTR_SF_Abnormal','LL_Right_DTR_SF_Abnormal_Touch','LL_Right_DTR_SF_Abnormal_Pain_Present',
                  'LL_Right_DTR_SF_Abnormal_Pressure_Abnormal','LL_Right_DTR_SF_Abnormal_Tenderness_Present',
                  'LL_Left_Appearance','LL_Left_Appearance_Abnormal','LL_Left_Motor_Function_Tone','LL_Left_Motor_Function_Range_of_Movement',
                  'LL_Left_Motor_Function_Strength','LL_Left_Motor_Function_Knee','LL_Left_Motor_Function_Knee_Abnormal',
                  'LL_Left_Deep_Tendon_Reflexes_Sensory_Function', 'LL_Left_DTR_SF_Abnormal','LL_Left_DTR_SF_Abnormal_Touch',
                  'LL_Left_DTR_SF_Abnormal_Pain_Present','LL_Left_DTR_SF_Abnormal_Pressure_Abnormal',
                  'LL_Left_DTR_SF_Abnormal_Tenderness_Present','Reviewed_By','Reviewed_On']
        
class StationESerializers5(serializers.ModelSerializer):
    class Meta:
        model = StationEModel
        fields = ['Other_Observations','Specialist_Referral_Needed',
                  'Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag','Other','Completed','Reviewed_By','Reviewed_On','EndTime']








class GetStationESerializers(serializers.ModelSerializer):
    class Meta:
        model = StationEModel
        fields = ['id','StationID','HCID','HCPID','InfoseekId','EntryTime','Child_Mobility','Child_Mobility_Can_not_Walk', 'Child_Mobility_Can_not_Walk_other', 'Student_Ambulant','Student_Ambulant_No' ,'Gait', 'Gait_Abnormal', 'Gait_Abnormal_Limp', 'Gait_Abnormal_Limp_other','Wear_Brace_Support', 'Wear_Brace_Support_Yes','Prosthesis','Prosthesis_Yes', 'Prosthesis_Yes_other','Spine_Appearance','Spine_Appearance_Abnormal','Spine_Appearance_Abnormal_Other','Shoulder_Griddle_Appearance','Shoulder_Griddle_Appearance_Abnormal',
                  'Shoulder_Griddle_Appearance_Abnormal_Other','Spine_Mobility','Spine_Mobility_Restricted_movement','Neck_Mobility','Neck_Mobility_Restricted_movement',
                 'UL_Right_Appearance', 'UL_Right_Appearance_Abnormal','UL_Right_Motor_Function_Tone','UL_Right_Motor_Function_Range_of_Movement', 'UL_Right_MF_RM_Abnormal', 'UL_Right_MF_RM_Abnormal_Hyper_Flexible',
                  'UL_Right_MF_RM_Abnormal_Restricted','UL_Right_Motor_Function_Strength','UL_Right_Deep_Tendon_Reflexes_Biceps',
                  'UL_Right_DTR_Biceps_Abnormal','UL_Right_Deep_Tendon_Reflexes_Radial','UL_Right_DTR_Radial_Abnormal',
                  'UL_Right_Deep_Tendon_Reflexes_Sensory_Function','UL_Right_DTR_SF_Abnormal_Touch',
                  'UL_Right_DTR_SF_Abnormal_Pain_Present','UL_Right_DTR_SF_Abnormal_Pressure_Abnormal',
                  'UL_Right_DTR_SF_Abnormal_Tenderness_Present','UL_Left_Appearance','UL_Left_Appearance_Abnormal',
                  'UL_Left_Motor_Function_Tone','UL_Left_Motor_Function_Range_of_Movement', 'UL_left_MF_RM_Abnormal','UL_Left_MF_RM_Abnormal_Hyper_Flexible',
                  'UL_Left_MF_RM_Abnormal_Restricted','UL_Left_Motor_Function_Strength','UL_Left_Deep_Tendon_Reflexes_Biceps',
                  'UL_Left_DTR_Biceps_Abnormal','UL_Left_Deep_Tendon_Reflexes_Radial','UL_Left_DTR_Radial_Abnormal',
                  'UL_Left_Deep_Tendon_Reflexes_Sensory_Function','UL_Left_DTR_SF_Abnormal_Touch',
                  'UL_Left_DTR_SF_Abnormal_Pain_Present','UL_Left_DTR_SF_Abnormal_Pressure_Abnormal',
                  'UL_Left_DTR_SF_Abnormal_Tenderness_Present',
                  'LL_Right_Appearance','LL_Right_Appearance_Abnormal','LL_Right_Motor_Function_Tone','LL_Right_Motor_Function_Range_of_Movement',
                  'LL_Right_Motor_Function_Strength','LL_Right_Motor_Function_Knee','LL_Right_Motor_Function_Knee_Abnormal',
                  'LL_Right_Deep_Tendon_Reflexes_Sensory_Function','LL_Right_DTR_SF_Abnormal_Touch','LL_Right_DTR_SF_Abnormal_Pain_Present',
                  'LL_Right_DTR_SF_Abnormal_Pressure_Abnormal','LL_Right_DTR_SF_Abnormal_Tenderness_Present',
                  'LL_Left_Appearance','LL_Left_Appearance_Abnormal','LL_Left_Motor_Function_Tone','LL_Left_Motor_Function_Range_of_Movement',
                  'LL_Left_Motor_Function_Strength','LL_Left_Motor_Function_Knee','LL_Left_Motor_Function_Knee_Abnormal',
                  'LL_Left_Deep_Tendon_Reflexes_Sensory_Function','LL_Left_DTR_SF_Abnormal_Touch',
                  'LL_Left_DTR_SF_Abnormal_Pain_Present','LL_Left_DTR_SF_Abnormal_Pressure_Abnormal',
                  'LL_Left_DTR_SF_Abnormal_Tenderness_Present','Other_Observations','Specialist_Referral_Needed',
                  'Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag','Other','Completed','Review_Status','Reviewed_By',
                  'Reviewed_On','Comments','EndTime']
        

