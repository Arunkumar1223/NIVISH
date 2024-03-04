from infoseek.models import InfoseekVerificationModel
import graphene



class ContactsType(graphene.ObjectType):

## Profile Information

    InfoseekId = graphene.Int()
    StudentFirstname = graphene.String()
    StudentDob = graphene.String()
    MothersFullname = graphene.String()
    Gender = graphene.String()
    BloodGroup = graphene.String()
    RhFactor = graphene.String()
    Uin = graphene.String()
    FathersFirstname = graphene.String()
    RegisteredEmailid = graphene.String()
    FamilyDoctorname = graphene.String()
    DoctorcontactNumber = graphene.String()
    

## Infoseek Information
    
    WhattypeofrecreationalactivitydoestheStudentenjoy = graphene.String()
    WhichofthefollowingactivitiesdoestheStudentenjoy = graphene.String()
    ActivitesOther = graphene.String()
    IsthestudentmemberofasportsteamatSchool = graphene.String()
    IsthestudentmemberofasportsteamatschoolYes = graphene.String()
    DoyouhavepetsatHome = graphene.String()
    DoyouhavepetsathomeyesAnimal = graphene.String()
    DoyouhavepetsathomeyesDuration = graphene.String()
    UsualnumberofMealsday = graphene.String()
    UsualnumberofSnacksday = graphene.String()
    WhatisthestudentsaverageFluidintake = graphene.String()
    TypeofMeal = graphene.String()
    TypeofmealOther = graphene.String()
    DoesthestudenthavebreakfastRegularly = graphene.String()
    DoesthestudenthaveregularmealatSchool = graphene.String()
    StudentIfyeswheredoesitcomefrom = graphene.String()
    StudentIfother = graphene.String()
    IsthestudentintoleranttoanyFoodgroup = graphene.String()
    FoodgroupOther = graphene.String()
    OnanaverageistheStudentfreshandrelaxednightsleep = graphene.String()
    DoestheStudenthaveanysleeprelatedissues = graphene.String()
    DoesthestudenthaveanysleeprelatedissuesYes = graphene.String()
    SleeprelatedissuesOther = graphene.String()
    WhatistheStudentsaveragelengthofsleeppernight = graphene.String()
    WhatisthestudentsnapcycleduringdayNap = graphene.String()
    HowwouldyoudescribethesocialpersonalityoftheStudent = graphene.String()
    SocialpersonalityOther = graphene.String()
    SpecifyiftheStudenthasanyirrationalfearsphobias = graphene.String()
    HowwouldyouratetheStudentsselfimageselfworth = graphene.String()
    HowwouldyourateStudentscooperationinhousedholdchores = graphene.String()
    HowwouldyoubestdescribetheStudentreactiontochange = graphene.String()
    StudentreactionOther = graphene.String()
    HowwouldyoudescribestudentrswithotherStudents = graphene.String()
    HowwouldyoudescribestudentrswithotherstudentsOther = graphene.String()
    DoestheStudenthaveanysignificantlyclosefriends = graphene.String()
    StudentclosefriendsyesHowmanygirls = graphene.String()
    StudentclosefriendsyesHowmanyboys = graphene.String()
    WhatisStudentgeneralopinionofschool = graphene.String()
    TheStudentgoestoschool = graphene.String()
    HowwouldyourateStudentoverallattendanceatschool = graphene.String()
    DoyouhaveconcernsfollowingrespecttotheStudent = graphene.String()
    HowwouldyouratetheStudentoverallphysicalhealth = graphene.String()
    IstheStudentsschoolperformanceaffectedbyanyfollowing = graphene.String()
    IstheStudentsignificantlydissatisfiedbyanyfollowing = graphene.String()
    StudentdissatisfiedOther = graphene.String()
    AnyOngoingillnessconditionmembersofthestudentsfamily = graphene.String()
    AnystudentsfamilyOther = graphene.String()
    DoesthestudenthaveanymedicalissueinthePast = graphene.String()
    DoesthestudenthaveanymedicalissueinthepastYes = graphene.String()
    PastMedication = graphene.String()
    DoesthestudenthaveanymedicalissueCurrently = graphene.String()
    DoesthestudenthaveanymedicalissuecurrentlyYes = graphene.String()
    CurrentMedication = graphene.String()
    # BcgDose0 = graphene.String()
    # BcgDose1 = graphene.String()
    # BcgDose2 = graphene.String()
    # BcgDose3 = graphene.String()
    # BcgDose4 = graphene.String()
    # ChickenpoxDose0 = graphene.String()
    # ChickenpoxDose1 = graphene.String()
    # ChickenpoxDose2 = graphene.String()
    # ChickenpoxDose3 = graphene.String()
    # ChickenpoxDose4 = graphene.String()
    # CholeraDose0 = graphene.String()
    # CholeraDose1 = graphene.String()
    # CholeraDose2 = graphene.String()
    # CholeraDose3 = graphene.String()
    # CholeraDose4 = graphene.String()
    # CovidvaccinationDose0 = graphene.String()
    # CovidvaccinationDose1 = graphene.String()
    # CovidvaccinationDose2 = graphene.String()
    # CovidvaccinationDose3 = graphene.String()
    # CovidvaccinationDose4 = graphene.String()
    # DptDose0 = graphene.String()
    # DptDose1 = graphene.String()
    # DptDose2 = graphene.String()
    # DptDose3 = graphene.String()
    # DptDose4 = graphene.String()
    # DtDose0 = graphene.String()
    # DtDose1 = graphene.String()
    # DtDose2 = graphene.String()
    # DtDose3 = graphene.String()
    # DtDose4 = graphene.String()

