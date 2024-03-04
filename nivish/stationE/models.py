
from django.db import models

# Create your models here.
from datetime import datetime

from Enum.enumstation_e import *
from Enum.enum import *

class StationEModel(models.Model):
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationE_StationId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationE_HCID',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationE_HcpId',on_delete=models.CASCADE)
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationE_InfoseekId',on_delete=models.CASCADE)

    EntryTime = models.TimeField()

    Child_Mobility = models.CharField(max_length=50, null=True, blank=True , choices=Child_Mobility_ENUM)  ## Master Data (Can Walk, Can not Walk)
    Child_Mobility_Can_not_Walk = models.CharField(max_length=50, null=True, blank=True, choices=Child_Mobility_Can_not_Walk_ENUM)  ## Master Data (No Developmental Delay, Delayed Milestone, Other)
    Child_Mobility_Can_not_Walk_other = models.TextField(null=True, blank=True)

    Student_Ambulant = models.CharField(max_length=50, choices=SRNYesorNo)
    Student_Ambulant_No = models.CharField(max_length=50, null=True, blank=True, choices=Student_Ambulant_No_ENUM) ## Master Data (Uses a Wheelchair,Uses Crutches, Uses other motorized system for movement)

    Gait = models.TextField(null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    Gait_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=Gait_Abnormal_ENUM) ## Master Data (Shuffling, Limp, Other abnormal gait )
    Gait_Abnormal_Limp = models.CharField(max_length=50, null=True, blank=True, choices=Gait_Abnormal_Limp_ENUM) ## Master Data (Lower limb length discrepancy,Other causes)
    Gait_Abnormal_Limp_other = models.TextField(null=True, blank=True)
    

    Wear_Brace_Support = models.CharField(max_length=1000, choices=SRNYesorNo, null=True, blank=True)
    Wear_Brace_Support_Yes = models.CharField(max_length=10000, null=True, blank=True) ## Master Data (Neck, Shoulders, Back, Chest, Right Upper Limb, Left Upper Limb, Right Lower Limb, Left Lower Limb)

    Prosthesis = models.CharField(max_length=1000, choices=SRNYesorNo, null=True, blank=True)
    Prosthesis_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Knee, Hip, Spine, Hip, Right Upper Limb, Left Upper Limb, Right Lower Limb, Left Lower Limb, Right shoulder, Left shoulder,Others)
    Prosthesis_Yes_other = models.TextField(null=True, blank=True)

    Spine_Appearance = models.CharField(max_length=50, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    Spine_Appearance_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=Spine_Appearance_Abnormal_ENUM) ## Master Data (Kyphosis, Scoliosis, Kypho-scoliosis, Rigid, Other)
    Spine_Appearance_Abnormal_Other = models.TextField(null=True, blank=True) 
    
    Shoulder_Griddle_Appearance = models.CharField(max_length=50, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    Shoulder_Griddle_Appearance_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Postural, Bony Causes, Muscle spasms / knots, Other)
    Shoulder_Griddle_Appearance_Abnormal_Other = models.TextField(null=True, blank=True) 


    Spine_Mobility = models.CharField(max_length=50, null=True, blank=True, choices=NormalandRestrictedmovement) ## Master Data (Normal, Restricted movement,)
    Spine_Mobility_Restricted_movement = models.CharField(max_length=50, null=True, blank=True, choices=Restricted_movement) ## Master Data (Mild, Moderate, Severe )

    Neck_Mobility = models.CharField(max_length=50, null=True, blank=True, choices=NormalandRestrictedmovement) ## Master Data (Normal, Restricted movement,)
    Neck_Mobility_Restricted_movement = models.CharField(max_length=50, null=True, blank=True, choices=Restricted_movement) ## Master Data (Mild, Moderate, Severe )
