from django.db import models
from datetime import datetime
from Enum.enum import SRNYesorNo, Referral_Needed_Flag, Review_Status_Enum

# STATION A
class StationAModel_Log(models.Model):
    # id_A = models.CharField(max_length=50)

    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationA_StationId_Log',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationA_HCID_Log',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationA_HcpId_Log',on_delete=models.CASCADE)
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationA_InfoseekId_Log',on_delete=models.CASCADE)
    HCP_TeamId = models.ForeignKey('super_admin.HealthCampTeamsModel',related_name='stationA_HealthCampTeamsModel_Log',on_delete=models.CASCADE)
    Height = models.IntegerField()
    Length = models.IntegerField()
    Weight = models.IntegerField()
    Calculated_BMI = models.CharField(max_length=250)
    Triceps_Skin_Fold = models.CharField(max_length=250)
    Subscapular_Skinfold = models.CharField(max_length=250,null=True,blank=True)
    Arm_Circumference = models.CharField(max_length=250)
    Head_Circumference = models.CharField(max_length=250)
    Abdominal_Girth = models.CharField(max_length=250)
    Abdominal_Girth_to_Hight_Ratio = models.CharField(max_length=250)
    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed  = models.CharField(max_length=250,)
    Specialist_Referral_Needed_Type  = models.CharField(max_length=100000,null=True,blank=True)
    Specialist_Referral_Needed_Flag  = models.CharField(max_length=250,null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)
    Review_Status = models.CharField(max_length=100)
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationA_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.CharField(max_length=250)
    Comments = models.TextField(null=True,blank=True)
    Logs_Time = models.DateTimeField(auto_now=True)
    objects = models.Manager
    class Meta:
        db_table = "StationA_logs"

# STATION B
        
class StationBModel_Log(models.Model):

    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationB_StationId_Log',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationB_HCID_Log',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationB_HcpId_Log',on_delete=models.CASCADE)
    InfoseekId  = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationB_InfoseekId_Log',on_delete=models.CASCADE)

    Blood_Pressure_Position = models.CharField(max_length=250)
    Blood_Pressure_Type_of_Instrument = models.CharField(max_length=250)
    Blood_Pressure_Systolic_BP = models.CharField(max_length=250)
    Blood_Pressure_Diastolic_BP = models.CharField(max_length=250)

    Respiration = models.CharField(max_length=250)
    Heart_Rate   = models.CharField(max_length=250)

    Temprature_Measurement_Site = models.CharField(max_length=250) # Master Data (Aural, Armpit, Forehead, Oral,Anal)
    Temprature_Measurement_Instrument = models.CharField(max_length=250) # Master Data (Digital, Analogue)
    Temprature = models.CharField(max_length=250)

    Oxygen_Saturation_SpO2    = models.CharField(max_length=250)
    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=250,null=True,blank=True)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
    Specialist_Referral_Needed_Flag =   models.CharField(max_length=25,null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)
    Review_Status = models.CharField(max_length=100)
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationB_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.CharField(max_length=250)
    Comments = models.TextField(null=True,blank=True)
    Logs_Time = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "StationB_logs"

# STATION C
        
