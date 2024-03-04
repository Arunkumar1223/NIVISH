from django.shortcuts import render
from super_admin.super_admin_crud.super_admin_post import SuperAdminPost
from super_admin.super_admin_crud.super_admin_get import SuperAdminGetById
from super_admin.super_admin_crud.super_admin_update import SuperAdminUpdate

from super_admin.super_admin_crud.healthcamp_teams_post import HealthCampTeamsPost
from super_admin.super_admin_crud.healthcamp_teams_get import HealthCampTeamsGet
from super_admin.super_admin_crud.healthcamp_teams_update import HealthCampTeamsUpdate



from super_admin.super_admin_crud.camp_post import CampRegPost
from super_admin.super_admin_crud.camp_update import CampRegUpdate
from super_admin.super_admin_crud.camp_get import CampRegGetById


from super_admin.super_admin_crud.stations_post import StationPost
from super_admin.super_admin_crud.stations_get import StationGetById

from super_admin.super_admin_crud.camp_schedule_post import HealthCampSchedulePost
from super_admin.super_admin_crud.camp_schedule_update import UpdateHealthCampSchedule
from super_admin.super_admin_crud.send_email import MailGeneration


SuperAdminPost()
SuperAdminGetById()
SuperAdminUpdate()

HealthCampTeamsPost()
HealthCampTeamsGet()
HealthCampTeamsUpdate()


CampRegPost()
CampRegUpdate()
CampRegGetById()

StationPost()
StationGetById()

HealthCampSchedulePost()
UpdateHealthCampSchedule()
MailGeneration()




