from django.db import models
from datetime import datetime
from Enum.enumstation_c import *
from Enum.enum import *
# Create your models here.



class StationCModel(models.Model):
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationC_StationId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationC_HCID',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationC_HcpId',on_delete=models.CASCADE)
    InfoseekId  = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationC_InfoseekId',on_delete=models.CASCADE)

    EntryTime = models.TimeField()
    Problem_reading_books = models.CharField(max_length=50, choices=SRNYesorNo,null=True,blank=True)
    Problem_reading_Blackboard = models.CharField(max_length=50, choices=SRNYesorNo,null=True,blank=True)
    Night_Vision  = models.CharField(max_length=50, choices=NormalandAbnormal,null=True,blank=True)
    Vision_Corrected  = models.CharField(max_length=50, choices=SRNYesorNo,null=True,blank=True)
    Vision_Corrected_Yes = models.CharField(max_length=100,null=True,blank=True)   # master data  (Glasses, Lenses, Surgical)

    Extra_Ocular_Right_Normal_Eye_Movement = models.CharField(max_length=50, choices=SRNYesorNo)
    Extra_Ocular_Right_Strabismus =models.CharField(max_length=50, choices=SRNYesorNo)
    Extra_Ocular_Right_Drooping_Lid =models.CharField(max_length=50, choices=SRNYesorNo)
    Extra_Ocular_Right_Restricted_Mobility = models.CharField(max_length=50, choices=SRNYesorNo)
    Extra_Ocular_Right_Nystagmus = models.CharField(max_length=50, choices=SRNYesorNo)
    Extra_Ocular_Right_Bulging = models.CharField(max_length=50, choices=SRNYesorNo)


    Extra_Ocular_Left_Normal_Eye_Movement = models.CharField(max_length=50, choices=SRNYesorNo)
    Extra_Ocular_Left_Strabismus = models.CharField(max_length=50, choices=SRNYesorNo)
    Extra_Ocular_Left_Drooping_Lid = models.CharField(max_length=50, choices=SRNYesorNo)
    Extra_Ocular_Left_Restricted_Mobility =models.CharField(max_length=50, choices=SRNYesorNo)
    Extra_Ocular_Left_Nystagmus =models.CharField(max_length=50, choices=SRNYesorNo)
    Extra_Ocular_Left_Bulging =models.CharField(max_length=50, choices=SRNYesorNo)



    Visually_Challenged_Right_Eye  = models.CharField(max_length=1000, choices=SRNYesorNo,default=None,null=True, blank=True)
    Visually_Challenged_Right_Eye_Enucleation  =models.CharField(max_length=50, choices=SRNYesorNo,null=True, blank=True)
    Visually_Challenged_Right_Eye_Enucleation_When_removed  = models.CharField(max_length=1000,null=True, blank=True,default=None)
    Visually_Challenged_Right_Eye_Enucleation_Why_removed  = models.CharField(max_length=1000,null=True, blank=True) ## master data  Tumor, Injury, Accident, Other     (Text Box )
    Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other  = models.CharField(max_length=50,null=True, blank=True) 
    VC_Right_Eye_Enucleation_Artificial_Eye_Used   = models.CharField(max_length=1000, choices=SRNYesorNo,null=True, blank=True)
    Visually_Challenged_Right_Eye_Enucleation_No = models.CharField (max_length=1000,null=True, blank=True)   ## master data    'Cataract','Corneal opacity','Glaucoma','Phthisis bulbi'
    Visually_Challenged_Right_Eye_Enucleation_Cataract = models.CharField(max_length=50, choices=Eye_Enucleation,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity = models.CharField(max_length=50, choices=Eye_Enucleation,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Right_Eye_Enucleation_Glaucoma = models.CharField(max_length=50, choices=Eye_Enucleation,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi = models.CharField(max_length=50, choices=Eye_Enucleation,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  



    Visually_Challenged_Left_Eye  = models.CharField(max_length=1000, choices=SRNYesorNo,null=True, blank=True)
    Visually_Challenged_Left_Eye_Enucleation  =models.CharField(max_length=50, choices=SRNYesorNo,null=True,blank=True)
    Visually_Challenged_Left_Eye_Enucleation_When_removed  = models.CharField(max_length=1000,null=True,blank=True)
    Visually_Challenged_Left_Eye_Enucleation_Why_removed  = models.CharField(max_length=1000, null=True, blank=True) ## master data  Tumor, Injury, Accident, Other     (Text Box )
    Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other  = models.CharField(max_length=1000, null=True, blank=True) 
    VC_Left_Eye_Enucleation_Artificial_Eye_Used   = models.CharField(max_length=50, choices=SRNYesorNo, null=True, blank=True)
    Visually_Challenged_Left_Eye_Enucleation_No = models.CharField (max_length=50, null=True, blank=True)   ## master data    'Cataract','Corneal opacity','Glaucoma','Phthisis bulbi'
    Visually_Challenged_Left_Eye_Enucleation_Cataract = models.CharField(max_length=50, choices=Eye_Enucleation,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity = models.CharField(max_length=50, choices=Eye_Enucleation,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Left_Eye_Enucleation_Glaucoma = models.CharField(max_length=50, choices=Eye_Enucleation,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
    Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi = models.CharField(max_length=50, choices=Eye_Enucleation,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  


    Visual_Acuity = models.CharField(max_length=10000) # master data [ Chart Type (Drop Down), Snellen's Chart (Default), Logmar Chart)
   
    Visual_Acuity_With_Lenses_Distant_Vision_Left  = models.IntegerField() 
    Visual_Acuity_With_Lenses_Distant_Vision_Right  = models.IntegerField()
    Visual_Acuity_With_Lenses_Near_Vision_Left = models.IntegerField() 
    Visual_Acuity_With_Lenses_Near_Vision_Right = models.IntegerField() 


    Visual_Acuity_without_Lenses_Distant_Vision_Left  = models.IntegerField(null=True,blank=True) 
    Visual_Acuity_without_Lenses_Distant_Vision_Right  = models.IntegerField(null=True,blank=True)
    Visual_Acuity_without_Lenses_Near_Vision_Left = models.IntegerField(null=True,blank=True) 
    Visual_Acuity_without_Lenses_Near_Vision_Right = models.IntegerField(null=True,blank=True) 

    
    Visual_Acuity_Color_Blindness = models.CharField(max_length=50,choices=SRNYesorNo,null=True,blank=True)  #Master Data => No Colour Blindness (Default), Red-Green Partial, Blue-Green Partial, Total Colour Blindness 
    Visual_Acuity_Color_Blindness_Yes = models.CharField(max_length=100, choices=colorblindness, null=True,blank=True)
    
    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=250, choices=SRNYesorNo)
    Specialist_Referral_Needed_Type = models.CharField(max_length=1000,null=True,blank=True)
    Specialist_Referral_Needed_Flag = models.CharField(max_length=250, choices=Referral_Needed_Flag,  null=True,blank=True) 
    Other  = models.TextField(null=True,blank=True)
    Completed = models.CharField(max_length=50, choices=SRNYesorNo,default='No')
    Review_Status = models.CharField(max_length=100,choices=Review_Status_Enum,default='Not Reviewed')
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationC_Reviewedby_HcpId',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.DateTimeField(null=True,blank=True)
    Comments = models.TextField(null=True,blank=True)
    EndTime = models.TimeField(null=True,blank=True)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = "StationC_Collection"





# class StationCModel_Log(models.Model):
#     StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationC_StationId_Log',on_delete=models.CASCADE)
#     HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationC_HCID_Log',on_delete=models.CASCADE)
#     HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationC_HcpId_Log',on_delete=models.CASCADE)
#     InfoseekId  = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationC_InfoseekId_Log',on_delete=models.CASCADE)

#     Problem_reading_books = models.CharField(max_length=50,null=True,blank=True)
#     Problem_reading_Blackboard = models.CharField(max_length=50,null=True,blank=True)
#     Night_Vision  = models.CharField(max_length=50,null=True,blank=True)
#     Vision_Corrected  = models.CharField(max_length=50,null=True,blank=True)
#     Vision_Corrected_Yes = models.CharField(max_length=100,null=True,blank=True)   # master data  (Glasses, Lenses, Surgical)

#     Extra_Ocular_Right_Normal_Eye_Movement = models.CharField(max_length=50)
#     Extra_Ocular_Right_Strabismus =models.CharField(max_length=50)
#     Extra_Ocular_Right_Drooping_Lid =models.CharField(max_length=50)
#     Extra_Ocular_Right_Restricted_Mobility = models.CharField(max_length=50)
#     Extra_Ocular_Right_Nystagmus = models.CharField(max_length=50)
#     Extra_Ocular_Right_Bulging = models.CharField(max_length=50)


#     Extra_Ocular_Left_Normal_Eye_Movement = models.CharField(max_length=50)
#     Extra_Ocular_Left_Strabismus = models.CharField(max_length=50)
#     Extra_Ocular_Left_Drooping_Lid = models.CharField(max_length=50)
#     Extra_Ocular_Left_Restricted_Mobility =models.CharField(max_length=50)
#     Extra_Ocular_Left_Nystagmus =models.CharField(max_length=50)
#     Extra_Ocular_Left_Bulging =models.CharField(max_length=50)



#     Visually_Challenged_Right_Eye  = models.CharField(max_length=1000,default=None,null=True, blank=True)
#     Visually_Challenged_Right_Eye_Enucleation  =models.CharField(max_length=50,null=True, blank=True)
#     Visually_Challenged_Right_Eye_Enucleation_When_removed  = models.CharField(max_length=1000,null=True, blank=True,default=None)
#     Visually_Challenged_Right_Eye_Enucleation_Why_removed  = models.CharField(max_length=1000,null=True, blank=True) ## master data  Tumor, Injury, Accident, Other     (Text Box )
#     Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other  = models.CharField(max_length=50,null=True, blank=True) 
#     VC_Right_Eye_Enucleation_Artificial_Eye_Used   = models.CharField(max_length=1000, null=True, blank=True)
#     Visually_Challenged_Right_Eye_Enucleation_No = models.CharField (max_length=1000,null=True, blank=True)   ## master data    'Cataract','Corneal opacity','Glaucoma','Phthisis bulbi'
#     Visually_Challenged_Right_Eye_Enucleation_Cataract = models.CharField(max_length=50, null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
#     Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity = models.CharField(max_length=50, null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
#     Visually_Challenged_Right_Eye_Enucleation_Glaucoma = models.CharField(max_length=50,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
#     Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi = models.CharField(max_length=50,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  



#     Visually_Challenged_Left_Eye  = models.CharField(max_length=1000, null=True, blank=True)
#     Visually_Challenged_Left_Eye_Enucleation  =models.CharField(max_length=50, null=True,blank=True)
#     Visually_Challenged_Left_Eye_Enucleation_When_removed  = models.CharField(max_length=1000,null=True,blank=True)
#     Visually_Challenged_Left_Eye_Enucleation_Why_removed  = models.CharField(max_length=1000, null=True, blank=True) ## master data  Tumor, Injury, Accident, Other     (Text Box )
#     Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other  = models.CharField(max_length=1000, null=True, blank=True) 
#     VC_Left_Eye_Enucleation_Artificial_Eye_Used   = models.CharField(max_length=50,null=True, blank=True)
#     Visually_Challenged_Left_Eye_Enucleation_No = models.CharField (max_length=50, null=True, blank=True)   ## master data    'Cataract','Corneal opacity','Glaucoma','Phthisis bulbi'
#     Visually_Challenged_Left_Eye_Enucleation_Cataract = models.CharField(max_length=50, null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
#     Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity = models.CharField(max_length=50, null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
#     Visually_Challenged_Left_Eye_Enucleation_Glaucoma = models.CharField(max_length=50,null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  
#     Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi = models.CharField(max_length=50, null=True, blank=True)  ## master data    Counting Fingers (Default), Light Perception, Hand Motion, No Light Perception  


#     Visual_Acuity = models.CharField(max_length=10000) # master data [ Chart Type (Drop Down), Snellen's Chart (Default), Logmar Chart)
   
#     Visual_Acuity_With_Lenses_Distant_Vision_Left  = models.IntegerField() 
#     Visual_Acuity_With_Lenses_Distant_Vision_Right  = models.IntegerField()
#     Visual_Acuity_With_Lenses_Near_Vision_Left = models.IntegerField() 
#     Visual_Acuity_With_Lenses_Near_Vision_Right = models.IntegerField() 


#     Visual_Acuity_without_Lenses_Distant_Vision_Left  = models.IntegerField(null=True,blank=True) 
#     Visual_Acuity_without_Lenses_Distant_Vision_Right  = models.IntegerField(null=True,blank=True)
#     Visual_Acuity_without_Lenses_Near_Vision_Left = models.IntegerField(null=True,blank=True) 
#     Visual_Acuity_without_Lenses_Near_Vision_Right = models.IntegerField(null=True,blank=True) 

    
#     Visual_Acuity_Color_Blindness = models.CharField(max_length=50,null=True,blank=True)  #Master Data => No Colour Blindness (Default), Red-Green Partial, Blue-Green Partial, Total Colour Blindness 
#     Visual_Acuity_Color_Blindness_Yes = models.CharField(max_length=100,  null=True,blank=True)
    
#     Other_Observations = models.TextField(null=True,blank=True)
#     Specialist_Referral_Needed = models.CharField(max_length=250)
#     Specialist_Referral_Needed_Type = models.CharField(max_length=1000,null=True,blank=True)
#     Specialist_Referral_Needed_Flag = models.CharField(max_length=250,   null=True,blank=True) 
#     Other  = models.TextField(null=True,blank=True)
#     Review_Status = models.CharField(max_length=100)
#     Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationC_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
#     Reviewed_On = models.CharField(max_length=250)
#     Comments = models.TextField(null=True,blank=True)
#     Logs_Time = models.DateTimeField(auto_now=True)
#     objects = models.Manager


#     class Meta:
#         db_table = "StationC_logs"
