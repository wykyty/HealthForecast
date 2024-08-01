import requests

url = "http://127.0.0.1:8080/health/user/login"
headers = {
    'Content-Type': 'application/json'
}

data = {
    "type": "login",
    "login_type": "password",
    "username": "19099933340",
    "password": "bd123sdf6"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
print(response.json())
