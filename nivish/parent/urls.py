from .views import *
from django.urls import path
from .parent_crud.grapgh_ql import schema
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [

   
    path('BMIPost/',BmiPost.as_view(), name='BMIPost'),
    path('GetBMI/<int:id>/',GetBmi.as_view(), name='GetBmi'),
    path('GetBMIDetails/',GetBmi.as_view(), name='GetBmi'),
    path('BMIUpdate/<int:id>/',BmiUpdate.as_view(), name='BmiUpdate'),
    path('HealthInsurancePost/',HealthInsurancePost.as_view(), name='HealthInsurancePost'),
    path('GetHealthInsurance/<int:InfoseekId>/',GetHealthInsurance.as_view(), name='GetHealthInsurance'),
    path('GetHealthInsuranceDetails/',GetHealthInsurance.as_view(), name='GetHealthInsuranceDetails'),
    path('HealthInsuranceUpdate/<int:id>/',HealthInsuranceUpdate.as_view(), name='HealthInsuranceUpdate'),

    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),

    path('ParentOtpGeneration/',ParentOtpGeneration.as_view(), name='ParentOtpGeneration'),
    path('ParentOtpVerification/',ParentOtpVerification.as_view(), name='ParentOtpVerification'),

    
    path('ParentBPVerification/',ParentBPVerification.as_view(), name='ParentBPVerification'),
    path("GetBPDetails/<int:InfoseekId>/",GetBPDetails.as_view(), name="GetBPDetails"),
    path("BPUpdate/<int:InfoseekId>/",BpUpdate.as_view(), name = 'BpUpdate'),

    path("AbdominalDetailsPost/",AbdominalVerification.as_view(), name="AbdominalDetailsPost"),
    path("GetAbdominalGirth/<int:InfoseekId>/",GetabdominalDetails.as_view(), name="GetAbdominal"),
    path("AbdominalGirthUpdate/<int:InfoseekId>/",AbdominalUpdate.as_view(), name="AbdominalUpdate"),


    
    path("chestcircumferncepost/",ChestVerification.as_view(), name = "chestcircumferncepost"),
    path("GetChestCircumferenceDetails/<int:InfoseekId>/",GetChestDetails.as_view(), name="GetChestDetails"),
    path("ChestCircumferenceUpdate/<int:InfoseekId>/",ChestUpdate.as_view(),name = "ChestUpdate"),
    

]

