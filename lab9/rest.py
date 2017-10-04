import requests
import json

base_url = "https://devnetapi.cisco.com/sandbox/apic_em"
api_url = "/api/v1/ticket"


response = requests.post(base_url + api_url, headers={'Content-Type':'application/json'}, data= json.dumps({'username': 'devnetuser', 'password':'Cisco123!'}))

print(response.json())