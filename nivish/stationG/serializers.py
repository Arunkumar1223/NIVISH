from .models import *
from rest_framework import serializers


class StationGSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = ['HCID','HCPID','InfoseekId','EntryTime','Central_Nervous_System_Alert','CNS_Oriented','CNS_Listens','CNS_Understands','CNS_Responds','CNS_Speech', 'CNS_Speech_Abnormal','CNS_Speech_Abnormal_Other',
                  'CNS_History_of_Headache','CNS_History_of_Headache_yes_Frequency','CNS_History_of_Headache_yes_Frequency_Continuous','CNS_History_of_Headache_yes_Associated_With',
                  'CNS_History_of_Headache_yes_Associated_With_Occurrence','CNS_History_of_Headache_yes_Associated_With_Other','CNS_History_of_Headache_yes_From','CNS_History_of_Headache_yes_Duration',
                  'CNS_History_of_Dizziness','CNS_History_of_Dizziness_yes_Frequency','CNS_History_of_Dizziness_yes_Frequency_Continuous','CNS_History_of_Dizziness_yes_Associated_With',       
                  'CNS_History_of_Dizziness_yes_Associated_With_Occurrence','CNS_History_of_Dizziness_yes_Associated_With_Other']


class GetStationGPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = ['id','StationID','HCID','HCPID','InfoseekId','EntryTime','Central_Nervous_System_Alert','CNS_Oriented','CNS_Listens','CNS_Understands','CNS_Responds','CNS_Speech', 'CNS_Speech_Abnormal','CNS_Speech_Abnormal_Other',
                  'CNS_History_of_Headache','CNS_History_of_Headache_yes_Frequency','CNS_History_of_Headache_yes_Frequency_Continuous','CNS_History_of_Headache_yes_Associated_With',
                  'CNS_History_of_Headache_yes_Associated_With_Occurrence','CNS_History_of_Headache_yes_Associated_With_Other','CNS_History_of_Headache_yes_From','CNS_History_of_Headache_yes_Duration',
                  'CNS_History_of_Dizziness','CNS_History_of_Dizziness_yes_Frequency','CNS_History_of_Dizziness_yes_Frequency_Continuous','CNS_History_of_Dizziness_yes_Associated_With',       
                  'CNS_History_of_Dizziness_yes_Associated_With_Occurrence','CNS_History_of_Dizziness_yes_Associated_With_Other']


class UpdateStationGSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = ['HCID','HCPID','InfoseekId','Central_Nervous_System_Alert','CNS_Oriented','CNS_Listens','CNS_Understands','CNS_Responds','CNS_Speech', 'CNS_Speech_Abnormal','CNS_Speech_Abnormal_Other',
                  'CNS_History_of_Headache','CNS_History_of_Headache_yes_Frequency','CNS_History_of_Headache_yes_Frequency_Continuous','CNS_History_of_Headache_yes_Associated_With',
                  'CNS_History_of_Headache_yes_Associated_With_Occurrence','CNS_History_of_Headache_yes_Associated_With_Other','CNS_History_of_Headache_yes_From','CNS_History_of_Headache_yes_Duration',
                  'CNS_History_of_Dizziness','CNS_History_of_Dizziness_yes_Frequency','CNS_History_of_Dizziness_yes_Frequency_Continuous','CNS_History_of_Dizziness_yes_Associated_With',       
                  'CNS_History_of_Dizziness_yes_Associated_With_Occurrence','CNS_History_of_Dizziness_yes_Associated_With_Other', 'Reviewed_By','Reviewed_On']


