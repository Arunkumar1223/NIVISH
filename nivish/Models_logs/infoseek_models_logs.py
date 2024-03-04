
from django.db import models
from datetime import datetime
import ast

class InfoseekMasterModel_Log(models.Model):
    Student_Admission_Code = models.CharField(max_length=20)
    Student_Admission_Date = models.CharField(max_length=20)
    Student_Roll_Number = models.CharField(max_length=20)
    Student_Class = models.CharField(max_length=100)
    Student_Section = models.CharField(max_length=100)
    Student_First_Name = models.CharField(max_length=200)
    Student_Middle_Name_1 = models.CharField(max_length=100)
    Student_Middle_Name_2 = models.CharField(max_length=100)
    Student_Last_Name = models.CharField(max_length=100)
    Date_of_Birth = models.DateField()
    Gender = models.CharField(max_length=100)
    Blood_Group = models.CharField(max_length=100)
    RH_Factor = models.CharField(max_length=100)
    Mothers_First_Name = models.CharField(max_length=100)
    Mothers_Middle_Name = models.CharField(max_length=200)
    Mothers_Last_Name = models.CharField(max_length=100)
    Fathers_First_Name = models.CharField(max_length=100)
    Fathers_Middle_Name = models.CharField(max_length=200)
    Fathers_Last_Name = models.CharField(max_length=100)
    Address_Building = models.CharField(max_length=250)
    Adress_Street = models.CharField(max_length=250)
    Other_Address_Part = models.CharField(max_length=250)
    Zip = models.CharField(max_length=10)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Student_Ethnic_Origin = models.CharField(max_length=50)
    Mothers_Ethnic_Origin = models.CharField(max_length=100)
    Fathers_Ethnic_Origin = models.CharField(max_length=100)
    Home_Phone = models.CharField(max_length=100)
    Mothers_Mobile_Phone = models.CharField(max_length=50)
    Fathers_Mobile_Phone = models.CharField(max_length=50)
    Parent_Email = models.EmailField()
    Emergency_Contact_First_Name = models.CharField(max_length=100)
    Emergency_Contact_Middle_Name = models.CharField(max_length=100)
    Emergency_Contact_Last_Name = models.CharField(max_length=100)
    Emergency_Contact_Relationship = models.CharField(max_length=50)
    Emergency_Contact_Phone_1 = models.CharField(max_length=15)
    Emergency_Contact_Phone_2 = models.CharField(max_length=15)
    Emergency_Doctor_Name = models.CharField(max_length=200)
    Emergency_Doctor_Phone_1 = models.CharField(max_length=15)
    Comments = models.CharField(max_length=400)
    Ent_id = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Logs_Time = models.DateTimeField(auto_now=True)

    objects = models.Manager
    class Meta: 
        db_table = 'Infoseek_Master_Logs'