## Emergency Contact
    
    PrimaryContact = graphene.String()
    PrimaryContactbelongsto = graphene.String()
    PrimarycontactbelongstoOther = graphene.String()
    PrimarycontactFullname = graphene.String()
    SecondaryContact = graphene.String()
    SecondaryContactbelongsto = graphene.String()
    SecondarycontactbelongstoOther = graphene.String()
    SecondarycontactFullname = graphene.String()
    

class GraphqlInfoseekGet(graphene.ObjectType):
    list_contact = graphene.List(ContactsType)
    read_contact = graphene.List(ContactsType, InfoseekId=graphene.Int())

    def resolve_list_contact(root, info):
        # Retrieve all records
        queryset = InfoseekVerificationModel.objects.all()

        # Convert queryset to a list of ContactsType objects
        return [ContactsType(InfoseekId=item.InfoseekId, StudentFirstname=item.Student_FirstName, StudentDob=item.Student_DOB, MothersFullname= item.Mothers_FullName, Gender= item.Gender,BloodGroup= item.BloodGroup,RhFactor= item.Rh_Factor,Uin= item.UIN,
                             FathersFirstname= item.Fathers_FirstName, RegisteredEmailid= item.Registered_EmailId,
                             FamilyDoctorname= item.Family_Doctor_Name, DoctorcontactNumber= item.Doctor_Contact_Number,
                             WhattypeofrecreationalactivitydoestheStudentenjoy=item.What_typeof_recreational_activity_doesthestudentenjoy,
                             WhichofthefollowingactivitiesdoestheStudentenjoy=item.Which_ofthe_following_activities_doesthestudentenjoy,
                             ActivitesOther=item.Activites_Other,IsthestudentmemberofasportsteamatSchool=item.Isthe_student_memberofasports_teamatschool,
                             IsthestudentmemberofasportsteamatschoolYes=item.Isthe_student_memberofasports_teamatschool_Yes,
                             DoyouhavepetsatHome=item.Do_you_have_pets_at_home,DoyouhavepetsathomeyesAnimal=item.Do_you_have_pets_at_home_Yes_Animal,
                             DoyouhavepetsathomeyesDuration=item.Do_you_have_pets_at_home_Yes_Duration,UsualnumberofMealsday=item.Usual_numberof_mealsday,
                             UsualnumberofSnacksday=item.Usual_numberof_snacksday,WhatisthestudentsaverageFluidintake=item.What_is_the_students_average_fluid_intake,
                             TypeofMeal=item.Type_of_meal,TypeofmealOther=item.Type_of_meal_Other,DoesthestudenthavebreakfastRegularly=item.Does_the_student_have_breakfast_regularly,
                             DoesthestudenthaveregularmealatSchool=item.Does_the_student_have_regular_meal_at_school,
                             StudentIfyeswheredoesitcomefrom=item.Student_If_Yes_where_does_it_come_from,
                             StudentIfother=item.Student_If_Other,IsthestudentintoleranttoanyFoodgroup=item.Is_the_student_intolerant_to_any_food_group,
                             FoodgroupOther=item.Food_Group_Other,OnanaverageistheStudentfreshandrelaxednightsleep=item.On_an_average_isthe_student_freshandrelaxed_night_sleep,
                             DoestheStudenthaveanysleeprelatedissues=item.Does_the_student_have_any_sleep_related_issues,
                             DoesthestudenthaveanysleeprelatedissuesYes=item.Does_the_student_have_any_sleep_related_issues_Yes,
                             SleeprelatedissuesOther=item.Sleep_related_issues_Other,WhatistheStudentsaveragelengthofsleeppernight=item.What_is_the_students_average_length_of_sleep_per_night,
                             WhatisthestudentsnapcycleduringdayNap=item.What_is_the_students_nap_cycle_during_day_Nap,
                             HowwouldyoudescribethesocialpersonalityoftheStudent=item.How_would_you_describe_the_social_personality_ofthe_student,
                             SocialpersonalityOther=item.Social_personality_Other,SpecifyiftheStudenthasanyirrationalfearsphobias=item.Specify_if_the_student_has_any_irrational_fears_phobias,
                             HowwouldyouratetheStudentsselfimageselfworth=item.How_would_you_rate_the_students_self_image_self_worth,
                             HowwouldyourateStudentscooperationinhousedholdchores=item.How_would_you_rate_students_cooperation_in_housedhold_chores,
                             HowwouldyoubestdescribetheStudentreactiontochange=item.How_would_you_best_describe_the_student_reaction_to_change,
                             StudentreactionOther=item.Student_reaction_Other,HowwouldyoudescribestudentrswithotherStudents=item.How_would_you_describe_student_rs_with_other_students,
                             HowwouldyoudescribestudentrswithotherstudentsOther=item.How_would_you_describe_student_rs_with_other_students_Other,
                             DoestheStudenthaveanysignificantlyclosefriends=item.Does_the_student_have_any_significantly_close_friends,
                             StudentclosefriendsyesHowmanygirls=item.student_close_friends_yes_how_many_girls,
                             StudentclosefriendsyesHowmanyboys=item.student_close_friends_yes_how_many_boys,
                             WhatisStudentgeneralopinionofschool=item.What_is_student_general_opinion_of_school,
                             TheStudentgoestoschool=item.The_student_goes_to_school,
                             HowwouldyourateStudentoverallattendanceatschool=item.How_would_you_rate_student_overall_attendance_at_school,
                             DoyouhaveconcernsfollowingrespecttotheStudent=item.Do_you_have_concerns_following_respect_tothe_student,
                             HowwouldyouratetheStudentoverallphysicalhealth=item.How_would_you_rate_the_student_overall_physical_health,
                             IstheStudentsschoolperformanceaffectedbyanyfollowing=item.Isthe_students_school_performance_affected_by_any_following,
                             IstheStudentsignificantlydissatisfiedbyanyfollowing=item.Isthe_student_significantly_dissatisfied_byany_following,
                             StudentdissatisfiedOther=item.Student_dissatisfied_Other,
                             AnyOngoingillnessconditionmembersofthestudentsfamily=item.Any_Ongoing_Illnesscondition_membersofthe_students_family,
                             AnystudentsfamilyOther=item.Any_students_family_Other,DoesthestudenthaveanymedicalissueinthePast=item.Does_the_student_have_any_medicalissue_In_The_Past,
                             DoesthestudenthaveanymedicalissueinthepastYes=item.Does_the_student_have_any_medicalissue_In_The_Past_Yes,PastMedication=item.Past_Medication,
                             DoesthestudenthaveanymedicalissueCurrently=item.Does_the_student_have_any_medicalissue_Currently,
                             DoesthestudenthaveanymedicalissuecurrentlyYes=item.Does_the_student_have_any_medicalissue_Currently_Yes,
                             CurrentMedication=item.Current_Medication,PrimaryContact=item.Primary_Contact,PrimaryContactbelongsto=item.Primary_Contact_Belongs_To,
                             PrimarycontactbelongstoOther=item.Primary_Contact_Belongs_To_Other,PrimarycontactFullname=item.Primary_Contact_Full_Name,
                             SecondaryContact=item.Secondary_Contact,SecondaryContactbelongsto=item.Secondary_Contact_Belongs_To,
                             SecondarycontactbelongstoOther=item.Secondary_Contact_Belongs_To_Other,SecondarycontactFullname=item.Secondary_Contact_Full_Name) for item in queryset]
    
        # return [ContactsType(VoterId=item.VoterId, FirstName=item.FirstName, Constituency=item.Constituency, Name=item.Name, Guardian=item.Guardian, Home=item.Home, Age=item.Age, LastName=item.LastName, IvinId=item.ivin_id, Gender=item.Gender, State=item.State, District=item.District, PollingStationNumber=item.Polling_Station_Number, PollingStationName=item.Polling_Station_Name, PollingStationLocation=item.Polling_Station_Location, CreatedOn=item.CreatedOn, UpdatedOn=item.UpdatedOn, AssemblyConstituencyNoAndName=item.Assembly_Constituency_No_and_Name, SectionNoAndName=item.Section_No_and_Name, Mandal=item.Mandal) for item in queryset]

    def resolve_read_contact(root, info, **kwargs):
        # Define an empty filter dictionary
        filter_kwargs = {}
        filter_kwargs1 = {}

        # Add the 'Constituency' filter if the 'Name' argument is provided
      
        if 'InfoseekId' in kwargs:
            filter_kwargs['InfoseekId'] = kwargs['InfoseekId']

        # Apply the filters to the queryset
        filter_kwargs1['InfoseekId'] = 1
        print("Mani")

        queryset = InfoseekVerificationModel.objects.filter(**filter_kwargs)
        queryset1 = InfoseekVerificationModel.objects.filter(**filter_kwargs1)
        print(queryset1)
        return [ContactsType(InfoseekId=item.InfoseekId, StudentFirstname=item.Student_FirstName, StudentDob=item.Student_DOB, MothersFullname= item.Mothers_FullName, Gender= item.Gender,BloodGroup= item.BloodGroup,RhFactor= item.Rh_Factor,Uin= item.UIN,
                             FathersFirstname= item.Fathers_FirstName, RegisteredEmailid= item.Registered_EmailId,
                             FamilyDoctorname= item.Family_Doctor_Name, DoctorcontactNumber= item.Doctor_Contact_Number,
                             WhattypeofrecreationalactivitydoestheStudentenjoy=item.What_typeof_recreational_activity_doesthestudentenjoy,
                             WhichofthefollowingactivitiesdoestheStudentenjoy=item.Which_ofthe_following_activities_doesthestudentenjoy,
                             ActivitesOther=item.Activites_Other,IsthestudentmemberofasportsteamatSchool=item.Isthe_student_memberofasports_teamatschool,
                             IsthestudentmemberofasportsteamatschoolYes=item.Isthe_student_memberofasports_teamatschool_Yes,
                             DoyouhavepetsatHome=item.Do_you_have_pets_at_home,DoyouhavepetsathomeyesAnimal=item.Do_you_have_pets_at_home_Yes_Animal,
                             DoyouhavepetsathomeyesDuration=item.Do_you_have_pets_at_home_Yes_Duration,UsualnumberofMealsday=item.Usual_numberof_mealsday,
                             UsualnumberofSnacksday=item.Usual_numberof_snacksday,WhatisthestudentsaverageFluidintake=item.What_is_the_students_average_fluid_intake,
                             TypeofMeal=item.Type_of_meal,TypeofmealOther=item.Type_of_meal_Other,DoesthestudenthavebreakfastRegularly=item.Does_the_student_have_breakfast_regularly,
                             DoesthestudenthaveregularmealatSchool=item.Does_the_student_have_regular_meal_at_school,
                             StudentIfyeswheredoesitcomefrom=item.Student_If_Yes_where_does_it_come_from,
                             StudentIfother=item.Student_If_Other,IsthestudentintoleranttoanyFoodgroup=item.Is_the_student_intolerant_to_any_food_group,
                             FoodgroupOther=item.Food_Group_Other,OnanaverageistheStudentfreshandrelaxednightsleep=item.On_an_average_isthe_student_freshandrelaxed_night_sleep,
                             DoestheStudenthaveanysleeprelatedissues=item.Does_the_student_have_any_sleep_related_issues,
                             DoesthestudenthaveanysleeprelatedissuesYes=item.Does_the_student_have_any_sleep_related_issues_Yes,
                             SleeprelatedissuesOther=item.Sleep_related_issues_Other,WhatistheStudentsaveragelengthofsleeppernight=item.What_is_the_students_average_length_of_sleep_per_night,
                             WhatisthestudentsnapcycleduringdayNap=item.What_is_the_students_nap_cycle_during_day_Nap,
                             HowwouldyoudescribethesocialpersonalityoftheStudent=item.How_would_you_describe_the_social_personality_ofthe_student,
                             SocialpersonalityOther=item.Social_personality_Other,SpecifyiftheStudenthasanyirrationalfearsphobias=item.Specify_if_the_student_has_any_irrational_fears_phobias,
                             HowwouldyouratetheStudentsselfimageselfworth=item.How_would_you_rate_the_students_self_image_self_worth,
                             HowwouldyourateStudentscooperationinhousedholdchores=item.How_would_you_rate_students_cooperation_in_housedhold_chores,
                             HowwouldyoubestdescribetheStudentreactiontochange=item.How_would_you_best_describe_the_student_reaction_to_change,
                             StudentreactionOther=item.Student_reaction_Other,HowwouldyoudescribestudentrswithotherStudents=item.How_would_you_describe_student_rs_with_other_students,
                             HowwouldyoudescribestudentrswithotherstudentsOther=item.How_would_you_describe_student_rs_with_other_students_Other,
                             DoestheStudenthaveanysignificantlyclosefriends=item.Does_the_student_have_any_significantly_close_friends,
                             StudentclosefriendsyesHowmanygirls=item.student_close_friends_yes_how_many_girls,
                             StudentclosefriendsyesHowmanyboys=item.student_close_friends_yes_how_many_boys,
                             WhatisStudentgeneralopinionofschool=item.What_is_student_general_opinion_of_school,
                             TheStudentgoestoschool=item.The_student_goes_to_school,
                             HowwouldyourateStudentoverallattendanceatschool=item.How_would_you_rate_student_overall_attendance_at_school,
                             DoyouhaveconcernsfollowingrespecttotheStudent=item.Do_you_have_concerns_following_respect_tothe_student,
                             HowwouldyouratetheStudentoverallphysicalhealth=item.How_would_you_rate_the_student_overall_physical_health,
                             IstheStudentsschoolperformanceaffectedbyanyfollowing=item.Isthe_students_school_performance_affected_by_any_following,
                             IstheStudentsignificantlydissatisfiedbyanyfollowing=item.Isthe_student_significantly_dissatisfied_byany_following,
                             StudentdissatisfiedOther=item.Student_dissatisfied_Other,
                             AnyOngoingillnessconditionmembersofthestudentsfamily=item.Any_Ongoing_Illnesscondition_membersofthe_students_family,
                             AnystudentsfamilyOther=item.Any_students_family_Other,DoesthestudenthaveanymedicalissueinthePast=item.Does_the_student_have_any_medicalissue_In_The_Past,
                             DoesthestudenthaveanymedicalissueinthepastYes=item.Does_the_student_have_any_medicalissue_In_The_Past_Yes,
                             PrimarycontactbelongstoOther=item.Primary_Contact_Belongs_To_Other,PrimarycontactFullname=item.Primary_Contact_Full_Name,
                             SecondaryContact=item.Secondary_Contact,SecondaryContactbelongsto=item.Secondary_Contact_Belongs_To,
                             SecondarycontactbelongstoOther=item.Secondary_Contact_Belongs_To_Other,SecondarycontactFullname=item.Secondary_Contact_Full_Name) for item in queryset]


        # Convert queryset to a list of ContactsType objects
        # return [ContactsType(VoterId=item.VoterId, FirstName=item.FirstName, Constituency=item.Constituency, Name=item.Name, Guardian=item.Guardian, Home=item.Home, Age=item.Age, LastName=item.LastName, IvinId=item.ivin_id, Gender=item.Gender, State=item.State, District=item.District, PollingStationNumber=item.Polling_Station_Number, PollingStationName=item.Polling_Station_Name, PollingStationLocation=item.Polling_Station_Location, CreatedOn=item.CreatedOn, UpdatedOn=item.UpdatedOn, AssemblyConstituencyNoAndName=item.Assembly_Constituency_No_and_Name, SectionNoAndName=item.Section_No_and_Name, Mandal=item.Mandal) for item in queryset]

schema = graphene.Schema(query=GraphqlInfoseekGet)