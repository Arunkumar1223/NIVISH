from django.db import models

# Create your models here.
from Enum.enumstation_g import *
from Enum.enum import *
from datetime import datetime

class StationGModel(models.Model):

    # section - 1
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationG_StationId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationG_HCID',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationG_HcpId',on_delete=models.CASCADE)
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationG_InfoseekId',on_delete=models.CASCADE)
    
    EntryTime = models.TimeField()
    Central_Nervous_System_Alert = models.CharField(max_length=500, choices=StationGYorN, blank=True, null=True)  
    CNS_Oriented = models.CharField(max_length=500, choices=StationGYorN, blank=True, null=True) 
    CNS_Listens = models.CharField(max_length=500, choices=StationGYorN, blank=True, null=True)
    CNS_Understands = models.CharField(max_length=500, choices=StationGYorN, blank=True, null=True) 
    CNS_Responds = models.CharField(max_length=500, choices=StationGYorN, blank=True, null=True) 
    CNS_Speech = models.CharField(max_length=500, choices=NormalandAbnormal, blank=True, null=True)  
    CNS_Speech_Abnormal = models.CharField(max_length=500, blank=True, null=True)  
    CNS_Speech_Abnormal_Other = models.TextField(blank=True, null=True) 
   
   
    CNS_History_of_Headache = models.CharField(max_length=500, choices=SRNYesorNo, blank=True, null=True)  
    CNS_History_of_Headache_yes_Frequency = models.CharField(max_length=500, choices  = CNS_History_of_Headache_yes_Frequency_ENUM, blank=True, null=True)  
    CNS_History_of_Headache_yes_Frequency_Continuous = models.CharField(max_length=500, choices = CNS_History_of_Headache_yes_Frequency_Continuous_ENUM, blank=True, null=True)   
    CNS_History_of_Headache_yes_Associated_With  = models.CharField(max_length=100000, blank=True, null=True) 
     # Master Data((Multiple Select)) (Reading, Watching TV/ Movies, Computer Use, Nausea / Vomiting, Movement, No Particular Activity, Change of Posture, Exercising /Gymming, Hyper-tension, Sleeping, Occurrence, 
     # Glaucoma, Other Eye condition, Vision Problem, Menstrual Cycle, Pregnancy, Driving, Hunger/ Fasting, Salt intake, MSG (Ajino-moto) intake, Heat, Cold, Other)
    CNS_History_of_Headache_yes_Associated_With_Occurrence  = models.CharField(max_length=500, blank=True, null=True) 
    CNS_History_of_Headache_yes_Associated_With_Other  = models.TextField(blank=True, null=True) 
    CNS_History_of_Headache_yes_From   = models.CharField(max_length=500, choices = CNS_History_of_Headache_yes_From_ENUM, blank=True, null=True) 
    CNS_History_of_Headache_yes_Duration = models.CharField(max_length=500, choices = CNS_History_of_Headache_yes_Duration_ENUM, blank=True, null=True)  

    
    CNS_History_of_Dizziness = models.CharField(max_length=500, choices=SRNYesorNo, blank=True, null=True)  
    CNS_History_of_Dizziness_yes_Frequency = models.CharField(max_length=500, choices = CNS_History_of_Dizziness_yes_Frequency_ENUM, blank=True, null=True)  
    CNS_History_of_Dizziness_yes_Frequency_Continuous = models.CharField(max_length=500, choices = CNS_History_of_Dizziness_yes_Frequency_Continuous_ENUM, blank=True, null=True)  
    CNS_History_of_Dizziness_yes_Associated_With  = models.CharField(max_length=100000, blank=True, null=True) 
     # Master Data((Multiple Select)) (Reading, Watching TV/ Movies, Computer Use, Nausea / Vomiting, Movement, No Particular Activity, Change of Posture, Exercising /Gymming, Hyper-tension, Sleeping, Occurrence, 
     # Glaucoma, Other Eye condition, Vision Problem, Menstrual Cycle, Pregnancy, Driving, Hunger/ Fasting, Salt intake, MSG (Ajino-moto) intake, Heat, Cold, Other)
    CNS_History_of_Dizziness_yes_Associated_With_Occurrence  = models.CharField(max_length=500,blank=True, null=True)  
    CNS_History_of_Dizziness_yes_Associated_With_Other  = models.TextField(blank=True, null=True) 



    # section - 2 StationG2YorN
    
    Respiratory_System_Do_you_Feel_Breathless = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    RS_Do_you_have_a_Cough  = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True) 
    RS_Shape_of_Chest = models.CharField(max_length=500, choices = NormalandAbnormal, blank=True, null=True)   
    RS_Shape_of_Chest_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=RS_Shape_of_Chest_Abnormal_ENUM) 
    RS_Shape_of_Chest_Abnormal_Other = models.TextField(blank=True, null=True) 
    RS_Type_of_Respiration = models.CharField(max_length=500, choices = RS_Type_of_Respiration_ENUM, blank=True, null=True) 
    RS_Type_of_Respiration_Abdominal = models.CharField(max_length=500, choices = RS_Type_of_Respiration_Label_ENUM, blank=True, null=True) 
    RS_Type_of_Respiration_Abdominal_Other =  models.TextField(blank=True, null=True) 
    RS_Type_of_Respiration_Thoracic = models.CharField(max_length=500, choices = RS_Type_of_Respiration_Label_ENUM, blank=True, null=True) 
    RS_Type_of_Respiration_Thoracic_Other =  models.TextField(blank=True, null=True) 
    RS_Type_of_Respiration_Abdomino_Thoracic = models.CharField(max_length=500, choices = RS_Type_of_Respiration_Label_ENUM, blank=True, null=True) 
    RS_Type_of_Respiration_Abdomino_Thoracic_Other =  models.TextField(blank=True, null=True) 

    RS_Trachea = models.CharField(max_length=500, choices = RS_Trachea_ENUM, blank=True, null=True) 
    RS_Evidence_of_Tracheostomy = models.CharField(max_length=500, choices = RS_Evidence_of_Tracheostomy_ENUM, blank=True, null=True) 
    # section - 3

    ## Right_Lung
    Right_Lung_Air_Entry_Normal = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True) 
    RL_Breath_Sounds = models.CharField(max_length=1000, choices = NormalandAbnormal, blank=True, null=True) 
    RL_Breath_Sounds_Abnormal = models.CharField(max_length=500,blank=True, null=True)  
    RL_Breath_Sounds_Abnormal_Apical = models.CharField(max_length=500, choices = RBE_ENUM, blank=True, null=True)  
    RL_Breath_Sounds_Abnormal_Mid_Zone = models.CharField(max_length=500, choices = RBE_ENUM, blank=True, null=True)   
    RL_Breath_Sounds_Abnormal_Basal = models.CharField(max_length=500, choices = RBE_ENUM, blank=True, null=True)  
    RL_Breath_Sounds_Abnormal_Sub_Scapular = models.CharField(max_length=500, choices = RBE_ENUM, blank=True, null=True)    
    RL_Breath_Sounds_Abnormal_Diffuse = models.CharField(max_length=500, choices = RBE_ENUM, blank=True, null=True) 

    RL_Rales_Crepts =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)  
    RL_Rales_Crepts_Present =  models.CharField(max_length=500, blank=True, null=True)  
    RL_Rales_Crepts_Present_Apical =  models.CharField(max_length=500, choices = FC_ENUM, blank=True, null=True)  
    RL_Rales_Crepts_Present_Apical_Fine =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True)  
    RL_Rales_Crepts_Present_Apical_Coarse =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True)

    RL_Rales_Crepts_Present_Mid_Zone =  models.CharField(max_length=500, choices = FC_ENUM, blank=True, null=True)  
    RL_Rales_Crepts_Present_Mid_Zone_Fine =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True)  
    RL_Rales_Crepts_Present_Mid_Zone_Coarse = models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True) 

    RL_Rales_Crepts_Present_Basal =  models.CharField(max_length=500, choices = FC_ENUM, blank=True, null=True)  
    RL_Rales_Crepts_Present_Basal_Fine =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True) 
    RL_Rales_Crepts_Present_Basal_Coarse =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True)  

    
    RL_Rales_Crepts_Present_Sub_Scapular = models.CharField(max_length=500, choices = FC_ENUM, blank=True, null=True)  
    RL_Rales_Crepts_Present_Sub_Scapular_Fine = models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True) 
    RL_Rales_Crepts_Present_Sub_Scapular_Coarse =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True) 


    RL_Rales_Crepts_Present_Diffuse =  models.CharField(max_length=500, choices = FC_ENUM, blank=True, null=True)  
    RL_Rales_Crepts_Present_Diffuse_Fine =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True)  
    RL_Rales_Crepts_Present_Diffuse_Coarse =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True) 


    RL_Rhonchi_Wheezing =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    RL_Rhonchi_Wheezing_Present = models.CharField(max_length=500, choices = OTW_ENUM, blank=True, null=True)  
    RL_Added_Sounds =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    RL_Added_Sounds_Present = models.TextField(blank=True, null=True)  
    RL_Added_Zone_of_Concern =  models.CharField(max_length=50, null=True, blank=True, choices=AbsentandPresent)
    RL_Added_Zone_of_Concern_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Apical,Mid Zone, Basal, Sub Scapular, Diffuse)
     

    ## Left_Lung
    Left_Lung_Air_Entry_Normal = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True) 
    LL_Breath_Sounds = models.CharField(max_length=500, choices = NormalandAbnormal, blank=True, null=True)
    LL_Breath_Sounds_Abnormal = models.CharField(max_length=500,blank=True, null=True)     
    LL_Breath_Sounds_Abnormal_Apical = models.CharField(max_length=500, choices = RBE_ENUM, blank=True, null=True)  
    LL_Breath_Sounds_Abnormal_Mid_Zone = models.CharField(max_length=500, choices = RBE_ENUM, blank=True, null=True)   
    LL_Breath_Sounds_Abnormal_Basal = models.CharField(max_length=500, choices = RBE_ENUM, blank=True, null=True)  
    LL_Breath_Sounds_Abnormal_Sub_Scapular = models.CharField(max_length=500, choices = RBE_ENUM, blank=True, null=True)    
    LL_Breath_Sounds_Abnormal_Diffuse = models.CharField(max_length=500, choices = RBE_ENUM, blank=True, null=True) 

    LL_Rales_Crepts =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)  
    LL_Rales_Crepts_Present =  models.CharField(max_length=500, blank=True, null=True)  
    LL_Rales_Crepts_Present_Apical =  models.CharField(max_length=500, choices = FC_ENUM, blank=True, null=True)  
    LL_Rales_Crepts_Present_Apical_Fine =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True)  
    LL_Rales_Crepts_Present_Apical_Coarse =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True)

    LL_Rales_Crepts_Present_Mid_Zone =  models.CharField(max_length=500, choices = FC_ENUM, blank=True, null=True)  
    LL_Rales_Crepts_Present_Mid_Zone_Fine =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True)  
    LL_Rales_Crepts_Present_Mid_Zone_Coarse = models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True) 

    LL_Rales_Crepts_Present_Basal =  models.CharField(max_length=500, choices = FC_ENUM, blank=True, null=True)  
    LL_Rales_Crepts_Present_Basal_Fine =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True) 
    LL_Rales_Crepts_Present_Basal_Coarse =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True)  

    
    LL_Rales_Crepts_Present_Sub_Scapular = models.CharField(max_length=500, choices = FC_ENUM, blank=True, null=True)  
    LL_Rales_Crepts_Present_Sub_Scapular_Fine = models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True) 
    LL_Rales_Crepts_Present_Sub_Scapular_Coarse =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True) 


    LL_Rales_Crepts_Present_Diffuse =  models.CharField(max_length=500, choices = FC_ENUM, blank=True, null=True)  
    LL_Rales_Crepts_Present_Diffuse_Fine =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True)  
    LL_Rales_Crepts_Present_Diffuse_Coarse =  models.CharField(max_length=500, choices = WD_ENUM, blank=True, null=True) 


    LL_Rhonchi_Wheezing =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    LL_Rhonchi_Wheezing_Present = models.CharField(max_length=500, choices = OTW_ENUM, blank=True, null=True)  
    LL_Added_Sounds =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    LL_Added_Sounds_Present = models.TextField(blank=True, null=True) 
    LL_Added_Zone_of_Concern =  models.CharField(max_length=50, null=True, blank=True, choices=AbsentandPresent) 
    LL_Added_Zone_of_Concern_Abnormal =  models.CharField(max_length=100, null=True, blank=True)## Master Data (Multiple Select) (Apical,Mid Zone, Basal, Sub Scapular, Diffuse)
     

    # Section - 4

    Cardio_Vascular_Systems_Do_you_get_Palpitation =  models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)
    CVS_Fainted_in_Home_School_Workplace_at_any_time =  models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)
    CVS_Jugular_Pulsations =  models.CharField(max_length=500, choices = CVS_Jugular_Pulsations_ENUM, blank=True, null=True) 
    CVS_Jugular_Pulsations_Visible =  models.CharField(max_length=500, choices=NormalandAbnormal, blank=True, null=True) 
    CVS_Jugular_Pulsations_Visible_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Exaggerated, Bruit, JVP raised, Murmur)

    CVS_Suprasternal_Pulsations = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)  
    CVS_Suprasternal_Pulsations_Present = models.CharField(max_length=500, blank=True, null=True)
 
    CVS_Peripheral_Pulsations_Radial = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)  
    CVS_Peripheral_Pulsations_Radial_Present =  models.CharField(max_length=500, choices=NormalandAbnormal, blank=True, null=True) 
    CVS_Peripheral_Pulsations_Radial_Present_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Weak, Exaggerated, Bruit, Murmur, Water Hammer Pulse)
    CVS_Peripheral_Pulsations_Dorsalis_Pedis = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    CVS_Peripheral_Pulsations_Dorsalis_Pedis_Present =  models.CharField(max_length=500, choices=NormalandAbnormal, blank=True, null=True) 
    CVS_Peripheral_Pulsations_Dorsalis_Pedis_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Weak, Exaggerated, Bruit, Murmur, Water Hammer Pulse)
    CVS_Peripheral_Pulsations_Other_abnormality =  models.TextField(blank=True, null=True) 

    CVS_S1 =  models.CharField(max_length=500, choices=NormalandAbnormal, blank=True, null=True) 
    CVS_S2 =  models.CharField(max_length=500, choices=NormalandAbnormal, blank=True, null=True) 
    CVS_S3 =  models.CharField(max_length=500, choices=AbsentandPresent, blank=True, null=True) 

    CVS_Murmur =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    CVS_Murmur_Present =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Multiple Select) (Mitral valve, Tricuspid valve, Other (Text Box))
    CVS_Murmur_Present_Other =  models.TextField(blank=True, null=True) 

    CVS_Click = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    CVS_Click_Present_Position =  models.TextField(blank=True, null=True) 

    CVS_Apex_Beat =  models.CharField(max_length=500, choices = CVS_Apex_Beat_ENUM, blank=True, null=True) 
    CVS_Apex_Beat_Present_Displaced =  models.TextField(blank=True, null=True) 


    # Section - 5
    Alimentary_and_Urinary_System_Do_you_have_Nausea_Vomiting =   models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_Do_you_have_Pain_in_your_Abdomen =   models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_Do_you_feel_Burning_when_you_pass_Urine =   models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_Cleft_Lip = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_Cleft_Lip_Present =  models.CharField(max_length=500, choices = AUS_Cleft_Lip_Present_ENUM, blank=True, null=True)   
    AUS_Cleft_Palate = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_Cleft_Palate_Present =  models.CharField(max_length=500, choices = AUS_Cleft_Lip_Present_ENUM, blank=True, null=True) 

    AUS_Abdominal_Distension = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_Exaggerate_Bowel_Sounds = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    AUS_Guarding  = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_Rigidity  = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 

    AUS_Right_Hypochondrium_Pain =  models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_RH_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_RH_Tenderness = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_RH_Tenderness_Present = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True)  
    AUS_RH_Swelling_Lumps =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    AUS_RH_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_RH_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_RH_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, choices = SFH_ENUM, blank=True, null=True) 
    AUS_RH_Liver =  models.CharField(max_length=500, choices = NP_ENUM, blank=True, null=True)  
    AUS_RH_Liver_Palpable =  models.CharField(max_length=500, choices = AUS_LH_Liver_Palpable_ENUM, blank=True, null=True)  
    AUS_RH_Gall_Bladder = models.CharField(max_length=500, choices = NT_ENUM, blank=True, null=True)
    AUS_RH_Gall_Bladder_Tender =  models.IntegerField(blank=True, null=True)

    AUS_Right_Lumbar_Pain = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_RL_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_RL_Tenderness = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    AUS_RL_Tenderness_Present = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True)  
    AUS_RL_Swelling_Lumps =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_RL_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_RL_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_RL_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, choices = SFH_ENUM, blank=True, null=True) 
    AUS_RL_Right_Kidney = models.CharField(max_length=500, choices = NP_ENUM, blank=True, null=True) 
    AUS_RL_Right_Kidney_Palpable = models.CharField(max_length=500, choices = SFH_ENUM, blank=True, null=True)

    AUS_Right_Iliac_Pain = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_RI_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_RI_MBP = models.CharField(max_length=500, choices = NT_ENUM, blank=True, null=True)
    AUS_RI_MBP_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_RI_Tenderness = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_RI_Tenderness_Present = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True) 
    AUS_RI_Swelling_Lumps =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_RI_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_RI_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_RI_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, choices = SFH_ENUM,blank=True, null=True)

    AUS_Epigastric_Pain = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_E_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_E_Tenderness = models.CharField(max_length=500, choices = Tenderness_ENUM, blank=True, null=True) 
    AUS_E_Tenderness_Present = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True)
    AUS_E_Tenderness_Present_Rebound = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True)  
    AUS_E_Swelling_Lumps =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_E_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_E_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_E_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, choices = SFH_ENUM, blank=True, null=True)

    AUS_Umbilical_Pain = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_U_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_U_Tenderness = models.CharField(max_length=500, choices = Tenderness_ENUM, blank=True, null=True) 
    AUS_U_Tenderness_Present = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True)
    AUS_U_Tenderness_Present_Rebound = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True)  
    AUS_U_Swelling_Lumps = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    AUS_U_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_U_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_U_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, choices = SFH_ENUM, blank=True, null=True)

    AUS_Suprapubic_Pain = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_S_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_S_Tenderness = models.CharField(max_length=500, choices = Tenderness_ENUM, blank=True, null=True) 
    AUS_S_Tenderness_Present = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True)
    AUS_S_Tenderness_Present_Rebound = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True)  
    AUS_S_Swelling_Lumps =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_S_Swelling_Lumps_Present_Description  =  models.CharField(max_length=1000,blank=True, null=True)
    AUS_S_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_S_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, choices = SFH_ENUM, blank=True, null=True)
    AUS_S_Uterus = models.CharField(max_length=500, choices = NP_ENUM, blank=True, null=True)
    AUS_S_Uterus_Palpable = models.CharField(max_length=500, choices = SFH_ENUM, blank=True, null=True)

    AUS_Left_Hypochondrium_Pain = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_LH_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_LH_Tenderness = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    AUS_LH_Tenderness_Present = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True) 
    AUS_LH_Swelling_Lumps = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_LH_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_LH_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_LH_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, choices = SFH_ENUM, blank=True, null=True) 
    AUS_LH_Spleen = models.CharField(max_length=500, choices = NP_ENUM)
    AUS_LH_Spleen_Palpable = models.CharField(max_length=500, choices = AUS_LH_Liver_Palpable_ENUM, blank=True, null=True)

    AUS_Left_Lumbar_Pain = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_LL_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_LL_Tenderness = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    AUS_LL_Tenderness_Present = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True) 
    AUS_LL_Swelling_Lumps =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    AUS_LL_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_LL_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_LL_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, choices = SFH_ENUM, blank=True, null=True) 
    AUS_LL_Left_Kidney = models.CharField(max_length=500, choices = NP_ENUM, blank=True, null=True) 
    AUS_LL_Left_Kidney_Palpable = models.CharField(max_length=500, choices = SFH_ENUM, blank=True, null=True)

    AUS_Left_Iliac_Pain = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    AUS_LI_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_LI_Tenderness = models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_LI_Tenderness_Present = models.CharField(max_length=500, choices = MDS_ENUM, blank=True, null=True)  
    AUS_LI_Swelling_Lumps =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True) 
    AUS_LI_Swelling_Lumps_Present_Description  =  models.CharField(max_length=500,blank=True, null=True)
    AUS_LI_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_LI_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, choices = SFH_ENUM, blank=True, null=True) 

    AUS_Hernia =  models.CharField(max_length=500, choices = AbsentandPresent, blank=True, null=True)
    AUS_Hernia_Present = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Multiple Select) (Hiatus, Umblical, Right Inguinal, Left Inguinal, Right Femoral, Left Femoral)
    AUS_Urinary_Bladder =  models.CharField(max_length=500, choices = NP_ENUM, blank=True, null=True) 
    AUS_Urinary_Bladder_Palpable = models.CharField(max_length=500, choices = AUS_Urinary_Bladder_Palpable_ENUM, blank=True, null=True)  #

    # Section - 6-A(Pubertal_Assessment_Girls)
