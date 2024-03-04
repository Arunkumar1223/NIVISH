from django.db import models

# Create your models here.

from Enum.enumstation_f import *
from Enum.enum import *
from datetime import datetime

class StationFModels(models.Model):
    StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationF_StationId',on_delete=models.CASCADE)
    HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationF_HCID',on_delete=models.CASCADE)
    HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationF_HcpId',on_delete=models.CASCADE)
    InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationF_InfoseekId',on_delete=models.CASCADE)

    EntryTime = models.TimeField()
    Skin_colour_Tone = models.CharField(max_length=1000, choices=NormalandAbnormal) 
    Skin_colour_Tone_Abnormal = models.CharField(max_length=50, choices=Skin_colour_Tone_Abnormal_ENUM, null=True, blank=True) 

    Skin_Texture_of_Skin = models.CharField(max_length=1000, choices=NormalandAbnormal) 
    Skin_Texture_of_Skin_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Dry, Crinkled, Scaly, Hemorrhages, Oily, Moist)
    
    skin_Rash = models.CharField(max_length=1000, choices=AbsentandPresent)
    skin_Rash_Present = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Face, Neck, Chest, Abdomen, Groin, Back, Arms, Hands, Legs, Feet)
    skin_Rash_Present_Face = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Neck = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Chest = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Abdomen = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Groin = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Back = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Arms = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Hands = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Legs = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    skin_Rash_Present_Feet = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    
    Other_Skin_lesions = models.CharField(max_length=1000, choices=SRNYesorNo)
    Other_Skin_lesions_Yes = models.CharField(max_length=1000, null=True, blank=True) # Mater Data(Multiple Select) (Finger web boils, Scabs, Ringworm, Leucoderma, Scratches, Birth marks)  
    Other_Skin_lesions_Yes_Other = models.CharField(max_length=100, null=True, blank=True)
    Other_Skin_lesions_Yes_Birth_marks = models.CharField(max_length=1000, null=True, blank=True) # Mater Data(Multiple Select) (Nevus, Café au lait, Other)  
    Other_Skin_lesions_Yes_Birth_marks_Other = models.TextField(max_length=100, null=True, blank=True) 


    skin_Acne = models.CharField(max_length=1000, choices=SRNYesorNo)
    skin_Acne_Yes = models.CharField(max_length=100, choices=skin_Acne_Yes_ENUM,null=True,blank=True)


    Nails_Color =  models.CharField(max_length=100, choices=Nails_Color_ENUM) 

    Nails_Shape = models.CharField(max_length=1000, choices=NormalandAbnormal) 
    Nails_Shape_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multi  Select) (Bitten, Clubbed, Spoon-shaped)

    Nails_Deformity = models.CharField(max_length=1000, choices=SRNYesorNo)
    Nails_Deformity_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multi  Select) (White Spots, Ridging, Brown lines / spots Irregular thickening)

    Nails_Cuticles = models.CharField(max_length=1000, choices=Nails_Cuticles_ENUM) 
    Nail_Bed_Infection = models.CharField(max_length=1000, choices=AbsentandPresent) 


    Head_Skull_Fontanelle = models.CharField(max_length=1000, choices=Head_Skull_Fontanelle_ENUM)
    Head_Skull_Fontanelle_Open = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Frontal Fontanella, Occipital Fontanella)
    Head_Skull_Fontanelle_Open_Fontanella = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Bulging, Sunken, Non-bulging / Flat, Enlarged / Wide)
    Head_Skull_Fontanelle_Open_Occipital = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Bulging, Sunken, Non-bulging / Flat, Enlarged / Wide)

    Head_Skull_Appearance_and_Size = models.CharField(max_length=1000, choices=HS_Appearance_and_Size_ENUM) 
    Head_Skull_Appearance_and_Size_Other = models.TextField(null=True, blank=True)

    Head_Hair_Appearance = models.CharField(max_length=50, choices=NormalandAbnormal) 
    Head_Hair_Appearance_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Greasy, Dry & Brittle, Other, Early greying)
    Head_Hair_Appearance_Abnormal_Other = models.TextField(null=True, blank=True)

    Head_Scalp = models.CharField(max_length=1000, choices=NormalandAbnormal) 
    Head_Scalp_Abnormal = models.CharField(max_length=10000, null=True, blank=True) ## Master Data(Multiple Select) (Dandruff, Edema, Ringworm, Ulcers, Hematoma, Folliculities, Swelling, Pustules, Sebaceous Cyst, Lipoma)

    Head_Parasites = models.CharField(max_length=50, choices=SRNYesorNo)
    Head_Parasites_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Adults, Nits, Other)
    Head_Parasites_Yes_Other = models.TextField(null=True, blank=True)
    
    Head_Hair_Loss = models.CharField(max_length=1000, choices=SRNYesorNo)
    Head_Hair_Loss_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Patchy, Generalized, Temporal, Crown, Frontal)

    Thyroid_Lymph_Thyroid_Gland = models.CharField(max_length=1000, choices=Thyroid_Lymph_Thyroid_Gland_ENUM,null=True,blank=True) 
    Thyroid_Lymph_Thyroid_Gland_Enlarged = models.CharField(max_length=1000, choices=Thyroid_Lymph_Gland_Enlarged_ENUM,null=True,blank=True) 

    Thyroid_Lymph_Cervical_LN = models.CharField(max_length=1000, choices=Thyroid_Gland_Lymph_ENUM) 
    Thyroid_Lymph_Cervical_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Submental,	Occipital, Submandibular R,	Submandibular L, Anterior Cervical R, Anterior Cervical L, Lateral Cervical R, Lateral Cervical L, Posterior Cervical R, Posterior Cervical L)

    Thyroid_Lymph_Supraclavicular_LN = models.CharField(max_length=1000, choices=Thyroid_Gland_Lymph_ENUM) 
    Thyroid_Lymph_Supraclavicular_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left)

    Thyroid_Lymph_Axillary_LN = models.CharField(max_length=1000, choices=Thyroid_Gland_Lymph_ENUM) 
    Thyroid_Lymph_Axillary_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left) 

    Thyroid_Lymph_Supratrochlear_LN = models.CharField(max_length=1000, choices=Thyroid_Gland_Lymph_ENUM) 
    Thyroid_Lymph_Supratrochlear_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left) 

    Thyroid_Lymph_Inguinal_LN = models.CharField(max_length=1000, choices=Thyroid_Gland_Lymph_ENUM)
    Thyroid_Lymph_Inguinal_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left)


    Eyes_Conjuctiva = models.CharField(max_length=50, choices=Eyes_Conjuctiva_ENUM) 

    Eyes_Sclera = models.CharField(max_length=50, choices=Eyes_Sclera_ENUM) 

    Eyes_Discharge = models.CharField(max_length=1000, choices=SRNYesorNo)
    Eyes_Discharge_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right Eye, Left Eye)
    Eyes_Discharge_Yes_Right_Eye = models.CharField(max_length=50, choices=Eyes_Discharge_ENUM,null=True, blank=True) 
    Eyes_Discharge_Yes_Left_Eye = models.CharField(max_length=50, choices=Eyes_Discharge_ENUM,null=True, blank=True) 

    Eyes_Eyelids = models.CharField(max_length=1000, choices=NormalandAbnormal) 
    Eyes_Eyelids_Abnormal = models.CharField(max_length=50, choices=Eyes_Eyelids_Abnormal_ENUM,null=True, blank=True) 

    Ears_Hearing = models.CharField(max_length=1000, choices=NormalandAbnormal) 
    Ears_Hearing_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Mulitiple Select) (Reduced, Tinnitus, Absent, Exaggerate, Other)
    Ears_Hearing_Abnormal_Reduced = models.CharField(max_length=50, choices=Ears_Hearing_Abnormal_Reduced_ENUM,null=True, blank=True) 
    Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid = models.CharField(max_length=50, choices=SRNYesorNo,null=True, blank=True)
    Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes = models.CharField(max_length=1000, null=True,blank=True) ## Master Data(Multiple Select) (Right, Left)
    Ears_Hearing_Abnormal_Reduced_Other = models.TextField(null=True, blank=True)


    Ears_Discharge = models.CharField(max_length=1000, choices=SRNYesorNo)
    Ears_Discharge_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right Ear, Left Ear)
    Ears_Discharge_Yes_Right_Ear = models.CharField(max_length=50, choices=Ears_Discharge_ENUM,null=True, blank=True) 
    Ears_Discharge_Yes_Left_Ear = models.CharField(max_length=50, choices=Ears_Discharge_ENUM,null=True, blank=True) 


    Ear_Wax = models.CharField(max_length=50, choices=Ear_Wax_ENUM) 
    Ear_Wax_Present = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left)


    Ear_Eardrum = models.CharField(max_length=1000, choices=Eardrum_ENUM) 
    Ear_Eardrum_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right Ear, Left Ear)
    Ear_Eardrum_Abnormal_Right_Ear = models.CharField(max_length=50, choices=Ear_Eardrum_Abnormal_RandL_Ear_ENUM,null=True, blank=True) 
    Ear_Eardrum_Abnormal_Left_Ear = models.CharField(max_length=50, choices=Ear_Eardrum_Abnormal_RandL_Ear_ENUM,null=True, blank=True) 


    Nose_Discharge = models.CharField(max_length=1000, choices=SRNYesorNo)
    Nose_Discharge_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right Nostril, Left Nostril)
    Nose_Discharge_Yes_Right_Nostril = models.CharField(max_length=50, choices=Nose_Discharge_Yes_RandL_Nostril_ENUM,null=True, blank=True) 
    Nose_Discharge_Yes_Left_Nostril = models.CharField(max_length=50, choices=Nose_Discharge_Yes_RandL_Nostril_ENUM,null=True, blank=True) 
    
    Nose_Dryness = models.CharField(max_length=1000, choices=SRNYesorNo)
    Nose_Dryness_Yes = models.CharField(max_length=50, choices=Nose_Yes_ENUM,null=True, blank=True) 

    Nose_Crusting = models.CharField(max_length=50, choices=SRNYesorNo)
    Nose_Crusting_Yes = models.CharField(max_length=50, choices=Nose_Yes_ENUM,null=True, blank=True) 

    Nose_Polyps = models.CharField(max_length=50, choices=SRNYesorNo)
    Nose_Polyps_Yes = models.CharField(max_length=50, choices=Nose_Yes_ENUM,null=True, blank=True) 

    Nose_Septum_Bridge = models.CharField(max_length=50, choices=Nose_Septum_Bridge_ENUM) 

    Nose_Sinuses = models.CharField(max_length=50, choices=Nose_Sinuses_ENUM) 

    Mouth_Throat_Mucosa = models.CharField(max_length=1000, choices=NormalandAbnormal) 
    Mouth_Throat_Mucosa_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Pale, Vesicles, Leukoplakia, Red, Ulcers, Others Cyanosed)
    Mouth_Throat_Mucosa_Abnormal_Other = models.TextField(null=True, blank=True)

    Mouth_Throat_Tongue = models.CharField(max_length=1000, choices=NormalandAbnormal) 
    Mouth_Throat_Tongue_Abnormal = models.CharField(max_length=10000, null=True, blank=True) ## Master Data(Multiple Select) (Pale, Protruded, Smooth/Bald, Red, Enlarged, Vesicles, Cyanosed, Purulent Lesions, Ulcers, Protruded, Leukoplakia, Other)
    Mouth_Throat_Tongue_Abnormal_Other = models.TextField(null=True, blank=True)


    Mouth_Tonsils = models.CharField(max_length=50, choices=NormalandAbnormal) 
    Mouth_Tonsils_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Enlarged, Purulent)

    Mouth_Uvula = models.CharField(max_length=50, choices=Mouth_Uvula_ENUM) 
    Mouth_Uvula_Abnormal = models.TextField(null=True, blank=True)

    Mouth_Palate = models.CharField(max_length=50, choices=Mouth_Palate_ENUM) 
    Mouth_Palate_Cleft_Palate = models.TextField(null=True, blank=True)
    Mouth_Palate_CleftLip_Palate = models.TextField(null=True, blank=True)
    Mouth_Palate_Other = models.TextField(null=True, blank=True)


    Hygiene_Nails = models.CharField(max_length=50, choices=Hygiene_ENUM) 

    Hygiene_Hair = models.CharField(max_length=50, choices=Hygiene_ENUM) 

    Hygiene_Skin = models.CharField(max_length=50, choices=Hygiene_ENUM)

    Hygiene_Odour = models.CharField(max_length=50, choices=Hygiene_Odour_ENUM) 

    
    Other_Observations = models.TextField(null=True,blank=True)
    Specialist_Referral_Needed = models.CharField(max_length=50, choices=SRNYesorNo)
    Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
    Specialist_Referral_Needed_Flag =   models.CharField(max_length=1000, choices=Referral_Needed_Flag,  null=True,blank=True)
    Other  = models.TextField(null=True,blank=True)
    Completed = models.CharField(max_length=50, choices=SRNYesorNo,default='No')
    Review_Status = models.CharField(max_length=100,choices=Review_Status_Enum,default='Not Reviewed')
    Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationF_Reviewedby_HcpId',on_delete=models.CASCADE,null=True,blank=True)
    Reviewed_On = models.DateTimeField(null=True,blank=True)
    Comments = models.TextField(null=True,blank=True)

    EndTime = models.TimeField(null=True,blank=True)

    CreatedOn = models.DateTimeField(default=datetime.today)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager


    class Meta:
         db_table = "StationF_Collection"


