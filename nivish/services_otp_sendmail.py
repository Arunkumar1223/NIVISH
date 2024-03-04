
import json
import requests

def Servicespost(Otp,Email,Student_FirstName):
    url = "http://65.1.50.165:8001/Nivish/InfoseekOtpGeneration/"

    json_data = {
        'Otp': Otp,
        'Email': Email,
        'Name': Student_FirstName
    }
    print(json_data,"json")

    json_payload = json.dumps(json_data)
    # print(json_payload,'satand')

    token ='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzOTUxNTQxLCJpYXQiOjE3MDYxNzU1NDEsImp0aSI6IjFmOWU2MzRkMTIzMTRkYzRiMzg4OGE3MTUyMTY5NThmIiwidXNlcl9pZCI6MX0.0dxDtNqoOhU7mT9dHEQo8ZQFEJFC_PBMVq5zNnT37Dk'
    try:
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'  # Replace with your token
        }

        response = requests.post(url, headers=headers, data=json_payload)
        print(response,"response")
        

        if response.status_code == 200:
            data = response.json()
            result = data
        else:
            result = False
    except requests.exceptions.RequestException as e:
        result = False
    # print(result,"result")

        # result_data = []
    return result