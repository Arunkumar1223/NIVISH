from django.db import models
from datetime import datetime
from Enum.enum import SRNYesorNo, Referral_Needed_Flag, Review_Status_Enum


class StationAModel(models.Model):
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationA_StationId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationA_HCID',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationA_HcpId',on_delete=models.CASCADE)

    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationA_InfoseekId',on_delete=models.CASCADE)
    
    HCP_TeamId = models.ForeignKey('super_admin.HealthCampTeamsModel',related_name='stationA_HealthCampTeamsModel',on_delete=models.CASCADE)

    EntryTime = models.TimeField()
    Height = models.IntegerField(null=True,blank=True)
    Length = models.IntegerField(null=True,blank=True)
    Weight = models.IntegerField()
    Calculated_BMI = models.CharField(max_length=250)
    Triceps_Skin_Fold = models.CharField(max_length=250)
    Subscapular_Skinfold = models.CharField(max_length=250,null=True,blank=True)
    Arm_Circumference = models.CharField(max_length=250,null=True,blank=True)
    Head_Circumference = models.CharField(max_length=250,null=True,blank=True)
    Abdominal_Girth = models.CharField(max_length=250)
    Abdominal_Girth_to_Hight_Ratio = models.CharField(max_length=250)
    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed  = models.CharField(max_length=50, choices=SRNYesorNo)
    Specialist_Referral_Needed_Type  = models.CharField(max_length=1000000,null=True,blank=True)
    Specialist_Referral_Needed_Flag  = models.CharField(max_length=50, choices=Referral_Needed_Flag,null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)
    Review_Status = models.CharField(max_length=100,choices=Review_Status_Enum,default='Not Reviewed')
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationA_Reviewedby_HcpId',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.DateTimeField(null=True,blank=True)
    Comments = models.TextField(null=True,blank=True)
    EndTime = models.TimeField(null=True,blank=True)
    Completed = models.CharField(max_length=50, choices=SRNYesorNo,default=None)
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "StationA_Collection"



# class StationAModel_Log(models.Model):
#     # id_A = models.CharField(max_length=50)

#     StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationA_StationId_Log',on_delete=models.CASCADE)
#     HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationA_HCID_Log',on_delete=models.CASCADE)
#     HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationA_HcpId_Log',on_delete=models.CASCADE)
#     InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationA_InfoseekId_Log',on_delete=models.CASCADE)
#     HCP_TeamId = models.ForeignKey('super_admin.HealthCampTeamsModel',related_name='stationA_HealthCampTeamsModel_Log',on_delete=models.CASCADE)
#     Height = models.IntegerField()
#     Length = models.IntegerField()
#     Weight = models.IntegerField()
#     Calculated_BMI = models.CharField(max_length=250)
#     Triceps_Skin_Fold = models.CharField(max_length=250)
#     Subscapular_Skinfold = models.CharField(max_length=250,null=True,blank=True)
#     Arm_Circumference = models.CharField(max_length=250)
#     Head_Circumference = models.CharField(max_length=250)
#     Abdominal_Girth = models.CharField(max_length=250)
#     Abdominal_Girth_to_Hight_Ratio = models.CharField(max_length=250)
#     Other_Observations = models.TextField(null=True,blank=True)
#     Specialist_Referral_Needed  = models.CharField(max_length=250,)
#     Specialist_Referral_Needed_Type  = models.CharField(max_length=100000,null=True,blank=True)
#     Specialist_Referral_Needed_Flag  = models.CharField(max_length=250,null=True,blank=True)
#     Other  = models.TextField(null=True,blank=True)
#     Review_Status = models.CharField(max_length=100)
#     Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationA_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
#     Reviewed_On = models.CharField(max_length=250)
#     Comments = models.TextField(null=True,blank=True)
#     Logs_Time = models.DateTimeField(auto_now=True)
#     objects = models.Manager
#     class Meta:
#         db_table = "StationA_logs"