class StationGSerializersS2(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = ['Respiratory_System_Do_you_Feel_Breathless','RS_Do_you_have_a_Cough',
                  'RS_Shape_of_Chest','RS_Shape_of_Chest_Abnormal','RS_Shape_of_Chest_Abnormal_Other',
                  'RS_Type_of_Respiration', 'RS_Type_of_Respiration_Abdominal','RS_Type_of_Respiration_Abdominal_Other',
                  'RS_Type_of_Respiration_Thoracic','RS_Type_of_Respiration_Thoracic_Other',
                  'RS_Type_of_Respiration_Abdomino_Thoracic','RS_Type_of_Respiration_Abdomino_Thoracic_Other','RS_Trachea',
                  'RS_Evidence_of_Tracheostomy', 'Reviewed_By','Reviewed_On']
        


class StationGSerializersS3(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = ['Right_Lung_Air_Entry_Normal','RL_Breath_Sounds','RL_Breath_Sounds_Abnormal','RL_Breath_Sounds_Abnormal_Apical','RL_Breath_Sounds_Abnormal_Mid_Zone','RL_Breath_Sounds_Abnormal_Basal','RL_Breath_Sounds_Abnormal_Sub_Scapular', 'RL_Breath_Sounds_Abnormal_Diffuse','RL_Rales_Crepts',
                  'RL_Rales_Crepts_Present','RL_Rales_Crepts_Present_Apical','RL_Rales_Crepts_Present_Apical_Fine','RL_Rales_Crepts_Present_Apical_Coarse','RL_Rales_Crepts_Present_Mid_Zone','RL_Rales_Crepts_Present_Mid_Zone_Fine','RL_Rales_Crepts_Present_Mid_Zone_Coarse',
                  'RL_Rales_Crepts_Present_Basal','RL_Rales_Crepts_Present_Basal_Fine','RL_Rales_Crepts_Present_Basal_Coarse','RL_Rales_Crepts_Present_Sub_Scapular',
                  'RL_Rales_Crepts_Present_Sub_Scapular_Fine','RL_Rales_Crepts_Present_Sub_Scapular_Coarse','RL_Rales_Crepts_Present_Diffuse','RL_Rales_Crepts_Present_Diffuse_Fine','RL_Rales_Crepts_Present_Diffuse_Coarse',
                  'RL_Rhonchi_Wheezing','RL_Rhonchi_Wheezing_Present','RL_Added_Sounds','RL_Added_Sounds_Present','RL_Added_Zone_of_Concern','RL_Added_Zone_of_Concern_Abnormal',
                  'Left_Lung_Air_Entry_Normal','LL_Breath_Sounds','LL_Breath_Sounds_Abnormal','LL_Breath_Sounds_Abnormal_Apical','LL_Breath_Sounds_Abnormal_Mid_Zone','LL_Breath_Sounds_Abnormal_Basal','LL_Breath_Sounds_Abnormal_Sub_Scapular', 'LL_Breath_Sounds_Abnormal_Diffuse','LL_Rales_Crepts',
                  'LL_Rales_Crepts_Present','LL_Rales_Crepts_Present_Apical','LL_Rales_Crepts_Present_Apical_Fine','LL_Rales_Crepts_Present_Apical_Coarse','LL_Rales_Crepts_Present_Mid_Zone','LL_Rales_Crepts_Present_Mid_Zone_Fine','LL_Rales_Crepts_Present_Mid_Zone_Coarse',
                  'LL_Rales_Crepts_Present_Basal','LL_Rales_Crepts_Present_Basal_Fine','LL_Rales_Crepts_Present_Basal_Coarse','LL_Rales_Crepts_Present_Sub_Scapular',
                  'LL_Rales_Crepts_Present_Sub_Scapular_Fine','LL_Rales_Crepts_Present_Sub_Scapular_Coarse','LL_Rales_Crepts_Present_Diffuse','LL_Rales_Crepts_Present_Diffuse_Fine','LL_Rales_Crepts_Present_Diffuse_Coarse',
                  'LL_Rhonchi_Wheezing','LL_Rhonchi_Wheezing_Present','LL_Added_Sounds','LL_Added_Sounds_Present','LL_Added_Zone_of_Concern','LL_Added_Zone_of_Concern_Abnormal', 'Reviewed_By','Reviewed_On',]
        

class StationGSerializersS4(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = ['Cardio_Vascular_Systems_Do_you_get_Palpitation','CVS_Fainted_in_Home_School_Workplace_at_any_time','CVS_Jugular_Pulsations',
                  'CVS_Jugular_Pulsations_Visible','CVS_Jugular_Pulsations_Visible_Abnormal','CVS_Suprasternal_Pulsations', 'CVS_Suprasternal_Pulsations_Present',
                  'CVS_Peripheral_Pulsations_Radial','CVS_Peripheral_Pulsations_Radial_Present','CVS_Peripheral_Pulsations_Radial_Present_Abnormal',
                  'CVS_Peripheral_Pulsations_Dorsalis_Pedis','CVS_Peripheral_Pulsations_Dorsalis_Pedis_Present','CVS_Peripheral_Pulsations_Dorsalis_Pedis_Abnormal',
                  'CVS_Peripheral_Pulsations_Other_abnormality','CVS_S1','CVS_S2','CVS_S3','CVS_Murmur','CVS_Murmur_Present','CVS_Murmur_Present_Other',
                  'CVS_Click','CVS_Click_Present_Position','CVS_Apex_Beat','CVS_Apex_Beat_Present_Displaced', 'Reviewed_By','Reviewed_On',]
                


class StationGSerializersS5(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = [
            'Alimentary_and_Urinary_System_Do_you_have_Nausea_Vomiting','AUS_Do_you_have_Pain_in_your_Abdomen','AUS_Do_you_feel_Burning_when_you_pass_Urine',
            'AUS_Cleft_Lip','AUS_Cleft_Lip_Present','AUS_Cleft_Palate','AUS_Cleft_Palate_Present','AUS_Abdominal_Distension','AUS_Exaggerate_Bowel_Sounds',
            'AUS_Guarding','AUS_Rigidity','AUS_Right_Hypochondrium_Pain','AUS_RH_Pain_Yes_Pain_Score','AUS_RH_Tenderness','AUS_RH_Tenderness_Present',
            'AUS_RH_Swelling_Lumps','AUS_RH_Swelling_Lumps_Present_Description','AUS_RH_Swelling_Lumps_Present_Size','AUS_RH_Swelling_Lumps_Present_Texture',
            'AUS_RH_Liver','AUS_RH_Liver_Palpable','AUS_RH_Gall_Bladder','AUS_RH_Gall_Bladder_Tender','AUS_Right_Lumbar_Pain','AUS_RL_Pain_Yes_Pain_Score',
            'AUS_RL_Tenderness','AUS_RL_Tenderness_Present','AUS_RL_Swelling_Lumps','AUS_RL_Swelling_Lumps_Present_Description','AUS_RL_Swelling_Lumps_Present_Size',
            'AUS_RL_Swelling_Lumps_Present_Texture','AUS_RL_Right_Kidney','AUS_RL_Right_Kidney_Palpable','AUS_Right_Iliac_Pain','AUS_RI_Pain_Yes_Pain_Score','AUS_RI_MBP','AUS_RI_MBP_Pain_Score',
            'AUS_RI_Tenderness','AUS_RI_Tenderness_Present','AUS_RI_Swelling_Lumps','AUS_RI_Swelling_Lumps_Present_Description','AUS_RI_Swelling_Lumps_Present_Size',
            'AUS_RI_Swelling_Lumps_Present_Texture','AUS_Epigastric_Pain','AUS_E_Pain_Yes_Pain_Score','AUS_E_Tenderness','AUS_E_Tenderness_Present','AUS_E_Tenderness_Present_Rebound',
            'AUS_E_Swelling_Lumps','AUS_E_Swelling_Lumps_Present_Description','AUS_E_Swelling_Lumps_Present_Size','AUS_E_Swelling_Lumps_Present_Texture',
            'AUS_Umbilical_Pain','AUS_U_Pain_Yes_Pain_Score','AUS_U_Tenderness','AUS_U_Tenderness_Present','AUS_U_Tenderness_Present_Rebound','AUS_U_Swelling_Lumps','AUS_U_Swelling_Lumps_Present_Description',
            'AUS_U_Swelling_Lumps_Present_Size','AUS_U_Swelling_Lumps_Present_Texture','AUS_Suprapubic_Pain','AUS_S_Pain_Yes_Pain_Score','AUS_S_Tenderness',
            'AUS_S_Tenderness_Present','AUS_S_Tenderness_Present_Rebound','AUS_S_Swelling_Lumps','AUS_S_Swelling_Lumps_Present_Description','AUS_S_Swelling_Lumps_Present_Size','AUS_S_Swelling_Lumps_Present_Texture','AUS_S_Uterus','AUS_S_Uterus_Palpable',
            'AUS_Left_Hypochondrium_Pain','AUS_LH_Pain_Yes_Pain_Score','AUS_LH_Tenderness','AUS_LH_Tenderness_Present','AUS_LH_Swelling_Lumps','AUS_LH_Swelling_Lumps_Present_Description',
            'AUS_LH_Swelling_Lumps_Present_Size','AUS_LH_Swelling_Lumps_Present_Texture','AUS_LH_Spleen','AUS_LH_Spleen_Palpable',
            'AUS_Left_Lumbar_Pain','AUS_LL_Pain_Yes_Pain_Score','AUS_LL_Tenderness','AUS_LL_Tenderness_Present','AUS_LL_Swelling_Lumps',
            'AUS_LL_Swelling_Lumps_Present_Description','AUS_LL_Swelling_Lumps_Present_Size','AUS_LL_Swelling_Lumps_Present_Texture','AUS_LL_Left_Kidney',
            'AUS_LL_Left_Kidney_Palpable','AUS_Left_Iliac_Pain','AUS_LI_Pain_Yes_Pain_Score','AUS_LI_Tenderness','AUS_LI_Tenderness_Present','AUS_LI_Swelling_Lumps',
            'AUS_LI_Swelling_Lumps_Present_Description','AUS_LI_Swelling_Lumps_Present_Size','AUS_LI_Swelling_Lumps_Present_Texture','AUS_Hernia',
            'AUS_Hernia_Present','AUS_Urinary_Bladder','AUS_Urinary_Bladder_Palpable', 'Reviewed_By','Reviewed_On',
        ]





class StationGSerializersS6A(serializers.ModelSerializer):
    class Meta:
        model = StationGModel

        fields = [
            'Pubertal_Assessment_Girls','PAG_Tanner_Score','PAG_Menarche_Attained','PAG_MA_Yes_Age_of_Menarche','PAG_MA_Yes_LMP_Date','PAG_MA_Yes_Character_Regularity',
            'PAG_MA_Yes_Character_Frequency_in_Days','PAG_MA_Yes_Duration_in_days','PAG_MA_Yes_Flow','PAG_MA_Yes_Comfort','PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses',
            'PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes','PAG_MA_Yes_Pain_in_other_parts_body_during_menses_Yes_Other','PAG_Yes_Cracking_of_Voice_or_chnage_in_voice',
            'PAG_HaveYouExperienced_A_change_in_behaviour_recently','PAG_Change_behaviour_Yes','PAG_Change_behaviour_Yes_Quiet_Withdrawn','PAG_Change_behaviour_Outgoing','PAG_Change_behaviour_Aggressive',
            'PAG_Change_behaviour_Bold_and_Daring','PAG_Change_behaviour_Careless','PAG_Prefer_company_of','PAG_Any_other_abnormal_finding','PAG_Any_other_abnormal_finding_Yes', 'Reviewed_By','Reviewed_On',
        ]




class StationGSerializersS6B(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = [
            'Pubertal_Assessment_Boys','PAB_Tanner_Score','PAB_Yes_Cracking_of_Voice_or_chnage_in_voice','PAB_Nightly_Emissions','PAB_HaveYouExperienced_A_change_in_behaviour_recently','PAB_Change_behaviour_Yes',
            'PAB_Change_behaviour_Yes_Quiet_Withdrawn','PAB_Change_behaviour_Outgoing','PAB_Change_behaviour_Aggressive','PAB_Change_behaviour_Bold_and_Daring',
            'PAB_Change_behaviour_Careless','PAB_Prefer_company_of','PAB_Any_other_abnormal_finding','PAB_Any_other_abnormal_finding_Yes', 'Reviewed_By','Reviewed_On',
        ]


class StationGSerializersS7(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = [
            # Your previous fields
            'History_of_Medication',
            'History_of_Medication_Yes',
            'Name_of_Medication',
            'Reviewed_By',
            'Reviewed_On',
            # Add any other fields you might have
        ]


        
class StationGSerializersS8(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = [
            'Milestones',
            'Reviewed_By',
            'Reviewed_On',
        ]


class StationGSerializersS9(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = [
            # Your previous fields
            'Other_Observations',
            'Specialist_Referral_Needed',
            'Specialist_Referral_Needed_Type',
            'Specialist_Referral_Needed_Flag',
            'Other','Completed','EndTime', 'Reviewed_By','Reviewed_On',
            
        ]



class GetStationGSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = ['id','StationID','HCID','HCPID','InfoseekId','EntryTime','Central_Nervous_System_Alert','CNS_Oriented','CNS_Listens','CNS_Understands','CNS_Responds','CNS_Speech', 'CNS_Speech_Abnormal','CNS_Speech_Abnormal_Other',
                  'CNS_History_of_Headache','CNS_History_of_Headache_yes_Frequency','CNS_History_of_Headache_yes_Frequency_Continuous','CNS_History_of_Headache_yes_Associated_With',
                  'CNS_History_of_Headache_yes_Associated_With_Occurrence','CNS_History_of_Headache_yes_Associated_With_Other','CNS_History_of_Headache_yes_From','CNS_History_of_Headache_yes_Duration',
                  'CNS_History_of_Dizziness','CNS_History_of_Dizziness_yes_Frequency','CNS_History_of_Dizziness_yes_Frequency_Continuous','CNS_History_of_Dizziness_yes_Associated_With',
                  'CNS_History_of_Dizziness_yes_Associated_With_Occurrence','CNS_History_of_Dizziness_yes_Associated_With_Other',
                  
                  'Respiratory_System_Do_you_Feel_Breathless','RS_Do_you_have_a_Cough',
                  'RS_Shape_of_Chest','RS_Shape_of_Chest_Abnormal','RS_Shape_of_Chest_Abnormal_Other',
                  'RS_Type_of_Respiration', 'RS_Type_of_Respiration_Abdominal','RS_Type_of_Respiration_Abdominal_Other',
                  'RS_Type_of_Respiration_Thoracic','RS_Type_of_Respiration_Thoracic_Other',
                  'RS_Type_of_Respiration_Abdomino_Thoracic','RS_Type_of_Respiration_Abdomino_Thoracic_Other','RS_Trachea',
                  'RS_Evidence_of_Tracheostomy',

                  'Right_Lung_Air_Entry_Normal','RL_Breath_Sounds','RL_Breath_Sounds_Abnormal','RL_Breath_Sounds_Abnormal_Apical','RL_Breath_Sounds_Abnormal_Mid_Zone','RL_Breath_Sounds_Abnormal_Basal','RL_Breath_Sounds_Abnormal_Sub_Scapular', 'RL_Breath_Sounds_Abnormal_Diffuse','RL_Rales_Crepts','RL_Rales_Crepts_Present',
                  'RL_Rales_Crepts_Present_Apical','RL_Rales_Crepts_Present_Apical_Fine','RL_Rales_Crepts_Present_Apical_Coarse','RL_Rales_Crepts_Present_Mid_Zone','RL_Rales_Crepts_Present_Mid_Zone_Fine','RL_Rales_Crepts_Present_Mid_Zone_Coarse',
                  'RL_Rales_Crepts_Present_Basal','RL_Rales_Crepts_Present_Basal_Fine','RL_Rales_Crepts_Present_Basal_Coarse','RL_Rales_Crepts_Present_Sub_Scapular',
                  'RL_Rales_Crepts_Present_Sub_Scapular_Fine','RL_Rales_Crepts_Present_Sub_Scapular_Coarse','RL_Rales_Crepts_Present_Diffuse','RL_Rales_Crepts_Present_Diffuse_Fine','RL_Rales_Crepts_Present_Diffuse_Coarse',
                  'RL_Rhonchi_Wheezing','RL_Rhonchi_Wheezing_Present','RL_Added_Sounds','RL_Added_Zone_of_Concern', 'RL_Added_Zone_of_Concern_Abnormal','RL_Added_Sounds_Present',
                  'Left_Lung_Air_Entry_Normal','LL_Breath_Sounds','LL_Breath_Sounds_Abnormal','LL_Breath_Sounds_Abnormal_Apical','LL_Breath_Sounds_Abnormal_Mid_Zone','LL_Breath_Sounds_Abnormal_Basal','LL_Breath_Sounds_Abnormal_Sub_Scapular', 'LL_Breath_Sounds_Abnormal_Diffuse','LL_Rales_Crepts','LL_Rales_Crepts_Present',
                  'LL_Rales_Crepts_Present_Apical','LL_Rales_Crepts_Present_Apical_Fine','LL_Rales_Crepts_Present_Apical_Coarse','LL_Rales_Crepts_Present_Mid_Zone','LL_Rales_Crepts_Present_Mid_Zone_Fine','LL_Rales_Crepts_Present_Mid_Zone_Coarse',
                  'LL_Rales_Crepts_Present_Basal','LL_Rales_Crepts_Present_Basal_Fine','LL_Rales_Crepts_Present_Basal_Coarse','LL_Rales_Crepts_Present_Sub_Scapular',
                  'LL_Rales_Crepts_Present_Sub_Scapular_Fine','LL_Rales_Crepts_Present_Sub_Scapular_Coarse','LL_Rales_Crepts_Present_Diffuse','LL_Rales_Crepts_Present_Diffuse_Fine','LL_Rales_Crepts_Present_Diffuse_Coarse',
                  'LL_Rhonchi_Wheezing','LL_Rhonchi_Wheezing_Present','LL_Added_Sounds','LL_Added_Zone_of_Concern','LL_Added_Zone_of_Concern_Abnormal','LL_Added_Sounds_Present',
        
                  'Cardio_Vascular_Systems_Do_you_get_Palpitation','CVS_Fainted_in_Home_School_Workplace_at_any_time','CVS_Jugular_Pulsations',
                  'CVS_Jugular_Pulsations_Visible','CVS_Jugular_Pulsations_Visible_Abnormal','CVS_Suprasternal_Pulsations', 'CVS_Suprasternal_Pulsations_Present',
                  'CVS_Peripheral_Pulsations_Radial','CVS_Peripheral_Pulsations_Radial_Present','CVS_Peripheral_Pulsations_Radial_Present_Abnormal',
                  'CVS_Peripheral_Pulsations_Dorsalis_Pedis','CVS_Peripheral_Pulsations_Dorsalis_Pedis_Present','CVS_Peripheral_Pulsations_Dorsalis_Pedis_Abnormal',
                  'CVS_Peripheral_Pulsations_Other_abnormality','CVS_S1','CVS_S2','CVS_S3','CVS_Murmur','CVS_Murmur_Present','CVS_Murmur_Present_Other',
                  'CVS_Click','CVS_Click_Present_Position','CVS_Apex_Beat','CVS_Apex_Beat_Present_Displaced',


                  'Alimentary_and_Urinary_System_Do_you_have_Nausea_Vomiting','AUS_Do_you_have_Pain_in_your_Abdomen','AUS_Do_you_feel_Burning_when_you_pass_Urine',
                    'AUS_Cleft_Lip','AUS_Cleft_Lip_Present','AUS_Cleft_Palate','AUS_Cleft_Palate_Present','AUS_Abdominal_Distension','AUS_Exaggerate_Bowel_Sounds',
                    'AUS_Guarding','AUS_Rigidity','AUS_Right_Hypochondrium_Pain','AUS_RH_Pain_Yes_Pain_Score','AUS_RH_Tenderness','AUS_RH_Tenderness_Present',
                    'AUS_RH_Swelling_Lumps','AUS_RH_Swelling_Lumps_Present_Description','AUS_RH_Swelling_Lumps_Present_Size','AUS_RH_Swelling_Lumps_Present_Texture',
                    'AUS_RH_Liver','AUS_RH_Liver_Palpable','AUS_RH_Gall_Bladder','AUS_RH_Gall_Bladder_Tender','AUS_Right_Lumbar_Pain','AUS_RL_Pain_Yes_Pain_Score',
                    'AUS_RL_Tenderness','AUS_RL_Tenderness_Present','AUS_RL_Swelling_Lumps','AUS_RL_Swelling_Lumps_Present_Description','AUS_RL_Swelling_Lumps_Present_Size',
                    'AUS_RL_Swelling_Lumps_Present_Texture','AUS_RL_Right_Kidney','AUS_RL_Right_Kidney_Palpable','AUS_Right_Iliac_Pain','AUS_RI_Pain_Yes_Pain_Score','AUS_RI_MBP','AUS_RI_MBP_Pain_Score',
                    'AUS_RI_Tenderness','AUS_RI_Tenderness_Present','AUS_RI_Swelling_Lumps','AUS_RI_Swelling_Lumps_Present_Description','AUS_RI_Swelling_Lumps_Present_Size',
                    'AUS_RI_Swelling_Lumps_Present_Texture','AUS_Epigastric_Pain','AUS_E_Pain_Yes_Pain_Score','AUS_E_Tenderness','AUS_E_Tenderness_Present','AUS_E_Tenderness_Present_Rebound',
                    'AUS_E_Swelling_Lumps','AUS_E_Swelling_Lumps_Present_Description','AUS_E_Swelling_Lumps_Present_Size','AUS_E_Swelling_Lumps_Present_Texture',
                    'AUS_Umbilical_Pain','AUS_U_Pain_Yes_Pain_Score','AUS_U_Tenderness','AUS_U_Tenderness_Present','AUS_U_Tenderness_Present_Rebound','AUS_U_Swelling_Lumps','AUS_U_Swelling_Lumps_Present_Description',
                    'AUS_U_Swelling_Lumps_Present_Size','AUS_U_Swelling_Lumps_Present_Texture','AUS_Suprapubic_Pain','AUS_S_Pain_Yes_Pain_Score','AUS_S_Tenderness',
                    'AUS_S_Tenderness_Present','AUS_S_Tenderness_Present_Rebound','AUS_S_Swelling_Lumps','AUS_S_Swelling_Lumps_Present_Description','AUS_S_Swelling_Lumps_Present_Size','AUS_S_Swelling_Lumps_Present_Texture','AUS_S_Uterus','AUS_S_Uterus_Palpable',
                    'AUS_Left_Hypochondrium_Pain','AUS_LH_Pain_Yes_Pain_Score','AUS_LH_Tenderness','AUS_LH_Tenderness_Present','AUS_LH_Swelling_Lumps','AUS_LH_Swelling_Lumps_Present_Description',
                    'AUS_LH_Swelling_Lumps_Present_Size','AUS_LH_Swelling_Lumps_Present_Texture','AUS_LH_Spleen','AUS_LH_Spleen_Palpable',
                    'AUS_Left_Lumbar_Pain','AUS_LL_Pain_Yes_Pain_Score','AUS_LL_Tenderness','AUS_LL_Tenderness_Present','AUS_LL_Swelling_Lumps',
                    'AUS_LL_Swelling_Lumps_Present_Description','AUS_LL_Swelling_Lumps_Present_Size','AUS_LL_Swelling_Lumps_Present_Texture','AUS_LL_Left_Kidney',
                    'AUS_LL_Left_Kidney_Palpable','AUS_Left_Iliac_Pain','AUS_LI_Pain_Yes_Pain_Score','AUS_LI_Tenderness','AUS_LI_Tenderness_Present','AUS_LI_Swelling_Lumps',
                    'AUS_LI_Swelling_Lumps_Present_Description','AUS_LI_Swelling_Lumps_Present_Size','AUS_LI_Swelling_Lumps_Present_Texture','AUS_Hernia',
                    'AUS_Hernia_Present','AUS_Urinary_Bladder','AUS_Urinary_Bladder_Palpable',



                    'Pubertal_Assessment_Girls','PAG_Tanner_Score','PAG_Menarche_Attained','PAG_MA_Yes_Age_of_Menarche','PAG_MA_Yes_LMP_Date','PAG_MA_Yes_Character_Regularity',
                    'PAG_MA_Yes_Character_Frequency_in_Days','PAG_MA_Yes_Duration_in_days','PAG_MA_Yes_Flow','PAG_MA_Yes_Comfort','PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses',
                    'PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes','PAG_MA_Yes_Pain_in_other_parts_body_during_menses_Yes_Other','PAG_Yes_Cracking_of_Voice_or_chnage_in_voice',
                    'PAG_HaveYouExperienced_A_change_in_behaviour_recently','PAG_Change_behaviour_Yes','PAG_Change_behaviour_Yes_Quiet_Withdrawn','PAG_Change_behaviour_Outgoing','PAG_Change_behaviour_Aggressive',
                    'PAG_Change_behaviour_Bold_and_Daring','PAG_Change_behaviour_Careless','PAG_Prefer_company_of','PAG_Any_other_abnormal_finding','PAG_Any_other_abnormal_finding_Yes',

                    'Pubertal_Assessment_Boys','PAB_Tanner_Score','PAB_Yes_Cracking_of_Voice_or_chnage_in_voice','PAB_Nightly_Emissions','PAB_HaveYouExperienced_A_change_in_behaviour_recently','PAB_Change_behaviour_Yes',
                    'PAB_Change_behaviour_Yes_Quiet_Withdrawn','PAB_Change_behaviour_Outgoing','PAB_Change_behaviour_Aggressive','PAB_Change_behaviour_Bold_and_Daring',
                    'PAB_Change_behaviour_Careless','PAB_Prefer_company_of','PAB_Any_other_abnormal_finding','PAB_Any_other_abnormal_finding_Yes',

                    'History_of_Medication','History_of_Medication_Yes','Name_of_Medication','Milestones','Other_Observations','Specialist_Referral_Needed',
                    'Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag','Other','Completed','Review_Status','Reviewed_By',
                    'Reviewed_On','Comments','EndTime'


                  ]
        

