from rest_framework import generics
from rest_framework.response import Response
from genericresponse import GenericResponse
from errormessage import Errormessage
import pycountry
from rest_framework import status
from unidecode import unidecode

class StatesGet(generics.GenericAPIView):
    """Here We can get the States based on Country Name"""

    def get_states(self, country_name):
        try:
            country = pycountry.countries.get(name=country_name)
            subdivisions = pycountry.subdivisions.get(country_code=country.alpha_2)
            states = [unidecode(subdivision.name).strip() for subdivision in subdivisions]
            return states
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        try:
            country_name = kwargs.get('country_name', None)
            if not country_name:
                return Response({"error": "Please provide a valid country_name parameter"}, status=status.HTTP_400_BAD_REQUEST)

            states = self.get_states(country_name)

            response = GenericResponse("Message", "Result", "Status", "HasError")
            if states:
                response.Message = "Successful"
                response.Result = states
                response.Status = 200
                response.HasError = False
            else:
                response.Message = f"States not found for {country_name}"
                response.Result = []
                response.Status = 404
                response.HasError = True

            return Response(response.__dict__, status=response.Status)

        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            return Response(response.__dict__, status=response.Status)