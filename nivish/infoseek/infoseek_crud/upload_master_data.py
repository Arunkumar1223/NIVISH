from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json
from genericresponse import GenericResponse
from ..serializers import InfoseekFileUploadSerializer
from ..models import InfoseekMasterModel
from errormessage import Errormessage
import pandas as pd
import requests
import pymongo
from manage_urls import *
from datetime import datetime

def api(file):
    df = pd.read_csv(file)
    length = len(df)
    success_message = "Data already exists"
    has_error = False
    uploaded_data = []

    for id_value in range(1, length + 1):
        filtered_data = df[df['S.No'] == id_value]
    
        filtered_data = df[df['S.No'] == id_value]

        Student_Admission_Code = filtered_data['Student_Admission_Code'].iloc[0]
        Student_Admission_Date = filtered_data['Student_Admission_Date'].iloc[0]
        Student_Roll_Number = filtered_data['Student_Roll_Number'].iloc[0]
        Student_Class = str(filtered_data['Student_Class'].iloc[0])
        Student_Section = filtered_data['Student_Section'].iloc[0]
        Student_First_Name = filtered_data['Student_First_Name'].iloc[0]
        Student_Middle_Name_1 = filtered_data['Student_Middle_Name_1'].iloc[0]
        Student_Middle_Name_2 = filtered_data['Student_Middle_Name_2'].iloc[0]
        Student_Last_Name = filtered_data['Student_Last_Name'].iloc[0]
        Date_of_Birth_str = filtered_data['Date_of_Birth'].iloc[0]
        Date_of_Birth_obj = datetime.strptime(Date_of_Birth_str, '%d-%m-%Y')
        Date_of_Birth_formatted = Date_of_Birth_obj.strftime('%Y-%m-%d')
        Gender = filtered_data['Gender'].iloc[0]
        Blood_Group = filtered_data['Blood_Group'].iloc[0]
        RH_Factor = filtered_data['RH_Factor'].iloc[0]
        Mothers_First_Name = filtered_data['Mothers_First_Name'].iloc[0]
        Mothers_Middle_Name = filtered_data['Mothers_Middle_Name'].iloc[0]
        Mothers_Last_Name = filtered_data['Mothers_Last_Name'].iloc[0]
        Fathers_First_Name = filtered_data['Fathers_First_Name'].iloc[0]
        Fathers_Middle_Name = filtered_data['Fathers_Middle_Name'].iloc[0]
        Fathers_Last_Name = filtered_data['Fathers_Last_Name'].iloc[0]
        Address_Building = filtered_data['Address_Building'].iloc[0]
        Adress_Street = filtered_data['Adress_Street'].iloc[0]
        Other_Address_Part = filtered_data['Other_Address_Part'].iloc[0]
        Zip = str(filtered_data['Zip'].iloc[0])
        City = filtered_data['City'].iloc[0]
        State = filtered_data['State'].iloc[0]
        Country = filtered_data['Country'].iloc[0]
        Student_Ethnic_Origin = filtered_data['Student_Ethnic_Origin'].iloc[0]
        Mothers_Ethnic_Origin = filtered_data['Mothers_Ethnic_Origin'].iloc[0]
        Fathers_Ethnic_Origin = filtered_data['Fathers_Ethnic_Origin'].iloc[0]
        Home_Phone = filtered_data['Home_Phone'].iloc[0]
        Mothers_Mobile_Phone = filtered_data['Mothers_Mobile_Phone'].iloc[0]
        Fathers_Mobile_Phone = filtered_data['Fathers_Mobile_Phone'].iloc[0]
        Parent_Email = filtered_data['Parent_Email'].iloc[0]
        Emergency_Contact_First_Name = filtered_data['Emergency_Contact_First_Name'].iloc[0]
        Emergency_Contact_Middle_Name = filtered_data['Emergency_Contact_Middle_Name'].iloc[0]
        Emergency_Contact_Last_Name = filtered_data['Emergency_Contact_Last_Name'].iloc[0]
        Emergency_Contact_Relationship = filtered_data['Emergency_Contact_Relationship'].iloc[0]
        Emergency_Contact_Phone_1 = filtered_data['Emergency_Contact_Phone_1'].iloc[0]
        Emergency_Contact_Phone_2 = filtered_data['Emergency_Contact_Phone_2'].iloc[0]
        Emergency_Doctor_Name = filtered_data['Emergency_Doctor_Name'].iloc[0]
        Emergency_Doctor_Phone_1 = filtered_data['Emergency_Doctor_Phone_1'].iloc[0]
        Comments = filtered_data['Comments'].iloc[0]
        Ent_id = filtered_data['Ent_id'].iloc[0]
        Status = filtered_data['Status'].iloc[0]

        
        existing_data = InfoseekMasterModel.objects.filter(Student_First_Name=Student_First_Name,Date_of_Birth=Date_of_Birth_formatted,Mothers_First_Name=Mothers_First_Name,Parent_Email=Parent_Email)

        json_data = {
            'Student_Admission_Code': str(Student_Admission_Code),
            'Student_Admission_Date': str(Student_Admission_Date),
            # 'Student_Admission_Date': '2023-10-01',
            'Student_Roll_Number': Student_Roll_Number,
            'Student_Class': Student_Class,
            'Student_Section': Student_Section,
            'Student_First_Name': Student_First_Name,
            'Student_Middle_Name_1': Student_Middle_Name_1,
            'Student_Middle_Name_2': Student_Middle_Name_2,
            'Student_Last_Name': Student_Last_Name,
            'Date_of_Birth': Date_of_Birth_formatted,
            # 'Date_of_Birth': '2023-10-01',
            'Gender': Gender,
            'Blood_Group': Blood_Group,
            'RH_Factor': RH_Factor,
            'Mothers_First_Name': Mothers_First_Name,
            'Mothers_Middle_Name': Mothers_Middle_Name,
            'Mothers_Last_Name': Mothers_Last_Name,
            'Fathers_First_Name': Fathers_First_Name,
            'Fathers_Middle_Name': Fathers_Middle_Name,
            'Fathers_Last_Name': Fathers_Last_Name,
            'Address_Building': Address_Building,
            'Adress_Street': Adress_Street,
            'Other_Address_Part': Other_Address_Part,
            # 'Zip': '545215',
            'Zip': str(Zip),
            'City': City,
            'State': State,
            'Country': Country,
            'Student_Ethnic_Origin': Student_Ethnic_Origin,
            'Mothers_Ethnic_Origin': Mothers_Ethnic_Origin,
            'Fathers_Ethnic_Origin': Fathers_Ethnic_Origin,
            'Home_Phone': Home_Phone,
            'Mothers_Mobile_Phone': Mothers_Mobile_Phone,
            'Fathers_Mobile_Phone': Fathers_Mobile_Phone,
            'Parent_Email': Parent_Email,
            'Emergency_Contact_First_Name': Emergency_Contact_First_Name,
            'Emergency_Contact_Middle_Name': Emergency_Contact_Middle_Name,
            'Emergency_Contact_Last_Name': Emergency_Contact_Last_Name,
            'Emergency_Contact_Relationship': Emergency_Contact_Relationship,
            'Emergency_Contact_Phone_1': Emergency_Contact_Phone_1,
            'Emergency_Contact_Phone_2': Emergency_Contact_Phone_2,
            'Emergency_Doctor_Name': Emergency_Doctor_Name,
            'Emergency_Doctor_Phone_1': Emergency_Doctor_Phone_1,
            'Comments': Comments,
            'Ent_id': str(Ent_id),
            'Status': str(Status),
        }

        json_payload = json.dumps(json_data)

        if not existing_data:
            url = infoseekmaster_url

            token = token1
            
            # try:
            headers = {
                                    'Accept': 'application/json',
                                    'Content-Type': 'application/json',
                                    'Authorization': f'Bearer {token}'  # Replace with your token
                            }
            
            response = requests.post(url, headers=headers, data=json_payload)
            if response.status_code == 200:
                uploaded_data.append(json_data)
                success_message = "New data uploaded successfully"
                has_error = True

    return success_message, has_error, uploaded_data


from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import parser_classes

@parser_classes((MultiPartParser,))


class InfoseekUploadExcel(generics.GenericAPIView):
    """Here We can uploading Infoseek Master Data"""
    serializer_class = InfoseekFileUploadSerializer

    def post(self, request, *args, **kwargs):
        try:
            file = request.data.get('file')

            success_message, has_error, uploaded_data = api(file)

            response = GenericResponse("Message", "Result", "Status", "HasError")

            if has_error:
                response.Message = success_message
                response.Result = uploaded_data
                response.Status = 200
                response.HasError = False
            else:
                response.Message = success_message
                response.Status = 400
                response.HasError = True

            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=response.Status)

        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)