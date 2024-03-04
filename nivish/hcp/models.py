import random
from infoseek.models import CountryMasterModel
from django.db import models
from datetime import datetime
# Create your models here.
from django.utils import timezone
from Enum.enumInfoseek import *
from Enum.enumhcp import *
from Enum.enum import *

class HcpMasteModel(models.Model):
    FullName = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10, choices=Gender_ENUM)
    Date_of_Birth = models.DateField()
    MobileNumber = models.CharField(max_length=100)
    Email = models.EmailField()
    Type = models.CharField(max_length=20,choices=Type_ENUM)
    Tag = models.BooleanField(default=None,null=True,blank=True)

    CreatedOn = models.DateTimeField(default=timezone.now)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta: 
        db_table = 'HCP_Master'

class HcpRegistrationModel(models.Model):
    HCPID = models.IntegerField(primary_key=True)
    ProviderID = models.ForeignKey('ProviderRegistrationModel',related_name='Hcp_provider',on_delete=models.CASCADE,null=True,blank=True)
    FullName = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    Date_of_Birth = models.DateField()
    Registered_Email = models.EmailField(unique=True)
    Registered_MobileNumber = models.CharField(max_length=100,null=True, blank=True)
    Type = models.CharField(max_length=20,choices=Type_ENUM)
    Password = models.CharField(max_length=20)

    Terms_and_conditions = models.BooleanField(default=None)
    Version = models.CharField(max_length=100,null=True,blank=True)
    Date = models.DateField()
    Upload_Your_Photo = models.ImageField(upload_to='HCP',null=True, blank=True,max_length=100000)
    NIV =  models.CharField(max_length=100,null=True,blank=True)
    Hcp_qrcode = models.ImageField(upload_to='HCP_qrcodes',null=True, blank=True,max_length=100000)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.NIV:
            self.NIV = str(random.randint(1, 99999999999))
        super(HcpRegistrationModel, self).save(*args, **kwargs)

    objects = models.Manager
    
    def save(self, *args, **kwargs):
            if not self.pk:
                latest_HCPID = HcpRegistrationModel.objects.order_by('-HCPID').first()
                if latest_HCPID:
                    self.HCPID = latest_HCPID.HCPID + 1
                else:
                    self.HCPID = 1
            return super().save(*args, **kwargs)

    class Meta: 
        db_table = 'HCP_Registration'



class ProviderRegistrationModel(models.Model):
    ProviderID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=100,null=True,blank=True)
    Date_of_Birth = models.DateField(null=True,blank=True)
    Email = models.EmailField()
    MobileNumber = models.CharField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=20)
    
    Terms_and_conditions = models.BooleanField(default=None)
    Version = models.CharField(max_length=100,null=True,blank=True)
    Date = models.DateField()
    
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager
    def save(self, *args, **kwargs):
            if not self.pk:
                latest_ProviderID = ProviderRegistrationModel.objects.order_by('-ProviderID').first()
                if latest_ProviderID:
                    self.ProviderID = latest_ProviderID.ProviderID + 1
                else:
                    self.ProviderID = 1
            return super().save(*args, **kwargs)

    class Meta: 
        db_table = 'Provider'


class HcpEducationModel(models.Model):
    HCPID = models.ForeignKey('HcpRegistrationModel',related_name='Personal_Info_HcpId',on_delete=models.CASCADE)
    ProviderID = models.ForeignKey('ProviderRegistrationModel',related_name='Provider_Hcp_Info',on_delete=models.CASCADE,null=True,blank=True)
    Name_of_institute = models.CharField(max_length=100)
    Type_of_degree = models.CharField(max_length=100)
    Filed_of_study = models.CharField(max_length=100)
    Country =  models.CharField(max_length=100)
    from_Date = models.CharField(max_length=50)
    to_Date = models.CharField(max_length=50)
    Upload_certificate = models.FileField(upload_to='HCP_education',null=True, blank=True,max_length=100000)
    
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta: 
        db_table = 'Hcp_Education_Info'