# class StationFModel_Log(models.Model):
#     StationID =models.ForeignKey('super_admin.StationNamesModel',related_name='StationF_StationId_Log',on_delete=models.CASCADE)
#     HCID = models.ForeignKey('super_admin.HealthCampModel',related_name='StationF_HCID_Log',on_delete=models.CASCADE)
#     HCPID = models.ForeignKey('hcp.HcpRegistrationModel',related_name='StationF_HcpId_Log',on_delete=models.CASCADE)
#     InfoseekId = models.ForeignKey('infoseek.InfoseekVerificationModel',related_name='StationF_InfoseekId_Log',on_delete=models.CASCADE)

    
#     Skin_colour_Tone = models.CharField(max_length=1000) 
#     Skin_colour_Tone_Abnormal = models.CharField(max_length=50, null=True, blank=True) 

#     Skin_Texture_of_Skin = models.CharField(max_length=1000) 
#     Skin_Texture_of_Skin_Abnormal = models.CharField(max_length=1000,null=True, blank=True) ## Master Data(Multiple Select) (Dry, Crinkled, Scaly, Hemorrhages, Oily, Moist)
    
#     skin_Rash = models.CharField(max_length=1000)
#     skin_Rash_Present = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Face, Neck, Chest, Abdomen, Groin, Back, Arms, Hands, Legs, Feet)
#     skin_Rash_Present_Face = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
#     skin_Rash_Present_Neck = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
#     skin_Rash_Present_Chest = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
#     skin_Rash_Present_Abdomen = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
#     skin_Rash_Present_Groin = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
#     skin_Rash_Present_Back = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
#     skin_Rash_Present_Arms = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
#     skin_Rash_Present_Hands = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
#     skin_Rash_Present_Legs = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
#     skin_Rash_Present_Feet = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Macular-Red Papular-Red, Pustular-intact, Macular-Pale,	Papular-Pale, Pustular-Broken)
    
