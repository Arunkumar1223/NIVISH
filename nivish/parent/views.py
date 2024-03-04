from django.shortcuts import render
from parent.parent_crud.bmi_post import BmiPost
from parent.parent_crud.bmi_get import GetBmi
from parent.parent_crud.bmi_update import BmiUpdate
from parent.parent_crud.health_insurance_post import HealthInsurancePost
from parent.parent_crud.health_insurance_get import GetHealthInsurance
from parent.parent_crud.health_insurance_update import HealthInsuranceUpdate
from parent.parent_crud.parent_otp_generation import ParentOtpGeneration
from parent.parent_crud.parent_otp_verification import ParentOtpVerification
from parent.parent_crud.bp_post import ParentBPVerification
from parent.parent_crud.bp_get import GetBPDetails
from parent.parent_crud.bp_update import BpUpdate
from parent.parent_crud.abdominal_post import AbdominalVerification
from parent.parent_crud.abdominal_get import GetabdominalDetails
from parent.parent_crud.chest_post import ChestVerification
from parent.parent_crud.chest_get import GetChestDetails
from parent.parent_crud.abdominal_update import AbdominalUpdate
from parent.parent_crud.chest_update import ChestUpdate

BmiPost()
GetBmi()
BmiUpdate()
HealthInsurancePost()
GetHealthInsurance()
HealthInsuranceUpdate()
ParentOtpGeneration()
ParentOtpVerification()
ParentBPVerification()
GetBPDetails()
BpUpdate()
AbdominalVerification()
ChestVerification()
ChestUpdate()
GetChestDetails()
GetabdominalDetails()
AbdominalUpdate()



