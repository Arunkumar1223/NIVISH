from .models import *
from rest_framework import serializers


class StationFSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['HCID','HCPID','InfoseekId','EntryTime','Skin_colour_Tone','Skin_colour_Tone_Abnormal','Skin_Texture_of_Skin', 'Skin_Texture_of_Skin_Abnormal',
                  'skin_Rash','skin_Rash_Present','skin_Rash_Present_Face','skin_Rash_Present_Neck','skin_Rash_Present_Chest','skin_Rash_Present_Abdomen',
                  'skin_Rash_Present_Groin','skin_Rash_Present_Back','skin_Rash_Present_Arms','skin_Rash_Present_Hands',
                  'skin_Rash_Present_Legs','skin_Rash_Present_Feet','Other_Skin_lesions','Other_Skin_lesions_Yes','Other_Skin_lesions_Yes_Other',
                  'Other_Skin_lesions_Yes_Birth_marks','Other_Skin_lesions_Yes_Birth_marks_Other','skin_Acne','skin_Acne_Yes']


class GetStationFPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['id','StationID','HCID','HCPID','InfoseekId','EntryTime','Skin_colour_Tone','Skin_colour_Tone_Abnormal','Skin_Texture_of_Skin', 'Skin_Texture_of_Skin_Abnormal',
                  'skin_Rash','skin_Rash_Present','skin_Rash_Present_Face','skin_Rash_Present_Neck','skin_Rash_Present_Chest','skin_Rash_Present_Abdomen',
                  'skin_Rash_Present_Groin','skin_Rash_Present_Back','skin_Rash_Present_Arms','skin_Rash_Present_Hands',
                  'skin_Rash_Present_Legs','skin_Rash_Present_Feet','Other_Skin_lesions','Other_Skin_lesions_Yes','Other_Skin_lesions_Yes_Other',
                  'Other_Skin_lesions_Yes_Birth_marks','Other_Skin_lesions_Yes_Birth_marks_Other','skin_Acne','skin_Acne_Yes']



class UpdateStationFSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['HCID','HCPID','InfoseekId','Skin_colour_Tone','Skin_colour_Tone_Abnormal','Skin_Texture_of_Skin', 'Skin_Texture_of_Skin_Abnormal',
                  'skin_Rash','skin_Rash_Present','skin_Rash_Present_Face','skin_Rash_Present_Neck','skin_Rash_Present_Chest','skin_Rash_Present_Abdomen',
                  'skin_Rash_Present_Groin','skin_Rash_Present_Back','skin_Rash_Present_Arms','skin_Rash_Present_Hands',
                  'skin_Rash_Present_Legs','skin_Rash_Present_Feet','Other_Skin_lesions','Other_Skin_lesions_Yes','Other_Skin_lesions_Yes_Other',
                  'Other_Skin_lesions_Yes_Birth_marks','Other_Skin_lesions_Yes_Birth_marks_Other','skin_Acne','skin_Acne_Yes','Reviewed_By','Reviewed_On']


