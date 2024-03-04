from django.shortcuts import render
from .review_doctor_crud.final_status_RD import FinalStatusPost
from .review_doctor_crud.get_infoseek_by_WNL import GetAllInfoseekWNL
from .review_doctor_crud.get_infoseek_id_by_status import GetAllInfoseekByReviewStatus
from .review_doctor_crud.update_FS_RD import UpdateFinalStatusRD
from .review_doctor_crud.get_final_status_RD import GetFinalStatusList
from .review_doctor_crud.global_search import GlobalSearch
from .review_doctor_crud.get_hcpdetails_by_hcpid import GetByHcpId
from .review_doctor_crud.get_alert_by_hcid import AlertAPI
from .review_doctor_crud.stations_flags_post import StationsFlagsPost
from .review_doctor_crud.get_allstations_observations import GetObservations
from .review_doctor_crud.stations_review_update import UpdateRDstations
from .review_doctor_crud.get_stations_hcid_uin import GetByHcidUINDetails



FinalStatusPost()
GetAllInfoseekWNL()
GetAllInfoseekByReviewStatus()
UpdateFinalStatusRD()
GetFinalStatusList()
GlobalSearch()
GetByHcpId()
AlertAPI()
StationsFlagsPost()
GetObservations()
UpdateRDstations()
GetByHcidUINDetails()