#     Other_Skin_lesions = models.CharField(max_length=1000)
#     Other_Skin_lesions_Yes = models.CharField(max_length=1000, null=True, blank=True) # Mater Data(Multiple Select) (Finger web boils, Scabs, Ringworm, Leucoderma, Scratches, Birth marks)  
#     Other_Skin_lesions_Yes_Other = models.CharField(max_length=100, null=True, blank=True)
#     Other_Skin_lesions_Yes_Birth_marks = models.CharField(max_length=1000, null=True, blank=True) # Mater Data(Multiple Select) (Nevus, Café au lait, Other)  
#     Other_Skin_lesions_Yes_Birth_marks_Other = models.TextField(max_length=100, null=True, blank=True) 


#     skin_Acne = models.CharField(max_length=1000)
#     skin_Acne_Yes = models.CharField(max_length=100,null=True,blank=True)


#     Nails_Color =  models.CharField(max_length=100) 

#     Nails_Shape = models.CharField(max_length=1000) 
#     Nails_Shape_Abnormal = models.CharField(max_length=1000,null=True, blank=True) ## Master Data(Multi  Select) (Bitten, Clubbed, Spoon-shaped)

#     Nails_Deformity = models.CharField(max_length=1000)
#     Nails_Deformity_Yes = models.CharField(max_length=1000,null=True, blank=True) ## Master Data(Multi  Select) (White Spots, Ridging, Brown lines / spots Irregular thickening)

