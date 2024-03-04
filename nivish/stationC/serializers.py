from rest_framework import serializers
from .models import *
from datetime import date
import datetime


class StationCSerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationCModel
        fields = ['HCID','HCPID','InfoseekId','EntryTime','Problem_reading_books', 'Problem_reading_Blackboard', 
                  'Night_Vision', 'Vision_Corrected', 'Vision_Corrected_Yes']

    def create(self, validated_data):

        infoseek_data = validated_data['InfoseekId']
        today = date.today()
        age = today.year - infoseek_data.Student_DOB.year - ((today.month, today.day) < (infoseek_data.Student_DOB.month, infoseek_data.Student_DOB.day))
        print(age)

        # Problem_reading_books
        if validated_data['Problem_reading_books']:
            if validated_data['Problem_reading_books'] == "Yes" or "No":
                if age < 2:
                    raise Exception("No need to enter Problem_reading_books")
        # Problem_reading_Blackboard        
        if validated_data['Problem_reading_Blackboard']:
            if validated_data['Problem_reading_Blackboard'] == "Yes" or "No":
                if age < 2:
                    raise Exception("No need to enter Problem_reading_Blackboard") 
        # Night_Vision        
        if validated_data['Night_Vision']:
            if validated_data['Night_Vision'] == "Normal" or "Abnormal":
                if age < 5:
                    raise Exception("No need to enter Night_Vision") 
        # Vision_Corrected        
        if validated_data['Vision_Corrected']:
            if validated_data['Vision_Corrected'] == "Yes" or "No":
                if validated_data['Vision_Corrected'] == "Yes":
                    if validated_data['Vision_Corrected'] == "Glasses" or "Lenses" or "Surgical":
                        if age < 2:
                            raise Exception("No need to enter Vision_Corrected") 
            else:
                if age < 2:
                        raise Exception("No need to enter Vision_Corrected")

        user = StationCModel.objects.create(HCID=validated_data['HCID'],
                                       HCPID=validated_data['HCPID'],
                                       InfoseekId=validated_data['InfoseekId'],
                                       EntryTime = validated_data['EntryTime'],
                                       Problem_reading_books = validated_data['Problem_reading_books'],
                                       Problem_reading_Blackboard = validated_data['Problem_reading_Blackboard'],
                                       Night_Vision = validated_data['Night_Vision'],
                                       Vision_Corrected = validated_data['Vision_Corrected'],
                                       Vision_Corrected_Yes = validated_data['Vision_Corrected_Yes'],
                                        )
        user.save()
        return user

class GetStationCPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationCModel
        fields = ['id','StationID','HCID','HCPID','InfoseekId','EntryTime','Problem_reading_books', 'Problem_reading_Blackboard', 
                  'Night_Vision', 'Vision_Corrected', 'Vision_Corrected_Yes']


class UpdateStationCSerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationCModel
        fields = ['HCID','HCPID','InfoseekId','Problem_reading_books', 'Problem_reading_Blackboard', 
                  'Night_Vision', 'Vision_Corrected', 'Vision_Corrected_Yes','Reviewed_By','Reviewed_On']


        
class StationCSerializers2(serializers.ModelSerializer):
    class Meta:
        model = StationCModel
        fields = ['id', 'Extra_Ocular_Right_Normal_Eye_Movement','Extra_Ocular_Right_Strabismus','Extra_Ocular_Right_Drooping_Lid',
                  'Extra_Ocular_Right_Restricted_Mobility','Extra_Ocular_Right_Nystagmus',
                  'Extra_Ocular_Right_Bulging','Extra_Ocular_Left_Normal_Eye_Movement','Extra_Ocular_Left_Strabismus',
                  'Extra_Ocular_Left_Drooping_Lid','Extra_Ocular_Left_Restricted_Mobility','Extra_Ocular_Left_Nystagmus','Extra_Ocular_Left_Bulging','Reviewed_By',
                  'Reviewed_On']        
        

