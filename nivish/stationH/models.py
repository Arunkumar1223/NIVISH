from django.db import models
# Create your models here.

from Enum.enumstation_h import *
from Enum.enum import *
from datetime import datetime




class StationHModel(models.Model):

    ## Section-1 
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationH_StationId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationH_HCID',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationH_HcpId',on_delete=models.CASCADE)
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationH_InfoseekId',on_delete=models.CASCADE)
    
    EntryTime = models.TimeField()
    
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

    Oral_Hygiene = models.CharField(max_length=50,choices=OralHygiene) ## Master Data (Satisfactory, Poor)
    Plaque = models.CharField(max_length=250,choices=SRNYesorNo)
    Dental_Stains = models.CharField(max_length=250,choices=SRNYesorNo)
    Malocclusion  = models.CharField(max_length=250,choices=SRNYesorNo)
    Crowding  = models.CharField(max_length=250,choices=SRNYesorNo)
    Impacted_Tooth  = models.CharField(max_length=250,choices=SRNYesorNo)
    Impacted_Tooth_Yes = models.CharField(max_length=1000, choices=Impacted_Tooth_Yes_Enum)
    Impacted_Tooth_Yes_Position = models.TextField(null=True, blank=True)

    
    Worn_Enamel   = models.CharField(max_length=250,choices=SRNYesorNo)

    ## Section-3 

    Sensitivity = models.CharField(max_length=250,choices=SRNYesorNo)
    Untreated_Caries = models.CharField(max_length=250,choices=SRNYesorNo)
    Caries_Experience = models.CharField(max_length=250,choices=SRNYesorNo)
    Dental_Sealants_Present  = models.CharField(max_length=250,choices=SRNYesorNo)
    
    Braces = models.CharField(max_length=250,choices=SRNYesorNo,null=True,blank=True)
    Braces_Yes = models.CharField(max_length=50,null=True,blank=True) ## Master Data(Multiple Select) (Upper Teeth, Lower Teeth)

    Bridges = models.CharField(max_length=250,choices=SRNYesorNo,null=True,blank=True)
    Bridges_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Upper Teeth, Lower Teeth)

    Dentures = models.CharField(max_length=250,choices=SRNYesorNo,null=True,blank=True)
    Dentures_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Upper Jaw, Lower Jaw)

    ## Section-4

    Soft_Tissue_Pathology = models.CharField(max_length=1000,choices=SRNYesorNo,null=True,blank=True)
    Soft_Tissue_Pathology_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Mutliple Select) (Gingivitis, Ulcer, Abscess, Vesicle, Growth, Bleeding Gum, Discoloration, Receding Gums, Other)
    Soft_Tissue_Pathology_Yes_Other = models.TextField(null=True, blank=True)

    Treatment_Needed = models.CharField(max_length=250,choices=SRNYesorNo,null=True,blank=True)
    Treatment_Needed_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Mutliple Select) (Urgent Treatment, Preventive Care, Restorative Care, Other)
    Treatment_Needed_Yes_Other = models.TextField(null=True, blank=True)

    Dental_Florosis  = models.CharField(max_length=250 ,choices=SRNYesorNo)

    ## Section-5 

    Other_Observations = models.TextField(null=True,blank=True)
    StationH_Dental_SR_Needed = models.CharField(max_length=250,choices=SRNYesorNo)
    StationH_Dental_SR_Needed_Yes_Type = models.CharField(max_length=100000,choices=DentalSpecialistReferralNeededType,  null=True,blank=True ) ## Master Data (Pediatric Dentist,Endodontist,Oral and Maxillofacial,Surgeon,Orthodontist,Periodontist,Prosthodontist)
    StationH_Dental_SR_Needed_Yes_Flag =  models.CharField(max_length=250, choices=DentalSpecialistReferralNeededFlag,  null=True,blank=True) ## Master Data (Non Urgent, Urgent, Emergency)

    ## Section-6

    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=250,choices=SRNYesorNo)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
    Specialist_Referral_Needed_Flag =   models.CharField(max_length=250 ,choices=AdditionalSpecialistReferalNeededFlag,  null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)
    Completed = models.CharField(max_length=50, choices=SRNYesorNo,default='No')

    Review_Status = models.CharField(max_length=100,choices=Review_Status_Enum,default='Not Reviewed')
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationH_Reviewedby_HcpId',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.DateTimeField(null=True,blank=True)
    Comments = models.TextField(null=True,blank=True)
    EndTime = models.TimeField(null=True,blank=True)
    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "StationH_Collection"






# class StationHModel_Log(models.Model):

#     ## Section-1 
#     StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationH_StationId_Log',on_delete=models.CASCADE)
#     HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationH_HCID_Log',on_delete=models.CASCADE)
#     HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationH_HcpId_Log',on_delete=models.CASCADE)
#     InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationH_InfoseekId_Log',on_delete=models.CASCADE)
    
    
#     Upper_Permanent = models.CharField(max_length=1000, null=True, blank=True)  ## Master data(Multiple Select) (Decayed,Missing,Filled,Prosthesis)
#     Upper_Permanent_Decayed = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select)