# AUS_S_Swelling_Lumps_Present_Description
    Pubertal_Assessment_Girls = models.CharField(max_length=500, choices = IN_ENUM, blank=True, null=True) 
    PAG_Tanner_Score = models.CharField(max_length=500, choices = Score_ENUM, blank=True, null=True) 
    PAG_Menarche_Attained = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    PAG_MA_Yes_Age_of_Menarche = models.CharField(max_length=500, blank=True, null=True)
    PAG_MA_Yes_LMP_Date = models.DateField(blank=True, null=True)
    PAG_MA_Yes_Character_Regularity  = models.CharField(max_length=500, choices = PAG_MA_Yes_Character_Regularity_ENUM, blank=True, null=True) 
    PAG_MA_Yes_Character_Frequency_in_Days = models.CharField(max_length=500, choices = PAG_MA_Yes_Character_Frequency_in_Days_ENUM, blank=True, null=True)
    PAG_MA_Yes_Duration_in_days = models.CharField(max_length=500, choices = PAG_MA_Yes_Duration_in_days_ENUM, blank=True, null=True)  
    PAG_MA_Yes_Flow = models.CharField(max_length=500, choices = PAG_MA_Yes_Flow_ENUM, blank=True, null=True) 
    PAG_MA_Yes_Comfort = models.CharField(max_length=500, choices = PAG_MA_Yes_Comfort_ENUM, blank=True, null=True)  
    PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes = models.CharField(max_length=50, null=True, blank=True)
    PAG_MA_Yes_Pain_in_other_parts_body_during_menses_Yes_Other  = models.TextField(blank=True, null=True)
    PAG_Yes_Cracking_of_Voice_or_chnage_in_voice = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    PAG_HaveYouExperienced_A_change_in_behaviour_recently = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)
    PAG_Change_behaviour_Yes =  models.CharField(max_length=500, blank=True, null=True)  
    PAG_Change_behaviour_Yes_Quiet_Withdrawn =  models.CharField(max_length=500, choices = ML_ENUM, blank=True, null=True) 
    PAG_Change_behaviour_Outgoing =  models.CharField(max_length=500, choices = ML_ENUM, blank=True, null=True)
    PAG_Change_behaviour_Aggressive = models.CharField(max_length=500, choices = ML_ENUM, blank=True, null=True) 
    PAG_Change_behaviour_Bold_and_Daring =  models.CharField(max_length=500, choices = ML_ENUM, blank=True, null=True) 
    PAG_Change_behaviour_Careless =  models.CharField(max_length=500, choices = ML_ENUM, blank=True, null=True) 
    PAG_Prefer_company_of =  models.CharField(max_length=500, choices = G_ENUM, blank=True, null=True) 
    PAG_Any_other_abnormal_finding = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    # Any other abnormal finding : e.g. Brest Lump, Testicular Lump, Abnormal Genitalia, Pain, Discharge etc.
    PAG_Any_other_abnormal_finding_Yes = models.CharField(max_length=250, blank=True, null=True)

    # Section - 6-B(Pubertal_Assessment_Boys)

    Pubertal_Assessment_Boys = models.CharField(max_length=500, choices = IN_ENUM, blank=True, null=True) 
    PAB_Tanner_Score = models.CharField(max_length=500, choices = Score_ENUM, blank=True, null=True) 
    PAB_Yes_Cracking_of_Voice_or_chnage_in_voice = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    PAB_Nightly_Emissions =  models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    PAB_HaveYouExperienced_A_change_in_behaviour_recently = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)
    PAB_Change_behaviour_Yes =  models.CharField(max_length=500, blank=True, null=True)  
    PAB_Change_behaviour_Yes_Quiet_Withdrawn =  models.CharField(max_length=500, choices = ML_ENUM, blank=True, null=True) 
    PAB_Change_behaviour_Outgoing =  models.CharField(max_length=500, choices = ML_ENUM, blank=True, null=True) 
    PAB_Change_behaviour_Aggressive =  models.CharField(max_length=500, choices = ML_ENUM, blank=True, null=True) 
    PAB_Change_behaviour_Bold_and_Daring =  models.CharField(max_length=500, choices = ML_ENUM, blank=True, null=True) 
    PAB_Change_behaviour_Careless =  models.CharField(max_length=500, choices = ML_ENUM, blank=True, null=True) 
    PAB_Prefer_company_of = models.CharField(max_length=500, choices = G_ENUM, blank=True, null=True)
    PAB_Any_other_abnormal_finding =  models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    # Any other abnormal finding : e.g. Brest Lump, Testicular Lump, Abnormal Genitalia, Pain, Discharge etc.
    PAB_Any_other_abnormal_finding_Yes = models.CharField(max_length=250, null=True,blank=True)


    # Section - 7

    History_of_Medication = models.CharField(max_length=500, choices = SRNYesorNo, blank=True, null=True)  
    History_of_Medication_Yes = models.CharField(max_length=500, choices = History_of_Medication_Yes_ENUM, blank=True, null=True)  
    Name_of_Medication = models.TextField(null=True,blank=True) #  Add More

    # Section - 8

    Milestones = models.TextField()  # Yet to be defined 

    # Section - 9

    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=250,choices = SRNYesorNo, blank=True, null=True)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000,blank=True, null=True)  
    Specialist_Referral_Needed_Flag =  models.CharField(max_length=500, choices = Referral_Needed_Flag, blank=True, null=True)  
    Other  = models.TextField(null=True,blank=True)
    Completed = models.CharField(max_length=50, choices=SRNYesorNo,default='No')

    Review_Status = models.CharField(max_length=100,choices=Review_Status_Enum,default='Not Reviewed')
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationG_Reviewedby_HcpId',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.DateTimeField(null=True,blank=True)
    Comments = models.TextField(null=True,blank=True)

    EndTime = models.TimeField(null=True,blank=True)
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
         db_table = "StationG_Collection"




