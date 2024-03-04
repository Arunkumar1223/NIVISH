import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from ..serializers import *
from ..models import *
from errormessage import Errormessage
from Multiselect.multiselectLists import *
from Multiselect.multiselectFunction import *
from Validations.infosek_Validations import *
# from rest_framework.decorators import parser_classes
# from rest_framework.parsers import MultiPartParser


# @parser_classes((MultiPartParser,))
class DynamicSerializerMixin:
    def get_serializer_class(self):
        # Implement your logic to determine the serializer class dynamically
        if self.custom_property == "section2":
            return InfoseekVerificationSerializers
        elif self.custom_property == "section3":
            return InfoseekVerificationSerializers2
        elif self.custom_property == "section4":
            return InfoseekVerificationSerializers3
        elif self.custom_property == "section5":
            return InfoseekVerificationSerializers4
        elif self.custom_property == "section6":
            return InfoseekVerificationSerializers5
        elif self.custom_property == "section7":
            return InfoseekVerificationSerializers6
        elif self.custom_property == "section8":
            return InfoseekVerificationSerializers7
        elif self.custom_property == "section9":
            return InfoseekVerificationSerializers8
        elif self.custom_property == "section10":
            return InfoseekVerificationSerializers9
        elif self.custom_property == "section11":
            return InfoseekVerificationSerializers10
        elif self.custom_property == "section12":
            return InfoseekVerificationSerializers11
        elif self.custom_property == "section13":
            return InfoseekVerificationSerializers12
        elif self.custom_property == "section14":
            return InfoseekVerificationSerializers13
        # elif self.custom_property == "InfoseekNote":
        #     return InfoseekVerificationNoteSerializers
        