#     Upper_Permanent_Missing = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select)((1 to 16)
#     Upper_Permanent_Filled = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (1 to 16)
#     Upper_Permanent_Prosthesis = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (1 to 16)
#     Upper_Permanent_Restoration_done = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (1 to 16)

#     Upper_Deciduous =models.CharField(max_length=1000, null=True, blank=True)  ## Master data(Multiple Select)(Decayed,Missing,Filled,Prosthesis,Restoration done )
#     Upper_Deciduous_Decayed = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (A to J)
#     Upper_Deciduous_Missing = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (A to J)
#     Upper_Deciduous_Filled = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (A to J)
#     Upper_Deciduous_Prosthesis = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (A to J)
#     Upper_Deciduous_Restoration_done = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (A to J)

#     Lower_Deciduous = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)(Decayed,Missing,Filled,Prosthesis,Restoration done )
#     Lower_Deciduous_Decayed = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)
#     Lower_Deciduous_Missing = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)
#     Lower_Deciduous_Filled = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)
#     Lower_Deciduous_Prosthesis = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)
#     Lower_Deciduous_Restoration_done = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (T to K)

#     Lower_Permanent = models.CharField(max_length=1000, null=True, blank=True)## Master data(Multiple Select) (T to K)(Decayed,Missing,Filled,Prosthesis,Restoration done )
#     Lower_Permanent_Decayed = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (32 to 17)
#     Lower_Permanent_Missing = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (32 to 17)
#     Lower_Permanent_Filled = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (32 to 17)
#     Lower_Permanent_Prosthesis = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (32 to 17)
#     Lower_Permanent_Restoration_done = models.CharField(max_length=1000, null=True, blank=True) ## Master data(Multiple Select) (32 to 17)

#     ## Section-2

#     Oral_Hygiene = models.CharField(max_length=50) ## Master Data (Satisfactory, Poor)
#     Plaque = models.CharField(max_length=250)
#     Dental_Stains = models.CharField(max_length=250)
#     Malocclusion  = models.CharField(max_length=250)
#     Crowding  = models.CharField(max_length=250)
#     Impacted_Tooth  = models.CharField(max_length=250)
#     Impacted_Tooth_Yes = models.CharField(max_length=1000)
#     Impacted_Tooth_Yes_Position = models.TextField(null=True, blank=True)

    
#     Worn_Enamel   = models.CharField(max_length=250)

#     ## Section-3 

#     Sensitivity = models.CharField(max_length=250)
#     Untreated_Caries = models.CharField(max_length=250)
#     Caries_Experience = models.CharField(max_length=250)
#     Dental_Sealants_Present  = models.CharField(max_length=250)
    
#     Braces = models.CharField(max_length=250,null=True,blank=True)
#     Braces_Yes = models.CharField(max_length=50,null=True,blank=True) ## Master Data(Multiple Select) (Upper Teeth, Lower Teeth)

#     Bridges = models.CharField(max_length=250,null=True,blank=True)
#     Bridges_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Upper Teeth, Lower Teeth)

#     Dentures = models.CharField(max_length=250,null=True,blank=True)
#     Dentures_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Upper Jaw, Lower Jaw)

#     ## Section-4

#     Soft_Tissue_Pathology = models.CharField(max_length=1000,null=True,blank=True)
#     Soft_Tissue_Pathology_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Mutliple Select) (Gingivitis, Ulcer, Abscess, Vesicle, Growth, Bleeding Gum, Discoloration, Receding Gums, Other)
#     Soft_Tissue_Pathology_Yes_Other = models.TextField(null=True, blank=True)

#     Treatment_Needed = models.CharField(max_length=250,null=True,blank=True)
#     Treatment_Needed_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Mutliple Select) (Urgent Treatment, Preventive Care, Restorative Care, Other)
#     Treatment_Needed_Yes_Other = models.TextField(null=True, blank=True)

#     Dental_Florosis  = models.CharField(max_length=250)

#     ## Section-5 

#     Other_Observations = models.TextField(null=True,blank=True)
#     StationH_Dental_SR_Needed = models.CharField(max_length=250)
#     StationH_Dental_SR_Needed_Yes_Type = models.CharField(max_length=100000,  null=True,blank=True ) ## Master Data (Pediatric Dentist,Endodontist,Oral and Maxillofacial,Surgeon,Orthodontist,Periodontist,Prosthodontist)
#     StationH_Dental_SR_Needed_Yes_Flag =  models.CharField(max_length=250,  null=True,blank=True) ## Master Data (Non Urgent, Urgent, Emergency)

#     ## Section-6

#     Other_Observations = models.TextField(null=True,blank=True)
#     Specialist_Referral_Needed = models.CharField(max_length=250)
#     Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
#     Specialist_Referral_Needed_Flag =   models.CharField(max_length=250,  null=True,blank=True)
#     Other  = models.TextField(null=True,blank=True)    

#     Review_Status = models.CharField(max_length=100)
#     Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationH_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
#     Reviewed_On = models.CharField(max_length=250)
#     Comments = models.TextField(null=True,blank=True)
#     Logs_Time = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "StationH_logs"


    

    

