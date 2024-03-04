import datetime
import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from hcp.models import HcpRegistrationModel,AssignmentModel
from hcp.serializers import HcpLoginSerializers, GetHcpRegistrationSerializers,LoginAssignmentSerializers
from errormessage import Errormessage
from tokengeneration import *
from super_admin.models import HealthCampModel



class HCPLogin(generics.GenericAPIView):
    serializer_class = HcpLoginSerializers
    
    def post(self, request, format=None):
        '''Login with PASSWORD for Health Camp, Registration Desk, Exit Desk and Review Doctor.'''




        try:
            email = request.data.get('Registered_Email')
            password = request.data.get('Password')
            User_Type = request.data.get('User_Type')


            print(User_Type,'User_Type')
            # Review_Doctor = request.data.get('Review_Doctor')
            # print(Review_Doctor,"Review_Doctor")
    
                   
            hcp_data = HcpRegistrationModel.objects.filter(Registered_Email=email, Password=password).first()

            if hcp_data: 
                type = hcp_data.Type
                current_datetime = datetime.datetime.now()

#   For Review Doctor
                
                if User_Type == 'Review Doctor':
                    health_camps = HealthCampModel.objects.all()
                    if health_camps:
                        camp_ids = [camp.HCID for camp in health_camps]

                        if type == 'Ops':
                            hcp_assignments = AssignmentModel.objects.filter(HCPID=hcp_data.HCPID,HCID__in=camp_ids)
                            if hcp_assignments:
                                for hcp_assignments_loop in hcp_assignments:
                                    print(hcp_assignments_loop.StationID.Station_Names)
                                    if hcp_assignments_loop.StationID.Station_Names == "Review Doctor":
                                        pass
                                    else:
                                        raise Exception("You are not a Review Doctor")
                            else:
                                raise Exception("This User dont have any Assainments")
                    else:
                        raise Exception("This User dont have any Camps")
                            
#   For Health Camp, Registration Desk user and  Exit desk

                elif User_Type  == None:
                    
                    active_camps = HealthCampModel.objects.filter(StartDate__lte=current_datetime, EndDate__gte=current_datetime)
                    if active_camps:

                        active_camp_ids = [camp.HCID for camp in active_camps]
                        
                        if type == 'HCP':
                            print(type)
                            hcp_assignments = AssignmentModel.objects.filter(HCPID=hcp_data.HCPID, HCID__in=active_camp_ids)
                            


                        elif type == 'Ops':
                            hcp_assignments = AssignmentModel.objects.filter(HCPID=hcp_data.HCPID, HCID__in=active_camp_ids)

                            if hcp_assignments:
                                for hcp_assignments_loop in hcp_assignments:
                                    ops_type = hcp_assignments_loop.StationID.Station_Names
                                    print(ops_type)
                                    if ops_type== "Registration Desk":
                                        pass
                                    elif ops_type== "Exit Desk":
                                        pass
                                    else:
                                        raise Exception("You or not a Registration or Exit User")
                            else:
                                raise Exception("This user don't have any access ")
                    else:
                        raise Exception("This User dont have any Camps")

                if hcp_assignments:
                    asss = LoginAssignmentSerializers(hcp_assignments, many=True)
                    hcp_data = GetHcpRegistrationSerializers(hcp_data)
                    a=logintoken()
                    bearer_token=a['access']
                    assement = asss.data
                    final_data = hcp_data.data
                    final_data['Stations'] = assement
                    final_data['Token'] = bearer_token
                
                # else:
                #     raise Exception("This User dont have any Camps")
            else:
                raise Exception("Please Enter Valid Email or Password")
            
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = final_data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)   

            
        # try:
        #     email = request.data.get('Registered_Email')
        #     password = request.data.get('Password')
        #     origin = request.data.get('Type')
        #     userType = ""
        #     if origin in ["Review Doctor", "Registration Desk","Exit Desk"]:
        #         userType = "Ops"
        #     else:
        #         userType = origin
            

        #     hcp_data = HcpRegistrationModel.objects.filter(Registered_Email=email, Password=password).first()
        #     type = hcp_data.Type
        #     if hcp_data is None or userType != type:
        #         raise Exception("Please Enter Valid Email Or Password")
            
        #     #need to check this logic
        #     current_datetime = datetime.datetime.now()
        #     active_camps = HealthCampModel.objects.filter(StartDate__lte=current_datetime, EndDate__gte=current_datetime)
        #     active_camp_ids = [camp.HCID for camp in active_camps]
            
        #     match origin:
        #         case "HCP":
        #             hcp_assignments = AssignmentModel.objects.filter(HCPID=hcp_data.HCPID, HCID__in=active_camp_ids)
        #         case "Review Doctor":
        #             hcp_assignments = AssignmentModel.objects.filter(HCPID=hcp_data.HCPID, HCID__in=active_camp_ids, StationID=100)
        #         case "Registration Desk":
        #              hcp_assignments = AssignmentModel.objects.filter(HCPID=hcp_data.HCPID, HCID__in=active_camp_ids, StationID=101)
        #         case "Exit Desk":
        #              hcp_assignments = AssignmentModel.objects.filter(HCPID=hcp_data.HCPID, HCID__in=active_camp_ids, StationID=102)
        #         case _:
        #             raise Exception("Invalid user type")
            
        #     if hcp_assignments:
        #             asss = LoginAssignmentSerializers(hcp_assignments, many=True)
        #             hcp_data = GetHcpRegistrationSerializers(hcp_data)
        #             a=logintoken()
        #             bearer_token=a['access']
        #             assement = asss.data
        #             data = hcp_data.data
        #             data['Stations'] = assement
        #             data['Token'] = bearer_token

        #     else:
        #          raise Exception("Invalid User Type or You do not have permission")
            
        #     response = GenericResponse("Message", "Result", "Status", "HasError")
        #     response.Message = "Successful"
        #     response.Result = data
        #     response.Status = 200
        #     response.HasError = False
        #     jsonStr = json.dumps(response.__dict__)
        #     return Response(json.loads(jsonStr), status=200)
        # except Exception as e:
        #     response = GenericResponse("message", "result", "status", "has_error")
        #     response.Message = Errormessage(e)
        #     response.Result = False
        #     response.Status = 400
        #     response.HasError = True
        #     jsonStr = json.dumps(response.__dict__)
        #     return Response(json.loads(jsonStr), status=400)                    

