def check_following_information_providedby(request):
    following_information_providedby = request.data.get('following_information_providedby')
    If_Other = request.data.get('If_Other')
    if following_information_providedby == 'Other':
        if  If_Other == None :
            raise Exception("Please provide any text that needs to be filled in")
    else:
        request.data['If_Other']= None

def check_Mothers_Ethnicity(request):
    Mothers_Ethnicity = request.data.get('Mothers_Ethnicity')
    Mothers_Ethnicity_If_Other = request.data.get('Mothers_Ethnicity_If_Other')
    if Mothers_Ethnicity == 'Other':
        if  Mothers_Ethnicity_If_Other == None :
            raise Exception("Please provide any text that needs to be filled in")
    else:
        request.data['Mothers_Ethnicity_If_Other']= None

def check_Fathers_Ethnicity(request):
    Fathers_Ethnicity = request.data.get('Fathers_Ethnicity')
    Fathers_Ethnicity_If_Other = request.data.get('Fathers_Ethnicity_If_Other')
    if Fathers_Ethnicity == 'Other':
        if  Fathers_Ethnicity_If_Other == None :
            raise Exception("Please provide any text that needs to be filled in")
    else:
        request.data['Fathers_Ethnicity_If_Other']= None

def check_Primary_Contact_Belongs(request):
    Primary_Contact_Belongs_To = request.data.get('Primary_Contact_Belongs_To')
    Primary_Contact_Belongs_To_Other = request.data.get('Primary_Contact_Belongs_To_Other')

    if Primary_Contact_Belongs_To == 'Other':
        if Primary_Contact_Belongs_To_Other == None:
            raise Exception("you have to select anyone")
    
    else:
        request.data['Primary_Contact_Belongs_To_Other']=None

def check_Activites_Others(request):
    Which_ofthe_following_activities_doesthestudentenjoy = request.data.get('Which_ofthe_following_activities_doesthestudentenjoy')
    Activites_Other = request.data.get('Activites_Other')

    if Which_ofthe_following_activities_doesthestudentenjoy is None:
        request.data['Activites_Other'] = None
    else:
        selected_values = Which_ofthe_following_activities_doesthestudentenjoy.split(',') 
        Other_value = None
        for i in selected_values:
            if i == 'Other':
                Other_value = Activites_Other
                if Activites_Other == None:
                    raise Exception('Please provide any text that needs to be filled in.')

        request.data['Activites_Other'] = Other_value


def check_Isthe_student_memberofasports_teamatschool(request):
    Isthe_student_memberofasports_teamatschool = request.data.get('Isthe_student_memberofasports_teamatschool')
    Isthe_student_memberofasports_teamatschool_Yes = request.data.get('Isthe_student_memberofasports_teamatschool_Yes')
    if Isthe_student_memberofasports_teamatschool == 'Yes':
        if Isthe_student_memberofasports_teamatschool_Yes == None:
            raise Exception('you have to select anyone')
    else:
        request.data['Isthe_student_memberofasports_teamatschool_Yes']= None

def check_Do_you_have_pets_at_home(request):
    Do_you_have_pets_at_home = request.data.get('Do_you_have_pets_at_home')
    Do_you_have_pets_at_home_Yes_Animal = request.data.get('Do_you_have_pets_at_home_Yes_Animal')
    Do_you_have_pets_at_home_Yes_Duration = request.data.get('Do_you_have_pets_at_home_Yes_Duration')
    if Do_you_have_pets_at_home == 'Yes':
        if Do_you_have_pets_at_home_Yes_Animal is None and Do_you_have_pets_at_home_Yes_Duration is None:
            raise Exception("You have to fill the option")
    else:
        request.data['Do_you_have_pets_at_home_Yes_Animal'] = None
        request.data['Do_you_have_pets_at_home_Yes_Duration'] = None

def check_Food_Group_Others(request):
    Is_the_student_intolerant_to_any_food_group = request.data.get('Is_the_student_intolerant_to_any_food_group')
    Food_Group_Other = request.data.get('Food_Group_Other')
    
    if Is_the_student_intolerant_to_any_food_group is None:
        request.data['Food_Group_Other'] = None
    else:
        selected_values = request.data.get('Is_the_student_intolerant_to_any_food_group', '').split(',')
        Other_value = None
        for i in selected_values:
            if i == 'Other':
                Other_value = Food_Group_Other
                if Food_Group_Other == None:
                    raise Exception('Please provide any text that needs to be filled in.')
        # request.data['Food_Group_Other']= Other_value

def check_Type_of_meal(request):
    Type_of_meal = request.data.get('Type_of_meal')
    Type_of_meal_Other = request.data.get('Type_of_meal_Other')
    if Type_of_meal == 'Other':
        if Type_of_meal_Other == None:
            raise Exception('Please provide any text that needs to be filled in.')
    else:
        request.data['Type_of_meal_Other'] = None