class StationCSerializers3(serializers.ModelSerializer):
    class Meta:
        model = StationCModel
        fields = ['id','Visually_Challenged_Right_Eye','Visually_Challenged_Right_Eye_Enucleation','Visually_Challenged_Right_Eye_Enucleation_When_removed','Visually_Challenged_Right_Eye_Enucleation_Why_removed','Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other','VC_Right_Eye_Enucleation_Artificial_Eye_Used',
        'Visually_Challenged_Right_Eye_Enucleation_No','Visually_Challenged_Right_Eye_Enucleation_Cataract','Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity','Visually_Challenged_Right_Eye_Enucleation_Glaucoma','Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi',
        'Visually_Challenged_Left_Eye','Visually_Challenged_Left_Eye_Enucleation','Visually_Challenged_Left_Eye_Enucleation_When_removed','Visually_Challenged_Left_Eye_Enucleation_Why_removed',
        'Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other','VC_Left_Eye_Enucleation_Artificial_Eye_Used',
        'Visually_Challenged_Left_Eye_Enucleation_No','Visually_Challenged_Left_Eye_Enucleation_Cataract','Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity','Visually_Challenged_Left_Eye_Enucleation_Glaucoma','Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi','Reviewed_By','Reviewed_On']

    def create(self, validated_data):
        # Assuming Infoseek is related to StationCModel through a ForeignKey
        infoseek_data = validated_data.get('id')  # Replace 'infoseek' with the actual related field name

        if infoseek_data:
            dob = infoseek_data.get('Student_DOB')
            if dob:
                today = date.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                print(age, "age")

        # Visually_Challenged_Right_Eye
        if validated_data['Visually_Challenged_Right_Eye'] == "Yes" or "No":               
            if age < 2:
                raise Exception("No need to enter Visually_Challenged_Right_Eye") 
            
        # Visually_Challenged_Left_Eye
        if validated_data['Visually_Challenged_Left_Eye'] == "Yes" or "No":               
            if age < 2:
                raise Exception("No need to enter Visually_Challenged_Left_Eye")

        user = StationCModel.objects.create(id=validated_data['id'],
                                       Visually_Challenged_Right_Eye=validated_data['Visually_Challenged_Right_Eye'],
                                       Visually_Challenged_Right_Eye_Enucleation=validated_data['Visually_Challenged_Right_Eye_Enucleation'],
                                       Visually_Challenged_Right_Eye_Enucleation_When_removed = validated_data['Visually_Challenged_Right_Eye_Enucleation_When_removed'],
                                       Visually_Challenged_Right_Eye_Enucleation_Why_removed = validated_data['Visually_Challenged_Right_Eye_Enucleation_Why_removed'],
                                       Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other = validated_data['Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other'],
                                       VC_Right_Eye_Enucleation_Artificial_Eye_Used = validated_data['VC_Right_Eye_Enucleation_Artificial_Eye_Used'],
                                       Visually_Challenged_Right_Eye_Enucleation_No = validated_data['Visually_Challenged_Right_Eye_Enucleation_No'],
                                       Visually_Challenged_Right_Eye_Enucleation_Cataract = validated_data['Visually_Challenged_Right_Eye_Enucleation_Cataract'],
                                       Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity = validated_data['Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity'],
                                       Visually_Challenged_Right_Eye_Enucleation_Glaucoma = validated_data['Visually_Challenged_Right_Eye_Enucleation_Glaucoma'],
                                       Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi = validated_data['Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi'],
                                       Visually_Challenged_Left_Eye = validated_data['Visually_Challenged_Left_Eye'],
                                       Visually_Challenged_Left_Eye_Enucleation = validated_data['Visually_Challenged_Left_Eye_Enucleation'],
                                       Visually_Challenged_Left_Eye_Enucleation_When_removed = validated_data['Visually_Challenged_Left_Eye_Enucleation_When_removed'],
                                       Visually_Challenged_Left_Eye_Enucleation_Why_removed = validated_data['Visually_Challenged_Left_Eye_Enucleation_Why_removed'],
                                       Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other = validated_data['Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other'],
                                       VC_Left_Eye_Enucleation_Artificial_Eye_Used = validated_data['VC_Left_Eye_Enucleation_Artificial_Eye_Used'],
                                       Visually_Challenged_Left_Eye_Enucleation_No = validated_data['Visually_Challenged_Left_Eye_Enucleation_No'],
                                       Visually_Challenged_Left_Eye_Enucleation_Cataract = validated_data['Visually_Challenged_Left_Eye_Enucleation_Cataract'],
                                       Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity = validated_data['Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity'],
                                       Visually_Challenged_Left_Eye_Enucleation_Glaucoma = validated_data['Visually_Challenged_Left_Eye_Enucleation_Glaucoma'],
                                       Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi = validated_data['Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi'],
                                       Reviewed_By = validated_data['Reviewed_By'],
                                       Reviewed_On = validated_data['Reviewed_On'],
                                       
                                        )
        user.save()
        return user


