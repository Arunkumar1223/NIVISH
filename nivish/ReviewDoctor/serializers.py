# serializers.py
from rest_framework import serializers
from .models import FinalStatusModel,AllStationsFlags


from stationA.models import StationAModel
from stationB.models import StationBModel
from stationC.models import StationCModel
from stationD.models import StationDModel
from stationE.models import StationEModel
from stationF.models import StationFModels
from stationG.models import StationGModel
from stationH.models import StationHModel
from infoseek.models import InfoseekVerificationModel
from hcp.models import HcpRegistrationModel



class FinalStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = FinalStatusModel
        fields = ['HCID','InfoseekId']

    def create(self, validated_data):

        InfoseekId = validated_data['InfoseekId']
        uin = InfoseekId.UIN

        flag_list = [
                    obj.Specialist_Referral_Needed_Flag
                    for model_cls in [StationAModel, StationBModel,StationCModel,StationDModel,StationEModel,StationFModels,StationGModel,StationHModel]
                    for obj in model_cls.objects.filter(InfoseekId_id=InfoseekId)
                    if obj.Specialist_Referral_Needed_Flag is not None
                ]
        
        if flag_list:
            if "Emergency" in flag_list:
                flag = 'Emergency'
            elif 'Urgent' in flag_list:
                flag = 'Urgent'
            else:
                flag = 'Non-Urgent'
        else:
            flag = 'WNL'


        user = FinalStatusModel.objects.create(HCID=validated_data['HCID'],
                                       InfoseekId=validated_data['InfoseekId'],
                                       Final_Flag_status=flag,
                                       UIN = uin
                                        )
                                        
        user.save()
        
        return user
    

class InfoseekVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoseekVerificationModel
        fields = ['InfoseekId', 'Student_FirstName','class_name','section_name' ]


class HcpSerializerRD(serializers.ModelSerializer):
    class Meta:
        model = HcpRegistrationModel
        fields = ['FullName',]
    
class GetFinalStatusSerializers(serializers.ModelSerializer):
    InfoseekId = InfoseekVerificationSerializer()
    Reviewed_by = HcpSerializerRD()

    class Meta:
        model = FinalStatusModel
        fields = ['InfoseekId','UIN','HCID','Final_Flag_status','Reviewed_by','Review_status','Reviewd_on']




class UpdateFinalStatusSerializers(serializers.ModelSerializer):

    class Meta:
        model = FinalStatusModel
        fields = ['Final_Flag_status','Reviewed_by','Reviewd_on','final_mark','Final_Review_Comments']


    def create(self, validated_data):

        final_mark = validated_data['final_mark']

        if final_mark == "completed_email" or "completed_In-person":
            Review_status = 'Review Completed'
        else: 
            Review_status = 'On Hold'



        user = FinalStatusModel.objects.create(Final_Flag_status=validated_data['Final_Flag_status'],
                                       Reviewed_by=validated_data['Reviewed_by'],
                                       Reviewd_on=validated_data['Reviewd_on'],
                                       final_mark = validated_data['final_mark'],
                                       Final_Review_Comments = validated_data['Final_Review_Comments'],
                                       Review_status = Review_status
                                        )
                                        
        user.save()
        
        return user

class FInalStatusFilterSerializer(serializers.ModelSerializer):
    page_size=serializers.IntegerField(required=False)
    page_number=serializers.IntegerField(required=False)
    
    class Meta:
        model = FinalStatusModel
        fields = ['HCID','Final_Flag_status','Review_status','page_size','page_number']

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalStatusModel 
        fields = ['UIN','Final_Flag_status']



class FlagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AllStationsFlags
        fields = ['InfoseekId','HCID']


    def create(self, validated_data):
        InfoseekId = validated_data['InfoseekId']
        Hcid = validated_data['HCID']
        

        flag_fields = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        flags = {}

        for field in flag_fields:
            model_name = f'Station{field}Model'

            # Special case for StationFModel
            if field == 'F':
                model_name = 'StationFModels'

            user_data = globals()[model_name].objects.filter(InfoseekId=InfoseekId, HCID=Hcid)
            flags[f'station{field}flag'] = user_data[0].Specialist_Referral_Needed_Flag if user_data else None

        user = AllStationsFlags.objects.create(
            HCID=validated_data['HCID'],
            InfoseekId=validated_data['InfoseekId'],
            **flags
        )
        user.save()
        return user


    

class GetFlagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AllStationsFlags
        fields = ['InfoseekId','HCID','stationAflag','stationBflag','stationCflag','stationDflag','stationEflag','stationFflag','stationGflag','stationHflag']




class Getobservationserializers(serializers.ModelSerializer):
    class Meta:
        model = StationAModel
        fields = ['Other_Observations']



class UpdateStationAReviewDoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationAModel
        fields = ['Review_Status','Reviewed_By','Reviewed_On','Comments']


class UpdateStationBReviewDoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationBModel
        fields = ['Review_Status','Reviewed_By','Reviewed_On','Comments']
        

class UpdateStationCReviewDoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationCModel
        fields = ['Review_Status','Reviewed_By','Reviewed_On','Comments']


class UpdateStationDReviewDoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationDModel
        fields = ['Review_Status','Reviewed_By','Reviewed_On','Comments']


class UpdateStationEReviewDoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationEModel
        fields = ['Review_Status','Reviewed_By','Reviewed_On','Comments']
        


class UpdateStationFReviewDoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationFModels
        fields = ['Review_Status','Reviewed_By','Reviewed_On','Comments']
        


class UpdateStationGReviewDoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationGModel
        fields = ['Review_Status','Reviewed_By','Reviewed_On','Comments']


class UpdateStationHReviewDoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationHModel
        fields = ['Review_Status','Reviewed_By','Reviewed_On','Comments']
        

class GetbyHcidUINSerializer(serializers.Serializer):
    
    StationName = serializers.CharField(required=False)
    UIN = serializers.IntegerField(required=False)
    HCID = serializers.CharField(required=False)
