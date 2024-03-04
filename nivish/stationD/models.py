from django.db import models
from datetime import datetime

from Enum.enumstation_d import *
from Enum.enum import *

class StationDModel(models.Model):
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationD_StationId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationD_HCID',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationD_HcpId',on_delete=models.CASCADE)
    InfoseekId  = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationD_InfoseekId',on_delete=models.CASCADE)
    
    EntryTime = models.TimeField()
    #section-1
    Do_you_have_problem_inhearing_your_Teachers_Friends_Parents = models.CharField(max_length=20,choices=problem_inhearing_Enum,null=True,blank=True)
    Do_you_have_problem_inhearing_your_Teachers_Yes = models.CharField(max_length=1000,null=True,blank=True)

    Does_any_fluid_come_out_of_your_ears = models.CharField(max_length=20,choices=SRNYesorNo,null=True,blank=True)
    Does_any_fluid_come_out_of_your_ears_Yes = models.CharField(max_length=1000,null=True,blank=True)

    #section-2
    Visual_inspection_Right_Ear_Pinna = models.CharField(max_length=200,null=True,blank=True, choices=NormalandAbnormal)
    Visual_inspection_Right_Ear_Pinna_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
    Visual_inspection_Right_Ear_EarCanal = models.CharField(max_length=200,null=True,blank=True,choices=NormalandAbnormal)
    Visual_inspection_Right_Ear_EarCanal_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
    Visual_inspection_Left_Ear_Pinna = models.CharField(max_length=200,null=True,blank=True,choices=NormalandAbnormal)
    Visual_inspection_Left_Ear_Pinna_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
    Visual_inspection_Left_Ear_EarCanal = models.CharField(max_length=200,null=True,blank=True,choices=NormalandAbnormal)
    Visual_inspection_Left_Ear_EarCanal_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
    Any_other_related_findings = models.TextField(null=True,blank=True)

    #section-3
    Pure_Tone_Audiometry_Right_Ear_500Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Right_Ear_500Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)

    Pure_Tone_Audiometry_Left_Ear_500Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Left_Ear_500Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
    Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB = models.CharField(max_length=200,null=True,blank=True,choices=Tone_Audiometry_Enum)
    Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)

    Upload_Pure_Tone_Test_Results = models.ImageField(upload_to='HCP',null=True, blank=True,max_length=100000)  #Upload / Image capture Button

    #section-4
    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=250,choices=SRNYesorNo,null=True,blank=True)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
    Specialist_Referral_Needed_Flag =   models.CharField(max_length=100,choices=Referral_Needed_Flag,null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)
    Completed = models.CharField(max_length=50, choices=SRNYesorNo,default='No')
    Review_Status = models.CharField(max_length=100,choices=Review_Status_Enum,default='Not Reviewed')
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationD_Reviewedby_HcpId',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.DateTimeField(null=True,blank=True)
    Comments = models.TextField(null=True,blank=True)
    EndTime = models.TimeField(null=True,blank=True)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "StationD_Collection"


class StationDModel_Doc(models.Model):
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationD_UploadDoc_StationId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationD_UploadDoc_HCID',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationD_UploadDoc_HcpId',on_delete=models.CASCADE)
    InfoseekId  = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationD_UploadDoc_InfoseekId',on_delete=models.CASCADE)
    Upload_Pure_Tone_Test_Results = models.ImageField(upload_to='HCP',null=True, blank=True,max_length=100000)
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "StationD_Collection_Docs"



# class StationDModel_Log(models.Model):
#     StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationD_StationId_Log',on_delete=models.CASCADE)
#     HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationD_HCID_Log',on_delete=models.CASCADE)
#     HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationD_HcpId_Log',on_delete=models.CASCADE)
#     InfoseekId  = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationD_InfoseekId_Log',on_delete=models.CASCADE)
    
#     #section-1
#     Do_you_have_problem_inhearing_your_Teachers_Friends_Parents = models.CharField(max_length=20,null=True,blank=True)
#     Do_you_have_problem_inhearing_your_Teachers_Yes = models.CharField(max_length=1000,null=True,blank=True)

#     Does_any_fluid_come_out_of_your_ears = models.CharField(max_length=20,null=True,blank=True)
#     Does_any_fluid_come_out_of_your_ears_Yes = models.CharField(max_length=1000,null=True,blank=True)

#     #section-2
#     Visual_inspection_Right_Ear_Pinna = models.CharField(max_length=200,null=True,blank=True)
#     Visual_inspection_Right_Ear_Pinna_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
#     Visual_inspection_Right_Ear_EarCanal = models.CharField(max_length=200,null=True,blank=True)
#     Visual_inspection_Right_Ear_EarCanal_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
#     Visual_inspection_Left_Ear_Pinna = models.CharField(max_length=200,null=True,blank=True)
#     Visual_inspection_Left_Ear_Pinna_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
#     Visual_inspection_Left_Ear_EarCanal = models.CharField(max_length=200,null=True,blank=True)
#     Visual_inspection_Left_Ear_EarCanal_Abnormal = models.CharField(max_length=1000,null=True,blank=True)
#     Any_other_related_findings = models.TextField(null=True,blank=True)

#     #section-3
#     Pure_Tone_Audiometry_Right_Ear_500Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Right_Ear_500Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
#     Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Right_Ear_1000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
#     Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Right_Ear_2000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
#     Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Right_Ear_4000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
#     Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Right_Ear_6000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
#     Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Right_Ear_8000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)

#     Pure_Tone_Audiometry_Left_Ear_500Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Left_Ear_500Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
#     Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Left_Ear_1000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
#     Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Left_Ear_2000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
#     Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Left_Ear_4000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
#     Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Left_Ear_6000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)
#     Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB = models.CharField(max_length=200,null=True,blank=True)
#     Pure_Tone_Audiometry_Left_Ear_8000Hz_25dB_Refer = models.CharField(max_length=1000,null=True,blank=True)

#     Upload_Pure_Tone_Test_Results = models.ImageField(upload_to='HCP',null=True, blank=True,max_length=100000)  #Upload / Image capture Button

#     #section-4
#     Other_Observations = models.TextField(null=True,blank=True)
#     Specialist_Referral_Needed = models.CharField(max_length=250,null=True,blank=True)
#     Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
#     Specialist_Referral_Needed_Flag =   models.CharField(max_length=100,null=True,blank=True)
#     Other  = models.TextField(null=True,blank=True)
#     Review_Status = models.CharField(max_length=100)
#     Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationD_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
#     Reviewed_On = models.CharField(max_length=250)
#     Comments = models.TextField(null=True,blank=True)
#     Logs_Time = models.DateTimeField(auto_now=True)
#     objects = models.Manager

#     class Meta:
#         db_table = "StationD_logs"



