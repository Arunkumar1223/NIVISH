from rest_framework import serializers
from infoseek.models import *
from .models import *


# class GetProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InfoseekVerificationModel
#         fields = ['Student_FirstName','Gender','Student_DOB','BloodGroup','Rh_Factor','UIN',
#                   'Fathers_FirstName','Registered_EmailId','Mothers_FullName','Family_Doctor_Name',
#                   'Doctor_Contact_Number']



# class GetInfoseekSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InfoseekVerificationModel
#         fields = ['What_typeof_recreational_activity_doesthestudentenjoy','Which_ofthe_following_activities_doesthestudentenjoy',
#                   'Activites_Other','Isthe_student_memberofasports_teamatschool','Isthe_student_memberofasports_teamatschool_Yes',
#                   'Do_you_have_pets_at_home','Do_you_have_pets_at_home_Yes_Animal','Do_you_have_pets_at_home_Yes_Duration',
#                   'Usual_numberof_mealsday','Usual_numberof_snacksday','What_is_the_students_average_fluid_intake',
#                   'Type_of_meal','Type_of_meal_Other','Does_the_student_have_breakfast_regularly',
#                   'Does_the_student_have_regular_meal_at_school','Student_If_Yes_where_does_it_come_from',
#                   'Student_If_Other','Is_the_student_intolerant_to_any_food_group','Food_Group_Other',
#                   'On_an_average_isthe_student_freshandrelaxed_night_sleep','Does_the_student_have_any_sleep_related_issues','Does_the_student_have_any_sleep_related_issues_Yes',
#                   'Sleep_related_issues_Other','What_is_the_students_average_length_of_sleep_per_night',
#                   'What_is_the_students_nap_cycle_during_day_Nap','How_would_you_describe_the_social_personality_ofthe_student','Social_personality_Other',
#                   'Specify_if_the_student_has_any_irrational_fears_phobias','How_would_you_rate_the_students_self_image_self_worth',
#                   'How_would_you_rate_students_cooperation_in_housedhold_chores','How_would_you_best_describe_the_student_reaction_to_change',
#                   'Student_reaction_Other','How_would_you_describe_student_rs_with_other_students','How_would_you_describe_student_rs_with_other_students_Other',
#                   'Does_the_student_have_any_significantly_close_friends','student_close_friends_yes_how_many_girls','student_close_friends_yes_how_many_boys',
#                   'What_is_student_general_opinion_of_school','The_student_goes_to_school',
#                   'How_would_you_rate_student_overall_attendance_at_school','Do_you_have_concerns_following_respect_tothe_student','How_would_you_rate_the_student_overall_physical_health',
#                   'Isthe_students_school_performance_affected_by_any_following','Isthe_student_significantly_dissatisfied_byany_following',
#                   'Student_dissatisfied_Other','Any_Ongoing_Illnesscondition_membersofthe_students_family','Any_students_family_Other',
#                   'Does_the_student_have_any_medicalissue_In_The_Past','Does_the_student_have_any_medicalissue_In_The_Past_Yes',
#                   'Does_the_student_have_any_medicalissue_Currently',
#                   'Does_the_student_have_any_medicalissue_Currently_Yes',
#                   'Past_Medication','Current_Medication','BCG_Dose0', 'BCG_Dose1', 'BCG_Dose2', 'BCG_Dose3', 'BCG_Dose4',
#                   'Chicken_Pox_Dose0', 'Chicken_Pox_Dose1', 'Chicken_Pox_Dose2', 'Chicken_Pox_Dose3', 
#                   'Chicken_Pox_Dose4','Cholera_Dose0', 'Cholera_Dose1', 'Cholera_Dose2', 'Cholera_Dose3', 
#                   'Cholera_Dose4','COVID_Vaccination_Dose0', 'COVID_Vaccination_Dose1', 'COVID_Vaccination_Dose2', 
#                   'COVID_Vaccination_Dose3', 'COVID_Vaccination_Dose4',
#                   'DPT_Dose0', 'DPT_Dose1', 'DPT_Dose2', 'DPT_Dose3', 'DPT_Dose4',
#                   'DT_Dose0', 'DT_Dose1', 'DT_Dose2', 'DT_Dose3', 'DT_Dose4',
#                   'HepatitisA_Dose0', 'HepatitisA_Dose1', 'HepatitisA_Dose2', 'HepatitisA_Dose3', 'HepatitisA_Dose4',
#                   'HepatitisB_Dose0', 'HepatitisB_Dose1', 'HepatitisB_Dose2', 'HepatitisB_Dose3', 'HepatitisB_Dose4',
#                   'HPV_Dose0', 'HPV_Dose1', 'HPV_Dose2', 'HPV_Dose3', 'HPV_Dose4',
#                   'Influenza_HIB_Dose0', 'Influenza_HIB_Dose1', 'Influenza_HIB_Dose2', 'Influenza_HIB_Dose3', 'Influenza_HIB_Dose4',
#                   'Influenza_Viral_Dose0', 'Influenza_Viral_Dose1', 'Influenza_Viral_Dose2', 'Influenza_Viral_Dose3', 'Influenza_Viral_Dose4',
#                   'MMR_Dose0', 'MMR_Dose1', 'MMR_Dose2', 'MMR_Dose3', 'MMR_Dose4',
#                   'Mumps_Measles_Dose0', 'Mumps_Measles_Dose1', 'Mumps_Measles_Dose2', 'Mumps_Measles_Dose3', 'Mumps_Measles_Dose4',
#                   'Oral_Polio_Dose0', 'Oral_Polio_Dose1', 'Oral_Polio_Dose2', 'Oral_Polio_Dose3', 'Oral_Polio_Dose4',
#                   'RotaVirus_Dose0', 'RotaVirus_Dose1', 'RotaVirus_Dose2', 'RotaVirus_Dose3', 'RotaVirus_Dose4',
#                   'Tetanus_Toxoid_Dose0', 'Tetanus_Toxoid_Dose1', 'Tetanus_Toxoid_Dose2', 'Tetanus_Toxoid_Dose3', 'Tetanus_Toxoid_Dose4',
#                   'Typhoid_Dose0', 'Typhoid_Dose1', 'Typhoid_Dose2', 'Typhoid_Dose3', 'Typhoid_Dose4',
#                   'Yellow_Fever_Dose0', 'Yellow_Fever_Dose1', 'Yellow_Fever_Dose2', 'Yellow_Fever_Dose3', 'Yellow_Fever_Dose4'
#         ]