# class StationGModel_Log(models.Model):

#     # section - 1
#     StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationG_StationId_Log',on_delete=models.CASCADE)
#     HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationG_HCID_Log',on_delete=models.CASCADE)
#     HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationG_HcpId_Log',on_delete=models.CASCADE)
#     InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationG_InfoseekId_Log',on_delete=models.CASCADE)
    
#     Central_Nervous_System_Alert = models.CharField(max_length=500,blank=True, null=True)  
#     CNS_Oriented = models.CharField(max_length=500,blank=True, null=True) 
#     CNS_Listens = models.CharField(max_length=500,blank=True, null=True)
#     CNS_Understands = models.CharField(max_length=500, blank=True, null=True) 
#     CNS_Responds = models.CharField(max_length=500,blank=True, null=True) 
#     CNS_Speech = models.CharField(max_length=500,blank=True, null=True)  
#     CNS_Speech_Abnormal = models.CharField(max_length=500, blank=True, null=True)  
#     CNS_Speech_Abnormal_Other = models.TextField(blank=True, null=True) 
   
   
#     CNS_History_of_Headache = models.CharField(max_length=500,blank=True, null=True)  
#     CNS_History_of_Headache_yes_Frequency = models.CharField(max_length=500, blank=True, null=True)  
#     CNS_History_of_Headache_yes_Frequency_Continuous = models.CharField(max_length=500,  blank=True, null=True)   
#     CNS_History_of_Headache_yes_Associated_With  = models.CharField(max_length=100000, blank=True, null=True) 
#      # Master Data((Multiple Select)) (Reading, Watching TV/ Movies, Computer Use, Nausea / Vomiting, Movement, No Particular Activity, Change of Posture, Exercising /Gymming, Hyper-tension, Sleeping, Occurrence, 
#      # Glaucoma, Other Eye condition, Vision Problem, Menstrual Cycle, Pregnancy, Driving, Hunger/ Fasting, Salt intake, MSG (Ajino-moto) intake, Heat, Cold, Other)
#     CNS_History_of_Headache_yes_Associated_With_Occurrence  = models.CharField(max_length=500, blank=True, null=True) 
#     CNS_History_of_Headache_yes_Associated_With_Other  = models.TextField(blank=True, null=True) 
#     CNS_History_of_Headache_yes_From   = models.CharField(max_length=500, blank=True, null=True) 
#     CNS_History_of_Headache_yes_Duration = models.CharField(max_length=500,blank=True, null=True)  

    
#     CNS_History_of_Dizziness = models.CharField(max_length=500, blank=True, null=True)  
#     CNS_History_of_Dizziness_yes_Frequency = models.CharField(max_length=500, blank=True, null=True)  
#     CNS_History_of_Dizziness_yes_Frequency_Continuous = models.CharField(max_length=500,  blank=True, null=True)  
#     CNS_History_of_Dizziness_yes_Associated_With  = models.CharField(max_length=100000, blank=True, null=True) 
#      # Master Data((Multiple Select)) (Reading, Watching TV/ Movies, Computer Use, Nausea / Vomiting, Movement, No Particular Activity, Change of Posture, Exercising /Gymming, Hyper-tension, Sleeping, Occurrence, 
#      # Glaucoma, Other Eye condition, Vision Problem, Menstrual Cycle, Pregnancy, Driving, Hunger/ Fasting, Salt intake, MSG (Ajino-moto) intake, Heat, Cold, Other)
#     CNS_History_of_Dizziness_yes_Associated_With_Occurrence  = models.CharField(max_length=500,blank=True, null=True)  
#     CNS_History_of_Dizziness_yes_Associated_With_Other  = models.TextField(blank=True, null=True) 