def check_Sleep_related_issues_Others(request):
    Does_the_student_have_any_sleep_related_issues = request.data.get('Does_the_student_have_any_sleep_related_issues')
    Does_the_student_have_any_sleep_related_issues_Yes = request.data.get('Does_the_student_have_any_sleep_related_issues_Yes')
    Sleep_related_issues_Other = request.data.get('Sleep_related_issues_Other')
    if Does_the_student_have_any_sleep_related_issues == 'Yes':
        if Does_the_student_have_any_sleep_related_issues_Yes == None:
            raise Exception('you have to select anyone')
   
        selected_values = request.data.get('Does_the_student_have_any_sleep_related_issues_Yes', '').split(',')
        Other_value = None
        for i in selected_values:
            if i == 'Other':
                Other_value = Sleep_related_issues_Other
                if Sleep_related_issues_Other == None:
                    raise Exception('Please provide any text that needs to be filled in.')
        request.data['Sleep_related_issues_Other']= Other_value
    else:
        request.data['Does_the_student_have_any_sleep_related_issues_Yes']= None
        request.data['Sleep_related_issues_Other']= None

def check_Social_personality_Others(request):
    How_would_you_describe_the_social_personality_ofthe_student = request.data.get('How_would_you_describe_the_social_personality_ofthe_student')
    Social_personality_Other = request.data.get('Social_personality_Other')
    if How_would_you_describe_the_social_personality_ofthe_student == 'Other':
        if Social_personality_Other == None:
            raise Exception('Please provide any text that needs to be filled in.')
    else:
        request.data['Social_personality_Other']= None

def check_Student_reaction_Others(request):
    How_would_you_best_describe_the_student_reaction_to_change = request.data.get('How_would_you_best_describe_the_student_reaction_to_change')
    Student_reaction_Other = request.data.get('Student_reaction_Other')
    if How_would_you_best_describe_the_student_reaction_to_change == 'Other':
        if Student_reaction_Other == None:
            raise Exception('Please provide any text that needs to be filled in.')
    else:
        request.data['Student_reaction_Other']= None

def check_Others(request):
    How_would_you_describe_student_rs_with_other_students = request.data.get('How_would_you_describe_student_rs_with_other_students')
    How_would_you_describe_student_rs_with_other_students_Other = request.data.get('How_would_you_describe_student_rs_with_other_students_Other')
    if How_would_you_describe_student_rs_with_other_students == 'Other':
        if How_would_you_describe_student_rs_with_other_students_Other == None:
            raise Exception('Please provide any text that needs to be filled in.')
    else:
        request.data['How_would_you_describe_student_rs_with_other_students_Other']= None

def check_Student_dissatisfied_Others(request):
    Isthe_student_significantly_dissatisfied_byany_following = request.data.get('Isthe_student_significantly_dissatisfied_byany_following')
    Student_dissatisfied_Other = request.data.get('Student_dissatisfied_Other')
    
    if Isthe_student_significantly_dissatisfied_byany_following is None:
        request.data['Student_dissatisfied_Other'] = None
    else:
        selected_values = Isthe_student_significantly_dissatisfied_byany_following.split(',')
        Other_value = None
        
        for i in selected_values:
            if i == 'Other':
                Other_value = Student_dissatisfied_Other
                if Student_dissatisfied_Other == None:
                    raise Exception('Please provide any text that needs to be filled in.')

        request.data['Student_dissatisfied_Other'] = Other_value

def check_Any_students_family_Others(request):
    Any_Ongoing_Illnesscondition_membersofthe_students_family = request.data.get('Any_Ongoing_Illnesscondition_membersofthe_students_family')
    Any_students_family_Other = request.data.get('Any_students_family_Other')

    if Any_Ongoing_Illnesscondition_membersofthe_students_family is None:
        request.data['Any_students_family_Other'] = None
    else:
        selected_values = Any_Ongoing_Illnesscondition_membersofthe_students_family.split(',')
        Other_value = None
        
        for i in selected_values:
            if i == 'Other':
                Other_value = Any_students_family_Other
                if Any_students_family_Other == None:
                    raise Exception('Please provide any text that needs to be filled in.')

        request.data['Any_students_family_Other'] = Other_value
     
def check_Any_Known_Allergies(request):
    Any_Known_Allergies = request.data.get('Any_Known_Allergies')
    Any_Known_Allergies_yes = request.data.get('Any_Known_Allergies_yes')
    if Any_Known_Allergies == 'Yes':
        if Any_Known_Allergies_yes == None:
            raise Exception('you have to select anyone')
    else:
        request.data['Any_Known_Allergies_yes']= None