class StationCModel_Log(models.Model):
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationC_StationId_Log',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationC_HCID_Log',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationC_HcpId_Log',on_delete=models.CASCADE)
    InfoseekId  = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationC_InfoseekId_Log',on_delete=models.CASCADE)

    Problem_reading_books = models.CharField(max_length=50,null=True,blank=True)
    Problem_reading_Blackboard = models.CharField(max_length=50,null=True,blank=True)
    Night_Vision  = models.CharField(max_length=50,null=True,blank=True)
    Vision_Corrected  = models.CharField(max_length=50,null=True,blank=True)
    Vision_Corrected_Yes = models.CharField(max_length=100,null=True,blank=True)   # master data  (Glasses, Lenses, Surgical)

    Extra_Ocular_Right_Normal_Eye_Movement = models.CharField(max_length=50)
    Extra_Ocular_Right_Strabismus =models.CharField(max_length=50)
    Extra_Ocular_Right_Drooping_Lid =models.CharField(max_length=50)
    Extra_Ocular_Right_Restricted_Mobility = models.CharField(max_length=50)
    Extra_Ocular_Right_Nystagmus = models.CharField(max_length=50)
    Extra_Ocular_Right_Bulging = models.CharField(max_length=50)


    Extra_Ocular_Left_Normal_Eye_Movement = models.CharField(max_length=50)
    Extra_Ocular_Left_Strabismus = models.CharField(max_length=50)
    Extra_Ocular_Left_Drooping_Lid = models.CharField(max_length=50)
    Extra_Ocular_Left_Restricted_Mobility =models.CharField(max_length=50)
    Extra_Ocular_Left_Nystagmus =models.CharField(max_length=50)
    Extra_Ocular_Left_Bulging =models.CharField(max_length=50)



    Visually_Challenged_Right_Eye  = models.CharField(max_length=1000,default=None,null=True, blank=True)
    Visually_Challenged_Right_Eye_Enucleation  =models.CharField(max_length=50,null=True, blank=True)
    Visually_Challenged_Right_Eye_Enucleation_When_removed  = models.CharField(max_length=1000,null=True, blank=True,default=None)
    Visually_Challenged_Right_Eye_Enucleation_Why_removed  = models.CharField(max_length=1000,null=True, blank=True) ## master data  Tumor, Injury, Accident, Other     (Text Box )
    Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other  = models.CharField(max_length=50,null=True, blank=True) 
    VC_Right_Eye_Enucleation_Artificial_Eye_Used   = models.CharField(max_length=1000, null=True, blank=True)
    Visually_Challenged_Right_Eye_Enucleation_No = models.CharField (max_length=1000,null=True, blank=True)   ## master data    'Cataract','Corneal opacity','Glaucoma','Phthisis bulbi'
    Visually_Challenged_Right_Eye_Enucleation_Cataract = models.CharField(max_length=50, null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity = models.CharField(max_length=50, null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Right_Eye_Enucleation_Glaucoma = models.CharField(max_length=50,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi = models.CharField(max_length=50,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  



    Visually_Challenged_Left_Eye  = models.CharField(max_length=1000, null=True, blank=True)
    Visually_Challenged_Left_Eye_Enucleation  =models.CharField(max_length=50, null=True,blank=True)
    Visually_Challenged_Left_Eye_Enucleation_When_removed  = models.CharField(max_length=1000,null=True,blank=True)
    Visually_Challenged_Left_Eye_Enucleation_Why_removed  = models.CharField(max_length=1000, null=True, blank=True) ## master data  Tumor, Injury, Accident, Other     (Text Box )
    Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other  = models.CharField(max_length=1000, null=True, blank=True) 
    VC_Left_Eye_Enucleation_Artificial_Eye_Used   = models.CharField(max_length=50,null=True, blank=True)
    Visually_Challenged_Left_Eye_Enucleation_No = models.CharField (max_length=50, null=True, blank=True)   ## master data    'Cataract','Corneal opacity','Glaucoma','Phthisis bulbi'
    Visually_Challenged_Left_Eye_Enucleation_Cataract = models.CharField(max_length=50, null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity = models.CharField(max_length=50, null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Left_Eye_Enucleation_Glaucoma = models.CharField(max_length=50,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi = models.CharField(max_length=50, null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  


    Visual_Acuity = models.CharField(max_length=10000) # master data [ Chart Type (Drop Down), Snellen's Chart (Default), Logmar Chart)
   
    Visual_Acuity_With_Lenses_Distant_Vision_Left  = models.IntegerField() 
    Visual_Acuity_With_Lenses_Distant_Vision_Right  = models.IntegerField()
    Visual_Acuity_With_Lenses_Near_Vision_Left = models.IntegerField() 
    Visual_Acuity_With_Lenses_Near_Vision_Right = models.IntegerField() 


    Visual_Acuity_without_Lenses_Distant_Vision_Left  = models.IntegerField(null=True,blank=True) 
    Visual_Acuity_without_Lenses_Distant_Vision_Right  = models.IntegerField(null=True,blank=True)
    Visual_Acuity_without_Lenses_Near_Vision_Left = models.IntegerField(null=True,blank=True) 
    Visual_Acuity_without_Lenses_Near_Vision_Right = models.IntegerField(null=True,blank=True) 

    
    Visual_Acuity_Color_Blindness = models.CharField(max_length=50,null=True,blank=True)  #Master Data => No Colour Blindness (Default), Red-Green Partial, Blue-Green Partial, Total Colour Blindness 
    Visual_Acuity_Color_Blindness_Yes = models.CharField(max_length=100,  null=True,blank=True)
    
    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=250)
    Specialist_Referral_Needed_Type = models.CharField(max_length=1000,null=True,blank=True)
    Specialist_Referral_Needed_Flag = models.CharField(max_length=250,   null=True,blank=True) 
    Other  = models.TextField(null=True,blank=True)
    Review_Status = models.CharField(max_length=100)
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationC_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.CharField(max_length=250)
    Comments = models.TextField(null=True,blank=True)
    Logs_Time = models.DateTimeField(auto_now=True)
    objects = models.Manager


    class Meta:
        db_table = "StationC_logs"

# STATION D

class StationDModel_Log(models.Model):
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationD_StationId_Log',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationD_HCID_Log',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationD_HcpId_Log',on_delete=models.CASCADE)
    InfoseekId  = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationD_InfoseekId_Log',on_delete=models.CASCADE)
    
    #section-1
    Do_you_have_problem_inhearing_your_Teachers_Friends_Parents = models.CharField(max_length=20,null=True,blank=True)
    Do_you_have_problem_inhearing_your_Teachers_Yes = models.CharField(max_length=1000,null=True,blank=True)

    Does_any_fluid_come_out_of_your_ears = models.CharField(max_length=20,null=True,blank=True)
    Does_any_fluid_come_out_of_your_ears_Yes = models.CharField(max_length=1000,null=True,blank=True)

    #section-2
    Visual_inspection_Right_Ear_Pinna = models.CharField(max_length=200,null=True,blank=True)
    Visual_inspection_Right_Ear_Pinna_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
    Visual_inspection_Right_Ear_EarCanal = models.CharField(max_length=200,null=True,blank=True)
    Visual_inspection_Right_Ear_EarCanal_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
    Visual_inspection_Left_Ear_Pinna = models.CharField(max_length=200,null=True,blank=True)
    Visual_inspection_Left_Ear_Pinna_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
    Visual_inspection_Left_Ear_EarCanal = models.CharField(max_length=200,null=True,blank=True)
    Visual_inspection_Left_Ear_EarCanal_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
    Any_other_related_findings = models.TextField(null=True,blank=True)

    #section-3
    Pure_Tone_Audiometry_Right_Ear_500Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_500Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)

    Pure_Tone_Audiometry_Left_Ear_500Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_500Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)

    Upload_Pure_Tone_Test_Results = models.ImageField(upload_to='HCP',null=True, blank=True,max_length=100000)  #Upload / Image capture Button

    #section-4
    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=250,null=True,blank=True)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
    Specialist_Referral_Needed_Flag =   models.CharField(max_length=100,null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)
    Review_Status = models.CharField(max_length=100)
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationD_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.CharField(max_length=250)
    Comments = models.TextField(null=True,blank=True)
    Logs_Time = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "StationD_logs"

# STATION E
        
class StationEModel_Log(models.Model):
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationE_StationId_Log',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationE_HCID_Log',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationE_HcpId_Log',on_delete=models.CASCADE)
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationE_InfoseekId_Log',on_delete=models.CASCADE)

    

    Child_Mobility = models.CharField(max_length=50, null=True, blank=True)  ## Master Data (Can Walk, Can not Walk)
    Child_Mobility_Can_not_Walk = models.CharField(max_length=50, null=True, blank=True)  ## Master Data (No Developmental Delay, Delayed Milestone, Other)
    Child_Mobility_Can_not_Walk_other = models.TextField(null=True, blank=True)

    Student_Ambulant = models.CharField(max_length=50)
    Student_Ambulant_No = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Uses a Wheelchair,Uses Crutches, Uses other motorized system for movement)

    Gait = models.TextField(null=True, blank=True) ## Master Data (Normal, Abnormal)
    Gait_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Shuffling, Limp, Other abnormal gait )
    Gait_Abnormal_Limp = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Lower limb length discrepancy,Other causes)
    Gait_Abnormal_Limp_other = models.TextField(null=True, blank=True)
    

    Wear_Brace_Support = models.CharField(max_length=1000, null=True, blank=True)
    Wear_Brace_Support_Yes = models.CharField(max_length=10000, null=True, blank=True) ## Master Data (Neck, Shoulders, Back, Chest, Right Upper Limb, Left Upper Limb, Right Lower Limb, Left Lower Limb)

    Prosthesis = models.CharField(max_length=1000,  null=True, blank=True)
    Prosthesis_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Knee, Hip, Spine, Hip, Right Upper Limb, Left Upper Limb, Right Lower Limb, Left Lower Limb, Right shoulder, Left shoulder,Others)
    Prosthesis_Yes_other = models.TextField(null=True, blank=True)

    Spine_Appearance = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    Spine_Appearance_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Kyphosis, Scoliosis, Kypho-scoliosis, Rigid, Other)
    Spine_Appearance_Abnormal_Other = models.TextField(null=True, blank=True) 
    
    Shoulder_Griddle_Appearance = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    Shoulder_Griddle_Appearance_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Postural, Bony Causes, Muscle spasms / knots, Other)
    Shoulder_Griddle_Appearance_Abnormal_Other = models.TextField(null=True, blank=True) 


    Spine_Mobility = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Restricted movement,)
    Spine_Mobility_Restricted_movement = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Mild, Moderate, Severe )

    Neck_Mobility = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Restricted movement,)
    Neck_Mobility_Restricted_movement = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Mild, Moderate, Severe )
## Upper Limib Right
    UL_Right_Appearance =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Abnormal)
    UL_Right_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

    UL_Right_Motor_Function_Tone =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
    UL_Right_Motor_Function_Range_of_Movement = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    UL_Right_MF_RM_Abnormal = models.CharField(max_length=50, null=True, blank=True) ##Master Data (Hyper Flexible, Restricted)
    UL_Right_MF_RM_Abnormal_Hyper_Flexible = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Fingers, Hand, Elbow, Shoulder)
    UL_Right_MF_RM_Abnormal_Restricted = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Mild, Moderate, Severe)
    UL_Right_Motor_Function_Strength = models.CharField(max_length=50)

    UL_Right_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    UL_Right_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    UL_Right_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    UL_Right_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    UL_Right_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    UL_Right_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
    UL_Right_DTR_SF_Abnormal_Touch = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Hot object, Cold object, Both hot & cold objects)
    UL_Right_DTR_SF_Abnormal_Pain_Present= models.IntegerField( null=True, blank=True)
    UL_Right_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField( null=True, blank=True)
    UL_Right_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField( null=True, blank=True)