class InfoseekVerfication2(DynamicSerializerMixin, generics.GenericAPIView):

    """Here We're updating the Student Information Infoseek based on InfoseekId
            (Here InfoseekId is nothing but Student Registration id)
                (Table_Name:'Infoseek')"""
    
    custom_property = None
    def __init__(self, *args, **kwargs):
        # Capture any custom keyword arguments passed during instantiation
        self.custom_property = kwargs.pop('custom_property', None)
        super().__init__(*args, **kwargs)

  
    

    def put(self, request, InfoseekId):
        print("put")
        print(self.request.path_info)
        try:
            
            r = InfoseekVerificationModel.objects.get(InfoseekId=InfoseekId)
            data = request.data
            field_lists = {}
            if self.custom_property == "section2":
                Student_FirstName = request.data.get('Student_FirstName')
                Student_DOB = request.data.get('Student_DOB')
              
                Student_MiddleName1 = request.data.get('Student_MiddleName1')
                Student_MiddleName2 = request.data.get('Student_MiddleName2')
                Student_LastName = request.data.get('Student_LastName')
                Gender = request.data.get('Gender')
                BloodGroup = request.data.get('BloodGroup')
                Rh_Factor = request.data.get('Rh_Factor')
                Mothers_FirstName = request.data.get('Mothers_FirstName')
                Mothers_MiddleName1 = request.data.get('Mothers_MiddleName1')
                Mothers_MiddleName2 = request.data.get('Mothers_MiddleName2')
                Mothers_LastName = request.data.get('Mothers_LastName')
                Fathers_FirstName = request.data.get('Fathers_FirstName')
                Fathers_MiddleName1 = request.data.get('Fathers_MiddleName1')
                Fathers_MiddleName2 = request.data.get('Fathers_MiddleName2')
                Fathers_LastName = request.data.get('Fathers_LastName')

                master_data = InfoseekMasterModel.objects.get(Student_First_Name=Student_FirstName,Date_of_Birth=Student_DOB)
                print(master_data,"iiiiiii")
                
                master_data.Student_Middle_Name_1 = Student_MiddleName1
                master_data.Student_Middle_Name_2 = Student_MiddleName2
                master_data.Student_Last_Name = Student_LastName
                master_data.Gender = Gender
                master_data.Blood_Group = BloodGroup
                master_data.RH_Factor = Rh_Factor
                master_data.Mothers_First_Name = Mothers_FirstName
                master_data.Mothers_Middle_Name = Mothers_MiddleName1
                master_data.Mothers_Middle_Name = Mothers_MiddleName2
                master_data.Fathers_First_Name = Fathers_FirstName
                master_data.Fathers_Middle_Name = Fathers_MiddleName1
                master_data.Fathers_Middle_Name = Fathers_MiddleName2
                master_data.Mothers_Last_Name = Mothers_LastName
                master_data.Fathers_Last_Name = Fathers_LastName

                master_data.save()
               
                check_following_information_providedby(request)
                check_Mothers_Ethnicity(request)
                check_Fathers_Ethnicity(request)

                serializer_class = InfoseekVerificationSerializers

            elif self.custom_property == "section3":

                check_Do_you_have_health_insurance(request)

                serializer_class = InfoseekVerificationSerializers2

            elif self.custom_property == "section4":
                
                # print(r.Student_FirstName)
                # print(r.Student_DOB)

                Building_Name = request.data.get('Building_Name')
                Street_No = request.data.get('Street_No')
                City = request.data.get('City')
                Country = request.data.get('Country')
                State = request.data.get('State')
                Zip_Code = request.data.get('Zip_Code')

                master_data = InfoseekMasterModel.objects.get(Student_First_Name=r.Student_FirstName,Date_of_Birth=r.Student_DOB)
                master_data.Address_Building = Building_Name
                master_data.Adress_Street = Street_No
                master_data.City = City
                master_data.Country = Country
                master_data.State = State
                master_data.Zip = Zip_Code

                master_data.save()

                check_Alternate_MobileNumber(request)

                serializer_class = InfoseekVerificationSerializers3

            elif self.custom_property == "section5":

                check_Primary_Contact_Belongs(request)
                check_Secondary_Contact(request)
                check_Family_Doctor_Name(request)
                
                serializer_class = InfoseekVerificationSerializers4
                
            elif self.custom_property == "section6":

                check_Activites_Others(request)
                check_Isthe_student_memberofasports_teamatschool(request)
                check_Do_you_have_pets_at_home(request)       
                field_lists = {
                    'Which_ofthe_following_activities_doesthestudentenjoy': following_activities_student_list,
                    }
                
                serializer_class = InfoseekVerificationSerializers5

            elif self.custom_property == "section7":

                check_Does_the_student_have_regular_meal_at_school(request)
                check_Food_Group_Others(request)
                check_Type_of_meal(request)

                field_lists = {
                    'Is_the_student_intolerant_to_any_food_group': Student_intolerant_food_group_list,
                }

                serializer_class = InfoseekVerificationSerializers6

            elif self.custom_property == "section8":
                    
                check_Sleep_related_issues_Others(request)
                field_lists = {
                    'Does_the_student_have_any_sleep_related_issues_Yes': Student_sleep_related_issues_list
                }

                serializer_class = InfoseekVerificationSerializers7

            elif self.custom_property == "section9":

                check_Social_personality_Others(request)
                check_Student_reaction_Others(request)
                check_Others(request)
                check_Does_the_student_have_any_significantly_close_friends(request)

                serializer_class = InfoseekVerificationSerializers8

            elif self.custom_property == "section10":
                serializer_class = InfoseekVerificationSerializers9
            elif self.custom_property == "section11":
                check_Student_dissatisfied_Others(request)
                field_lists = {
                    'Do_you_have_concerns_following_respect_tothe_student' : Concerns_following_respect_student_list,
                    'Isthe_students_school_performance_affected_by_any_following' : Students_performance_affected_list,
                    'Isthe_student_significantly_dissatisfied_byany_following' : Student_significantly_dissatisfied_list
                }
                serializer_class = InfoseekVerificationSerializers10
            elif self.custom_property == "section12":
                check_Any_students_family_Others(request)
                field_lists = {
                    'Any_Ongoing_Illnesscondition_membersofthe_students_family' : Any_Ongoing_Illnesscondition_students_list
                }
                serializer_class = InfoseekVerificationSerializers11
            elif self.custom_property == "section13":
                check_student_medicalissue_Past_Yes(request)
                check_student_medicalissue_Currently_Yes(request)
                check_Any_Known_Allergies(request)
                field_lists = {
                    'Does_the_student_have_any_medicalissue_In_The_Past_Yes' : Student_medicalissue_Current_Past_Yes_list,
                    'Does_the_student_have_any_medicalissue_Currently_Yes' : Student_medicalissue_Current_Past_Yes_list
                }
                serializer_class = InfoseekVerificationSerializers12

            elif self.custom_property == "section14":
                serializer_class = InfoseekVerificationSerializers13
                
            
            
            validation_result = multiselect.check_field_lists(data, field_lists)
            if validation_result is not None:
                return validation_result
            
                
            serializer = serializer_class(r, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()               
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = serializer.data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)