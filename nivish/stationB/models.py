from django.db import models

# Create your models here.
from datetime import datetime


from Enum.enumstation_b import *
from Enum.enum import *

class StationBModel(models.Model):
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationB_StationId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationB_HCID',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationB_HcpId',on_delete=models.CASCADE)
    InfoseekId  = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationB_InfoseekId',on_delete=models.CASCADE)

    EntryTime = models.TimeField()
    Blood_Pressure_Position = models.CharField(max_length=250 ,choices=Blood_Pressure_Position)
    Blood_Pressure_Type_of_Instrument = models.CharField(max_length=250 ,choices=Blood_Pressure_Instrument)
    Blood_Pressure_Systolic_BP = models.CharField(max_length=250)
    Blood_Pressure_Diastolic_BP = models.CharField(max_length=250)


    Respiration = models.CharField(max_length=250)
    Heart_Rate   = models.CharField(max_length=250)


    Temprature_Measurement_Site = models.CharField(max_length=250,choices=TempratureMeasurementSite) # Master Data (Aural, Armpit, Forehead, Oral,Anal)
    Temprature_Measurement_Instrument = models.CharField(max_length=250,choices=MeasurementInstrument) # Master Data (Digital, Analogue)
    Temprature = models.CharField(max_length=250)



    Oxygen_Saturation_SpO2    = models.CharField(max_length=250)
    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=250,choices=SRNYesorNo,null=True,blank=True)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
    Specialist_Referral_Needed_Flag =   models.CharField(max_length=25,choices=Referral_Needed_Flag,null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)
    Completed = models.CharField(max_length=50, choices=SRNYesorNo,default=None)
    Review_Status = models.CharField(max_length=100,choices=Review_Status_Enum,default='Not Reviewed')
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationB_Reviewedby_HcpId',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.DateTimeField(null=True,blank=True)
    Comments = models.TextField(null=True,blank=True)
    EndTime = models.TimeField(null=True,blank=True)


    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "StationB_Collection"




# class StationBModel_Log(models.Model):

#     StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationB_StationId_Log',on_delete=models.CASCADE)
#     HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationB_HCID_Log',on_delete=models.CASCADE)
#     HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationB_HcpId_Log',on_delete=models.CASCADE)
#     InfoseekId  = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationB_InfoseekId_Log',on_delete=models.CASCADE)

#     Blood_Pressure_Position = models.CharField(max_length=250)
#     Blood_Pressure_Type_of_Instrument = models.CharField(max_length=250)
#     Blood_Pressure_Systolic_BP = models.CharField(max_length=250)
#     Blood_Pressure_Diastolic_BP = models.CharField(max_length=250)

#     Respiration = models.CharField(max_length=250)
#     Heart_Rate   = models.CharField(max_length=250)

#     Temprature_Measurement_Site = models.CharField(max_length=250) # Master Data (Aural, Armpit, Forehead, Oral,Anal)
#     Temprature_Measurement_Instrument = models.CharField(max_length=250) # Master Data (Digital, Analogue)
#     Temprature = models.CharField(max_length=250)

#     Oxygen_Saturation_SpO2    = models.CharField(max_length=250)
#     Other_Observations = models.TextField(null=True,blank=True)
#     Specialist_Referral_Needed = models.CharField(max_length=250,null=True,blank=True)
#     Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
#     Specialist_Referral_Needed_Flag =   models.CharField(max_length=25,null=True,blank=True)
#     Other  = models.TextField(null=True,blank=True)
#     Review_Status = models.CharField(max_length=100)
#     Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationB_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
#     Reviewed_On = models.CharField(max_length=250)
#     Comments = models.TextField(null=True,blank=True)
#     Logs_Time = models.DateTimeField(auto_now=True)
#     objects = models.Manager

#     class Meta:
#         db_table = "StationB_logs"