## Upper Limib Left
    UL_Left_Appearance =  models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    UL_Left_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

    UL_Left_Motor_Function_Tone =  models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
    UL_Left_Motor_Function_Range_of_Movement = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    UL_left_MF_RM_Abnormal = models.CharField(max_length=50, null=True, blank=True) ##Master Data (Hyper Flexible, Restricted)
    UL_Left_MF_RM_Abnormal_Hyper_Flexible = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Fingers, Hand, Elbow, Shoulder)
    UL_Left_MF_RM_Abnormal_Restricted = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Mild, Moderate, Severe)
    UL_Left_Motor_Function_Strength = models.CharField(max_length=50)

    UL_Left_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=100, null=True, blank=True) ## Master Data (Normal, Abnormal)
    UL_Left_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    UL_Left_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    UL_Left_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    UL_Left_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=100, null=True, blank=True) ## Master Data (Normal, Abnormal)
    UL_Left_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
    UL_Left_DTR_SF_Abnormal_Touch = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Hot object, Cold object, Both hot & cold objects)
    UL_Left_DTR_SF_Abnormal_Pain_Present= models.IntegerField(null=True, blank=True)
    UL_Left_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField(null=True, blank=True)
    UL_Left_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField(null=True, blank=True)
## Lower Limib Right
    LL_Right_Appearance =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Normal, Abnormal)
    LL_Right_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

    LL_Right_Motor_Function_Tone =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
    LL_Right_Motor_Function_Range_of_Movement = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Abnormal)
    LL_Right_Motor_Function_Strength = models.CharField(max_length=50)

    LL_Right_Motor_Function_Knee = models.CharField(max_length=250, null=True, blank=True) ## Master Data (Normal, Abnormal)
    LL_Right_Motor_Function_Knee_Abnormal = models.CharField(max_length=250, null=True, blank=True) ## Master Data (Absent, Sluggish, Exaggerated, Clonus)

    # LL_Right_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=50, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    # LL_Right_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=DTR_Abnormal) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)


    # LL_Right_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    # LL_Right_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    LL_Right_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Abnormal)
    LL_Right_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
    LL_Right_DTR_SF_Abnormal_Touch = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Hot object, Cold object, Both hot & cold objects)
    LL_Right_DTR_SF_Abnormal_Pain_Present= models.IntegerField(null=True, blank=True)
    LL_Right_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField(null=True, blank=True)
    LL_Right_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField(null=True, blank=True)
## Lower Limib Left
    LL_Left_Appearance =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Abnormal)
    LL_Left_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

    LL_Left_Motor_Function_Tone =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
    LL_Left_Motor_Function_Range_of_Movement = models.CharField(max_length=100, null=True, blank=True) ## Master Data (Normal, Abnormal)
    LL_Left_Motor_Function_Strength = models.CharField(max_length=50)

    LL_Left_Motor_Function_Knee = models.CharField(max_length=250, null=True, blank=True) ## Master Data (Normal, Abnormal)
    LL_Left_Motor_Function_Knee_Abnormal = models.CharField(max_length=250, null=True, blank=True) ## Master Data (Absent, Sluggish, Exaggerated, Clonus)

    # LL_Left_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    # LL_Left_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    # LL_Left_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    # LL_Left_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    LL_Left_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    LL_Left_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
    LL_Left_DTR_SF_Abnormal_Touch = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Hot object, Cold object, Both hot & cold objects)
    LL_Left_DTR_SF_Abnormal_Pain_Present= models.IntegerField(null=True, blank=True)
    LL_Left_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField(null=True, blank=True)
    LL_Left_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField(null=True, blank=True)

    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed     = models.CharField(max_length=250,  null=True,blank=True)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000, null=True,blank=True)
    Specialist_Referral_Needed_Flag =   models.CharField(max_length=250,   null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)
    Review_Status = models.CharField(max_length=100)
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationE_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.CharField(max_length=100)
    Comments = models.TextField(null=True,blank=True)
    Logs_Time = models.DateTimeField(auto_now=True)
    
    objects = models.Manager 

    class Meta:
        db_table = 'StationE_logs'

# STATION F
        
