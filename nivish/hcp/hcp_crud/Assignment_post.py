from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import AssignmentSerializers, GetAssignmentSerializers
from errormessage import Errormessage
from rest_framework.permissions import IsAuthenticated
from ..models import HcpRegistrationModel, AssignmentModel



class AssignmentPost(generics.GenericAPIView):
    serializer_class = AssignmentSerializers
    def post(self, request, *args, **kwargs):
        try:
            hcpid = request.data.get('HCPID')
            stationid = request.data.get('StationID')
            HCID = request.data.get('HCID')
           
            # existing_data = AssignmentModel.objects.all()
            # print("Existing Data:", existing_data)
            
            existing_assignment = AssignmentModel.objects.filter(HCPID=hcpid, StationID=stationid, HCID=HCID).first()
            if existing_assignment:
                raise Exception("This HCPID,HCID and StationID already exists.")
            hcpdata = HcpRegistrationModel.objects.get(HCPID=hcpid)
            hcp_type = hcpdata.Type
            print("Type:", hcp_type)

            if hcp_type == 'Ops':
                
                valid_ops_stationids = {100, 101, 102}
                print('Ops')
                if int(stationid) not in valid_ops_stationids:
                    raise Exception("Invalid StationID for Ops type. Should be 100, 101, or 102.")
                
            elif hcp_type == 'HCP':
                print('HCP')
                
                if int(stationid) not in range(1, 9):
                    raise Exception("Invalid StationID for HCP type. Should be between 1 to 8.")
            else:
                raise Exception("Invalid Type provided. Type should be 'Ops' or 'HCP'.")
            print("Mani")
            
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = GetAssignmentSerializers(user).data
            response.Status = 200
            response.HasError = False
            json_str = json.dumps(response.__dict__)
            return Response(json.loads(json_str), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = str(e)  
            response.Result = False
            response.Status = 400
            response.HasError = True
            json_str = json.dumps(response.__dict__)
            return Response(json.loads(json_str), status=400)