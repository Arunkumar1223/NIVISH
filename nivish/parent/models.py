from django.db import models
from datetime import datetime

class BmiModel(models.Model):
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='BmiCalculation_InfoseekId',on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    calculated_bmi  = models.IntegerField()
    
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "BMI_Table"

class HealthInsuranceModel(models.Model):
    InfoseekId  = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='HealthInsurance_InfoseekId',on_delete=models.CASCADE)
    Health_insurance = models.CharField(max_length=100) 
    Policy = models.CharField(max_length=100)
    Date_of_Expiry = models.DateField()

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "Health_Insurance"


class ParentOtpModel(models.Model):
    MobileNumber = models.CharField(max_length=50)
    Otp = models.CharField(max_length=10)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager
    
    class Meta:
        db_table = 'Parent_OTP'

class BPModel(models.Model):
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='BP_InfoseekId',on_delete=models.CASCADE)
    SystolicBP = models.CharField(max_length=100)
    DiastolicBP = models.CharField(max_length=100)

    objects = models.Manager

    class Meta:
        db_table = "BP_table"
    

class AbdominalModel(models.Model):
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='Abdominal_InfoseekId',on_delete=models.CASCADE)
    Abdominal_Girth = models.CharField(max_length=100)

    objects = models.Manager()

    class Meta:
        db_table = "AbdominalTable"


class ChestModel(models.Model):
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='Chest_InfoseekId',on_delete=models.CASCADE)
    Chest_Circumference = models.CharField(max_length=100)

    objects = models.Manager()

    class Meta:
        db_table = "ChestTable"