# ------------------------------------------------------------------------------------------------------------------------------------
        


        #     if HcpRegistrationModel.objects.filter(Registered_Email=email, Password=password).first():

        #         type = hcp_data.Type
                
        #         current_datetime = datetime.datetime.now()
        #         active_camps = HealthCampModel.objects.filter(StartDate__lte=current_datetime, EndDate__gte=current_datetime)
        #         active_camp_ids = [camp.HCID for camp in active_camps]

        #         if Type  == 'HCP':
        #             if type == 'HCP':
        #                 hcp_assignments = AssignmentModel.objects.filter(HCPID=hcp_data.HCPID, HCID__in=active_camp_ids)
        #                 pass
        #             else:
        #                 raise Exception("You are not a Health Camp Doctor")
                        

        #         elif Type == 'Review Doctor':
        #             if type == 'Ops':
        #                 hcp_assignments = AssignmentModel.objects.filter(HCPID=hcp_data.HCPID, HCID__in=active_camp_ids)
        #                 if hcp_assignments:
        #                     for hcp_assignments_loop in hcp_assignments:
        #                         if hcp_assignments_loop.StationID.Station_Names == "Review Doctor":
        #                             pass
        #                         else:
        #                             raise Exception("You are not a Review Doctor")
                                    
        #                 else:
        #                     raise Exception("This User dont have any stations")
                            
        #             else:
        #                 raise Exception("You are not a Ops User or Review Doctor")

        #         elif Type == 'Registration Desk':
        #             if type == 'Ops':
        #                 hcp_assignments = AssignmentModel.objects.filter(HCPID=hcp_data.HCPID, HCID__in=active_camp_ids)
        #                 print("hcp_assignments",hcp_assignments)
        #                 if hcp_assignments:
        #                     for hcp_assignments_loop in hcp_assignments:
        #                         print(hcp_assignments_loop.StationID)
        #                         sId = hcp_assignments_loop.StationID
        #                         print(sId,'sid')
        #                         if hcp_assignments_loop.StationID.Station_Names == "Registration Desk":
        #                             pass
        #                         else:
        #                             raise Exception("You are not a Registration_Desk User")
                                    
        #                 else:
        #                     raise Exception("This User dont have any stations")
                            
        #             else:
        #                 raise Exception("You are not a Ops User or Registration_Desk user")

        #         elif Type == 'Exit Desk':
        #             if type == 'Ops':
        #                 hcp_assignments = AssignmentModel.objects.filter(HCPID=hcp_data.HCPID, HCID__in=active_camp_ids)
        #                 if hcp_assignments:
        #                     for hcp_assignments_loop in hcp_assignments:
        #                         if hcp_assignments_loop.StationID.Station_Names == "Exit Desk":
        #                             pass
        #                         else:
        #                             raise Exception("You are not a Exit_Desk User")
        #                 else:
        #                     raise Exception("This User dont have any stations")
                            
        #             else:
        #                 raise Exception("You are not a Ops User or Exit_Desk user")
            
        #         if hcp_assignments:
        #             asss = LoginAssignmentSerializers(hcp_assignments, many=True)
        #             hcp_data = GetHcpRegistrationSerializers(hcp_data)
        #             a=logintoken()
        #             bearer_token=a['access']
        #             assement = asss.data
        #             data = hcp_data.data
        #             data['Stations'] = assement
        #             data['Token'] = bearer_token

        #         else:
        #             raise Exception("There is No stations for this user")  

        #         response = GenericResponse("Message", "Result", "Status", "HasError")
        #         response.Message = "Successful"
        #         response.Result = data
        #         response.Status = 200
        #         response.HasError = False
        #         jsonStr = json.dumps(response.__dict__)
        #         return Response(json.loads(jsonStr), status=200)
                   
        #     else:
        #         raise Exception("Please Enter Valid Email Or Password")
           
                
        # except Exception as e:
        #     response = GenericResponse("message", "result", "status", "has_error")
        #     response.Message = Errormessage(e)
        #     response.Result = False
        #     response.Status = 400
        #     response.HasError = True
        #     jsonStr = json.dumps(response.__dict__)
        #     return Response(json.loads(jsonStr), status=400)         

        #    =====================================================================================     
                
