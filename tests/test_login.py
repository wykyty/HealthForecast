import requests

url = "http://127.0.0.1:8080/health/user/auth"
headers = {
    'Content-Type': 'application/json'
}

data = {
    "type": "login",
    "login_type": "password",
    "phone_number": "19099933340",
    "passwd": "bd123sdf6"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
print(response.json())
