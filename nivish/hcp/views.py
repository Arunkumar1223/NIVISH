from django.shortcuts import render

# Create your views here.
from hcp.hcp_crud.hcp_post import HcpRegistrationPost
from hcp.hcp_crud.hcp_update import HcpRegistrationUpdate
from hcp.hcp_crud.hcp_Get_by_id import HcpRegistrationGetById
from hcp.hcp_crud.hcp_niv_update import nivupdate

from hcp.hcp_crud.provider_post import ProviderPost
from hcp.hcp_crud.provider_get import GetProvider
from hcp.hcp_crud.provider_update import ProviderUpdate
from hcp.hcp_crud.education_post import HcpEducationPost
from hcp.hcp_crud.education_get import GetHcpEducation
from hcp.hcp_crud.education_update import HcpEducationUpdate
from hcp.hcp_crud.education_getbyid import GetByHcpEducation

from hcp.hcp_crud.provider_Terms_update import ProviderTermsUpdate


from hcp.hcp_crud.License_Details_post import HcpLicenseDetailsPost
from hcp.hcp_crud.License_Details_get import GetHcpLicenseDetails
from hcp.hcp_crud.License_Details_update import HcpLicenseDetailsUpdate
from hcp.hcp_crud.license_details_getbyid import GetByHcpLicenseDetails



from hcp.hcp_crud.hcp_master_post import HcpMaster
from hcp.hcp_crud.hcp_master_Get import HcpMasterGetById , HcpMasterGetByType
from hcp.hcp_crud.hcp_master_update import HcpMasterUpdate

from hcp.hcp_crud.hcp_otp_generation import HcpOtpGeneration
from hcp.hcp_crud.hcp_otp_verification import HcpOtpVerfication

from hcp.hcp_crud.provider_otp_generation import ProviderOtpGeneration
from hcp.hcp_crud.provider_otp_verification import ProviderOtpVerfication

from hcp.hcp_crud.Assignment_post import AssignmentPost
from hcp.hcp_crud.Assignment_Get import GetAssignment
from hcp.hcp_crud.Assignment_update import AssignmentUpdate
from hcp.hcp_crud.hcp_login import HCPLogin

from hcp.hcp_crud.experience_post import ExperiencePost
from hcp.hcp_crud.experience_get import GetExperience
from hcp.hcp_crud.experience_update import ExperienceUpdate

from hcp.hcp_crud.note_post import NotePost
from hcp.hcp_crud.note_update import NoteUpdate
from hcp.hcp_crud.note_Terms_Update import NoteTermsUpdate
from hcp.hcp_crud.Hcp_note_Get import NoteGet

from hcp.hcp_crud.hcp_postby_Type import HcpGetbyType
from hcp.hcp_crud.hcp_upload_master_data import HcpUploadExcel

from hcp.hcp_crud.hcp_get_idcard import HcpIdCardGetById


from hcp.hcp_crud.registrationdesk_post import RegistrationDeskPost
from hcp.hcp_crud.registrationdesk_get import AllStationsStatus

from hcp.hcp_crud.Exitdesk import ExitdeskGet

from hcp.hcp_crud.reviewdoctor_get import ReviewdoctorGet

from hcp.hcp_crud.registrationdesk_update import UpdateRegistrationDesk

from hcp.hcp_crud.hcp_upload_image_update import HcpPhotoUploadUpdate
from hcp.hcp_crud.registration_desk_get_UIN import RegistrationDeskDetails


from hcp.hcp_crud.License_Details_upload_doc_update import HcpLicenseDetailsUploadDocUpdate
from hcp.hcp_crud.education_upload_doc_update import HcpEducationUploadDocUpdate


RegistrationDeskDetails()
HcpRegistrationPost()
HcpRegistrationUpdate()
HcpRegistrationGetById()
HCPLogin()
nivupdate()

ProviderPost()
GetProvider()
ProviderUpdate()

ProviderTermsUpdate()

HcpEducationPost()
GetHcpEducation()
HcpEducationUpdate()
GetByHcpEducation()

HcpLicenseDetailsPost()
GetHcpLicenseDetails()
HcpLicenseDetailsUpdate()
GetByHcpLicenseDetails()

HcpMaster()
HcpMasterGetById()
HcpMasterGetByType()
HcpMasterUpdate()

HcpOtpGeneration()
HcpOtpVerfication()

ProviderOtpGeneration()
ProviderOtpVerfication()

AssignmentPost()
GetAssignment()
AssignmentUpdate()

ExperiencePost()
GetExperience()
ExperienceUpdate()

NotePost()
NoteUpdate()
NoteGet()
NoteTermsUpdate()

HcpGetbyType()

HcpUploadExcel()

HcpIdCardGetById()


RegistrationDeskPost()
AllStationsStatus()

ExitdeskGet()

UpdateRegistrationDesk()

ReviewdoctorGet()

HcpPhotoUploadUpdate()


HcpLicenseDetailsUploadDocUpdate()
HcpEducationUploadDocUpdate()