# class EmergencyContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InfoseekVerificationModel
#         fields = [
#             'Primary_Contact','Primary_Contact_Belongs_To','Primary_Contact_Belongs_To_Other','Primary_Contact_Full_Name',
#             'Secondary_Contact','Secondary_Contact_Belongs_To','Secondary_Contact_Belongs_To_Other','Secondary_Contact_Full_Name'
#         ]


def calculate(h,w):
    bmi = w/(h/100) ** 2 
    print(bmi)
    return bmi

class BmiSerializers(serializers.ModelSerializer):
    class Meta:
        model = BmiModel
        fields = ['InfoseekId','height','weight']

    def create(self, validated_data):
        InfoseekId = validated_data['InfoseekId']
        height = validated_data['height']
        weight = validated_data['weight']
        calculated_bmi = calculate(height,weight)
        print(calculated_bmi)
        user = BmiModel.objects.create(InfoseekId=validated_data['InfoseekId'],height=validated_data['height'],weight=validated_data['weight'],
                                       calculated_bmi = calculated_bmi)
        user.save()
        return user


class GetBmiSerializers(serializers.ModelSerializer):
    class Meta:
        model = BmiModel
        fields = ['InfoseekId','height','weight','calculated_bmi']


class HealthInsuranceSerializers(serializers.ModelSerializer):
    class Meta:
        model = HealthInsuranceModel
        fields = ['InfoseekId','Health_insurance','Policy','Date_of_Expiry']


class GetHealthInsuranceSerializers(serializers.ModelSerializer):
    class Meta:
        model = HealthInsuranceModel
        fields = ['id','InfoseekId','Health_insurance','Policy','Date_of_Expiry']


import math
import random

def GenerateOtp():
    digits = "0123456789"
    otp = ""
    for i in range(4):
        otp += digits[math.floor(random.random() * 10)]
    return otp


class ParentOtpSerializers(serializers.ModelSerializer):
    class Meta:
        model = ParentOtpModel
        fields = ['MobileNumber']

    def create(self, validated_data):
        otp=GenerateOtp()
        user = ParentOtpModel.objects.create(MobileNumber=validated_data['MobileNumber'],
                                       Otp=otp)

        user.save()
        return user


class ParentOtpGenerationSerializers(serializers.ModelSerializer):
    class Meta:
        model = ParentOtpModel
        fields = ['MobileNumber','Otp'] 


class updateBPSerializers(serializers.ModelSerializer):
    class Meta:
        model = BPModel
        fields = ['SystolicBP','DiastolicBP']

class GetBPSerializers(serializers.ModelSerializer):
    class Meta:
        model = BPModel 
        fields = ['InfoseekId','SystolicBP','DiastolicBP']

class updateAbdominalSerializers(serializers.ModelSerializer):
    class Meta:
        model = AbdominalModel
        fields = ['Abdominal_Girth']   


class GetAbdominalSerializers(serializers.ModelSerializer):
    class Meta:
        model = AbdominalModel 
        fields = ['InfoseekId','Abdominal_Girth'] 


class updatechestserializers(serializers.ModelSerializer):
    class Meta:
        model = ChestModel 
        fields = ['Chest_Circumference']




class GetChestSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChestModel 
        fields = ["InfoseekId","Chest_Circumference"]

        
        
         