from rest_framework import serializers
from .models import *


class StationHSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationHModel
        fields = ['HCID','HCPID','InfoseekId','EntryTime','Upper_Permanent', 'Upper_Permanent_Decayed','Upper_Permanent_Missing','Upper_Permanent_Filled','Upper_Permanent_Prosthesis',
                  'Upper_Permanent_Restoration_done','Upper_Deciduous','Upper_Deciduous_Decayed','Upper_Deciduous_Missing','Upper_Deciduous_Filled',
                  'Upper_Deciduous_Prosthesis','Upper_Deciduous_Restoration_done','Lower_Deciduous','Lower_Deciduous_Decayed','Lower_Deciduous_Missing',
                  'Lower_Deciduous_Filled','Lower_Deciduous_Prosthesis','Lower_Deciduous_Restoration_done','Lower_Permanent','Lower_Permanent_Decayed',
                  'Lower_Permanent_Missing','Lower_Permanent_Filled','Lower_Permanent_Prosthesis','Lower_Permanent_Restoration_done']


class GetStationHPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationHModel
        fields = ['id','StationID','HCID','HCPID','InfoseekId','EntryTime','Upper_Permanent', 'Upper_Permanent_Decayed','Upper_Permanent_Missing','Upper_Permanent_Filled','Upper_Permanent_Prosthesis',
                  'Upper_Permanent_Restoration_done','Upper_Deciduous','Upper_Deciduous_Decayed','Upper_Deciduous_Missing','Upper_Deciduous_Filled',
                  'Upper_Deciduous_Prosthesis','Upper_Deciduous_Restoration_done','Lower_Deciduous','Lower_Deciduous_Decayed','Lower_Deciduous_Missing',
                  'Lower_Deciduous_Filled','Lower_Deciduous_Prosthesis','Lower_Deciduous_Restoration_done','Lower_Permanent','Lower_Permanent_Decayed',
                  'Lower_Permanent_Missing','Lower_Permanent_Filled','Lower_Permanent_Prosthesis','Lower_Permanent_Restoration_done']  


class UpdateStationHSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationHModel
        fields = ['HCID','HCPID','InfoseekId','Upper_Permanent', 'Upper_Permanent_Decayed','Upper_Permanent_Missing','Upper_Permanent_Filled','Upper_Permanent_Prosthesis',
                  'Upper_Permanent_Restoration_done','Upper_Deciduous','Upper_Deciduous_Decayed','Upper_Deciduous_Missing','Upper_Deciduous_Filled',
                  'Upper_Deciduous_Prosthesis','Upper_Deciduous_Restoration_done','Lower_Deciduous','Lower_Deciduous_Decayed','Lower_Deciduous_Missing',
                  'Lower_Deciduous_Filled','Lower_Deciduous_Prosthesis','Lower_Deciduous_Restoration_done','Lower_Permanent','Lower_Permanent_Decayed',
                  'Lower_Permanent_Missing','Lower_Permanent_Filled','Lower_Permanent_Prosthesis','Lower_Permanent_Restoration_done','Reviewed_By','Reviewed_On',]



class StationHSerializers2(serializers.ModelSerializer):
    class Meta:
        model = StationHModel
        fields = ['Oral_Hygiene','Plaque','Dental_Stains','Malocclusion','Crowding','Impacted_Tooth','Impacted_Tooth_Yes',
                  'Impacted_Tooth_Yes_Position','Worn_Enamel','Reviewed_By','Reviewed_On'] 



class StationHSerializers3(serializers.ModelSerializer):
    class Meta:
        model = StationHModel
        fields = ['Sensitivity','Untreated_Caries','Caries_Experience','Dental_Sealants_Present','Braces','Braces_Yes',
                  'Bridges','Bridges_Yes','Dentures','Dentures_Yes','Reviewed_By','Reviewed_On',]    
        

class StationHSerializers4(serializers.ModelSerializer):
    class Meta:
        model = StationHModel
        fields = ['Soft_Tissue_Pathology','Soft_Tissue_Pathology_Yes','Soft_Tissue_Pathology_Yes_Other',
                  'Treatment_Needed','Treatment_Needed_Yes','Treatment_Needed_Yes_Other','Dental_Florosis','Reviewed_By','Reviewed_On',]
        

class StationHSerializers5(serializers.ModelSerializer):
    class Meta:
        model = StationHModel
        fields = ['Other_Observations','StationH_Dental_SR_Needed','StationH_Dental_SR_Needed_Yes_Type',
                  'StationH_Dental_SR_Needed_Yes_Flag','Reviewed_By','Reviewed_On',]
        

class StationHSerializers6(serializers.ModelSerializer):
    class Meta:
        model = StationHModel
        fields = ['Other_Observations','Specialist_Referral_Needed','Specialist_Referral_Needed_Type',
                  'Specialist_Referral_Needed_Flag','Other','Completed','EndTime','Reviewed_By','Reviewed_On',]
        

class GetStationHSerializers(serializers.ModelSerializer):
    class Meta:
        model = StationHModel
        fields = ['id','StationID','HCID','HCPID','InfoseekId','EntryTime','Upper_Permanent', 'Upper_Permanent_Decayed','Upper_Permanent_Missing','Upper_Permanent_Filled','Upper_Permanent_Prosthesis',
                  'Upper_Permanent_Restoration_done','Upper_Deciduous','Upper_Deciduous_Decayed','Upper_Deciduous_Missing','Upper_Deciduous_Filled',
                  'Upper_Deciduous_Prosthesis','Upper_Deciduous_Restoration_done','Lower_Deciduous','Lower_Deciduous_Decayed','Lower_Deciduous_Missing',
                  'Lower_Deciduous_Filled','Lower_Deciduous_Prosthesis','Lower_Deciduous_Restoration_done','Lower_Permanent','Lower_Permanent_Decayed',
                  'Lower_Permanent_Missing','Lower_Permanent_Filled','Lower_Permanent_Prosthesis','Lower_Permanent_Restoration_done',
                  'Oral_Hygiene','Plaque','Dental_Stains','Malocclusion','Crowding','Impacted_Tooth','Impacted_Tooth_Yes',
                  'Impacted_Tooth_Yes_Position','Worn_Enamel','Sensitivity','Untreated_Caries','Caries_Experience','Dental_Sealants_Present','Braces','Braces_Yes',
                  'Bridges','Bridges_Yes','Dentures','Dentures_Yes','Soft_Tissue_Pathology','Soft_Tissue_Pathology_Yes','Soft_Tissue_Pathology_Yes_Other',
                  'Treatment_Needed','Treatment_Needed_Yes','Treatment_Needed_Yes_Other','Dental_Florosis','Other_Observations','StationH_Dental_SR_Needed','StationH_Dental_SR_Needed_Yes_Type',
                  'StationH_Dental_SR_Needed_Yes_Flag','Other_Observations','Specialist_Referral_Needed','Specialist_Referral_Needed_Type',
                  'Specialist_Referral_Needed_Flag','Other','Completed','Review_Status','Reviewed_By',
                  'Reviewed_On','Comments','EndTime']
        

