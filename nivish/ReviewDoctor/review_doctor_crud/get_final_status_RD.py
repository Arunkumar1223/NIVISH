from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import FInalStatusFilterSerializer,GetFinalStatusSerializers
from ..models import FinalStatusModel
from errormessage import Errormessage





class GetFinalStatusList(generics.GenericAPIView):
    serializer_class = FInalStatusFilterSerializer

    def post(self, request, *args, **kwargs):
        try:
            # request
            HCID = request.data.get('HCID')
            Review_status = request.data.get('Review_status')
            Final_Flag_status = request.data.get('Final_Flag_status')
            page_size = request.data.get('page_size')
            page_number = request.data.get('page_number')

            if Final_Flag_status is None and Review_status is not None:
                print("Final_Flag_status",Final_Flag_status)
                
                Review_status_values = Review_status.split(',')
                final = FinalStatusModel.objects.filter(HCID = HCID, Review_status__in=Review_status_values)

                
            elif Review_status is None and Final_Flag_status is not None:

                Final_Flag_status_values = Final_Flag_status.split(',')
                final = FinalStatusModel.objects.filter(HCID = HCID, Final_Flag_status__in=Final_Flag_status_values)


            elif Review_status and Final_Flag_status is not None  :
                Review_status_values = Review_status.split(',')
                Final_Flag_status_values = Final_Flag_status.split(',')
                final = FinalStatusModel.objects.filter(HCID = HCID, Review_status__in=Review_status_values, Final_Flag_status__in=Final_Flag_status_values)
            else:
                final = FinalStatusModel.objects.filter(HCID = HCID)
            print(final,'FinalStatusModel')

            length = len(final)
            pagecount = round(length / page_size)
            start_index = (page_number - 1) * page_size
            end_index = page_number * page_size
            paginated_result_list = final[start_index:end_index]
            serializer=GetFinalStatusSerializers(paginated_result_list,many = True).data 
            serializer_data={"data":serializer,"pagecount":pagecount}

            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = serializer_data
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