#     # section - 2 StationG2YorN
    
#     Respiratory_System_Do_you_Feel_Breathless = models.CharField(max_length=500, blank=True, null=True)  
#     RS_Do_you_have_a_Cough  = models.CharField(max_length=500,  blank=True, null=True) 
#     RS_Shape_of_Chest = models.CharField(max_length=500, blank=True, null=True)   
#     RS_Shape_of_Chest_Abnormal = models.CharField(max_length=50, null=True, blank=True) 
#     RS_Shape_of_Chest_Abnormal_Other = models.TextField(blank=True, null=True) 
#     RS_Type_of_Respiration = models.CharField(max_length=500,  blank=True, null=True) 
#     RS_Type_of_Respiration_Abdominal = models.CharField(max_length=500, blank=True, null=True) 
#     RS_Type_of_Respiration_Abdominal_Other =  models.TextField(blank=True, null=True) 
#     RS_Type_of_Respiration_Thoracic = models.CharField(max_length=500, blank=True, null=True) 
#     RS_Type_of_Respiration_Thoracic_Other =  models.TextField(blank=True, null=True) 
#     RS_Type_of_Respiration_Abdomino_Thoracic = models.CharField(max_length=500, blank=True, null=True) 
#     RS_Type_of_Respiration_Abdomino_Thoracic_Other =  models.TextField(blank=True, null=True) 

