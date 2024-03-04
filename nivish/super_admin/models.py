from django.db import models
from datetime import datetime

class SuperAdminModel(models.Model):
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=10)
    MobileNumber = models.CharField(max_length=100)
    Email = models.EmailField()

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta: 
        db_table = 'Super_Admin'


class HealthCampTeamsModel(models.Model):
    TeamName = models.CharField(max_length=100)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta: 
        db_table = 'HealthCamp_Teams'




class HealthCampModel(models.Model):
    HCID = models.IntegerField(primary_key=True)
    SA_ID = models.ForeignKey('SuperAdminModel',related_name='said_Super_adminmodel',on_delete=models.CASCADE)
    Place = models.CharField(max_length=100)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Health_Assessment_Name = models.CharField(max_length=100,null=True,blank=True)
    Created_By = models.CharField(max_length=100,null=True,blank=True)
    Updated_By = models.CharField(max_length=100,null=True,blank=True)
    Number_of_Participant = models.IntegerField()


    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager
    def save(self, *args, **kwargs):
            if not self.pk:
                latest_HCID = HealthCampModel.objects.order_by('-HCID').first()
                if latest_HCID:
                    self.HCID = latest_HCID.HCID + 1
                else:
                    self.HCID = 1
            return super().save(*args, **kwargs)

    class Meta: 
        db_table = 'HealthCamp_Collection'

class StationNamesModel(models.Model):
    Station_Names = models.CharField(max_length=100)

    class Meta:
        db_table = 'Stations_Master'

class MailModel(models.Model):
    Email = models.EmailField()





class HealthCampScheduleModel(models.Model):
    HcID = models.ForeignKey(HealthCampModel,on_delete = models.CASCADE, related_name = 'HC_ScheduleId')
    Date = models.DateField()
    Scheduled_Start_Time = models.DateTimeField()                       #  From Super Admin
    Scheduled_End_Time = models.DateTimeField()                         #  From Super Admin
    Actual_Start_Time = models.DateTimeField(null=True,blank=True)      # update from  Camp Admin
    Actual_End_Time = models.DateTimeField(null=True,blank=True)        # update from  Camp Admin

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager
    
    class Meta:
        db_table = 'Camp_Schedule'