class StationFModel_Log(models.Model):
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationF_StationId_Log',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationF_HCID_Log',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationF_HcpId_Log',on_delete=models.CASCADE)
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationF_InfoseekId_Log',on_delete=models.CASCADE)

    
    Skin_colour_Tone = models.CharField(max_length=1000) 
    Skin_colour_Tone_Abnormal = models.CharField(max_length=50, null=True, blank=True) 

    Skin_Texture_of_Skin = models.CharField(max_length=1000) 
    Skin_Texture_of_Skin_Abnormal = models.CharField(max_length=1000,null=True, blank=True) ## Master Data(Multiple Select) (Dry, Crinkled, Scaly, Hemorrhages, Oily, Moist)
    
    skin_Rash = models.CharField(max_length=1000)
    skin_Rash_Present = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Face, Neck, Chest, Abdomen, Groin, Back, Arms, Hands, Legs, Feet)
    skin_Rash_Present_Face = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Neck = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Chest = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Abdomen = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Groin = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Back = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Arms = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Hands = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Legs = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Feet = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    
    Other_Skin_lesions = models.CharField(max_length=1000)
    Other_Skin_lesions_Yes = models.CharField(max_length=1000, null=True, blank=True) # Mater Data(Multiple Select) (Finger web boils, Scabs, Ringworm, Leucoderma, Scratches, Birth marks)  
    Other_Skin_lesions_Yes_Other = models.CharField(max_length=100, null=True, blank=True)
    Other_Skin_lesions_Yes_Birth_marks = models.CharField(max_length=1000, null=True, blank=True) # Mater Data(Multiple Select) (Nevus, Café au lait, Other)  
    Other_Skin_lesions_Yes_Birth_marks_Other = models.TextField(max_length=100, null=True, blank=True) 


    skin_Acne = models.CharField(max_length=1000)
    skin_Acne_Yes = models.CharField(max_length=100,null=True,blank=True)


    Nails_Color =  models.CharField(max_length=100) 

    Nails_Shape = models.CharField(max_length=1000) 
    Nails_Shape_Abnormal = models.CharField(max_length=1000,null=True, blank=True) ## Master Data(Multi  Select) (Bitten, Clubbed, Spoon-shaped)

    Nails_Deformity = models.CharField(max_length=1000)
    Nails_Deformity_Yes = models.CharField(max_length=1000,null=True, blank=True) ## Master Data(Multi  Select) (White Spots, Ridging, Brown lines / spots Irregular thickening)

    Nails_Cuticles = models.CharField(max_length=1000) 
    Nail_Bed_Infection = models.CharField(max_length=1000) 


    Head_Skull_Fontanelle = models.CharField(max_length=1000)
    Head_Skull_Fontanelle_Open = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Frontal Fontanella, Occipital Fontanella)
    Head_Skull_Fontanelle_Open_Fontanella = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Bulging, Sunken, Non-bulging / Flat, Enlarged / Wide)
    Head_Skull_Fontanelle_Open_Occipital = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Bulging, Sunken, Non-bulging / Flat, Enlarged / Wide)

    Head_Skull_Appearance_and_Size = models.CharField(max_length=1000) 
    Head_Skull_Appearance_and_Size_Other = models.TextField(null=True, blank=True)

    Head_Hair_Appearance = models.CharField(max_length=50) 
    Head_Hair_Appearance_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Greasy, Dry & Brittle, Other, Early greying)
    Head_Hair_Appearance_Abnormal_Other = models.TextField(null=True, blank=True)

    Head_Scalp = models.CharField(max_length=1000) 
    Head_Scalp_Abnormal = models.CharField(max_length=10000, null=True, blank=True) ## Master Data(Multiple Select) (Dandruff, Edema, Ringworm, Ulcers, Hematoma, Folliculities, Swelling, Pustules, Sebaceous Cyst, Lipoma)

    Head_Parasites = models.CharField(max_length=50)
    Head_Parasites_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Adults, Nits, Other)
    Head_Parasites_Yes_Other = models.TextField(null=True, blank=True)
    
    Head_Hair_Loss = models.CharField(max_length=1000)
    Head_Hair_Loss_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Patchy, Generalized, Temporal, Crown, Frontal)

    Thyroid_Lymph_Thyroid_Gland = models.CharField(max_length=1000,null=True,blank=True) 
    Thyroid_Lymph_Thyroid_Gland_Enlarged = models.CharField(max_length=1000, null=True,blank=True) 

    Thyroid_Lymph_Cervical_LN = models.CharField(max_length=1000) 
    Thyroid_Lymph_Cervical_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Submental,	Occipital, Submandibular R,	Submandibular L, Anterior Cervical R, Anterior Cervical L, Lateral Cervical R, Lateral Cervical L, Posterior Cervical R, Posterior Cervical L)

    Thyroid_Lymph_Supraclavicular_LN = models.CharField(max_length=1000) 
    Thyroid_Lymph_Supraclavicular_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left)

    Thyroid_Lymph_Axillary_LN = models.CharField(max_length=1000) 
    Thyroid_Lymph_Axillary_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left) 

    Thyroid_Lymph_Supratrochlear_LN = models.CharField(max_length=1000) 
    Thyroid_Lymph_Supratrochlear_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left) 

    Thyroid_Lymph_Inguinal_LN = models.CharField(max_length=1000)
    Thyroid_Lymph_Inguinal_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left)


    Eyes_Conjuctiva = models.CharField(max_length=50) 

    Eyes_Sclera = models.CharField(max_length=50) 

    Eyes_Discharge = models.CharField(max_length=1000)
    Eyes_Discharge_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right Eye, Left Eye)
    Eyes_Discharge_Yes_Right_Eye = models.CharField(max_length=50,null=True, blank=True) 
    Eyes_Discharge_Yes_Left_Eye = models.CharField(max_length=50,null=True, blank=True) 

    Eyes_Eyelids = models.CharField(max_length=1000) 
    Eyes_Eyelids_Abnormal = models.CharField(max_length=50,null=True, blank=True) 

    Ears_Hearing = models.CharField(max_length=1000) 
    Ears_Hearing_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Mulitiple Select) (Reduced, Tinnitus, Absent, Exaggerate, Other)
    Ears_Hearing_Abnormal_Reduced = models.CharField(max_length=50,null=True, blank=True) 
    Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid = models.CharField(max_length=50,null=True, blank=True)
    Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes = models.CharField(max_length=1000, null=True,blank=True) ## Master Data(Multiple Select) (Right, Left)
    Ears_Hearing_Abnormal_Reduced_Other = models.TextField(null=True, blank=True)


    Ears_Discharge = models.CharField(max_length=1000)
    Ears_Discharge_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right Ear, Left Ear)
    Ears_Discharge_Yes_Right_Ear = models.CharField(max_length=50,null=True, blank=True) 
    Ears_Discharge_Yes_Left_Ear = models.CharField(max_length=50,null=True, blank=True) 


    Ear_Wax = models.CharField(max_length=50) 
    Ear_Wax_Present = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left)


    Ear_Eardrum = models.CharField(max_length=1000) 
    Ear_Eardrum_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right Ear, Left Ear)
    Ear_Eardrum_Abnormal_Right_Ear = models.CharField(max_length=50,null=True, blank=True) 
    Ear_Eardrum_Abnormal_Left_Ear = models.CharField(max_length=50,null=True, blank=True) 


    Nose_Discharge = models.CharField(max_length=1000)
    Nose_Discharge_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right Nostril, Left Nostril)
    Nose_Discharge_Yes_Right_Nostril = models.CharField(max_length=50,null=True, blank=True) 
    Nose_Discharge_Yes_Left_Nostril = models.CharField(max_length=50,null=True, blank=True) 
    
    Nose_Dryness = models.CharField(max_length=1000)
    Nose_Dryness_Yes = models.CharField(max_length=50, null=True, blank=True) 

    Nose_Crusting = models.CharField(max_length=50)
    Nose_Crusting_Yes = models.CharField(max_length=50, null=True, blank=True) 

    Nose_Polyps = models.CharField(max_length=50)
    Nose_Polyps_Yes = models.CharField(max_length=50,null=True, blank=True) 

    Nose_Septum_Bridge = models.CharField(max_length=50) 

    Nose_Sinuses = models.CharField(max_length=50) 

    Mouth_Throat_Mucosa = models.CharField(max_length=1000) 
    Mouth_Throat_Mucosa_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Pale, Vesicles, Leukoplakia, Red, Ulcers, Others Cyanosed)
    Mouth_Throat_Mucosa_Abnormal_Other = models.TextField(null=True, blank=True)

    Mouth_Throat_Tongue = models.CharField(max_length=1000) 
    Mouth_Throat_Tongue_Abnormal = models.CharField(max_length=10000, null=True, blank=True) ## Master Data(Multiple Select) (Pale, Protruded, Smooth/Bald, Red, Enlarged, Vesicles, Cyanosed, Purulent Lesions, Ulcers, Protruded, Leukoplakia, Other)
    Mouth_Throat_Tongue_Abnormal_Other = models.TextField(null=True, blank=True)


    Mouth_Tonsils = models.CharField(max_length=50) 
    Mouth_Tonsils_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Enlarged, Purulent)

    Mouth_Uvula = models.CharField(max_length=50) 
    Mouth_Uvula_Abnormal = models.TextField(null=True, blank=True)

    Mouth_Palate = models.CharField(max_length=50) 
    Mouth_Palate_Cleft_Palate = models.TextField(null=True, blank=True)
    Mouth_Palate_CleftLip_Palate = models.TextField(null=True, blank=True)
    Mouth_Palate_Other = models.TextField(null=True, blank=True)


    Hygiene_Nails = models.CharField(max_length=50) 

    Hygiene_Hair = models.CharField(max_length=50) 

    Hygiene_Skin = models.CharField(max_length=50)

    Hygiene_Odour = models.CharField(max_length=50) 

    
    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=50)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
    Specialist_Referral_Needed_Flag =   models.CharField(max_length=1000 , null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)
    Review_Status = models.CharField(max_length=100,default='Not Reviewed')
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationF_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.CharField(max_length=100)
    Comments = models.TextField(null=True,blank=True)
    Logs_Time = models.DateTimeField(auto_now=True)

    objects = models.Manager


    class Meta:
         db_table = "StationF_logs"

# STATION G

