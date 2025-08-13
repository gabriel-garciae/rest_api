import requests

url = "http://localhost:8000/recursos"

response = requests.get(url)

print(response.status_code)
print(response.json())