class Hcp_License_Details_Model(models.Model):
    HCPID = models.ForeignKey('HcpRegistrationModel',related_name='Professional_Info_HcpId',on_delete=models.CASCADE)
    ProviderID = models.ForeignKey('ProviderRegistrationModel',related_name='Professional_Info_provider',on_delete=models.CASCADE,null=True,blank=True)
    Category = models.CharField(max_length=100, choices=Category_ENUM) #enums (Nurse,Doctor,Physiotherapist,Optometrist,Dentist,If other)
    Category_Others = models.CharField(max_length=100,null=True, blank=True)
    License_Authority = models.CharField(max_length=100 , choices=License_Authority_ENUM) #enum (DHA,DOH,MOH,If other)
    License_Authority_others = models.CharField(max_length=100,null=True, blank=True)
    License_Number = models.CharField(max_length=30)
    Country = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Issued_Date = models.CharField(max_length=50)
    Validate_till = models.CharField(max_length=50,null=True, blank=True)
    Life_long_till = models.CharField(max_length=100,null=True, blank=True)
    Upload_certificate = models.FileField(upload_to='HCP_license',null=True, blank=True,max_length=100000)
    
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta: 
        db_table = 'Hcp_License_Details'



        

class HcpOtpModel(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Date_of_Birth = models.DateField(null=True,blank=True)
    Email = models.EmailField()
    MobileNumber = models.CharField(max_length=100,null=True,blank=True)
    Otp = models.CharField(max_length=10)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager
    
    class Meta:
        db_table = 'hcp_OTP'
        
class ProviderOtpModel(models.Model):
    # Registered_Email = models.EmailField()
    Email = models.EmailField()
    Otp = models.CharField(max_length=10)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager
    class Meta:
        db_table = 'provider_OTP'

class AssignmentModel(models.Model):
    TeamId = models.ForeignKey('super_admin.HealthCampTeamsModel',related_name='HealthCampTeamsModel',on_delete=models.CASCADE,null=True,blank=True)
    HCPID = models.ForeignKey('HcpRegistrationModel',related_name='HcpModel_HcpId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='HcpModel_HCID',on_delete=models.CASCADE)
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='HcpModel_StationId',on_delete=models.CASCADE)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager
    class Meta:
        db_table = 'Assignment'


class ExperienceModel(models.Model):
    HCPID = models.OneToOneField('HcpRegistrationModel',related_name='LicenseExperience_HcpId',on_delete=models.CASCADE)
    ProviderID = models.ForeignKey('ProviderRegistrationModel',related_name='LicenseExperience_Provider',on_delete=models.CASCADE,null=True,blank=True)
    Total_Experience_Years = models.IntegerField(null=True,blank=True)
    Total_Experience_Months = models.IntegerField(null=True,blank=True)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager
    class Meta:
        db_table = 'Hcp_Experience'

class NoteModel(models.Model):
    HCPID = models.ForeignKey('HcpRegistrationModel',related_name='Note_HcpId',on_delete=models.CASCADE)
    ProviderID = models.ForeignKey('ProviderRegistrationModel',related_name='Note_Provider',on_delete=models.CASCADE,null=True,blank=True)
    Full_Name = models.CharField(max_length=100,null=True,blank=True)
    Signature =  models.CharField(max_length=100,null=True,blank=True)
    Upload_Your_Sign = models.ImageField(upload_to='HCP',null=True, blank=True,max_length=100000)
    
    Submitted_date = models.CharField(max_length=100,null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    Accepted = models.BooleanField()
    

    # Hcp_qrcode = models.ImageField(upload_to='HCP_qrcodes',null=True, blank=True,max_length=100000)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)

    

    objects = models.Manager
    class Meta:
        db_table = 'Hcp_Note'

class HcpFileUploadModel(models.Model):
    file = models.FileField()



class RegistrationDeskModel(models.Model):
    RegisteredBy = models.ForeignKey('HcpRegistrationModel',related_name='RegistrationDesk_HcpId',on_delete=models.CASCADE)
    ExitedBy = models.ForeignKey('HcpRegistrationModel',related_name='Exitedby_HcpId',on_delete=models.CASCADE,null=True,blank=True)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='RegistrationDesk_HCID',on_delete=models.CASCADE)
    UIN = models.CharField(max_length=50)
    RegisteredStatus = models.CharField(max_length=100,choices=SRNYesorNo)
    # View_reports = models.CharField(max_length=100,choices=SRNYesorNo)
    ExitStatus = models.CharField(max_length=100, choices=SRNYesorNo,null=True,blank=True)
    RegistrationTime = models.DateTimeField()
    ExitTime = models.CharField(null=True, blank=True, max_length=1000, default=None)
    RegistrationEntryTime = models.CharField(null=True, blank=True, max_length=100, default=None)
    ExitEntryTime = models.CharField(null=True, blank=True, max_length=100, default=None)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = 'Registration_Desk'

        

