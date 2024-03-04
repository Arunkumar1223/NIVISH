import requests
def logintoken():
    url="http://65.1.50.165:8000/"
    api = url + "Api/token/"
    headers = {'Content-Type': 'application/json'}

    # null = None
    post = {
        "username": "nivish",
        "password": "nivish@1",

    }

    r = requests.post(api, json=post, headers=headers)
    data = r.json()
    return data

