import requests

url = "http://127.0.0.1:8080/health/users/item"
headers = {
    'Content-Type': 'application/json'
}

data = {
    "username": "19044449870",
    "password": "bd123456",
    "nickname": "Bob"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