class StationGModel_Log(models.Model):

    # section - 1
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationG_StationId_Log',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationG_HCID_Log',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationG_HcpId_Log',on_delete=models.CASCADE)
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationG_InfoseekId_Log',on_delete=models.CASCADE)
    
    Central_Nervous_System_Alert = models.CharField(max_length=500,blank=True, null=True)  
    CNS_Oriented = models.CharField(max_length=500,blank=True, null=True) 
    CNS_Listens = models.CharField(max_length=500,blank=True, null=True)
    CNS_Understands = models.CharField(max_length=500, blank=True, null=True) 
    CNS_Responds = models.CharField(max_length=500,blank=True, null=True) 
    CNS_Speech = models.CharField(max_length=500,blank=True, null=True)  
    CNS_Speech_Abnormal = models.CharField(max_length=500, blank=True, null=True)  
    CNS_Speech_Abnormal_Other = models.TextField(blank=True, null=True) 
   
   
    CNS_History_of_Headache = models.CharField(max_length=500,blank=True, null=True)  
    CNS_History_of_Headache_yes_Frequency = models.CharField(max_length=500, blank=True, null=True)  
    CNS_History_of_Headache_yes_Frequency_Continuous = models.CharField(max_length=500,  blank=True, null=True)   
    CNS_History_of_Headache_yes_Associated_With  = models.CharField(max_length=100000, blank=True, null=True) 
     # Master Data((Multiple Select)) (Reading, Watching TV/ Movies, Computer Use, Nausea / Vomiting, Movement, No Particular Activity, Change of Posture, Exercising /Gymming, Hyper-tension, Sleeping, Occurrence, 
     # Glaucoma, Other Eye condition, Vision Problem, Menstrual Cycle, Pregnancy, Driving, Hunger/ Fasting, Salt intake, MSG (Ajino-moto) intake, Heat, Cold, Other)
    CNS_History_of_Headache_yes_Associated_With_Occurrence  = models.CharField(max_length=500, blank=True, null=True) 
    CNS_History_of_Headache_yes_Associated_With_Other  = models.TextField(blank=True, null=True) 
    CNS_History_of_Headache_yes_From   = models.CharField(max_length=500, blank=True, null=True) 
    CNS_History_of_Headache_yes_Duration = models.CharField(max_length=500,blank=True, null=True)  

    
    CNS_History_of_Dizziness = models.CharField(max_length=500, blank=True, null=True)  
    CNS_History_of_Dizziness_yes_Frequency = models.CharField(max_length=500, blank=True, null=True)  
    CNS_History_of_Dizziness_yes_Frequency_Continuous = models.CharField(max_length=500,  blank=True, null=True)  
    CNS_History_of_Dizziness_yes_Associated_With  = models.CharField(max_length=100000, blank=True, null=True) 
     # Master Data((Multiple Select)) (Reading, Watching TV/ Movies, Computer Use, Nausea / Vomiting, Movement, No Particular Activity, Change of Posture, Exercising /Gymming, Hyper-tension, Sleeping, Occurrence, 
     # Glaucoma, Other Eye condition, Vision Problem, Menstrual Cycle, Pregnancy, Driving, Hunger/ Fasting, Salt intake, MSG (Ajino-moto) intake, Heat, Cold, Other)
    CNS_History_of_Dizziness_yes_Associated_With_Occurrence  = models.CharField(max_length=500,blank=True, null=True)  
    CNS_History_of_Dizziness_yes_Associated_With_Other  = models.TextField(blank=True, null=True) 



    # section - 2 StationG2YorN
    
    Respiratory_System_Do_you_Feel_Breathless = models.CharField(max_length=500, blank=True, null=True)  
    RS_Do_you_have_a_Cough  = models.CharField(max_length=500,  blank=True, null=True) 
    RS_Shape_of_Chest = models.CharField(max_length=500, blank=True, null=True)   
    RS_Shape_of_Chest_Abnormal = models.CharField(max_length=50, null=True, blank=True) 
    RS_Shape_of_Chest_Abnormal_Other = models.TextField(blank=True, null=True) 
    RS_Type_of_Respiration = models.CharField(max_length=500,  blank=True, null=True) 
    RS_Type_of_Respiration_Abdominal = models.CharField(max_length=500, blank=True, null=True) 
    RS_Type_of_Respiration_Abdominal_Other =  models.TextField(blank=True, null=True) 
    RS_Type_of_Respiration_Thoracic = models.CharField(max_length=500, blank=True, null=True) 
    RS_Type_of_Respiration_Thoracic_Other =  models.TextField(blank=True, null=True) 
    RS_Type_of_Respiration_Abdomino_Thoracic = models.CharField(max_length=500, blank=True, null=True) 
    RS_Type_of_Respiration_Abdomino_Thoracic_Other =  models.TextField(blank=True, null=True) 

    RS_Trachea = models.CharField(max_length=500, blank=True, null=True) 
    RS_Evidence_of_Tracheostomy = models.CharField(max_length=500,blank=True, null=True) 
    # section - 3

    ## Right_Lung
    Right_Lung_Air_Entry_Normal = models.CharField(max_length=500, blank=True, null=True) 
    RL_Breath_Sounds = models.CharField(max_length=1000, blank=True, null=True) 
    RL_Breath_Sounds_Abnormal = models.CharField(max_length=500,blank=True, null=True)  
    RL_Breath_Sounds_Abnormal_Apical = models.CharField(max_length=500, blank=True, null=True)  
    RL_Breath_Sounds_Abnormal_Mid_Zone = models.CharField(max_length=500,  blank=True, null=True)   
    RL_Breath_Sounds_Abnormal_Basal = models.CharField(max_length=500, blank=True, null=True)  
    RL_Breath_Sounds_Abnormal_Sub_Scapular = models.CharField(max_length=500, blank=True, null=True)    
    RL_Breath_Sounds_Abnormal_Diffuse = models.CharField(max_length=500, blank=True, null=True) 

    RL_Rales_Crepts =  models.CharField(max_length=500, blank=True, null=True)  
    RL_Rales_Crepts_Present =  models.CharField(max_length=500, blank=True, null=True)  
    RL_Rales_Crepts_Present_Apical =  models.CharField(max_length=500,  blank=True, null=True)  
    RL_Rales_Crepts_Present_Apical_Fine =  models.CharField(max_length=500, blank=True, null=True)  
    RL_Rales_Crepts_Present_Apical_Coarse =  models.CharField(max_length=500, blank=True, null=True)

    RL_Rales_Crepts_Present_Mid_Zone =  models.CharField(max_length=500, blank=True, null=True)  
    RL_Rales_Crepts_Present_Mid_Zone_Fine =  models.CharField(max_length=500, blank=True, null=True)  
    RL_Rales_Crepts_Present_Mid_Zone_Coarse = models.CharField(max_length=500,  blank=True, null=True) 

    RL_Rales_Crepts_Present_Basal =  models.CharField(max_length=500,  blank=True, null=True)  
    RL_Rales_Crepts_Present_Basal_Fine =  models.CharField(max_length=500,  blank=True, null=True) 
    RL_Rales_Crepts_Present_Basal_Coarse =  models.CharField(max_length=500,  blank=True, null=True)  

    
    RL_Rales_Crepts_Present_Sub_Scapular = models.CharField(max_length=500,  blank=True, null=True)  
    RL_Rales_Crepts_Present_Sub_Scapular_Fine = models.CharField(max_length=500,  blank=True, null=True) 
    RL_Rales_Crepts_Present_Sub_Scapular_Coarse =  models.CharField(max_length=500,  blank=True, null=True) 


    RL_Rales_Crepts_Present_Diffuse =  models.CharField(max_length=500,  blank=True, null=True)  
    RL_Rales_Crepts_Present_Diffuse_Fine =  models.CharField(max_length=500,  blank=True, null=True)  
    RL_Rales_Crepts_Present_Diffuse_Coarse =  models.CharField(max_length=500, blank=True, null=True) 


    RL_Rhonchi_Wheezing =  models.CharField(max_length=500, blank=True, null=True) 
    RL_Rhonchi_Wheezing_Present = models.CharField(max_length=500,  blank=True, null=True)  
    RL_Added_Sounds =  models.CharField(max_length=500,  blank=True, null=True)
    RL_Added_Sounds_Present = models.TextField(blank=True, null=True)  
    RL_Added_Zone_of_Concern =  models.CharField(max_length=50, null=True, blank=True)
    RL_Added_Zone_of_Concern_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Apical,Mid Zone, Basal, Sub Scapular, Diffuse)
     

    ## Left_Lung
    Left_Lung_Air_Entry_Normal = models.CharField(max_length=500,  blank=True, null=True) 
    LL_Breath_Sounds = models.CharField(max_length=500, blank=True, null=True)
    LL_Breath_Sounds_Abnormal = models.CharField(max_length=500,blank=True, null=True)     
    LL_Breath_Sounds_Abnormal_Apical = models.CharField(max_length=500,  blank=True, null=True)  
    LL_Breath_Sounds_Abnormal_Mid_Zone = models.CharField(max_length=500,  blank=True, null=True)   
    LL_Breath_Sounds_Abnormal_Basal = models.CharField(max_length=500,  blank=True, null=True)  
    LL_Breath_Sounds_Abnormal_Sub_Scapular = models.CharField(max_length=500,  blank=True, null=True)    
    LL_Breath_Sounds_Abnormal_Diffuse = models.CharField(max_length=500,  blank=True, null=True) 

    LL_Rales_Crepts =  models.CharField(max_length=500,  blank=True, null=True)  
    LL_Rales_Crepts_Present =  models.CharField(max_length=500, blank=True, null=True)  
    LL_Rales_Crepts_Present_Apical =  models.CharField(max_length=500, blank=True, null=True)  
    LL_Rales_Crepts_Present_Apical_Fine =  models.CharField(max_length=500, blank=True, null=True)  
    LL_Rales_Crepts_Present_Apical_Coarse =  models.CharField(max_length=500, blank=True, null=True)

    LL_Rales_Crepts_Present_Mid_Zone =  models.CharField(max_length=500,  blank=True, null=True)  
    LL_Rales_Crepts_Present_Mid_Zone_Fine =  models.CharField(max_length=500,  blank=True, null=True)  
    LL_Rales_Crepts_Present_Mid_Zone_Coarse = models.CharField(max_length=500,  blank=True, null=True) 

    LL_Rales_Crepts_Present_Basal =  models.CharField(max_length=500,  blank=True, null=True)  
    LL_Rales_Crepts_Present_Basal_Fine =  models.CharField(max_length=500,  blank=True, null=True) 
    LL_Rales_Crepts_Present_Basal_Coarse =  models.CharField(max_length=500,  blank=True, null=True)  

    
    LL_Rales_Crepts_Present_Sub_Scapular = models.CharField(max_length=500,  blank=True, null=True)  
    LL_Rales_Crepts_Present_Sub_Scapular_Fine = models.CharField(max_length=500,  blank=True, null=True) 
    LL_Rales_Crepts_Present_Sub_Scapular_Coarse =  models.CharField(max_length=500,  blank=True, null=True) 


    LL_Rales_Crepts_Present_Diffuse =  models.CharField(max_length=500,  blank=True, null=True)  
    LL_Rales_Crepts_Present_Diffuse_Fine =  models.CharField(max_length=500,  blank=True, null=True)  
    LL_Rales_Crepts_Present_Diffuse_Coarse =  models.CharField(max_length=500,  blank=True, null=True) 


    LL_Rhonchi_Wheezing =  models.CharField(max_length=500,  blank=True, null=True) 
    LL_Rhonchi_Wheezing_Present = models.CharField(max_length=500,  blank=True, null=True)  
    LL_Added_Sounds =  models.CharField(max_length=500, blank=True, null=True) 
    LL_Added_Sounds_Present = models.TextField(blank=True, null=True) 
    LL_Added_Zone_of_Concern =  models.CharField(max_length=50, null=True, blank=True) 
    LL_Added_Zone_of_Concern_Abnormal =  models.CharField(max_length=100, null=True, blank=True)## Master Data (Multiple Select) (Apical,Mid Zone, Basal, Sub Scapular, Diffuse)
     

    # Section - 4

    Cardio_Vascular_Systems_Do_you_get_Palpitation =  models.CharField(max_length=500,  blank=True, null=True)
    CVS_Fainted_in_Home_School_Workplace_at_any_time =  models.CharField(max_length=500,  blank=True, null=True)
    CVS_Jugular_Pulsations =  models.CharField(max_length=500,  blank=True, null=True) 
    CVS_Jugular_Pulsations_Visible =  models.CharField(max_length=500, blank=True, null=True) 
    CVS_Jugular_Pulsations_Visible_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Exaggerated, Bruit, JVP raised, Murmur)

    CVS_Suprasternal_Pulsations = models.CharField(max_length=500, blank=True, null=True)  
    CVS_Suprasternal_Pulsations_Present = models.CharField(max_length=500, blank=True, null=True)
 
    CVS_Peripheral_Pulsations_Radial = models.CharField(max_length=500,  blank=True, null=True)  
    CVS_Peripheral_Pulsations_Radial_Present =  models.CharField(max_length=500, blank=True, null=True) 
    CVS_Peripheral_Pulsations_Radial_Present_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Weak, Exaggerated, Bruit, Murmur, Water Hammer Pulse)
    CVS_Peripheral_Pulsations_Dorsalis_Pedis = models.CharField(max_length=500, blank=True, null=True) 
    CVS_Peripheral_Pulsations_Dorsalis_Pedis_Present =  models.CharField(max_length=500,  blank=True, null=True) 
    CVS_Peripheral_Pulsations_Dorsalis_Pedis_Abnormal =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Multiple Select) (Weak, Exaggerated, Bruit, Murmur, Water Hammer Pulse)
    CVS_Peripheral_Pulsations_Other_abnormality =  models.TextField(blank=True, null=True) 

    CVS_S1 =  models.CharField(max_length=500,  blank=True, null=True) 
    CVS_S2 =  models.CharField(max_length=500, blank=True, null=True) 
    CVS_S3 =  models.CharField(max_length=500,  blank=True, null=True) 

    CVS_Murmur =  models.CharField(max_length=500,  blank=True, null=True)
    CVS_Murmur_Present =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Multiple Select) (Mitral valve, Tricuspid valve, Other (Text Box))
    CVS_Murmur_Present_Other =  models.TextField(blank=True, null=True) 

    CVS_Click = models.CharField(max_length=500,  blank=True, null=True) 
    CVS_Click_Present_Position =  models.TextField(blank=True, null=True) 

    CVS_Apex_Beat =  models.CharField(max_length=500,  blank=True, null=True) 
    CVS_Apex_Beat_Present_Displaced =  models.TextField(blank=True, null=True) 


    # Section - 5
    Alimentary_and_Urinary_System_Do_you_have_Nausea_Vomiting =   models.CharField(max_length=500,  blank=True, null=True)  
    AUS_Do_you_have_Pain_in_your_Abdomen =   models.CharField(max_length=500,  blank=True, null=True)  
    AUS_Do_you_feel_Burning_when_you_pass_Urine =   models.CharField(max_length=500,  blank=True, null=True)  
    AUS_Cleft_Lip = models.CharField(max_length=500,  blank=True, null=True)
    AUS_Cleft_Lip_Present =  models.CharField(max_length=500,  blank=True, null=True)   
    AUS_Cleft_Palate = models.CharField(max_length=500, blank=True, null=True)
    AUS_Cleft_Palate_Present =  models.CharField(max_length=500, blank=True, null=True) 

    AUS_Abdominal_Distension = models.CharField(max_length=500, blank=True, null=True)
    AUS_Exaggerate_Bowel_Sounds = models.CharField(max_length=500, blank=True, null=True) 
    AUS_Guarding  = models.CharField(max_length=500, blank=True, null=True)
    AUS_Rigidity  = models.CharField(max_length=500, blank=True, null=True) 

    AUS_Right_Hypochondrium_Pain =  models.CharField(max_length=500, blank=True, null=True)  
    AUS_RH_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_RH_Tenderness = models.CharField(max_length=500,  blank=True, null=True)
    AUS_RH_Tenderness_Present = models.CharField(max_length=500,blank=True, null=True)  
    AUS_RH_Swelling_Lumps =  models.CharField(max_length=500,  blank=True, null=True) 
    AUS_RH_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_RH_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_RH_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_RH_Liver =  models.CharField(max_length=500, blank=True, null=True)  
    AUS_RH_Liver_Palpable =  models.CharField(max_length=500, blank=True, null=True)  
    AUS_RH_Gall_Bladder = models.CharField(max_length=500,  blank=True, null=True)
    AUS_RH_Gall_Bladder_Tender =  models.IntegerField(blank=True, null=True)

    AUS_Right_Lumbar_Pain = models.CharField(max_length=500,  blank=True, null=True)  
    AUS_RL_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_RL_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_RL_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True)  
    AUS_RL_Swelling_Lumps =  models.CharField(max_length=500, blank=True, null=True)
    AUS_RL_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_RL_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_RL_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_RL_Right_Kidney = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_RL_Right_Kidney_Palpable = models.CharField(max_length=500,  blank=True, null=True)

    AUS_Right_Iliac_Pain = models.CharField(max_length=500,  blank=True, null=True)  
    AUS_RI_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_RI_MBP = models.CharField(max_length=500,  blank=True, null=True)
    AUS_RI_MBP_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_RI_Tenderness = models.CharField(max_length=500,  blank=True, null=True)
    AUS_RI_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_RI_Swelling_Lumps =  models.CharField(max_length=500, blank=True, null=True)
    AUS_RI_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_RI_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_RI_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, blank=True, null=True)

    AUS_Epigastric_Pain = models.CharField(max_length=500,  blank=True, null=True)  
    AUS_E_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_E_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_E_Tenderness_Present = models.CharField(max_length=500, blank=True, null=True)
    AUS_E_Tenderness_Present_Rebound = models.CharField(max_length=500,  blank=True, null=True)  
    AUS_E_Swelling_Lumps =  models.CharField(max_length=500,  blank=True, null=True)
    AUS_E_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_E_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_E_Swelling_Lumps_Present_Texture = models.CharField(max_length=500, blank=True, null=True)

    AUS_Umbilical_Pain = models.CharField(max_length=500,  blank=True, null=True)  
    AUS_U_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_U_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_U_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True)
    AUS_U_Tenderness_Present_Rebound = models.CharField(max_length=500,  blank=True, null=True)  
    AUS_U_Swelling_Lumps = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_U_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_U_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_U_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True)

    AUS_Suprapubic_Pain = models.CharField(max_length=500,  blank=True, null=True)  
    AUS_S_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_S_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_S_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True)
    AUS_S_Tenderness_Present_Rebound = models.CharField(max_length=500,  blank=True, null=True)  
    AUS_S_Swelling_Lumps =  models.CharField(max_length=500, blank=True, null=True)
    AUS_S_Swelling_Lumps_Present_Description  =  models.CharField(max_length=1000,blank=True, null=True)
    AUS_S_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_S_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True)
    AUS_S_Uterus = models.CharField(max_length=500,  blank=True, null=True)
    AUS_S_Uterus_Palpable = models.CharField(max_length=500,  blank=True, null=True)

    AUS_Left_Hypochondrium_Pain = models.CharField(max_length=500, blank=True, null=True)  
    AUS_LH_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_LH_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_LH_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_LH_Swelling_Lumps = models.CharField(max_length=500,  blank=True, null=True)
    AUS_LH_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_LH_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_LH_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_LH_Spleen = models.CharField(max_length=500)
    AUS_LH_Spleen_Palpable = models.CharField(max_length=500,  blank=True, null=True)

    AUS_Left_Lumbar_Pain = models.CharField(max_length=500, blank=True, null=True)  
    AUS_LL_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_LL_Tenderness = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_LL_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_LL_Swelling_Lumps =  models.CharField(max_length=500,  blank=True, null=True) 
    AUS_LL_Swelling_Lumps_Present_Description  = models.CharField(max_length=1000,blank=True, null=True)
    AUS_LL_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_LL_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_LL_Left_Kidney = models.CharField(max_length=500,  blank=True, null=True) 
    AUS_LL_Left_Kidney_Palpable = models.CharField(max_length=500,  blank=True, null=True)

    AUS_Left_Iliac_Pain = models.CharField(max_length=500,  blank=True, null=True)  
    AUS_LI_Pain_Yes_Pain_Score = models.IntegerField(blank=True, null=True)
    AUS_LI_Tenderness = models.CharField(max_length=500,  blank=True, null=True)
    AUS_LI_Tenderness_Present = models.CharField(max_length=500,  blank=True, null=True)  
    AUS_LI_Swelling_Lumps =  models.CharField(max_length=500, blank=True, null=True) 
    AUS_LI_Swelling_Lumps_Present_Description  =  models.CharField(max_length=500,blank=True, null=True)
    AUS_LI_Swelling_Lumps_Present_Size  = models.IntegerField(blank=True, null=True)
    AUS_LI_Swelling_Lumps_Present_Texture = models.CharField(max_length=500,  blank=True, null=True) 

    AUS_Hernia =  models.CharField(max_length=500, blank=True, null=True)
    AUS_Hernia_Present = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Multiple Select) (Hiatus, Umblical, Right Inguinal, Left Inguinal, Right Femoral, Left Femoral)
    AUS_Urinary_Bladder =  models.CharField(max_length=500,  blank=True, null=True) 
    AUS_Urinary_Bladder_Palpable = models.CharField(max_length=500, blank=True, null=True)  #

    # Section - 6-A(Pubertal_Assessment_Girls)
