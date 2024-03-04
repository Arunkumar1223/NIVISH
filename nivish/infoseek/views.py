from django.shortcuts import render

# Create your views here.
from infoseek.infoseek_crud.infoseek_master_post import InfoseekMaster
from infoseek.infoseek_crud.infoseek_master_update import InfoseekUpdate
from infoseek.infoseek_crud.infoseek_master_Get import GetAllInfoseek
from infoseek.infoseek_crud.infoseek_S2_Verfication import InfoseekVerfication2
from infoseek.infoseek_crud.infoseek_Verification_update import InfoseekVerficationUpdate
from infoseek.infoseek_crud.infoseek_Verification_Get import InfoseekVerficationDetails
from infoseek.infoseek_crud.infoseek_Otp_Generation import InfoseekOtpGeneration
from infoseek.infoseek_crud.infoseek_Otp_Verification import InfoseekOtpVerfication
from infoseek.infoseek_crud.infoseek_User_Verification import InfoseekUserVerification
from infoseek.infoseek_crud.upload_master_data import InfoseekUploadExcel
from infoseek.infoseek_crud.Infoseek_get_UIN import UINInfoseekGet

from infoseek.infoseek_crud.Infoseek_Terms_Update import InfoseekTermsUpdate

from infoseek.infoseek_crud.infoseek_notepost import NotePost
from infoseek.infoseek_crud.infoseek_photoupload_Update import InfoseekPhotoUploadUpdate

from infoseek.infoseek_crud.infoseek_idcard_Get import InfoseekIdCardGet
from infoseek.infoseek_crud.image_post import ImageUploadPost
from infoseek.infoseek_crud.image_update import ImageUpdate

from infoseek.infoseek_crud.country_get import CountryGet
from infoseek.infoseek_crud.States_get import StatesGet

from infoseek.infoseek_crud.immunization_master_post import ImmunizationMasterPost
from infoseek.infoseek_crud.immunization_master_get import ImmunizationGet



InfoseekMaster()
InfoseekUpdate()
GetAllInfoseek()
InfoseekVerfication2()
InfoseekVerficationUpdate()
InfoseekVerficationDetails()
InfoseekOtpGeneration()
InfoseekOtpVerfication()
InfoseekUserVerification()
InfoseekUploadExcel()
UINInfoseekGet()

NotePost()
InfoseekPhotoUploadUpdate()
ImageUploadPost()
ImageUpdate()
InfoseekIdCardGet()

InfoseekTermsUpdate()

CountryGet()
StatesGet()

ImmunizationMasterPost()
ImmunizationGet()