#     RS_Trachea = models.CharField(max_length=500, blank=True, null=True) 
#     RS_Evidence_of_Tracheostomy = models.CharField(max_length=500,blank=True, null=True) 
#     # section - 3

#     ## Right_Lung
#     Right_Lung_Air_Entry_Normal = models.CharField(max_length=500, blank=True, null=True) 
#     RL_Breath_Sounds = models.CharField(max_length=1000, blank=True, null=True) 
#     RL_Breath_Sounds_Abnormal = models.CharField(max_length=500,blank=True, null=True)  
#     RL_Breath_Sounds_Abnormal_Apical = models.CharField(max_length=500, blank=True, null=True)  
#     RL_Breath_Sounds_Abnormal_Mid_Zone = models.CharField(max_length=500,  blank=True, null=True)   
#     RL_Breath_Sounds_Abnormal_Basal = models.CharField(max_length=500, blank=True, null=True)  
#     RL_Breath_Sounds_Abnormal_Sub_Scapular = models.CharField(max_length=500, blank=True, null=True)    
#     RL_Breath_Sounds_Abnormal_Diffuse = models.CharField(max_length=500, blank=True, null=True) 

#     RL_Rales_Crepts =  models.CharField(max_length=500, blank=True, null=True)  
#     RL_Rales_Crepts_Present =  models.CharField(max_length=500, blank=True, null=True)  
#     RL_Rales_Crepts_Present_Apical =  models.CharField(max_length=500,  blank=True, null=True)  
#     RL_Rales_Crepts_Present_Apical_Fine =  models.CharField(max_length=500, blank=True, null=True)  
#     RL_Rales_Crepts_Present_Apical_Coarse =  models.CharField(max_length=500, blank=True, null=True)

