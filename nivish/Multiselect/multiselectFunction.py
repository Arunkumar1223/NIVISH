import json
from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse


class multiselect :
       def check_field_lists(data, field_lists):
              if field_lists is not None:
                for field, value in data.items():
                    if value is not None:
                        if field in field_lists:
                            value_list = value.split(',')
                            if not all(item in field_lists[field] for item in value_list):
                                response = GenericResponse('message', 'result', 'status', 'Haserror')
                                response.Message = 'Select exact values for ' + field
                                response.Result = False
                                response.Status = 200
                                response.HasError = True
                                jsonStr = json.dumps(response.__dict__)
                                return Response(json.loads(jsonStr), status=400)
                    else:
                         pass



              