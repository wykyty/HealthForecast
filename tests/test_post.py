import requests

url = "http://127.0.0.1:8080/register"
headers = {
    'Content-Type': 'application/json'
}

data = {
    "username": "19099933340",
    "password": "bd123sdf6",
    "nickname": "Candy"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
