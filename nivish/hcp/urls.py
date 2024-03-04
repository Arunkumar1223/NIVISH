from .views import *
from django.urls import path


urlpatterns = [

path('HcpMaster/',HcpMaster.as_view(), name='HcpMaster'),
path('HcpMasterGetById/<int:id>/',HcpMasterGetById.as_view(), name='HcpMasterGetById'),
path('HcpMasterGet/',HcpMasterGetById.as_view(), name='HcpMasterGet'),
path('HcpMasterGetByType/<str:Type>/',HcpMasterGetByType.as_view(), name='HcpMasterGetByType'),
path('HcpMasterUpdate/<int:id>/',HcpMasterUpdate.as_view(), name='HcpMasterUpdate'),
path('HCPLogin/',HCPLogin.as_view(), name='HCPLogin'),
path('HCPUploadExcel/',HcpUploadExcel.as_view(), name='HcpUploadExcel'),

path('HcpRegistrationPost/',HcpRegistrationPost.as_view(), name='HcpRegistrationPost'),
path('HcpRegistrationUpdate/<int:HCPID>/',HcpRegistrationUpdate.as_view(), name='HcpRegistrationUpdate'),
path('HcpRegistrationGetById/<int:HCPID>/',HcpRegistrationGetById.as_view(), name='HcpRegistrationGetbyid'),
path('GetallHcpRegistration/',HcpRegistrationGetById.as_view(), name='HcpRegistrationGetall'),
path('HcpGetbyType/',HcpGetbyType.as_view(), name='HcpGetbyType'),
path('NIVUpdate/',nivupdate.as_view(),name = "NIVUpdate"),


path('ProviderPost/',ProviderPost.as_view(), name='ProviderPost'),
path('GetProvider/<int:ProviderID>/',GetProvider.as_view(), name='GetProvider'),
path('GetProvider/',GetProvider.as_view(), name='GetProvider'),
path('ProviderUpdate/<int:ProviderID>',ProviderUpdate.as_view(), name='ProviderUpdate'),
path('ProviderTermsUpdate/<int:ProviderID>',ProviderTermsUpdate.as_view(), name='ProviderTermsUpdate'),

path('HcpEducationPost/',HcpEducationPost.as_view(), name='HcpEducationPost'),
path('GetHcpEducation/<int:HCPID>/',GetHcpEducation.as_view(), name='GetHcpEducation'),
path('GetHcpEducation/',GetHcpEducation.as_view(), name='GetHcpEducation'),
path('HcpEducationUpdate/<int:id>/',HcpEducationUpdate.as_view(), name='HcpEducationUpdate'),
path('GetHcpEducationId/<int:EducationId>/',GetByHcpEducation.as_view(), name='GetHcpEducationId'),
path('HcpEducationUploadDoc/<int:EducationId>/',HcpEducationUploadDocUpdate.as_view(), name='HcpEducationUploadDocUpdate'),

path('HcpLicenseDetailsPost/',HcpLicenseDetailsPost.as_view(), name='HcpLicenseDetailsPost'),
path('GetHcpLicenseDetails/<int:HCPID>/',GetHcpLicenseDetails.as_view(), name='GetHcpLicenseDetails'),
path('GetHcpLicenseDetails/',GetHcpLicenseDetails.as_view(), name='GetHcpLicenseDetails'),
path('HcpLicenseDetailsUpdate/<int:id>/',HcpLicenseDetailsUpdate.as_view(), name='HcpLicenseDetailsUpdate'),
path('GetHcpLicenseDetailsId/<int:LicenseId>/',GetByHcpLicenseDetails.as_view(), name='GetHcpLicenseDetailsId'),
path('HcpLicenseDetailsUploadDoc/<int:LicenseId>/',HcpLicenseDetailsUploadDocUpdate.as_view(), name='HcpLicenseDetailsUploadDocUpdate'),

path('HcpOtpGeneration/',HcpOtpGeneration.as_view(), name='HcpOtpGeneration'),
path('HcpOtpVerfication/',HcpOtpVerfication.as_view(), name='HcpOtpVerfication'),

path('ProviderOtpGeneration/',ProviderOtpGeneration.as_view(), name='ProviderOtpGeneration'),
path('ProviderOtpVerfication/',ProviderOtpVerfication.as_view(), name='ProviderOtpVerfication'),

path('AssignmentPost/',AssignmentPost.as_view(), name='AssignmentPost'),
path('GetAssignment/',GetAssignment.as_view(), name='GetAssignment'),
path('GetAssignment/<int:id>/',GetAssignment.as_view(), name='GetbyidAssignment'),
path('AssignmentUpdate/<int:id>/',AssignmentUpdate.as_view(), name='AssignmentUpdate'),

path('HcpExperiencePost/',ExperiencePost.as_view(), name='HcpLicenseDetailsExperiencePost'),
path('GetHcpExperience/<int:HCPID>/',GetExperience.as_view(), name='GetHcpLicenseDetailsExperience'),
path('GetHcpExperience/',GetExperience.as_view(), name='GetAllHcpLicenseDetailsExperience'),
path('HcpExperienceUpdate/<int:HCPID>/',ExperienceUpdate.as_view(), name='HcpLicenseDetailsExperienceUpdate'),

path('HcpNote/',NotePost.as_view(), name='HcpNote'),
path('HcpNoteUpdate/<int:id>/',NoteUpdate.as_view(), name='HcpNoteUpdate'),
path('NoteGet/<int:HCPID>/',NoteGet.as_view(), name='NoteGet'),
path('NoteGet/',NoteGet.as_view(), name='NoteGet'),

path('GetHcpIDCard/<int:HCPID>',HcpIdCardGetById.as_view(), name='GetHcpIDCard'),

path('RegistrationDeskPost/',RegistrationDeskPost.as_view(), name='RegistrationDeskPost'),
path('AllStationsStatus/<int:HCID>/<int:UIN>/',AllStationsStatus.as_view(), name='HealthcampDetailsGetById'),
path('ExitdeskGet/<int:HCID>/<int:UIN>/',ExitdeskGet.as_view(), name='ExitdeskGet'),

path('ReviewdoctorGet/<int:HCID>/',ReviewdoctorGet.as_view(), name='ReviewdoctorGet'),

path('RegistrationDeskUpdate/<int:id>/',UpdateRegistrationDesk.as_view(), name='UpdateRegistrationDesk'),

path('HcpNoteTermsUpdate/<int:HCPID>/',NoteTermsUpdate.as_view(), name='HcpNoteTermsUpdate'),

path('HcpPhotoUploadUpdate/<int:HCPID>/',HcpPhotoUploadUpdate.as_view(), name='HcpPhotoUploadUpdate'),

path('RegistrationDeskDetail/<int:UIN>/<int:HCID>/',RegistrationDeskDetails.as_view(), name='RegistrationDeskDetails'),

]
