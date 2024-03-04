from rest_framework import serializers
from .models import *

import base64
import pyqrcode
from django.core.files.base import ContentFile

from rest_framework import serializers
from .models import InfoseekMasterModel

class InfoseekMasterSerilizers(serializers.ModelSerializer):
    class Meta:
        model = InfoseekMasterModel
        fields = [
            'Student_Admission_Code','Student_Admission_Date','Student_Roll_Number','Student_Class','Student_Section','Student_First_Name','Student_Middle_Name_1',
            'Student_Middle_Name_2','Student_Last_Name','Date_of_Birth','Gender','Blood_Group','RH_Factor','Mothers_First_Name','Mothers_Middle_Name',
            'Mothers_Last_Name','Fathers_First_Name','Fathers_Middle_Name','Fathers_Last_Name','Address_Building','Adress_Street','Other_Address_Part',
            'Zip','City','State','Country','Student_Ethnic_Origin','Mothers_Ethnic_Origin','Fathers_Ethnic_Origin','Home_Phone','Mothers_Mobile_Phone',
            'Fathers_Mobile_Phone','Parent_Email','Emergency_Contact_First_Name','Emergency_Contact_Middle_Name','Emergency_Contact_Last_Name','Emergency_Contact_Relationship',
            'Emergency_Contact_Phone_1','Emergency_Contact_Phone_2','Emergency_Doctor_Name','Emergency_Doctor_Phone_1','Comments','Ent_id','Status',
        ]

class GetInfoseekMasterSerilizers(serializers.ModelSerializer):
    class Meta:
        model = InfoseekMasterModel
        fields = ['id',
            'Student_Admission_Code','Student_Admission_Date','Student_Roll_Number','Student_Class','Student_Section','Student_First_Name','Student_Middle_Name_1',
            'Student_Middle_Name_2','Student_Last_Name','Date_of_Birth','Gender','Blood_Group','RH_Factor','Mothers_First_Name','Mothers_Middle_Name',
            'Mothers_Last_Name','Fathers_First_Name','Fathers_Middle_Name','Fathers_Last_Name','Address_Building','Adress_Street','Other_Address_Part',
            'Zip','City','State','Country','Student_Ethnic_Origin','Mothers_Ethnic_Origin','Fathers_Ethnic_Origin','Home_Phone','Mothers_Mobile_Phone',
            'Fathers_Mobile_Phone','Parent_Email','Emergency_Contact_First_Name','Emergency_Contact_Middle_Name','Emergency_Contact_Last_Name','Emergency_Contact_Relationship',
            'Emergency_Contact_Phone_1','Emergency_Contact_Phone_2','Emergency_Doctor_Name','Emergency_Doctor_Phone_1','Comments','Ent_id','Status',
        ]

# class InfoseekSerilizers(serializers.ModelSerializer):
#     class Meta:
#         model = InfoseekModel
#         fields = ['UserName', 'FirstName','LastName','Email','MobileNumber','Password']




# class GetInfoseekSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = InfoseekModel
#         fields = ['id', 'UserName', 'FirstName','LastName','Email','MobileNumber','Password']


class InfoseekUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['Student_FirstName','Student_DOB','Mothers_FullName','Registered_EmailId','Gender',
                  'Student_MiddleName1','Student_MiddleName2','Student_LastName','Mothers_FirstName','Mothers_MiddleName1','Mothers_LastName','Mothers_MiddleName2','Fathers_MiddleName2','Fathers_MiddleName1','Fathers_FirstName',
                  'Fathers_LastName','BloodGroup','Rh_Factor','Street_No','Building_Name','Zip_Code','Email_Registered_With_School','section_name','class_name'
                  ]

class GetInfoseekUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['InfoseekId','Student_FirstName','Student_DOB','Mothers_FullName','Registered_EmailId','Gender',
                  'Student_MiddleName1','Student_MiddleName2','Student_LastName','Mothers_FirstName','Mothers_MiddleName1','Mothers_LastName','Mothers_MiddleName2','Fathers_MiddleName2','Fathers_MiddleName1','Fathers_FirstName',
                  'Fathers_LastName','BloodGroup','Rh_Factor','Street_No','Building_Name','Zip_Code','Email_Registered_With_School','section_name','class_name'
                  ]

        
class InfoseekVerificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['following_information_providedby', 'If_Other','Student_FirstName','Student_MiddleName1',
                  'Student_MiddleName2','Student_LastName','Gender','Student_DOB','BloodGroup','Rh_Factor',
                  'Number_Of_Sisters','Number_Of_Brothers','Mothers_FirstName','Mothers_MiddleName1','Mothers_MiddleName2','Mothers_LastName',
                  'Mothers_Ethnicity', 'Mothers_Ethnicity_If_Other','Fathers_FirstName','Fathers_MiddleName1','Fathers_MiddleName2',
                  'Fathers_LastName','Fathers_Ethnicity','Fathers_Ethnicity_If_Other']