class StationFSerializers2(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['Nails_Color','Nails_Shape','Nails_Shape_Abnormal','Nails_Deformity','Nails_Deformity_Yes','Nails_Cuticles',
                  'Nail_Bed_Infection','Reviewed_By','Reviewed_On']
        

class StationFSerializers3(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['Head_Skull_Fontanelle','Head_Skull_Fontanelle_Open','Head_Skull_Fontanelle_Open_Fontanella','Head_Skull_Fontanelle_Open_Occipital','Head_Skull_Appearance_and_Size',
                  'Head_Skull_Appearance_and_Size_Other','Head_Hair_Appearance','Head_Hair_Appearance_Abnormal',
                  'Head_Hair_Appearance_Abnormal_Other','Head_Scalp','Head_Scalp_Abnormal','Head_Parasites','Head_Parasites_Yes',
                  'Head_Parasites_Yes_Other','Head_Hair_Loss','Head_Hair_Loss_Yes','Reviewed_By','Reviewed_On']
        

class StationFSerializers4(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['Thyroid_Lymph_Thyroid_Gland','Thyroid_Lymph_Thyroid_Gland_Enlarged','Thyroid_Lymph_Cervical_LN','Thyroid_Lymph_Cervical_LN_Palpable',
                  'Thyroid_Lymph_Supraclavicular_LN','Thyroid_Lymph_Supraclavicular_LN_Palpable','Thyroid_Lymph_Axillary_LN',
                  'Thyroid_Lymph_Axillary_LN_Palpable','Thyroid_Lymph_Supratrochlear_LN','Thyroid_Lymph_Supratrochlear_LN_Palpable',
                  'Thyroid_Lymph_Inguinal_LN','Thyroid_Lymph_Inguinal_LN_Palpable','Reviewed_By','Reviewed_On']
        

class StationFSerializers5(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['Eyes_Conjuctiva','Eyes_Sclera','Eyes_Discharge','Eyes_Discharge_Yes','Eyes_Discharge_Yes_Right_Eye',
                  'Eyes_Discharge_Yes_Left_Eye','Eyes_Eyelids','Eyes_Eyelids_Abnormal','Reviewed_By','Reviewed_On']
        


class StationFSerializers6(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['Ears_Hearing','Ears_Hearing_Abnormal','Ears_Hearing_Abnormal_Reduced','Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid',
                  'Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes','Ears_Hearing_Abnormal_Reduced_Other','Ears_Discharge','Ears_Discharge_Yes',
                  'Ears_Discharge_Yes_Right_Ear','Ears_Discharge_Yes_Left_Ear','Ear_Wax','Ear_Wax_Present','Ear_Eardrum',
                  'Ear_Eardrum_Abnormal','Ear_Eardrum_Abnormal_Right_Ear','Ear_Eardrum_Abnormal_Left_Ear','Reviewed_By','Reviewed_On']
        
    
class StationFSerializers7(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['Nose_Discharge','Nose_Discharge_Yes','Nose_Discharge_Yes_Right_Nostril','Nose_Discharge_Yes_Left_Nostril',
                  'Nose_Dryness','Nose_Dryness_Yes','Nose_Crusting','Nose_Crusting_Yes','Nose_Polyps','Nose_Polyps_Yes',
                  'Nose_Septum_Bridge','Nose_Sinuses','Reviewed_By','Reviewed_On']
        

class StationFSerializers8(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['Mouth_Throat_Mucosa','Mouth_Throat_Mucosa_Abnormal','Mouth_Throat_Mucosa_Abnormal_Other',
                  'Mouth_Throat_Tongue','Mouth_Throat_Tongue_Abnormal','Mouth_Throat_Tongue_Abnormal_Other',
                  'Mouth_Tonsils','Mouth_Tonsils_Abnormal','Mouth_Uvula','Mouth_Uvula_Abnormal','Mouth_Palate',
                  'Mouth_Palate_Cleft_Palate','Mouth_Palate_CleftLip_Palate','Mouth_Palate_Other','Reviewed_By','Reviewed_On']
        

class StationFSerializers9(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['Hygiene_Nails','Hygiene_Hair','Hygiene_Skin','Hygiene_Odour','Reviewed_By','Reviewed_On']


class StationFSerializers10(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['Other_Observations','Specialist_Referral_Needed','Specialist_Referral_Needed_Type',
                  'Specialist_Referral_Needed_Flag','Other','Completed','Reviewed_By','Reviewed_On','EndTime']
        

class GetStationFSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['id','StationID','HCID','HCPID','InfoseekId','EntryTime','Skin_colour_Tone','Skin_colour_Tone_Abnormal','Skin_Texture_of_Skin', 'Skin_Texture_of_Skin_Abnormal',
                  'skin_Rash','skin_Rash_Present','skin_Rash_Present_Face','skin_Rash_Present_Neck','skin_Rash_Present_Chest','skin_Rash_Present_Abdomen',
                  'skin_Rash_Present_Groin','skin_Rash_Present_Back','skin_Rash_Present_Arms','skin_Rash_Present_Hands',
                  'skin_Rash_Present_Legs','skin_Rash_Present_Feet','Other_Skin_lesions','Other_Skin_lesions_Yes','Other_Skin_lesions_Yes_Other',
                  'Other_Skin_lesions_Yes_Birth_marks','Other_Skin_lesions_Yes_Birth_marks_Other','skin_Acne','skin_Acne_Yes',
                  'Nails_Color','Nails_Shape','Nails_Shape_Abnormal','Nails_Deformity','Nails_Deformity_Yes','Nails_Cuticles',
                  'Nail_Bed_Infection','Head_Skull_Fontanelle','Head_Skull_Fontanelle_Open','Head_Skull_Fontanelle_Open_Fontanella','Head_Skull_Fontanelle_Open_Occipital','Head_Skull_Appearance_and_Size',
                  'Head_Skull_Appearance_and_Size_Other','Head_Hair_Appearance','Head_Hair_Appearance_Abnormal',
                  'Head_Hair_Appearance_Abnormal_Other','Head_Scalp','Head_Scalp_Abnormal','Head_Parasites','Head_Parasites_Yes',
                  'Head_Parasites_Yes_Other','Head_Hair_Loss','Head_Hair_Loss_Yes','Thyroid_Lymph_Thyroid_Gland','Thyroid_Lymph_Thyroid_Gland_Enlarged','Thyroid_Lymph_Cervical_LN','Thyroid_Lymph_Cervical_LN_Palpable',
                  'Thyroid_Lymph_Supraclavicular_LN','Thyroid_Lymph_Supraclavicular_LN_Palpable','Thyroid_Lymph_Axillary_LN',
                  'Thyroid_Lymph_Axillary_LN_Palpable','Thyroid_Lymph_Supratrochlear_LN','Thyroid_Lymph_Supratrochlear_LN_Palpable',
                  'Thyroid_Lymph_Inguinal_LN','Thyroid_Lymph_Inguinal_LN_Palpable','Eyes_Conjuctiva','Eyes_Sclera','Eyes_Discharge','Eyes_Discharge_Yes','Eyes_Discharge_Yes_Right_Eye',
                  'Eyes_Discharge_Yes_Left_Eye','Eyes_Eyelids','Eyes_Eyelids_Abnormal','Ears_Hearing','Ears_Hearing_Abnormal','Ears_Hearing_Abnormal_Reduced','Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid',
                  'Ears_Hearing_Abnormal_Reduced_Wears_Hearing_Aid_Yes','Ears_Hearing_Abnormal_Reduced_Other','Ears_Discharge','Ears_Discharge_Yes',
                  'Ears_Discharge_Yes_Right_Ear','Ears_Discharge_Yes_Left_Ear','Ear_Wax','Ear_Wax_Present','Ear_Eardrum',
                  'Ear_Eardrum_Abnormal','Ear_Eardrum_Abnormal_Right_Ear','Ear_Eardrum_Abnormal_Left_Ear','Nose_Discharge','Nose_Discharge_Yes','Nose_Discharge_Yes_Right_Nostril','Nose_Discharge_Yes_Left_Nostril',
                  'Nose_Dryness','Nose_Dryness_Yes','Nose_Crusting','Nose_Crusting_Yes','Nose_Polyps','Nose_Polyps_Yes',
                  'Nose_Septum_Bridge','Nose_Sinuses','Mouth_Throat_Mucosa','Mouth_Throat_Mucosa_Abnormal','Mouth_Throat_Mucosa_Abnormal_Other',
                  'Mouth_Throat_Tongue','Mouth_Throat_Tongue_Abnormal','Mouth_Throat_Tongue_Abnormal_Other',
                  'Mouth_Tonsils','Mouth_Tonsils_Abnormal','Mouth_Uvula','Mouth_Uvula_Abnormal','Mouth_Palate',
                  'Mouth_Palate_Cleft_Palate','Mouth_Palate_CleftLip_Palate','Mouth_Palate_Other','Hygiene_Nails','Hygiene_Hair','Hygiene_Skin','Hygiene_Odour',
                  'Other_Observations','Specialist_Referral_Needed','Specialist_Referral_Needed_Type',
                  'Specialist_Referral_Needed_Flag','Other','Completed','Review_Status','Reviewed_By',
                  'Reviewed_On','Comments','EndTime']
        



        

        
