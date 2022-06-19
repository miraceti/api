import requests
from requests import status_codes

api_url = "http://shibe.online/api/shibes?count=1"

response = requests.get(api_url)

status_code = response.status_code
print("satus code : ", status_code)

response_json = response.json()
print(response_json)