#     Nails_Cuticles = models.CharField(max_length=1000) 
#     Nail_Bed_Infection = models.CharField(max_length=1000) 


#     Head_Skull_Fontanelle = models.CharField(max_length=1000)
#     Head_Skull_Fontanelle_Open = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Frontal Fontanella, Occipital Fontanella)
#     Head_Skull_Fontanelle_Open_Fontanella = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Bulging, Sunken, Non-bulging / Flat, Enlarged / Wide)
#     Head_Skull_Fontanelle_Open_Occipital = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(MultiSelect) (Bulging, Sunken, Non-bulging / Flat, Enlarged / Wide)

#     Head_Skull_Appearance_and_Size = models.CharField(max_length=1000) 
#     Head_Skull_Appearance_and_Size_Other = models.TextField(null=True, blank=True)

#     Head_Hair_Appearance = models.CharField(max_length=50) 
#     Head_Hair_Appearance_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Greasy, Dry & Brittle, Other, Early greying)
#     Head_Hair_Appearance_Abnormal_Other = models.TextField(null=True, blank=True)

#     Head_Scalp = models.CharField(max_length=1000) 
#     Head_Scalp_Abnormal = models.CharField(max_length=10000, null=True, blank=True) ## Master Data(Multiple Select) (Dandruff, Edema, Ringworm, Ulcers, Hematoma, Folliculities, Swelling, Pustules, Sebaceous Cyst, Lipoma)