#     RL_Rales_Crepts_Present_Mid_Zone =  models.CharField(max_length=500, blank=True, null=True)  
#     RL_Rales_Crepts_Present_Mid_Zone_Fine =  models.CharField(max_length=500, blank=True, null=True)  
#     RL_Rales_Crepts_Present_Mid_Zone_Coarse = models.CharField(max_length=500,  blank=True, null=True) 

#     RL_Rales_Crepts_Present_Basal =  models.CharField(max_length=500,  blank=True, null=True)  
#     RL_Rales_Crepts_Present_Basal_Fine =  models.CharField(max_length=500,  blank=True, null=True) 
#     RL_Rales_Crepts_Present_Basal_Coarse =  models.CharField(max_length=500,  blank=True, null=True)  

    
#     RL_Rales_Crepts_Present_Sub_Scapular = models.CharField(max_length=500,  blank=True, null=True)  
#     RL_Rales_Crepts_Present_Sub_Scapular_Fine = models.CharField(max_length=500,  blank=True, null=True) 
#     RL_Rales_Crepts_Present_Sub_Scapular_Coarse =  models.CharField(max_length=500,  blank=True, null=True) 


#     RL_Rales_Crepts_Present_Diffuse =  models.CharField(max_length=500,  blank=True, null=True)  
#     RL_Rales_Crepts_Present_Diffuse_Fine =  models.CharField(max_length=500,  blank=True, null=True)  
#     RL_Rales_Crepts_Present_Diffuse_Coarse =  models.CharField(max_length=500, blank=True, null=True) 


#     RL_Rhonchi_Wheezing =  models.CharField(max_length=500, blank=True, null=True) 
#     RL_Rhonchi_Wheezing_Present = models.CharField(max_length=500,  blank=True, null=True)  
#     RL_Added_Sounds =  models.CharField(max_length=500,  blank=True, null=True)
#     RL_Added_Sounds_Present = models.TextField(blank=True, null=True)  
#     RL_Added_Zone_of_Concern =  models.CharField(max_length=50, null=True, blank=True)
#     RL_Added_Zone_of_Concern_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Apical,Mid Zone, Basal, Sub Scapular, Diffuse)
     

#     ## Left_Lung
#     Left_Lung_Air_Entry_Normal = models.CharField(max_length=500,  blank=True, null=True) 
#     LL_Breath_Sounds = models.CharField(max_length=500, blank=True, null=True)
#     LL_Breath_Sounds_Abnormal = models.CharField(max_length=500,blank=True, null=True)     
#     LL_Breath_Sounds_Abnormal_Apical = models.CharField(max_length=500,  blank=True, null=True)  
#     LL_Breath_Sounds_Abnormal_Mid_Zone = models.CharField(max_length=500,  blank=True, null=True)   
#     LL_Breath_Sounds_Abnormal_Basal = models.CharField(max_length=500,  blank=True, null=True)  
#     LL_Breath_Sounds_Abnormal_Sub_Scapular = models.CharField(max_length=500,  blank=True, null=True)    
#     LL_Breath_Sounds_Abnormal_Diffuse = models.CharField(max_length=500,  blank=True, null=True) 

#     LL_Rales_Crepts =  models.CharField(max_length=500,  blank=True, null=True)  
#     LL_Rales_Crepts_Present =  models.CharField(max_length=500, blank=True, null=True)  
#     LL_Rales_Crepts_Present_Apical =  models.CharField(max_length=500, blank=True, null=True)  
#     LL_Rales_Crepts_Present_Apical_Fine =  models.CharField(max_length=500, blank=True, null=True)  
#     LL_Rales_Crepts_Present_Apical_Coarse =  models.CharField(max_length=500, blank=True, null=True)

#     LL_Rales_Crepts_Present_Mid_Zone =  models.CharField(max_length=500,  blank=True, null=True)  
#     LL_Rales_Crepts_Present_Mid_Zone_Fine =  models.CharField(max_length=500,  blank=True, null=True)  
#     LL_Rales_Crepts_Present_Mid_Zone_Coarse = models.CharField(max_length=500,  blank=True, null=True) 

#     LL_Rales_Crepts_Present_Basal =  models.CharField(max_length=500,  blank=True, null=True)  
#     LL_Rales_Crepts_Present_Basal_Fine =  models.CharField(max_length=500,  blank=True, null=True) 
#     LL_Rales_Crepts_Present_Basal_Coarse =  models.CharField(max_length=500,  blank=True, null=True)  

    
#     LL_Rales_Crepts_Present_Sub_Scapular = models.CharField(max_length=500,  blank=True, null=True)  
#     LL_Rales_Crepts_Present_Sub_Scapular_Fine = models.CharField(max_length=500,  blank=True, null=True) 
#     LL_Rales_Crepts_Present_Sub_Scapular_Coarse =  models.CharField(max_length=500,  blank=True, null=True) 


#     LL_Rales_Crepts_Present_Diffuse =  models.CharField(max_length=500,  blank=True, null=True)  
#     LL_Rales_Crepts_Present_Diffuse_Fine =  models.CharField(max_length=500,  blank=True, null=True)  
#     LL_Rales_Crepts_Present_Diffuse_Coarse =  models.CharField(max_length=500,  blank=True, null=True) 


#     LL_Rhonchi_Wheezing =  models.CharField(max_length=500,  blank=True, null=True) 
#     LL_Rhonchi_Wheezing_Present = models.CharField(max_length=500,  blank=True, null=True)  
#     LL_Added_Sounds =  models.CharField(max_length=500, blank=True, null=True) 
#     LL_Added_Sounds_Present = models.TextField(blank=True, null=True) 
#     LL_Added_Zone_of_Concern =  models.CharField(max_length=50, null=True, blank=True) 
#     LL_Added_Zone_of_Concern_Abnormal =  models.CharField(max_length=100, null=True, blank=True)## Master Data (Multiple Select) (Apical,Mid Zone, Basal, Sub Scapular, Diffuse)
     

#     # Section - 4

#     Cardio_Vascular_Systems_Do_you_get_Palpitation =  models.CharField(max_length=500,  blank=True, null=True)
#     CVS_Fainted_in_Home_School_Workplace_at_any_time =  models.CharField(max_length=500,  blank=True, null=True)
#     CVS_Jugular_Pulsations =  models.CharField(max_length=500,  blank=True, null=True) 
#     CVS_Jugular_Pulsations_Visible =  models.CharField(max_length=500, blank=True, null=True) 
#     CVS_Jugular_Pulsations_Visible_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Exaggerated, Bruit, JVP raised, Murmur)

#     CVS_Suprasternal_Pulsations = models.CharField(max_length=500, blank=True, null=True)  
#     CVS_Suprasternal_Pulsations_Present = models.CharField(max_length=500, blank=True, null=True)
 