class UpdateInfoseekVerificationSerializers(serializers.ModelSerializer):
    class Meta:
        model =InfoseekVerificationModel
        fields = ['upload_photo']


class InfoseekVerificationSerializers2(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['Do_you_have_health_insurance','Medical_Aid','Policy_Card','Expiry_Date']



       
class InfoseekVerificationSerializers3(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['Building_Name','Apartment_Villa_No','Street_No','Area','City','Country','State','Zip_Code','Emergency_MobileNumber_Registered_with_school',
                  'Alternate_MobileNumber','Belongs_To','Email_Registered_With_School']



class InfoseekVerificationSerializers4(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['Primary_Contact','Primary_Contact_Belongs_To','Primary_Contact_Belongs_To_Other',
                  'Primary_Contact_Full_Name','Secondary_Contact','Secondary_Contact_Belongs_To',
                  'Secondary_Contact_Belongs_To_Other','Secondary_Contact_Full_Name',
                  'Family_Doctor_Name','Doctor_Contact_Number']
        



class InfoseekVerificationSerializers5(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['What_typeof_recreational_activity_doesthestudentenjoy','Which_ofthe_following_activities_doesthestudentenjoy',
                  'Activites_Other','Isthe_student_memberofasports_teamatschool','Isthe_student_memberofasports_teamatschool_Yes',
                  'Do_you_have_pets_at_home','Do_you_have_pets_at_home_Yes_Animal','Do_you_have_pets_at_home_Yes_Duration']


class InfoseekVerificationSerializers6(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['Usual_numberof_mealsday','Usual_numberof_snacksday','What_is_the_students_average_fluid_intake',
                  'Type_of_meal','Type_of_meal_Other','Does_the_student_have_breakfast_regularly','Does_the_student_have_regular_meal_at_school',
                  'Student_If_Yes_where_does_it_come_from','Student_If_Other','Is_the_student_intolerant_to_any_food_group',
                  'Food_Group_Other']




class InfoseekVerificationSerializers7(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['On_an_average_isthe_student_freshandrelaxed_night_sleep','Does_the_student_have_any_sleep_related_issues','Does_the_student_have_any_sleep_related_issues_Yes',
                  'Sleep_related_issues_Other','What_is_the_students_average_length_of_sleep_per_night',
                  'What_is_the_students_nap_cycle_during_day_Nap']
    

class InfoseekVerificationSerializers8(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['How_would_you_describe_the_social_personality_ofthe_student','Social_personality_Other',
                  'Specify_if_the_student_has_any_irrational_fears_phobias','How_would_you_rate_the_students_self_image_self_worth',
                  'How_would_you_rate_students_cooperation_in_housedhold_chores','How_would_you_best_describe_the_student_reaction_to_change',
                  'Student_reaction_Other','How_would_you_describe_student_rs_with_other_students','How_would_you_describe_student_rs_with_other_students_Other',
                  'Does_the_student_have_any_significantly_close_friends','student_close_friends_yes_how_many_girls','student_close_friends_yes_how_many_boys']
        
    


class InfoseekVerificationSerializers9(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['What_is_student_general_opinion_of_school','The_student_goes_to_school',
                  'How_would_you_rate_student_overall_attendance_at_school']
    

class InfoseekVerificationSerializers10(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['Do_you_have_concerns_following_respect_tothe_student','How_would_you_rate_the_student_overall_physical_health',
                  'Isthe_students_school_performance_affected_by_any_following','Isthe_student_significantly_dissatisfied_byany_following',
                  'Student_dissatisfied_Other']
    


class InfoseekVerificationSerializers11(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['Any_Ongoing_Illnesscondition_membersofthe_students_family','Any_students_family_Other']
       
      

class InfoseekVerificationSerializers12(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['Does_the_student_have_any_medicalissue_In_The_Past','Does_the_student_have_any_medicalissue_In_The_Past_Yes',
                  'Does_the_student_have_any_medicalissue_Currently',
                  'Does_the_student_have_any_medicalissue_Currently_Yes',
                  'Past_Medication','Current_Medication','Any_Known_Allergies','Any_Known_Allergies_yes']
        

class InfoseekVerificationSerializers13(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel  
        fields = ['BCG_Dose0', 'BCG_Dose1', 'BCG_Dose2', 'BCG_Dose3', 'BCG_Dose4',
            'Chicken_Pox_Dose0', 'Chicken_Pox_Dose1', 'Chicken_Pox_Dose2', 'Chicken_Pox_Dose3', 
            'Chicken_Pox_Dose4','Cholera_Dose0', 'Cholera_Dose1', 'Cholera_Dose2', 'Cholera_Dose3', 
            'Cholera_Dose4','COVID_Vaccination_Dose0', 'COVID_Vaccination_Dose1', 'COVID_Vaccination_Dose2', 
            'COVID_Vaccination_Dose3', 'COVID_Vaccination_Dose4',
            'DPT_Dose0', 'DPT_Dose1', 'DPT_Dose2', 'DPT_Dose3', 'DPT_Dose4',
            'DT_Dose0', 'DT_Dose1', 'DT_Dose2', 'DT_Dose3', 'DT_Dose4',
            'HepatitisA_Dose0', 'HepatitisA_Dose1', 'HepatitisA_Dose2', 'HepatitisA_Dose3', 'HepatitisA_Dose4',
            'HepatitisB_Dose0', 'HepatitisB_Dose1', 'HepatitisB_Dose2', 'HepatitisB_Dose3', 'HepatitisB_Dose4',
            'HPV_Dose0', 'HPV_Dose1', 'HPV_Dose2', 'HPV_Dose3', 'HPV_Dose4',
            'Influenza_HIB_Dose0', 'Influenza_HIB_Dose1', 'Influenza_HIB_Dose2', 'Influenza_HIB_Dose3', 'Influenza_HIB_Dose4',
            'Influenza_Viral_Dose0', 'Influenza_Viral_Dose1', 'Influenza_Viral_Dose2', 'Influenza_Viral_Dose3', 'Influenza_Viral_Dose4',
            'MMR_Dose0', 'MMR_Dose1', 'MMR_Dose2', 'MMR_Dose3', 'MMR_Dose4',
            'Mumps_Measles_Dose0', 'Mumps_Measles_Dose1', 'Mumps_Measles_Dose2', 'Mumps_Measles_Dose3', 'Mumps_Measles_Dose4',
            'Oral_Polio_Dose0', 'Oral_Polio_Dose1', 'Oral_Polio_Dose2', 'Oral_Polio_Dose3', 'Oral_Polio_Dose4',
            'RotaVirus_Dose0', 'RotaVirus_Dose1', 'RotaVirus_Dose2', 'RotaVirus_Dose3', 'RotaVirus_Dose4',
            'Tetanus_Toxoid_Dose0', 'Tetanus_Toxoid_Dose1', 'Tetanus_Toxoid_Dose2', 'Tetanus_Toxoid_Dose3', 'Tetanus_Toxoid_Dose4',
            'Typhoid_Dose0', 'Typhoid_Dose1', 'Typhoid_Dose2', 'Typhoid_Dose3', 'Typhoid_Dose4',
            'Yellow_Fever_Dose0', 'Yellow_Fever_Dose1', 'Yellow_Fever_Dose2', 'Yellow_Fever_Dose3', 'Yellow_Fever_Dose4'
        ]

    




class InfoseekNoteSerializers(serializers.ModelSerializer):  
    class Meta:
        model = NoteModel
        fields = ['InfoseekId','Last_date_signed_copy_of_form', 'type_your_name', 'gaurdian_of', 'of_class', 'Signature', 'Submitted_date', 'place','upload_sign','Accepted']
        
    def validate_Accepted(self, value):
        if not value:
            raise serializers.ValidationError("Accepted field must be True to post the note.")
        return value  
    
class InfoseekGetNoteSerializers(serializers.ModelSerializer):  
    class Meta:
        model = NoteModel
        fields = ['InfoseekId','Last_date_signed_copy_of_form', 'type_your_name', 'gaurdian_of', 'of_class', 'Signature', 'Submitted_date', 'place','upload_sign','Accepted'] 
    
class InfoseekTermsSerializers(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['Terms_and_conditions', 'Version','Date']
   
    

    
    
# class GetUpdateInfoseekVerificationNoteSerializers(serializers.ModelSerializer):
#     class Meta:
#         model =InfoseekVerificationModel
#         fields = ['upload_photo','UIN','qrcode_image']

    


class GetAllInfoseekSerializers(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['InfoseekId','Student_FirstName','Student_DOB','Mothers_FullName','Registered_EmailId','following_information_providedby', 'If_Other','Student_MiddleName1',
                  'Student_MiddleName2','Student_LastName','Gender','BloodGroup','Rh_Factor','class_name','section_name',
                  'Number_Of_Sisters','Number_Of_Brothers','Mothers_FirstName','Mothers_MiddleName1','Mothers_MiddleName2','Mothers_LastName',
                  'Mothers_Ethnicity','Mothers_Ethnicity_If_Other','Fathers_FirstName','Fathers_MiddleName1','Fathers_MiddleName2','Fathers_LastName','Fathers_Ethnicity','Fathers_Ethnicity_If_Other',
                  'Do_you_have_health_insurance','Medical_Aid','Policy_Card','Expiry_Date',
                  'Building_Name','Apartment_Villa_No','Street_No','Area','City','Country','State','Zip_Code','Emergency_MobileNumber_Registered_with_school',
                  'Alternate_MobileNumber','Belongs_To','Email_Registered_With_School',
                  'Primary_Contact','Primary_Contact_Belongs_To','Primary_Contact_Belongs_To_Other',
                  'Primary_Contact_Full_Name','Secondary_Contact','Secondary_Contact_Belongs_To',
                  'Secondary_Contact_Belongs_To_Other','Secondary_Contact_Full_Name','Family_Doctor_Name','Doctor_Contact_Number',
                  'What_typeof_recreational_activity_doesthestudentenjoy','Which_ofthe_following_activities_doesthestudentenjoy',
                  'Activites_Other','Isthe_student_memberofasports_teamatschool','Isthe_student_memberofasports_teamatschool_Yes',
                  'Do_you_have_pets_at_home','Do_you_have_pets_at_home_Yes_Animal','Do_you_have_pets_at_home_Yes_Duration',     
                  'Usual_numberof_mealsday','Usual_numberof_snacksday','What_is_the_students_average_fluid_intake',
                  'Type_of_meal','Type_of_meal_Other','Does_the_student_have_breakfast_regularly','Does_the_student_have_regular_meal_at_school',
                  'Student_If_Yes_where_does_it_come_from','Student_If_Other','Is_the_student_intolerant_to_any_food_group',
                  'Food_Group_Other',
                  'On_an_average_isthe_student_freshandrelaxed_night_sleep','Does_the_student_have_any_sleep_related_issues','Does_the_student_have_any_sleep_related_issues_Yes',
                  'Sleep_related_issues_Other','What_is_the_students_average_length_of_sleep_per_night',
                  'What_is_the_students_nap_cycle_during_day_Nap',
                  'How_would_you_describe_the_social_personality_ofthe_student','Social_personality_Other',
                  'Specify_if_the_student_has_any_irrational_fears_phobias','How_would_you_rate_the_students_self_image_self_worth',
                  'How_would_you_rate_students_cooperation_in_housedhold_chores','How_would_you_best_describe_the_student_reaction_to_change',
                  'Student_reaction_Other','How_would_you_describe_student_rs_with_other_students','How_would_you_describe_student_rs_with_other_students_Other',
                  'Does_the_student_have_any_significantly_close_friends','student_close_friends_yes_how_many_girls','student_close_friends_yes_how_many_boys',
                  'What_is_student_general_opinion_of_school','The_student_goes_to_school',
                  'How_would_you_rate_student_overall_attendance_at_school',
                  'Do_you_have_concerns_following_respect_tothe_student','How_would_you_rate_the_student_overall_physical_health',
                  'Isthe_students_school_performance_affected_by_any_following','Isthe_student_significantly_dissatisfied_byany_following',
                  'Student_dissatisfied_Other',
                  'Any_Ongoing_Illnesscondition_membersofthe_students_family','Any_students_family_Other',
                  'Does_the_student_have_any_medicalissue_In_The_Past','Does_the_student_have_any_medicalissue_In_The_Past_Yes',
                  'Does_the_student_have_any_medicalissue_Currently',
                  'Does_the_student_have_any_medicalissue_Currently_Yes',
                  'Past_Medication','Current_Medication','Any_Known_Allergies','Any_Known_Allergies_yes',
                  'BCG_Dose0', 'BCG_Dose1', 'BCG_Dose2', 'BCG_Dose3', 'BCG_Dose4',
                  'Chicken_Pox_Dose0', 'Chicken_Pox_Dose1', 'Chicken_Pox_Dose2', 'Chicken_Pox_Dose3', 
                  'Chicken_Pox_Dose4','Cholera_Dose0', 'Cholera_Dose1', 'Cholera_Dose2', 'Cholera_Dose3', 
                  'Cholera_Dose4','COVID_Vaccination_Dose0', 'COVID_Vaccination_Dose1', 'COVID_Vaccination_Dose2', 
                  'COVID_Vaccination_Dose3', 'COVID_Vaccination_Dose4',
                  'DPT_Dose0', 'DPT_Dose1', 'DPT_Dose2', 'DPT_Dose3', 'DPT_Dose4',
                  'DT_Dose0', 'DT_Dose1', 'DT_Dose2', 'DT_Dose3', 'DT_Dose4',
                  'HepatitisA_Dose0', 'HepatitisA_Dose1', 'HepatitisA_Dose2', 'HepatitisA_Dose3', 'HepatitisA_Dose4',
                  'HepatitisB_Dose0', 'HepatitisB_Dose1', 'HepatitisB_Dose2', 'HepatitisB_Dose3', 'HepatitisB_Dose4',
                  'HPV_Dose0', 'HPV_Dose1', 'HPV_Dose2', 'HPV_Dose3', 'HPV_Dose4',
                  'Influenza_HIB_Dose0', 'Influenza_HIB_Dose1', 'Influenza_HIB_Dose2', 'Influenza_HIB_Dose3', 'Influenza_HIB_Dose4',
                  'Influenza_Viral_Dose0', 'Influenza_Viral_Dose1', 'Influenza_Viral_Dose2', 'Influenza_Viral_Dose3', 'Influenza_Viral_Dose4',
                  'MMR_Dose0', 'MMR_Dose1', 'MMR_Dose2', 'MMR_Dose3', 'MMR_Dose4',
                  'Mumps_Measles_Dose0', 'Mumps_Measles_Dose1', 'Mumps_Measles_Dose2', 'Mumps_Measles_Dose3', 'Mumps_Measles_Dose4',
                  'Oral_Polio_Dose0', 'Oral_Polio_Dose1', 'Oral_Polio_Dose2', 'Oral_Polio_Dose3', 'Oral_Polio_Dose4',
                  'RotaVirus_Dose0', 'RotaVirus_Dose1', 'RotaVirus_Dose2', 'RotaVirus_Dose3', 'RotaVirus_Dose4',
                  'Tetanus_Toxoid_Dose0', 'Tetanus_Toxoid_Dose1', 'Tetanus_Toxoid_Dose2', 'Tetanus_Toxoid_Dose3', 'Tetanus_Toxoid_Dose4',
                  'Typhoid_Dose0', 'Typhoid_Dose1', 'Typhoid_Dose2', 'Typhoid_Dose3', 'Typhoid_Dose4',
                  'Yellow_Fever_Dose0', 'Yellow_Fever_Dose1', 'Yellow_Fever_Dose2', 'Yellow_Fever_Dose3', 'Yellow_Fever_Dose4',
                  'UIN','qrcode_image','Terms_and_conditions','upload_photo']
            


import math
import random
from rest_framework import serializers
from .models import OtpModel  # Import your OtpModel here

def GenerateOtp():
    digits = "0123456789"
    otp = ""
    for i in range(4):
        otp += digits[math.floor(random.random() * 10)]
    return otp

class InfoseekOtpSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = OtpModel
        fields = ['Student_FirstName', 'Student_DOB', 'Mothers_FullName', 'Email']
   
    def create(self, validated_data):       
        otp = GenerateOtp()
        user = OtpModel.objects.create(
            Student_FirstName=validated_data['Student_FirstName'],
            Student_DOB=validated_data['Student_DOB'],
            Mothers_FullName=validated_data['Mothers_FullName'],
            Email=validated_data['Email'],
            Otp=otp
        )

        user.save()
        return user





class OtpGenerationSerializers(serializers.ModelSerializer):
    class Meta:
        model = OtpModel
        fields = ['Student_FirstName','Student_DOB','Mothers_FullName','Email','Otp']


class InfoseekFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoseekFileUploadModels
        fields = ['file']




class ImmunizationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImmunizationModel
        fields = ['Vaccine','Vaccine_Code','Vaccine_Shortname','Vaccine_Description','Area','Source_Comments','Validations']

class GetImmunizationMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImmunizationModel
        fields = ['ImmunizationId','Vaccine','Vaccine_Code','Vaccine_Shortname','Vaccine_Description','Area','Source_Comments','Validations']






class CountryMasterSerailizer(serializers.ModelSerializer):
    class Meta:
        model = CountryMasterModel
        fields = "__all__"

        
class StateMasterSerailizer(serializers.ModelSerializer):
    class Meta:
        model = StateMasterModel
        fields = "__all__"

        
class CityMasterSerailizer(serializers.ModelSerializer):
    class Meta:
        model = CityMasterModel
        fields = "__all__"

class InfoseekIdCardGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['Student_FirstName','class_name','section_name','Gender','Student_DOB','UIN','qrcode_image','upload_photo']


        
class ImageUploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = "__all__"