#     Head_Parasites = models.CharField(max_length=50)
#     Head_Parasites_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Adults, Nits, Other)
#     Head_Parasites_Yes_Other = models.TextField(null=True, blank=True)
    
#     Head_Hair_Loss = models.CharField(max_length=1000)
#     Head_Hair_Loss_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Patchy, Generalized, Temporal, Crown, Frontal)

#     Thyroid_Lymph_Thyroid_Gland = models.CharField(max_length=1000,null=True,blank=True) 
#     Thyroid_Lymph_Thyroid_Gland_Enlarged = models.CharField(max_length=1000, null=True,blank=True) 

#     Thyroid_Lymph_Cervical_LN = models.CharField(max_length=1000) 
#     Thyroid_Lymph_Cervical_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Submental,	Occipital, Submandibular R,	Submandibular L, Anterior Cervical R, Anterior Cervical L, Lateral Cervical R, Lateral Cervical L, Posterior Cervical R, Posterior Cervical L)

#     Thyroid_Lymph_Supraclavicular_LN = models.CharField(max_length=1000) 
#     Thyroid_Lymph_Supraclavicular_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left)

#     Thyroid_Lymph_Axillary_LN = models.CharField(max_length=1000) 
#     Thyroid_Lymph_Axillary_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left) 

#     Thyroid_Lymph_Supratrochlear_LN = models.CharField(max_length=1000) 
#     Thyroid_Lymph_Supratrochlear_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left) 

#     Thyroid_Lymph_Inguinal_LN = models.CharField(max_length=1000)
#     Thyroid_Lymph_Inguinal_LN_Palpable = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left)


#     Eyes_Conjuctiva = models.CharField(max_length=50) 

#     Eyes_Sclera = models.CharField(max_length=50) 

#     Eyes_Discharge = models.CharField(max_length=1000)
#     Eyes_Discharge_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right Eye, Left Eye)
#     Eyes_Discharge_Yes_Right_Eye = models.CharField(max_length=50,null=True, blank=True) 
#     Eyes_Discharge_Yes_Left_Eye = models.CharField(max_length=50,null=True, blank=True) 

#     Eyes_Eyelids = models.CharField(max_length=1000) 
#     Eyes_Eyelids_Abnormal = models.CharField(max_length=50,null=True, blank=True) 

#     Ears_Hearing = models.CharField(max_length=1000) 
#     Ears_Hearing_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Mulitiple Select) (Reduced, Tinnitus, Absent, Exaggerate, Other)
#     Ears_Hearing_Abnormal_Reduced = models.CharField(max_length=50,null=True, blank=True) 
#     Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid = models.CharField(max_length=50,null=True, blank=True)
#     Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes = models.CharField(max_length=1000, null=True,blank=True) ## Master Data(Multiple Select) (Right, Left)
#     Ears_Hearing_Abnormal_Reduced_Other = models.TextField(null=True, blank=True)


#     Ears_Discharge = models.CharField(max_length=1000)
#     Ears_Discharge_Yes = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right Ear, Left Ear)
#     Ears_Discharge_Yes_Right_Ear = models.CharField(max_length=50,null=True, blank=True) 
#     Ears_Discharge_Yes_Left_Ear = models.CharField(max_length=50,null=True, blank=True) 