#     CVS_Peripheral_Pulsations_Radial = models.CharField(max_length=500,  blank=True, null=True)  
#     CVS_Peripheral_Pulsations_Radial_Present =  models.CharField(max_length=500, blank=True, null=True) 
#     CVS_Peripheral_Pulsations_Radial_Present_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Weak, Exaggerated, Bruit, Murmur, Water Hammer Pulse)
#     CVS_Peripheral_Pulsations_Dorsalis_Pedis = models.CharField(max_length=500, blank=True, null=True) 
#     CVS_Peripheral_Pulsations_Dorsalis_Pedis_Present =  models.CharField(max_length=500,  blank=True, null=True) 
#     CVS_Peripheral_Pulsations_Dorsalis_Pedis_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Weak, Exaggerated, Bruit, Murmur, Water Hammer Pulse)
#     CVS_Peripheral_Pulsations_Other_abnormality =  models.TextField(blank=True, null=True) 

#     CVS_S1 =  models.CharField(max_length=500,  blank=True, null=True) 
#     CVS_S2 =  models.CharField(max_length=500, blank=True, null=True) 
#     CVS_S3 =  models.CharField(max_length=500,  blank=True, null=True) 

#     CVS_Murmur =  models.CharField(max_length=500,  blank=True, null=True)
#     CVS_Murmur_Present =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Multiple Select) (Mitral valve, Tricuspid valve, Other (Text Box))
#     CVS_Murmur_Present_Other =  models.TextField(blank=True, null=True) 

#     CVS_Click = models.CharField(max_length=500,  blank=True, null=True) 
#     CVS_Click_Present_Position =  models.TextField(blank=True, null=True) 

#     CVS_Apex_Beat =  models.CharField(max_length=500,  blank=True, null=True) 
#     CVS_Apex_Beat_Present_Displaced =  models.TextField(blank=True, null=True) 


#     # Section - 5
#     Alimentary_and_Urinary_System_Do_you_have_Nausea_Vomiting =   models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_Do_you_have_Pain_in_your_Abdomen =   models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_Do_you_feel_Burning_when_you_pass_Urine =   models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_Cleft_Lip = models.CharField(max_length=500,  blank=True, null=True)
#     AUS_Cleft_Lip_Present =  models.CharField(max_length=500,  blank=True, null=True)   
#     AUS_Cleft_Palate = models.CharField(max_length=500, blank=True, null=True)
#     AUS_Cleft_Palate_Present =  models.CharField(max_length=500, blank=True, null=True) 

#     AUS_Abdominal_Distension = models.CharField(max_length=500, blank=True, null=True)
#     AUS_Exaggerate_Bowel_Sounds = models.CharField(max_length=500, blank=True, null=True) 
#     AUS_Guarding  = models.CharField(max_length=500, blank=True, null=True)
#     AUS_Rigidity  = models.CharField(max_length=500, blank=True, null=True) 

#     AUS_Right_Hypochondrium_Pain =  models.CharField(max_length=500, blank=True, null=True)  
#     AUS_RH_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
#     AUS_RH_Tenderness = models.CharField(max_length=500,  blank=True, null=True)
#     AUS_RH_Tenderness_Present = models.CharField(max_length=500,blank=True, null=True)  
#     AUS_RH_Swelling_Lumps =  models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_RH_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
#     AUS_RH_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
#     AUS_RH_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_RH_Liver =  models.CharField(max_length=500, blank=True, null=True)  
#     AUS_RH_Liver_Palpable =  models.CharField(max_length=500, blank=True, null=True)  
#     AUS_RH_Gall_Bladder = models.CharField(max_length=500,  blank=True, null=True)
#     AUS_RH_Gall_Bladder_Tender =  models.IntegerField(blank=True, null=True)

#     AUS_Right_Lumbar_Pain = models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_RL_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
#     AUS_RL_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_RL_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_RL_Swelling_Lumps =  models.CharField(max_length=500, blank=True, null=True)
#     AUS_RL_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
#     AUS_RL_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
#     AUS_RL_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_RL_Right_Kidney = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_RL_Right_Kidney_Palpable = models.CharField(max_length=500,  blank=True, null=True)

#     AUS_Right_Iliac_Pain = models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_RI_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
#     AUS_RI_MBP = models.CharField(max_length=500,  blank=True, null=True)
#     AUS_RI_MBP_Pain_Score = models.IntegerField(blank=True, null=True)
#     AUS_RI_Tenderness = models.CharField(max_length=500,  blank=True, null=True)
#     AUS_RI_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_RI_Swelling_Lumps =  models.CharField(max_length=500, blank=True, null=True)
#     AUS_RI_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
#     AUS_RI_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
#     AUS_RI_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, blank=True, null=True)

#     AUS_Epigastric_Pain = models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_E_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
#     AUS_E_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_E_Tenderness_Present = models.CharField(max_length=500, blank=True, null=True)
#     AUS_E_Tenderness_Present_Rebound = models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_E_Swelling_Lumps =  models.CharField(max_length=500,  blank=True, null=True)
#     AUS_E_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
#     AUS_E_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
#     AUS_E_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, blank=True, null=True)

#     AUS_Umbilical_Pain = models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_U_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
#     AUS_U_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_U_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True)
#     AUS_U_Tenderness_Present_Rebound = models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_U_Swelling_Lumps = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_U_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
#     AUS_U_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
#     AUS_U_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True)

#     AUS_Suprapubic_Pain = models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_S_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
#     AUS_S_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_S_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True)
#     AUS_S_Tenderness_Present_Rebound = models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_S_Swelling_Lumps =  models.CharField(max_length=500, blank=True, null=True)
#     AUS_S_Swelling_Lumps_Present_Description  =  models.CharField(max_length=1000,blank=True, null=True)
#     AUS_S_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
#     AUS_S_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True)
#     AUS_S_Uterus = models.CharField(max_length=500,  blank=True, null=True)
#     AUS_S_Uterus_Palpable = models.CharField(max_length=500,  blank=True, null=True)

#     AUS_Left_Hypochondrium_Pain = models.CharField(max_length=500, blank=True, null=True)  
#     AUS_LH_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
#     AUS_LH_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_LH_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_LH_Swelling_Lumps = models.CharField(max_length=500,  blank=True, null=True)
#     AUS_LH_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
#     AUS_LH_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
#     AUS_LH_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_LH_Spleen = models.CharField(max_length=500)
#     AUS_LH_Spleen_Palpable = models.CharField(max_length=500,  blank=True, null=True)

#     AUS_Left_Lumbar_Pain = models.CharField(max_length=500, blank=True, null=True)  
#     AUS_LL_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
#     AUS_LL_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_LL_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_LL_Swelling_Lumps =  models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_LL_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
#     AUS_LL_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
#     AUS_LL_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_LL_Left_Kidney = models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_LL_Left_Kidney_Palpable = models.CharField(max_length=500,  blank=True, null=True)