class StationCSerializers4(serializers.ModelSerializer):
    class Meta:
        model = StationCModel
        fields = ['id','Visual_Acuity','Visual_Acuity_With_Lenses_Distant_Vision_Left','Visual_Acuity_With_Lenses_Distant_Vision_Right','Visual_Acuity_With_Lenses_Near_Vision_Left','Visual_Acuity_With_Lenses_Near_Vision_Right',
        'Visual_Acuity_without_Lenses_Distant_Vision_Left','Visual_Acuity_without_Lenses_Distant_Vision_Right','Visual_Acuity_without_Lenses_Near_Vision_Left','Visual_Acuity_without_Lenses_Near_Vision_Right',
        'Visual_Acuity_Color_Blindness','Visual_Acuity_Color_Blindness_Yes','Reviewed_By','Reviewed_On']

    # def create(self, validated_data):

    #     infoseek_data = validated_data['InfoseekId']
    #     today = date.today()
    #     age = today.year - infoseek_data.Student_DOB.year - ((today.month, today.day) < (infoseek_data.Student_DOB.month, infoseek_data.Student_DOB.day))
    #     print(age)

    #     # Visually_Challenged_Right_Eye
    #     if validated_data['Visually_Challenged_Right_Eye']:               
    #         if age < 2:
    #             raise Exception("No need to enter Visually_Challenged_Right_Eye") 
            
    #     # Visually_Challenged_Left_Eye
    #     if validated_data['Visually_Challenged_Left_Eye']:               
    #         if age < 2:
    #             raise Exception("No need to enter Visually_Challenged_Left_Eye")

    #     user = StationCModel.objects.create(id=validated_data['id'],
    #                                    Visual_Acuity=validated_data['Visual_Acuity'],
    #                                    Visual_Acuity_With_Lenses_Distant_Vision_Left=validated_data['Visual_Acuity_With_Lenses_Distant_Vision_Left'],
    #                                    Visually_Challenged_Right_Eye_Enucleation_When_removed = validated_data['Visually_Challenged_Right_Eye_Enucleation_When_removed'],
    #                                    Visually_Challenged_Right_Eye_Enucleation_Why_removed = validated_data['Visually_Challenged_Right_Eye_Enucleation_Why_removed'],
    #                                    Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other = validated_data['Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other'],
    #                                    VC_Right_Eye_Enucleation_Artificial_Eye_Used = validated_data['VC_Right_Eye_Enucleation_Artificial_Eye_Used'],
    #                                    Visually_Challenged_Right_Eye_Enucleation_No = validated_data['Visually_Challenged_Right_Eye_Enucleation_No'],
    #                                    Visually_Challenged_Right_Eye_Enucleation_Cataract = validated_data['Visually_Challenged_Right_Eye_Enucleation_Cataract'],
    #                                    Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity = validated_data['Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity'],
    #                                    Visually_Challenged_Right_Eye_Enucleation_Glaucoma = validated_data['Visually_Challenged_Right_Eye_Enucleation_Glaucoma'],
    #                                    Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi = validated_data['Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi'],
    #                                    Visually_Challenged_Left_Eye = validated_data['Visually_Challenged_Left_Eye'],
    #                                    Visually_Challenged_Left_Eye_Enucleation = validated_data['Visually_Challenged_Left_Eye_Enucleation'],
    #                                    Visually_Challenged_Left_Eye_Enucleation_When_removed = validated_data['Visually_Challenged_Left_Eye_Enucleation_When_removed'],
    #                                    Visually_Challenged_Left_Eye_Enucleation_Why_removed = validated_data['Visually_Challenged_Left_Eye_Enucleation_Why_removed'],
    #                                    Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other = validated_data['Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other'],
    #                                    VC_Left_Eye_Enucleation_Artificial_Eye_Used = validated_data['VC_Left_Eye_Enucleation_Artificial_Eye_Used'],
    #                                    Visually_Challenged_Left_Eye_Enucleation_No = validated_data['Visually_Challenged_Left_Eye_Enucleation_No'],
    #                                    Visually_Challenged_Left_Eye_Enucleation_Cataract = validated_data['Visually_Challenged_Left_Eye_Enucleation_Cataract'],
    #                                    Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity = validated_data['Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity'],
    #                                    Visually_Challenged_Left_Eye_Enucleation_Glaucoma = validated_data['Visually_Challenged_Left_Eye_Enucleation_Glaucoma'],
    #                                    Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi = validated_data['Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi'],
    #                                    Reviewed_By = validated_data['Reviewed_By'],
    #                                    Reviewed_On = validated_data['Reviewed_On'],
                                       
    #                                     )
    #     user.save()
    #     return user        