## Upper Limib Right
    UL_Right_Appearance =  models.CharField(max_length=1000, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    UL_Right_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

    UL_Right_Motor_Function_Tone =  models.CharField(max_length=1000, null=True, blank=True, choices=Motor_Function_Tone) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
    UL_Right_Motor_Function_Range_of_Movement = models.CharField(max_length=50, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    UL_Right_MF_RM_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=MF_RM_Abnormal) ##Master Data (Hyper Flexible, Restricted)
    UL_Right_MF_RM_Abnormal_Hyper_Flexible = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Fingers, Hand, Elbow, Shoulder)
    UL_Right_MF_RM_Abnormal_Restricted = models.CharField(max_length=50, null=True, blank=True, choices=Restricted_movement) ## Master Data (Mild, Moderate, Severe)
    UL_Right_Motor_Function_Strength = models.CharField(max_length=50, choices=Motor_Function_Strength)

    UL_Right_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=50, null=True, blank=True, choices=DTRNormalandAbnormal) ## Master Data (Normal, Abnormal)
    UL_Right_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=DTR_Abnormal) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    UL_Right_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True, choices=DTRNormalandAbnormal) ## Master Data (Normal, Abnormal)
    UL_Right_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=DTR_Abnormal) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    UL_Right_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=50, null=True, blank=True, choices=DTR_Sensory_Function) ## Master Data (Normal, Abnormal)
    UL_Right_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
    UL_Right_DTR_SF_Abnormal_Touch = models.CharField(max_length=50, null=True, blank=True, choices=Touch_Abnormal) ## Master Data (Hot object, Cold object, Both hot & cold objects)
    UL_Right_DTR_SF_Abnormal_Pain_Present= models.IntegerField( null=True, blank=True)
    UL_Right_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField( null=True, blank=True)
    UL_Right_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField( null=True, blank=True)
## Upper Limib Left
    UL_Left_Appearance =  models.CharField(max_length=50, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    UL_Left_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

    UL_Left_Motor_Function_Tone =  models.CharField(max_length=50, null=True, blank=True, choices=Motor_Function_Tone) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
    UL_Left_Motor_Function_Range_of_Movement = models.CharField(max_length=50, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    UL_left_MF_RM_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=MF_RM_Abnormal) ##Master Data (Hyper Flexible, Restricted)
    UL_Left_MF_RM_Abnormal_Hyper_Flexible = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Fingers, Hand, Elbow, Shoulder)
    UL_Left_MF_RM_Abnormal_Restricted = models.CharField(max_length=50, null=True, blank=True, choices=Restricted_movement) ## Master Data (Mild, Moderate, Severe)
    UL_Left_Motor_Function_Strength = models.CharField(max_length=50, choices=Motor_Function_Strength)

    UL_Left_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=100, null=True, blank=True, choices=DTRNormalandAbnormal) ## Master Data (Normal, Abnormal)
    UL_Left_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=DTR_Abnormal) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    UL_Left_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True, choices=DTRNormalandAbnormal) ## Master Data (Normal, Abnormal)
    UL_Left_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=DTR_Abnormal) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    UL_Left_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=100, null=True, blank=True, choices=DTR_Sensory_Function) ## Master Data (Normal, Abnormal)
    UL_Left_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
    UL_Left_DTR_SF_Abnormal_Touch = models.CharField(max_length=1000, null=True, blank=True, choices=Touch_Abnormal) ## Master Data (Hot object, Cold object, Both hot & cold objects)
    UL_Left_DTR_SF_Abnormal_Pain_Present= models.IntegerField(null=True, blank=True)
    UL_Left_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField(null=True, blank=True)
    UL_Left_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField(null=True, blank=True)