# AUS_S_Swelling_Lumps_Present_Description
    Pubertal_Assessment_Girls = models.CharField(max_length=500, blank=True, null=True) 
    PAG_Tanner_Score = models.CharField(max_length=500,blank=True, null=True) 
    PAG_Menarche_Attained = models.CharField(max_length=500, blank=True, null=True)  
    PAG_MA_Yes_Age_of_Menarche = models.CharField(max_length=500, blank=True, null=True)
    PAG_MA_Yes_LMP_Date = models.DateField(blank=True, null=True)
    PAG_MA_Yes_Character_Regularity  = models.CharField(max_length=500, blank=True, null=True) 
    PAG_MA_Yes_Character_Frequency_in_Days = models.CharField(max_length=500,  blank=True, null=True)
    PAG_MA_Yes_Duration_in_days = models.CharField(max_length=500,  blank=True, null=True)  
    PAG_MA_Yes_Flow = models.CharField(max_length=500, blank=True, null=True) 
    PAG_MA_Yes_Comfort = models.CharField(max_length=500,blank=True, null=True)  
    PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses = models.CharField(max_length=500,  blank=True, null=True)  
    PAG_MA_Yes_Pain_in_other_parts_of_body_during_menses_Yes = models.CharField(max_length=50, null=True, blank=True)
    PAG_MA_Yes_Pain_in_other_parts_body_during_menses_Yes_Other  = models.TextField(blank=True, null=True)
    PAG_Yes_Cracking_of_Voice_or_chnage_in_voice = models.CharField(max_length=500,  blank=True, null=True)  
    PAG_HaveYouExperienced_A_change_in_behaviour_recently = models.CharField(max_length=500, blank=True, null=True)
    PAG_Change_behaviour_Yes =  models.CharField(max_length=500, blank=True, null=True)  
    PAG_Change_behaviour_Yes_Quiet_Withdrawn =  models.CharField(max_length=500,  blank=True, null=True) 
    PAG_Change_behaviour_Outgoing =  models.CharField(max_length=500,blank=True, null=True)
    PAG_Change_behaviour_Aggressive = models.CharField(max_length=500,  blank=True, null=True) 
    PAG_Change_behaviour_Bold_and_Daring =  models.CharField(max_length=500, blank=True, null=True) 
    PAG_Change_behaviour_Careless =  models.CharField(max_length=500,  blank=True, null=True) 
    PAG_Prefer_company_of =  models.CharField(max_length=500,  blank=True, null=True) 
    PAG_Any_other_abnormal_finding = models.CharField(max_length=500, blank=True, null=True)  
    # Any other abnormal finding : e.g. Brest Lump, Testicular Lump, Abnormal Genitalia, Pain, Discharge etc.
    PAG_Any_other_abnormal_finding_Yes = models.CharField(max_length=250, blank=True, null=True)

    # Section - 6-B(Pubertal_Assessment_Boys)

    Pubertal_Assessment_Boys = models.CharField(max_length=500, blank=True, null=True) 
    PAB_Tanner_Score = models.CharField(max_length=500, blank=True, null=True) 
    PAB_Yes_Cracking_of_Voice_or_chnage_in_voice = models.CharField(max_length=500, blank=True, null=True)  
    PAB_Nightly_Emissions =  models.CharField(max_length=500, blank=True, null=True)  
    PAB_HaveYouExperienced_A_change_in_behaviour_recently = models.CharField(max_length=500, blank=True, null=True)
    PAB_Change_behaviour_Yes =  models.CharField(max_length=500, blank=True, null=True)  
    PAB_Change_behaviour_Yes_Quiet_Withdrawn =  models.CharField(max_length=500,  blank=True, null=True) 
    PAB_Change_behaviour_Outgoing =  models.CharField(max_length=500,  blank=True, null=True) 
    PAB_Change_behaviour_Aggressive =  models.CharField(max_length=500,  blank=True, null=True) 
    PAB_Change_behaviour_Bold_and_Daring =  models.CharField(max_length=500,  blank=True, null=True) 
    PAB_Change_behaviour_Careless =  models.CharField(max_length=500, blank=True, null=True) 
    PAB_Prefer_company_of = models.CharField(max_length=500, blank=True, null=True)
    PAB_Any_other_abnormal_finding =  models.CharField(max_length=500, blank=True, null=True)  
    # Any other abnormal finding : e.g. Brest Lump, Testicular Lump, Abnormal Genitalia, Pain, Discharge etc.
    PAB_Any_other_abnormal_finding_Yes = models.CharField(max_length=250, null=True,blank=True)


    # Section - 7

    History_of_Medication = models.CharField(max_length=500, blank=True, null=True)  
    History_of_Medication_Yes = models.CharField(max_length=500, blank=True, null=True)  
    Name_of_Medication = models.TextField(null=True,blank=True) #  Add More

    # Section - 8

    Milestones = models.TextField()  # Yet to be defined 

    # Section - 9

    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=250,blank=True, null=True)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000,blank=True, null=True)  
    Specialist_Referral_Needed_Flag =  models.CharField(max_length=500,  blank=True, null=True)  
    Other  = models.TextField(null=True,blank=True)
    Review_Status = models.CharField(max_length=100)
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationG_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.CharField(max_length=250)
    Comments = models.TextField(null=True,blank=True)
    Logs_Time = models.DateTimeField(auto_now=True)

    objects = models.Manager

    class Meta:
         db_table = "StationG_logs"

