import requests
import json

base_url = "https://devnetapi.cisco.com/sandbox/apic_em"
api_url = "/api/v1/ticket"
service_ticket = ""
request_header = {'Content-Type':'application/json'}
credentials_dict =  {'username': 'devnetuser', 'password':'Cisco123!'}
request_data = credentials_dict

## api call to set the service ticket param ##
response = requests.post(base_url + api_url, headers={'Content-Type':'application/json'}, data= json.dumps(request_data))
response_json = response.json()
service_ticket = response_json['response']['serviceTicket']

## api call to get network hosts details ##
api_url = "/api/v1/host"
request_header['X-Auth-Token'] = service_ticket  ## setting the service ticket fetched previously to the request header
response = requests.get(base_url + api_url, headers= request_header)
response_json = response.json()
print(response_json)