#     Ear_Wax = models.CharField(max_length=50) 
#     Ear_Wax_Present = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right, Left)


#     Ear_Eardrum = models.CharField(max_length=1000) 
#     Ear_Eardrum_Abnormal = models.CharField(max_length=50, null=True, blank=True) ## Master Data(Multiple Select) (Right Ear, Left Ear)
#     Ear_Eardrum_Abnormal_Right_Ear = models.CharField(max_length=50,null=True, blank=True) 
#     Ear_Eardrum_Abnormal_Left_Ear = models.CharField(max_length=50,null=True, blank=True) 


#     Nose_Discharge = models.CharField(max_length=1000)
#     Nose_Discharge_Yes = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Right Nostril, Left Nostril)
#     Nose_Discharge_Yes_Right_Nostril = models.CharField(max_length=50,null=True, blank=True) 
#     Nose_Discharge_Yes_Left_Nostril = models.CharField(max_length=50,null=True, blank=True) 
    
#     Nose_Dryness = models.CharField(max_length=1000)
#     Nose_Dryness_Yes = models.CharField(max_length=50, null=True, blank=True) 

#     Nose_Crusting = models.CharField(max_length=50)
#     Nose_Crusting_Yes = models.CharField(max_length=50, null=True, blank=True) 

#     Nose_Polyps = models.CharField(max_length=50)
#     Nose_Polyps_Yes = models.CharField(max_length=50,null=True, blank=True) 

#     Nose_Septum_Bridge = models.CharField(max_length=50) 

#     Nose_Sinuses = models.CharField(max_length=50) 

#     Mouth_Throat_Mucosa = models.CharField(max_length=1000) 
#     Mouth_Throat_Mucosa_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Pale, Vesicles, Leukoplakia, Red, Ulcers, Others Cyanosed)
#     Mouth_Throat_Mucosa_Abnormal_Other = models.TextField(null=True, blank=True)

#     Mouth_Throat_Tongue = models.CharField(max_length=1000) 
#     Mouth_Throat_Tongue_Abnormal = models.CharField(max_length=10000, null=True, blank=True) ## Master Data(Multiple Select) (Pale, Protruded, Smooth/Bald, Red, Enlarged, Vesicles, Cyanosed, Purulent Lesions, Ulcers, Protruded, Leukoplakia, Other)
#     Mouth_Throat_Tongue_Abnormal_Other = models.TextField(null=True, blank=True)


#     Mouth_Tonsils = models.CharField(max_length=50) 
#     Mouth_Tonsils_Abnormal = models.CharField(max_length=1000, null=True, blank=True) ## Master Data(Multiple Select) (Enlarged, Purulent)

#     Mouth_Uvula = models.CharField(max_length=50) 
#     Mouth_Uvula_Abnormal = models.TextField(null=True, blank=True)

#     Mouth_Palate = models.CharField(max_length=50) 
#     Mouth_Palate_Cleft_Palate = models.TextField(null=True, blank=True)
#     Mouth_Palate_CleftLip_Palate = models.TextField(null=True, blank=True)
#     Mouth_Palate_Other = models.TextField(null=True, blank=True)


#     Hygiene_Nails = models.CharField(max_length=50) 

#     Hygiene_Hair = models.CharField(max_length=50) 

#     Hygiene_Skin = models.CharField(max_length=50)

#     Hygiene_Odour = models.CharField(max_length=50) 

    
#     Other_Observations = models.TextField(null=True,blank=True)
#     Specialist_Referral_Needed = models.CharField(max_length=50)
#     Specialist_Referral_Needed_Type = models.CharField(max_length=100000,null=True,blank=True)
#     Specialist_Referral_Needed_Flag =   models.CharField(max_length=1000 , null=True,blank=True)
#     Other  = models.TextField(null=True,blank=True)
#     Review_Status = models.CharField(max_length=100,default='Not Reviewed')
#     Reviewed_By = models.ForeignKey('hcp.HcpRegistrationModel',related_name='stationF_Reviewedby_HcpId_Log',on_delete=models.CASCADE,null=True,blank=True)
#     Reviewed_On = models.CharField(max_length=100)
#     Comments = models.TextField(null=True,blank=True)
#     Logs_Time = models.DateTimeField(auto_now=True)

#     objects = models.Manager


#     class Meta:
#          db_table = "StationF_logs"
