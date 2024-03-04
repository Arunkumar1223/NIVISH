from django.db import models
from Enum.enum import Review_Status_Enum
# Create your models here


class FinalStatusModel(models.Model):
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='status_InfoseekId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='Status_HCID',on_delete=models.CASCADE)
    UIN = models.CharField(max_length=255)
    Final_Flag_status = models.CharField(max_length=255, null=True, blank=True)
    Reviewed_by = models.ForeignKey('hcp.HcpRegistrationModel',related_name='RD_ID',on_delete=models.CASCADE, null=True, blank=True)
    Review_status = models.CharField(max_length=255, null=True, blank=True,choices=Review_Status_Enum,default='Not Reviewed')
    Reviewd_on = models.DateTimeField(null=True,  default = None, blank=True)
    final_mark = models.CharField(max_length=255)
    Final_Review_Comments = models.TextField()


    class Meta:
        db_table = "Review_Doctor"


class AllStationsFlags(models.Model):
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='Flags_InfoseekId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='Flags_HCID',on_delete=models.CASCADE)
    stationAflag = models.CharField(max_length=100)
    stationBflag = models.CharField(max_length=100)
    stationCflag = models.CharField(max_length=100)
    stationDflag = models.CharField(max_length=100)
    stationEflag = models.CharField(max_length=100)
    stationFflag = models.CharField(max_length=100)
    stationGflag = models.CharField(max_length=100)
    stationHflag = models.CharField(max_length=100)

    class Meta:
        db_table = "StationsFlags"