# STATION H
         
class StationHModel_Log(models.Model):

    ## Section-1 
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationH_StationId_Log',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationH_HCID_Log',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationH_HcpId_Log',on_delete=models.CASCADE)
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationH_InfoseekId_Log',on_delete=models.CASCADE)
    
    
    Upper_Permanent = models.CharField(max_length=1000, null=True, blank=True)  ## Master data(Multiple Select) (Decayed,Missing,Filled,Prosthesis)
    Upper_Permanent_Decayed = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select)

    Upper_Permanent_Missing = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select)((1 to 16)
    Upper_Permanent_Filled = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (1 to 16)
    Upper_Permanent_Prosthesis = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (1 to 16)
    Upper_Permanent_Restoration_done = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (1 to 16)

    Upper_Deciduous =models.CharField(max_length=1000, null=True, blank=True)  ## Master data(Multiple Select)(Decayed,Missing,Filled,Prosthesis,Restoration done )
    Upper_Deciduous_Decayed = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (A to J)
    Upper_Deciduous_Missing = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (A to J)
    Upper_Deciduous_Filled = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (A to J)
    Upper_Deciduous_Prosthesis = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (A to J)
    Upper_Deciduous_Restoration_done = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (A to J)

    Lower_Deciduous = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)(Decayed,Missing,Filled,Prosthesis,Restoration done )
    Lower_Deciduous_Decayed = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)
    Lower_Deciduous_Missing = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)
    Lower_Deciduous_Filled = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)
    Lower_Deciduous_Prosthesis = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)
    Lower_Deciduous_Restoration_done = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)

    Lower_Permanent = models.CharField(max_length=1000, null=True, blank=True)## Master data(Multiple Select) (T to K)(Decayed,Missing,Filled,Prosthesis,Restoration done )
    Lower_Permanent_Decayed = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (32 to 17)
    Lower_Permanent_Missing = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (32 to 17)
    Lower_Permanent_Filled = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (32 to 17)
    Lower_Permanent_Prosthesis = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (32 to 17)
    Lower_Permanent_Restoration_done = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (32 to 17)

    ## Section-2

    Oral_Hygiene = models.CharField(max_length=50) ## Master Data (Satisfactory, Poor)
    Plaque = models.CharField(max_length=250)
    Dental_Stains = models.CharField(max_length=250)
    Malocclusion  = models.CharField(max_length=250)
    Crowding  = models.CharField(max_length=250)
    Impacted_Tooth  = models.CharField(max_length=250)
    Impacted_Tooth_Yes = models.CharField(max_length=1000)
    Impacted_Tooth_Yes_Position = models.TextField(null=True, blank=True)

    
    Worn_Enamel   = models.CharField(max_length=250)

    ## Section-3 

    Sensitivity = models.CharField(max_length=250)
    Untreated_Caries = models.CharField(max_length=250)
    Caries_Experience = models.CharField(max_length=250)
    Dental_Sealants_Present  = models.CharField(max_length=250)
    
    Braces = models.CharField(max_length=250,null=True,blank=True)
    Braces_Yes = models.CharField(max_length=50,null=True,blank=True) ## Master Data(Multiple Select) (Upper Teeth, Lower Teeth)

    Bridges = models.CharField(max_length=250,null=True,blank=True)
    Bridges_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Upper Teeth, Lower Teeth)

    Dentures = models.CharField(max_length=250,null=True,blank=True)
    Dentures_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Upper Jaw, Lower Jaw)

    ## Section-4

    Soft_Tissue_Pathology = models.CharField(max_length=1000,null=True,blank=True)
    Soft_Tissue_Pathology_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Mutliple Select) (Gingivitis, Ulcer, Abscess, Vesicle, Growth, Bleeding Gum, Discoloration, Receding Gums, Other)
    Soft_Tissue_Pathology_Yes_Other = models.TextField(null=True, blank=True)

    Treatment_Needed = models.CharField(max_length=250,null=True,blank=True)
    Treatment_Needed_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Mutliple Select) (Urgent Treatment, Preventive Care, Restorative Care, Other)
    Treatment_Needed_Yes_Other = models.TextField(null=True, blank=True)

    Dental_Florosis  = models.CharField(max_length=250)

    ## Section-5 

    Other_Observations = models.TextField(null=True,blank=True)
    StationH_Dental_SR_Needed = models.CharField(max_length=250)
    StationH_Dental_SR_Needed_Yes_Type = models.CharField(max_length=100000,  null=True,blank=True ) ## Master Data (Pediatric Dentist,Endodontist,Oral and Maxillofacial,Surgeon,Orthodontist,Periodontist,Prosthodontist)
    StationH_Dental_SR_Needed_Yes_Flag =  models.CharField(max_length=250,  null=True,blank=True) ## Master Data (Non Urgent, Urgent, Emergency)

    ## Section-6

    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=250)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
    Specialist_Referral_Needed_Flag =   models.CharField(max_length=250,  null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)    

    Review_Status = models.CharField(max_length=100)
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationH_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.CharField(max_length=250)
    Comments = models.TextField(null=True,blank=True)
    Logs_Time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "StationH_logs"