def check_student_medicalissue_Past_Yes(request):
    Does_the_student_have_any_medicalissue_In_The_Past = request.data.get("Does_the_student_have_any_medicalissue_In_The_Past")
    Does_the_student_have_any_medicalissue_In_The_Past_Yes = request.data.get("Does_the_student_have_any_medicalissue_In_The_Past_Yes")
    if Does_the_student_have_any_medicalissue_In_The_Past == 'Yes':
        if Does_the_student_have_any_medicalissue_In_The_Past_Yes == None:
            raise Exception('you have to select anyone')     
    else:
        request.data['Does_the_student_have_any_medicalissue_In_The_Past_Yes'] = None

def check_student_medicalissue_Currently_Yes(request):
    Does_the_student_have_any_medicalissue_Currently = request.data.get("Does_the_student_have_any_medicalissue_Currently")
    Does_the_student_have_any_medicalissue_Currently_Yes = request.data.get("Does_the_student_have_any_medicalissue_Currently_Yes")
    if Does_the_student_have_any_medicalissue_Currently == 'Yes':
        if Does_the_student_have_any_medicalissue_Currently_Yes == None:
            raise Exception('you have to select anyone')     
    else:
        request.data['Does_the_student_have_any_medicalissue_Currently_Yes'] = None

def check_Do_you_have_health_insurance(request):
    Do_you_have_health_insurance = request.data.get('Do_you_have_health_insurance')
    Medical_Aid = request.data.get('Medical_Aid')
    Expiry_Date = request.data.get('Expiry_Date')
    Policy_Card = request.data.get('Policy_Card')
    if Do_you_have_health_insurance == 'Yes':
        if Medical_Aid == None or Expiry_Date == None or Policy_Card == None:
            raise Exception('You have to enter details')
        
    else:
        request.data['Medical_Aid'] = None
        request.data['Expiry_Date'] = None
        request.data['Policy_Card'] = None

def check_Alternate_MobileNumber(request):
    Alternate_MobileNumber = request.data.get('Alternate_MobileNumber')
    Belongs_To = request.data.get('Belongs_To')
    if Alternate_MobileNumber:
        if Belongs_To == None:
            raise Exception('Enter belongs to details')
        
    else:
        request.data['Belongs_To'] = None

def check_Secondary_Contact(request):
    Secondary_Contact = request.data.get('Secondary_Contact')
    Secondary_Contact_Belongs_To = request.data.get('Secondary_Contact_Belongs_To')
    Secondary_Contact_Full_Name = request.data.get('Secondary_Contact_Full_Name')
    Secondary_Contact_Belongs_To_Other = request.data.get('Secondary_Contact_Belongs_To_Other')
    if Secondary_Contact:
        if Secondary_Contact_Belongs_To == None or Secondary_Contact_Full_Name == None:
            raise Exception('Enter Secondary Contact details')
        if Secondary_Contact_Belongs_To == 'Other':
            if Secondary_Contact_Belongs_To_Other == None:
                raise Exception ('Please provide any text that needs to be filled in.')
        
    else:
        request.data['Secondary_Contact_Belongs_To'] = None
        request.data['Secondary_Contact_Full_Name'] = None
        request.data['Secondary_Contact_Belongs_To_Other'] = None

def check_Family_Doctor_Name(request):
    Family_Doctor_Name = request.data.get('Family_Doctor_Name')
    Doctor_Contact_Number = request.data.get('Doctor_Contact_Number')
    if Family_Doctor_Name:
        if Doctor_Contact_Number == None:
            raise Exception('Enter doctor details')
        
    else:
        request.data['Doctor_Contact_Number'] = None

def check_Does_the_student_have_regular_meal_at_school(request):
    Does_the_student_have_regular_meal_at_school = request.data.get('Does_the_student_have_regular_meal_at_school')
    Student_If_Yes_where_does_it_come_from = request.data.get('Student_If_Yes_where_does_it_come_from')
    Student_If_Other = request.data.get('Student_If_Other')
    
    if Does_the_student_have_regular_meal_at_school == 'Yes':
        if Student_If_Yes_where_does_it_come_from == None :
            raise Exception('Enter meal details')
        if Student_If_Yes_where_does_it_come_from == 'Other':
            if Student_If_Other == None:
                raise Exception ('Please provide any text that needs to be filled in.')
        
    else:
        request.data['Student_If_Yes_where_does_it_come_from'] = None
        request.data['Student_If_Other'] = None
       
def check_Does_the_student_have_any_significantly_close_friends(request):
    Does_the_student_have_any_significantly_close_friends = request.data.get('Does_the_student_have_any_significantly_close_friends')
    student_close_friends_yes_how_many_girls = request.data.get('student_close_friends_yes_how_many_girls')
    student_close_friends_yes_how_many_boys = request.data.get('student_close_friends_yes_how_many_boys')

    if Does_the_student_have_any_significantly_close_friends == 'Yes':
        if student_close_friends_yes_how_many_girls == None or student_close_friends_yes_how_many_boys == None:
            raise Exception('You have to enter details')
        
    else:
        request.data['student_close_friends_yes_how_many_girls'] = None
        request.data['student_close_friends_yes_how_many_boys'] = None
      