import requests
response = requests.get("https://api.github.com")

print(response.status_code)
print(response.text)

import requests

response = requests.get("https://api.github.com")
data = response.json

print(data)

import requests
r = requests.get("https://httpbin.org/get")
print(r.status_code)

import requests
data = {"name": "Anamika",
        "age": 18
}
r = requests.post("https://httpbin.org/post",data = data)

print(r.text)