#     AUS_Left_Iliac_Pain = models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_LI_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
#     AUS_LI_Tenderness = models.CharField(max_length=500,  blank=True, null=True)
#     AUS_LI_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True)  
#     AUS_LI_Swelling_Lumps =  models.CharField(max_length=500, blank=True, null=True) 
#     AUS_LI_Swelling_Lumps_Present_Description  =  models.CharField(max_length=500,blank=True, null=True)
#     AUS_LI_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
#     AUS_LI_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True) 

#     AUS_Hernia =  models.CharField(max_length=500, blank=True, null=True)
#     AUS_Hernia_Present = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Multiple Select) (Hiatus, Umblical, Right Inguinal, Left Inguinal, Right Femoral, Left Femoral)
#     AUS_Urinary_Bladder =  models.CharField(max_length=500,  blank=True, null=True) 
#     AUS_Urinary_Bladder_Palpable = models.CharField(max_length=500, blank=True, null=True)  #

#     # Section - 6-A(Pubertal_Assessment_Girls)
# # AUS_S_Swelling_Lumps_Present_Description
#     Pubertal_Assessment_Girls = models.CharField(max_length=500, blank=True, null=True) 
#     PAG_Tanner_Score = models.CharField(max_length=500,blank=True, null=True) 
#     PAG_Menarche_Attained = models.CharField(max_length=500, blank=True, null=True)  
#     PAG_MA_Yes_Age_of_Menarche = models.CharField(max_length=500, blank=True, null=True)
#     PAG_MA_Yes_LMP_Date = models.DateField(blank=True, null=True)
#     PAG_MA_Yes_Character_Regularity  = models.CharField(max_length=500, blank=True, null=True) 
#     PAG_MA_Yes_Character_Frequency_in_Days = models.CharField(max_length=500,  blank=True, null=True)
#     PAG_MA_Yes_Duration_in_days = models.CharField(max_length=500,  blank=True, null=True)  
#     PAG_MA_Yes_Flow = models.CharField(max_length=500, blank=True, null=True) 
#     PAG_MA_Yes_Comfort = models.CharField(max_length=500,blank=True, null=True)  
#     PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses = models.CharField(max_length=500,  blank=True, null=True)  
#     PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes = models.CharField(max_length=50, null=True, blank=True)
#     PAG_MA_Yes_Pain_in_other_parts_body_during_menses_Yes_Other  = models.TextField(blank=True, null=True)
#     PAG_Yes_Cracking_of_Voice_or_chnage_in_voice = models.CharField(max_length=500,  blank=True, null=True)  
#     PAG_HaveYouExperienced_A_change_in_behaviour_recently = models.CharField(max_length=500, blank=True, null=True)
#     PAG_Change_behaviour_Yes =  models.CharField(max_length=500, blank=True, null=True)  
#     PAG_Change_behaviour_Yes_Quiet_Withdrawn =  models.CharField(max_length=500,  blank=True, null=True) 
#     PAG_Change_behaviour_Outgoing =  models.CharField(max_length=500,blank=True, null=True)
#     PAG_Change_behaviour_Aggressive = models.CharField(max_length=500,  blank=True, null=True) 
#     PAG_Change_behaviour_Bold_and_Daring =  models.CharField(max_length=500, blank=True, null=True) 
#     PAG_Change_behaviour_Careless =  models.CharField(max_length=500,  blank=True, null=True) 
#     PAG_Prefer_company_of =  models.CharField(max_length=500,  blank=True, null=True) 
#     PAG_Any_other_abnormal_finding = models.CharField(max_length=500, blank=True, null=True)  
#     # Any other abnormal finding : e.g. Brest Lump, Testicular Lump, Abnormal Genitalia, Pain, Discharge etc.
#     PAG_Any_other_abnormal_finding_Yes = models.CharField(max_length=250, blank=True, null=True)

#     # Section - 6-B(Pubertal_Assessment_Boys)

#     Pubertal_Assessment_Boys = models.CharField(max_length=500, blank=True, null=True) 
#     PAB_Tanner_Score = models.CharField(max_length=500, blank=True, null=True) 
#     PAB_Yes_Cracking_of_Voice_or_chnage_in_voice = models.CharField(max_length=500, blank=True, null=True)  
#     PAB_Nightly_Emissions =  models.CharField(max_length=500, blank=True, null=True)  
#     PAB_HaveYouExperienced_A_change_in_behaviour_recently = models.CharField(max_length=500, blank=True, null=True)
#     PAB_Change_behaviour_Yes =  models.CharField(max_length=500, blank=True, null=True)  
#     PAB_Change_behaviour_Yes_Quiet_Withdrawn =  models.CharField(max_length=500,  blank=True, null=True) 
#     PAB_Change_behaviour_Outgoing =  models.CharField(max_length=500,  blank=True, null=True) 
#     PAB_Change_behaviour_Aggressive =  models.CharField(max_length=500,  blank=True, null=True) 
#     PAB_Change_behaviour_Bold_and_Daring =  models.CharField(max_length=500,  blank=True, null=True) 
#     PAB_Change_behaviour_Careless =  models.CharField(max_length=500, blank=True, null=True) 
#     PAB_Prefer_company_of = models.CharField(max_length=500, blank=True, null=True)
#     PAB_Any_other_abnormal_finding =  models.CharField(max_length=500, blank=True, null=True)  
#     # Any other abnormal finding : e.g. Brest Lump, Testicular Lump, Abnormal Genitalia, Pain, Discharge etc.
#     PAB_Any_other_abnormal_finding_Yes = models.CharField(max_length=250, null=True,blank=True)


#     # Section - 7

#     History_of_Medication = models.CharField(max_length=500, blank=True, null=True)  
#     History_of_Medication_Yes = models.CharField(max_length=500, blank=True, null=True)  
#     Name_of_Medication = models.TextField(null=True,blank=True) #  Add More

#     # Section - 8

#     Milestones = models.TextField()  # Yet to be defined 

#     # Section - 9

#     Other_Observations = models.TextField(null=True,blank=True)
#     Specialist_Referral_Needed = models.CharField(max_length=250,blank=True, null=True)
#     Specialist_Referral_Needed_Type = models.CharField(max_length=100000,blank=True, null=True)  
#     Specialist_Referral_Needed_Flag =  models.CharField(max_length=500,  blank=True, null=True)  
#     Other  = models.TextField(null=True,blank=True)
#     Review_Status = models.CharField(max_length=100)
#     Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationG_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
#     Reviewed_On = models.CharField(max_length=250)
#     Comments = models.TextField(null=True,blank=True)
#     Logs_Time = models.DateTimeField(auto_now=True)

#     objects = models.Manager

#     class Meta:
#          db_table = "StationG_logs"