class InfoseekVerificationModel_Log(models.Model):

    ## User Verification
    InfoseekId = models.IntegerField(primary_key=True)
    Student_FirstName = models.CharField(max_length=50)
    Student_DOB =  models.DateField()
    Mothers_FullName = models.CharField(max_length=50)
    Registered_EmailId = models.EmailField()

    ## A. Student Personal Information
    
    following_information_providedby = models.CharField(max_length=50) 
    If_Other = models.CharField(max_length=200,null=True, blank=True)

    Student_MiddleName1 = models.CharField(max_length=200)
    Student_MiddleName2 = models.CharField(max_length=200)
    Student_LastName = models.CharField(max_length=200)
    Gender = models.CharField(max_length=10, )
    BloodGroup =models.CharField(max_length=50, )
    Rh_Factor = models.CharField(max_length=50, )
    Number_Of_Sisters = models.CharField(max_length=200, null=True, blank=True)
    Number_Of_Brothers = models.CharField(max_length=200, null=True, blank=True)
    Mothers_FirstName = models.CharField(max_length=200, null=True, blank=True)
    Mothers_MiddleName1 = models.CharField(max_length=200, null=True, blank=True)
    Mothers_MiddleName2 = models.CharField(max_length=200, null=True, blank=True)
    Mothers_LastName = models.CharField(max_length=200, null=True, blank=True)
    Mothers_Ethnicity = models.CharField(max_length=200, )
    Mothers_Ethnicity_If_Other = models.CharField(max_length=200,null=True, blank=True) 
    Fathers_FirstName = models.CharField(max_length=200, null=True, blank=True)
    Fathers_MiddleName1 = models.CharField(max_length=200, null=True, blank=True)
    Fathers_MiddleName2 = models.CharField(max_length=200, null=True, blank=True) 
    Fathers_LastName  = models.CharField(max_length=200, null=True, blank=True) 
    Fathers_Ethnicity = models.CharField(max_length=200, )
    Fathers_Ethnicity_If_Other = models.CharField(max_length=200,null=True, blank=True)
    upload_photo = models.ImageField(upload_to='Infoseek',null=True, blank=True,max_length=100000) 

    # B. Health Insurance Information

    Do_you_have_health_insurance = models.CharField(max_length=100, ) 
    Medical_Aid = models.CharField(max_length=100, null=True, blank=True)
    Policy_Card = models.CharField(max_length=100, null=True, blank=True)
    Expiry_Date = models.CharField(max_length=100, null=True, blank=True)


    # C. Address Information

    Building_Name = models.CharField(max_length=100)
    Apartment_Villa_No = models.CharField(max_length=100)
    Street_No = models.CharField(max_length=100)
    Area = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Zip_Code = models.CharField(max_length=100)
    Emergency_MobileNumber_Registered_with_school = models.BigIntegerField(null=True,blank=True)
    Alternate_MobileNumber = models.BigIntegerField(null=True,blank=True)
    Belongs_To = models.CharField(max_length=100,  null=True,blank=True)
    Email_Registered_With_School = models.EmailField()
    

    # D. Emergency Contact
    Primary_Contact = models.BigIntegerField(null=True, blank=True)
    Primary_Contact_Belongs_To = models.CharField(max_length=100, null=True,blank=True) 
    Primary_Contact_Belongs_To_Other = models.CharField(max_length=100,null=True, blank=True)
    Primary_Contact_Full_Name = models.CharField(max_length=100,null=True, blank=True) 
    Secondary_Contact = models.BigIntegerField(null=True,blank=True) 
    Secondary_Contact_Belongs_To = models.CharField(max_length=100, null=True,blank=True)
    Secondary_Contact_Belongs_To_Other = models.CharField(max_length=1000, null=True, blank=True)
    Secondary_Contact_Full_Name = models.CharField(max_length=100, null=True, blank=True)
    Family_Doctor_Name = models.CharField(max_length=100, null=True, blank=True)
    Doctor_Contact_Number = models.BigIntegerField(null=True, blank=True)

    # E. Basic Lifestyle

    What_typeof_recreational_activity_doesthestudentenjoy = models.CharField(max_length=100, null=True,blank=True)
    Which_ofthe_following_activities_doesthestudentenjoy = models.CharField(max_length=1000, null=True, blank=True) 
    Activites_Other = models.CharField(max_length=10000, null=True, blank=True)
    Isthe_student_memberofasports_teamatschool = models.CharField(max_length=100, null=True,blank=True)
    Isthe_student_memberofasports_teamatschool_Yes = models.CharField(max_length=100, null=True, blank=True)
    Do_you_have_pets_at_home = models.CharField(max_length=100, null=True,blank=True)
    Do_you_have_pets_at_home_Yes_Animal = models.CharField(max_length=100, null=True, blank=True)
    Do_you_have_pets_at_home_Yes_Duration = models.CharField(max_length=100, null=True, blank=True)


    # F. Dietary Habits

    Usual_numberof_mealsday = models.IntegerField(null=True,blank=True) 
    Usual_numberof_snacksday = models.IntegerField(null=True,blank=True)
    What_is_the_students_average_fluid_intake = models.CharField(max_length=100, null=True, blank=True) 
    Type_of_meal = models.CharField(max_length=1000, null=True,blank=True)
    Type_of_meal_Other = models.CharField(max_length=10000, null=True, blank=True)
    Does_the_student_have_breakfast_regularly = models.CharField(max_length=100,null=True,blank=True)
    Does_the_student_have_regular_meal_at_school = models.CharField(max_length=100, null=True,blank=True)
    Student_If_Yes_where_does_it_come_from = models.CharField(max_length=100,null=True,blank=True)
    Student_If_Other = models.CharField(max_length=10000, null=True, blank=True)
    Is_the_student_intolerant_to_any_food_group = models.CharField(max_length=100, null=True, blank=True) 
    Food_Group_Other = models.CharField(max_length=10000, null=True, blank=True)

    # G. Sleep Pattern and Quality

    On_an_average_isthe_student_freshandrelaxed_night_sleep = models.CharField(max_length=100, null=True, blank=True)
    Does_the_student_have_any_sleep_related_issues = models.CharField(max_length=1000, null=True, blank=True) 
    Does_the_student_have_any_sleep_related_issues_Yes = models.CharField(max_length=1000, null=True, blank=True) 
    Sleep_related_issues_Other = models.CharField(max_length=10000, null=True, blank=True)
    What_is_the_students_average_length_of_sleep_per_night = models.CharField(max_length=100, null=True,blank=True) 
    What_is_the_students_nap_cycle_during_day_Nap = models.CharField(max_length=10000, null=True, blank=True)

    How_would_you_describe_the_social_personality_ofthe_student = models.CharField(max_length=1000, null=True,blank=True) 
    Social_personality_Other = models.CharField(max_length=10000, null=True, blank=True)
    Specify_if_the_student_has_any_irrational_fears_phobias = models.CharField(max_length=100, null=True, blank=True)
    How_would_you_rate_the_students_self_image_self_worth = models.CharField(max_length=100, null=True,blank=True)
    How_would_you_rate_students_cooperation_in_housedhold_chores = models.CharField(max_length=100, null=True, blank=True) ## Exceedingly Uncooperative, Exceedingly Cooperative
    How_would_you_best_describe_the_student_reaction_to_change = models.CharField(max_length=100, null=True,blank=True) 
    Student_reaction_Other = models.CharField(max_length=10000, null=True, blank=True)
    How_would_you_describe_student_rs_with_other_students = models.CharField(max_length=100, null=True,blank=True) 
    How_would_you_describe_student_rs_with_other_students_Other = models.CharField(max_length=10000,null=True,blank=True)
    Does_the_student_have_any_significantly_close_friends = models.CharField(max_length=100, null=True,blank=True) 
    student_close_friends_yes_how_many_girls = models.CharField(max_length=200,null=True,blank=True)
    student_close_friends_yes_how_many_boys = models.CharField(max_length=200,null=True,blank=True)
    

    

    # I. Life at School

    What_is_student_general_opinion_of_school = models.CharField(max_length=100, null=True,blank=True) 
    The_student_goes_to_school = models.CharField(max_length=100, null=True,blank=True) 
    How_would_you_rate_student_overall_attendance_at_school = models.CharField(max_length=100, null=True, blank=True) ## Very Irregular, Always Regular


    # J. General History

    Do_you_have_concerns_following_respect_tothe_student = models.CharField(max_length=1000, null=True, blank=True) 
    How_would_you_rate_the_student_overall_physical_health = models.CharField(max_length=1000, null=True, blank=True) 
    Isthe_students_school_performance_affected_by_any_following = models.CharField(max_length=1000, null=True, blank=True) 
    Isthe_student_significantly_dissatisfied_byany_following = models.CharField(max_length=1000, null=True, blank=True) 
    Student_dissatisfied_Other = models.CharField(max_length=10000, null=True, blank=True)


    # K. Family History

    Any_Ongoing_Illnesscondition_membersofthe_students_family = models.CharField(max_length=1000, null=True, blank=True) 
    Any_students_family_Other = models.TextField(null=True, blank=True)


    # L. Medical History

    Does_the_student_have_any_medicalissue_In_The_Past = models.CharField(max_length=1000,  null=True, blank=True)
    Does_the_student_have_any_medicalissue_In_The_Past_Yes = models.CharField(max_length=1000, null=True, blank=True) 
    Does_the_student_have_any_medicalissue_Currently = models.CharField(max_length=1000,  null=True, blank=True) 
    Does_the_student_have_any_medicalissue_Currently_Yes = models.CharField(max_length=1000, null=True, blank=True) 
    Past_Medication = models.CharField(max_length=100, null=True, blank=True)
    Current_Medication = models.CharField(max_length=100, null=True, blank=True)
    Any_Known_Allergies = models.CharField(max_length=100, null=True, blank=True) 
    Any_Known_Allergies_yes = models.CharField(max_length=100, null=True, blank=True)


    # Immunization

    BCG_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    BCG_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    BCG_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    BCG_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    BCG_Dose4 = models.CharField(max_length=100,null=True,blank=True)

    Chicken_Pox_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    Chicken_Pox_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    Chicken_Pox_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    Chicken_Pox_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    Chicken_Pox_Dose4 = models.CharField(max_length=100,null=True,blank=True)

    Cholera_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    Cholera_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    Cholera_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    Cholera_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    Cholera_Dose4 = models.CharField(max_length=100,null=True,blank=True)

    COVID_Vaccination_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    COVID_Vaccination_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    COVID_Vaccination_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    COVID_Vaccination_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    COVID_Vaccination_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    DPT_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    DPT_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    DPT_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    DPT_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    DPT_Dose4 = models.CharField(max_length=100,null=True,blank=True)

    DT_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    DT_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    DT_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    DT_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    DT_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    HepatitisA_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    HepatitisA_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    HepatitisA_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    HepatitisA_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    HepatitisA_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    HepatitisB_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    HepatitisB_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    HepatitisB_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    HepatitisB_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    HepatitisB_Dose4 = models.CharField(max_length=100,null=True,blank=True)

    HPV_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    HPV_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    HPV_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    HPV_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    HPV_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    Influenza_HIB_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    Influenza_HIB_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    Influenza_HIB_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    Influenza_HIB_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    Influenza_HIB_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    Influenza_Viral_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    Influenza_Viral_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    Influenza_Viral_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    Influenza_Viral_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    Influenza_Viral_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    MMR_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    MMR_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    MMR_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    MMR_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    MMR_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    Mumps_Measles_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    Mumps_Measles_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    Mumps_Measles_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    Mumps_Measles_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    Mumps_Measles_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    Oral_Polio_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    Oral_Polio_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    Oral_Polio_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    Oral_Polio_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    Oral_Polio_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    RotaVirus_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    RotaVirus_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    RotaVirus_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    RotaVirus_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    RotaVirus_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    Tetanus_Toxoid_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    Tetanus_Toxoid_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    Tetanus_Toxoid_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    Tetanus_Toxoid_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    Tetanus_Toxoid_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    Typhoid_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    Typhoid_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    Typhoid_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    Typhoid_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    Typhoid_Dose4 = models.CharField(max_length=100,null=True,blank=True)
    
    Yellow_Fever_Dose0 = models.CharField(max_length=100,null=True,blank=True)
    Yellow_Fever_Dose1 = models.CharField(max_length=100,null=True,blank=True)
    Yellow_Fever_Dose2 = models.CharField(max_length=100,null=True,blank=True)
    Yellow_Fever_Dose3 = models.CharField(max_length=100,null=True,blank=True)
    Yellow_Fever_Dose4 = models.CharField(max_length=100,null=True,blank=True)

    qrcode_image = models.ImageField(upload_to='Infoseek_qrcodes',null=True, blank=True,max_length=100000)
    
    UIN =  models.CharField(max_length=100,null=True,blank=True)

    Terms_and_conditions = models.BooleanField(default=None)
    Version = models.CharField(max_length=100,null=True,blank=True)
    Date = models.DateField()

    class_name = models.CharField(max_length=100)
    section_name = models.CharField(max_length=100)

    Logs_Time = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta: 
        db_table = 'Infoseek_Logs'