## Lower Limib Right
    LL_Right_Appearance =  models.CharField(max_length=100, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    LL_Right_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

    LL_Right_Motor_Function_Tone =  models.CharField(max_length=1000, null=True, blank=True, choices=Motor_Function_Tone) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
    LL_Right_Motor_Function_Range_of_Movement = models.CharField(max_length=1000, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    LL_Right_Motor_Function_Strength = models.CharField(max_length=50, choices=Motor_Function_Strength)

    LL_Right_Motor_Function_Knee = models.CharField(max_length=250, null=True, blank=True, choices=DTRNormalandAbnormal) ## Master Data (Normal, Abnormal)
    LL_Right_Motor_Function_Knee_Abnormal = models.CharField(max_length=250, null=True, blank=True, choices=DTR_Abnormal) ## Master Data (Absent, Sluggish, Exaggerated, Clonus)

    # LL_Right_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=50, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    # LL_Right_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=DTR_Abnormal) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)


    # LL_Right_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    # LL_Right_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    LL_Right_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=1000, null=True, blank=True, choices=DTR_Sensory_Function) ## Master Data (Normal, Abnormal)
    LL_Right_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
    LL_Right_DTR_SF_Abnormal_Touch = models.CharField(max_length=50, null=True, blank=True, choices=Touch_Abnormal) ## Master Data (Hot object, Cold object, Both hot & cold objects)
    LL_Right_DTR_SF_Abnormal_Pain_Present= models.IntegerField(null=True, blank=True)
    LL_Right_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField(null=True, blank=True)
    LL_Right_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField(null=True, blank=True)
## Lower Limib Left
    LL_Left_Appearance =  models.CharField(max_length=1000, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    LL_Left_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

    LL_Left_Motor_Function_Tone =  models.CharField(max_length=100, null=True, blank=True, choices=Motor_Function_Tone) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
    LL_Left_Motor_Function_Range_of_Movement = models.CharField(max_length=100, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
    LL_Left_Motor_Function_Strength = models.CharField(max_length=50, choices=Motor_Function_Strength)

    LL_Left_Motor_Function_Knee = models.CharField(max_length=250, null=True, blank=True, choices=DTRNormalandAbnormal) ## Master Data (Normal, Abnormal)
    LL_Left_Motor_Function_Knee_Abnormal = models.CharField(max_length=250, null=True, blank=True, choices=DTR_Abnormal) ## Master Data (Absent, Sluggish, Exaggerated, Clonus)

    # LL_Left_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    # LL_Left_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    # LL_Left_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
    # LL_Left_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

    LL_Left_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=50, null=True, blank=True, choices=DTR_Sensory_Function) ## Master Data (Normal, Abnormal)
    LL_Left_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
    LL_Left_DTR_SF_Abnormal_Touch = models.CharField(max_length=50, null=True, blank=True, choices=Touch_Abnormal) ## Master Data (Hot object, Cold object, Both hot & cold objects)
    LL_Left_DTR_SF_Abnormal_Pain_Present= models.IntegerField(null=True, blank=True)
    LL_Left_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField(null=True, blank=True)
    LL_Left_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField(null=True, blank=True)

    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed     = models.CharField(max_length=250, choices=SRNYesorNo, null=True,blank=True)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000, null=True,blank=True)
    Specialist_Referral_Needed_Flag =   models.CharField(max_length=250, choices=Referral_Needed_Flag,  null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)
    Completed = models.CharField(max_length=50, choices=SRNYesorNo,default='No')

    Review_Status = models.CharField(max_length=100,choices=Review_Status_Enum,default='Not Reviewed')
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationE_Reviewedby_HcpId',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.DateTimeField(null=True,blank=True)
    Comments = models.TextField(null=True,blank=True)

    EndTime = models.TimeField(null=True,blank=True)
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "StationE_Collection"



# class StationEModel_Log(models.Model):
#     StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationE_StationId_Log',on_delete=models.CASCADE)
#     HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationE_HCID_Log',on_delete=models.CASCADE)
#     HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationE_HcpId_Log',on_delete=models.CASCADE)
#     InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationE_InfoseekId_Log',on_delete=models.CASCADE)

    

#     Child_Mobility = models.CharField(max_length=50, null=True, blank=True)  ## Master Data (Can Walk, Can not Walk)
#     Child_Mobility_Can_not_Walk = models.CharField(max_length=50, null=True, blank=True)  ## Master Data (No Developmental Delay, Delayed Milestone, Other)
#     Child_Mobility_Can_not_Walk_other = models.TextField(null=True, blank=True)

#     Student_Ambulant = models.CharField(max_length=50)
#     Student_Ambulant_No = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Uses a Wheelchair,Uses Crutches, Uses other motorized system for movement)

#     Gait = models.TextField(null=True, blank=True) ## Master Data (Normal, Abnormal)
#     Gait_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Shuffling, Limp, Other abnormal gait )
#     Gait_Abnormal_Limp = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Lower limb length discrepancy,Other causes)
#     Gait_Abnormal_Limp_other = models.TextField(null=True, blank=True)
    

#     Wear_Brace_Support = models.CharField(max_length=1000, null=True, blank=True)
#     Wear_Brace_Support_Yes = models.CharField(max_length=10000, null=True, blank=True) ## Master Data (Neck, Shoulders, Back, Chest, Right Upper Limb, Left Upper Limb, Right Lower Limb, Left Lower Limb)

#     Prosthesis = models.CharField(max_length=1000,  null=True, blank=True)
#     Prosthesis_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Knee, Hip, Spine, Hip, Right Upper Limb, Left Upper Limb, Right Lower Limb, Left Lower Limb, Right shoulder, Left shoulder,Others)
#     Prosthesis_Yes_other = models.TextField(null=True, blank=True)

#     Spine_Appearance = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     Spine_Appearance_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Kyphosis, Scoliosis, Kypho-scoliosis, Rigid, Other)
#     Spine_Appearance_Abnormal_Other = models.TextField(null=True, blank=True) 
    
#     Shoulder_Griddle_Appearance = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     Shoulder_Griddle_Appearance_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Postural, Bony Causes, Muscle spasms / knots, Other)
#     Shoulder_Griddle_Appearance_Abnormal_Other = models.TextField(null=True, blank=True) 


#     Spine_Mobility = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Restricted movement,)
#     Spine_Mobility_Restricted_movement = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Mild, Moderate, Severe )

#     Neck_Mobility = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Restricted movement,)
#     Neck_Mobility_Restricted_movement = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Mild, Moderate, Severe )
# ## Upper Limib Right
#     UL_Right_Appearance =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     UL_Right_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

#     UL_Right_Motor_Function_Tone =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
#     UL_Right_Motor_Function_Range_of_Movement = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     UL_Right_MF_RM_Abnormal = models.CharField(max_length=50, null=True, blank=True) ##Master Data (Hyper Flexible, Restricted)
#     UL_Right_MF_RM_Abnormal_Hyper_Flexible = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Fingers, Hand, Elbow, Shoulder)
#     UL_Right_MF_RM_Abnormal_Restricted = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Mild, Moderate, Severe)
#     UL_Right_Motor_Function_Strength = models.CharField(max_length=50)

#     UL_Right_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     UL_Right_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

#     UL_Right_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     UL_Right_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

#     UL_Right_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     UL_Right_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
#     UL_Right_DTR_SF_Abnormal_Touch = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Hot object, Cold object, Both hot & cold objects)
#     UL_Right_DTR_SF_Abnormal_Pain_Present= models.IntegerField( null=True, blank=True)
#     UL_Right_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField( null=True, blank=True)
#     UL_Right_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField( null=True, blank=True)
# ## Upper Limib Left
#     UL_Left_Appearance =  models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     UL_Left_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

#     UL_Left_Motor_Function_Tone =  models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
#     UL_Left_Motor_Function_Range_of_Movement = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     UL_left_MF_RM_Abnormal = models.CharField(max_length=50, null=True, blank=True) ##Master Data (Hyper Flexible, Restricted)
#     UL_Left_MF_RM_Abnormal_Hyper_Flexible = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Fingers, Hand, Elbow, Shoulder)
#     UL_Left_MF_RM_Abnormal_Restricted = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Mild, Moderate, Severe)
#     UL_Left_Motor_Function_Strength = models.CharField(max_length=50)

#     UL_Left_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=100, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     UL_Left_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

#     UL_Left_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     UL_Left_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

#     UL_Left_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=100, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     UL_Left_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
#     UL_Left_DTR_SF_Abnormal_Touch = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Hot object, Cold object, Both hot & cold objects)
#     UL_Left_DTR_SF_Abnormal_Pain_Present= models.IntegerField(null=True, blank=True)
#     UL_Left_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField(null=True, blank=True)
#     UL_Left_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField(null=True, blank=True)
# ## Lower Limib Right
#     LL_Right_Appearance =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     LL_Right_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

#     LL_Right_Motor_Function_Tone =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
#     LL_Right_Motor_Function_Range_of_Movement = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     LL_Right_Motor_Function_Strength = models.CharField(max_length=50)

#     LL_Right_Motor_Function_Knee = models.CharField(max_length=250, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     LL_Right_Motor_Function_Knee_Abnormal = models.CharField(max_length=250, null=True, blank=True) ## Master Data (Absent, Sluggish, Exaggerated, Clonus)

#     # LL_Right_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=50, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
#     # LL_Right_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True, choices=DTR_Abnormal) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)


#     # LL_Right_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True, choices=NormalandAbnormal) ## Master Data (Normal, Abnormal)
#     # LL_Right_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

#     LL_Right_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     LL_Right_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
#     LL_Right_DTR_SF_Abnormal_Touch = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Hot object, Cold object, Both hot & cold objects)
#     LL_Right_DTR_SF_Abnormal_Pain_Present= models.IntegerField(null=True, blank=True)
#     LL_Right_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField(null=True, blank=True)
#     LL_Right_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField(null=True, blank=True)
# ## Lower Limib Left
#     LL_Left_Appearance =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     LL_Left_Appearance_Abnormal =  models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Atrophy, Contracture, Deformity, Hypertrophy, Oedema)

#     LL_Left_Motor_Function_Tone =  models.CharField(max_length=100, null=True, blank=True) ## Master Data (Normal, Fasciculations, Rigidity [hypertonia], Flaccidity [hypotonia], Spasticity [hypertonia] )
#     LL_Left_Motor_Function_Range_of_Movement = models.CharField(max_length=100, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     LL_Left_Motor_Function_Strength = models.CharField(max_length=50)

#     LL_Left_Motor_Function_Knee = models.CharField(max_length=250, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     LL_Left_Motor_Function_Knee_Abnormal = models.CharField(max_length=250, null=True, blank=True) ## Master Data (Absent, Sluggish, Exaggerated, Clonus)

#     # LL_Left_Deep_Tendon_Reflexes_Biceps = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     # LL_Left_DTR_Biceps_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

#     # LL_Left_Deep_Tendon_Reflexes_Radial = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     # LL_Left_DTR_Radial_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Absen, Sluggish, Exaggerated, Clonus)

#     LL_Left_Deep_Tendon_Reflexes_Sensory_Function = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Normal, Abnormal)
#     LL_Left_DTR_SF_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data (Touch Abnormal, Pain Present, Pressure Abnormal, Tenderness Present)
#     LL_Left_DTR_SF_Abnormal_Touch = models.CharField(max_length=50, null=True, blank=True) ## Master Data (Hot object, Cold object, Both hot & cold objects)
#     LL_Left_DTR_SF_Abnormal_Pain_Present= models.IntegerField(null=True, blank=True)
#     LL_Left_DTR_SF_Abnormal_Pressure_Abnormal = models.BooleanField(null=True, blank=True)
#     LL_Left_DTR_SF_Abnormal_Tenderness_Present= models.IntegerField(null=True, blank=True)

#     Other_Observations = models.TextField(null=True,blank=True)
#     Specialist_Referral_Needed     = models.CharField(max_length=250,  null=True,blank=True)
#     Specialist_Referral_Needed_Type = models.CharField(max_length=100000, null=True,blank=True)
#     Specialist_Referral_Needed_Flag =   models.CharField(max_length=250,   null=True,blank=True)
#     Other  = models.TextField(null=True,blank=True)
#     Review_Status = models.CharField(max_length=100)
#     Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationE_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
#     Reviewed_On = models.CharField(max_length=100)
#     Comments = models.TextField(null=True,blank=True)
#     Logs_Time = models.DateTimeField(auto_now=True)
    
#     objects = models.Manager 

#     class Meta:
#         db_table = 'StationE_logs'