class StationCSerializers5(serializers.ModelSerializer):
    class Meta:
        model = StationCModel
        fields =  ['Other_Observations', 'Specialist_Referral_Needed','Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag',
        'Other','Completed','Reviewed_By','Reviewed_On','EndTime']     
 
        
        



class GetStationCSerilizers(serializers.ModelSerializer):
    class Meta:
        model = StationCModel
        fields = ['id','StationID','HCID', 'HCPID', 'InfoseekId','EntryTime',
        'Problem_reading_books', 'Problem_reading_Blackboard', 'Night_Vision', 'Vision_Corrected','Vision_Corrected_Yes', 'Extra_Ocular_Right_Normal_Eye_Movement',
        'Extra_Ocular_Right_Strabismus','Extra_Ocular_Right_Drooping_Lid','Extra_Ocular_Right_Restricted_Mobility','Extra_Ocular_Right_Nystagmus',
        'Extra_Ocular_Right_Bulging','Extra_Ocular_Left_Normal_Eye_Movement','Extra_Ocular_Left_Strabismus','Extra_Ocular_Left_Drooping_Lid','Extra_Ocular_Left_Restricted_Mobility','Extra_Ocular_Left_Nystagmus','Extra_Ocular_Left_Bulging',
        'Visually_Challenged_Right_Eye','Visually_Challenged_Right_Eye_Enucleation','Visually_Challenged_Right_Eye_Enucleation_When_removed','Visually_Challenged_Right_Eye_Enucleation_Why_removed',
        'Visually_Challenged_Right_Eye_Enucleation_Why_removed_Other','VC_Right_Eye_Enucleation_Artificial_Eye_Used',
        'Visually_Challenged_Right_Eye_Enucleation_Cataract','Visually_Challenged_Right_Eye_Enucleation_Corneal_opacity','Visually_Challenged_Right_Eye_Enucleation_Glaucoma','Visually_Challenged_Right_Eye_Enucleation_Phthisis_bulbi',
        'Visually_Challenged_Left_Eye','Visually_Challenged_Left_Eye_Enucleation','Visually_Challenged_Left_Eye_Enucleation_When_removed','Visually_Challenged_Left_Eye_Enucleation_Why_removed',
        'Visually_Challenged_Left_Eye_Enucleation_Why_removed_Other','VC_Left_Eye_Enucleation_Artificial_Eye_Used',
        'Visually_Challenged_Left_Eye_Enucleation_Cataract','Visually_Challenged_Left_Eye_Enucleation_Corneal_opacity','Visually_Challenged_Left_Eye_Enucleation_Glaucoma','Visually_Challenged_Left_Eye_Enucleation_Phthisis_bulbi',
        'Visual_Acuity','Visual_Acuity_With_Lenses_Distant_Vision_Left','Visual_Acuity_With_Lenses_Distant_Vision_Right','Visual_Acuity_With_Lenses_Near_Vision_Left','Visual_Acuity_With_Lenses_Near_Vision_Right',
        'Visual_Acuity_without_Lenses_Distant_Vision_Left','Visual_Acuity_without_Lenses_Distant_Vision_Right','Visual_Acuity_without_Lenses_Near_Vision_Left','Visual_Acuity_without_Lenses_Near_Vision_Right',
        'Visual_Acuity_Color_Blindness','Visual_Acuity_Color_Blindness_Yes','Other_Observations','Specialist_Referral_Needed','Specialist_Referral_Needed_Type','Specialist_Referral_Needed_Flag',
        'Other','Completed','Review_Status','Reviewed_By','Reviewed_On','Comments','EndTime']

    
