from .views import *
from django.urls import path


urlpatterns = [

path('InfoseekMaster/',InfoseekMaster.as_view(), name='InfoseekMaster'),
path('InfoseekUploadExcel/',InfoseekUploadExcel.as_view(), name='InfoseekUploadExcel'),
path('InfoseekUpdate/<int:id>/',InfoseekUpdate.as_view(), name='InfoseekUpdate'),
path('GetAllInfoseekMasterData/',GetAllInfoseek.as_view(), name='GetAllInfoseekMaster'),
path('InfoseekUserVerification/', InfoseekUserVerification.as_view(), name='InfoseekUserVerification'),

path('Infoseek_S2_Verification/<int:InfoseekId>',InfoseekVerfication2.as_view(custom_property='section2'), name='Infoseek_S2_Verification'),
path('Infoseek_S3_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section3'), name = 'Infoseek_S3_Verification'),
path('Infoseek_S4_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section4'), name = 'Infoseek_S4_Verification'),
path('Infoseek_S5_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section5'), name = 'Infoseek_S5_Verification'),
path('Infoseek_S6_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section6'), name = 'Infoseek_S6_Verificationn'),
path('Infoseek_S7_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section7'), name = 'Infoseek_S7_Verification'),
path('Infoseek_S8_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section8'), name = 'Infoseek_S8_Verification'),
path('Infoseek_S9_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section9'), name = 'Infoseek_S9_Verification'),
path('Infoseek_S10_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section10'), name = 'Infoseek_S10_Verification'),
path('Infoseek_S11_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section11'), name = 'Infoseek_S11_Verification'),
path('Infoseek_S12_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section12'), name = 'Infoseek_S12_Verification'),
path('Infoseek_S13_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section13'), name = 'Infoseek_S13_Verification'),
path('Infoseek_S14_Verification/<int:InfoseekId>', InfoseekVerfication2.as_view(custom_property='section14'), name = 'Infoseek_S14_Verification'),

path('InfoseekNote/', NotePost.as_view(), name = 'InfoseekNote'),
path('UINInfoseekGet/<str:UIN>', UINInfoseekGet.as_view(), name = 'UINInfoseekGet'),

path('InfoseekVerificationUpdate/<int:InfoseekId>/', InfoseekVerficationUpdate.as_view(), name='InfoseekVerficationUpdate'),
path('InfoseekPhotoUploadUpdate/<int:InfoseekId>', InfoseekPhotoUploadUpdate.as_view(), name = 'InfoseekPhotoUploadUpdate'),

path('InfoseekTermsUpdate/<int:InfoseekId>', InfoseekTermsUpdate.as_view(), name = 'InfoseekTermsUpdate'),



path('InfoseekVerificationDetails/<int:InfoseekId>/', InfoseekVerficationDetails.as_view(), name='InfoseekVerificationDetails'),
path('InfoseekVerificationDetails/', InfoseekVerficationDetails.as_view(), name='InfoseekVerificationDetails'),
path('InfoseekOtpGeneration/', InfoseekOtpGeneration.as_view(), name='InfoseekOtpGeneration'),
path('InfoseekOtpVerification/', InfoseekOtpVerfication.as_view(), name='InfoseekOtpVerification'),

path('InfoseekIdCardGet/<int:InfoseekId>/', InfoseekIdCardGet.as_view(), name='InfoseekIdCardGet'),

path('ImageUploadPost/', ImageUploadPost.as_view(), name='ImageUploadPost'),
# path('ImageUpdate/<int:id>/', ImageUpdate.as_view(), name='ImageUpdate'),
path('ImageUpdate/<int:id>', ImageUpdate.as_view(), name = 'ImageUpdate'),


path('CountryGet/', CountryGet.as_view(), name = 'CountryGet'),
path('StatesGet/<str:country_name>', StatesGet.as_view(), name = 'StatesGet'),


path('ImmunizationMaster/', ImmunizationMasterPost.as_view(), name='ImmunizationMasterPost'),
path('ImmunizationMasterGet/<int:ImmunizationId>/', ImmunizationGet.as_view(), name='ImmunizationMasterGet'),



]


