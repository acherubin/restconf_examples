import requests
import json

# Disable SSL verification warnings
requests.packages.urllib3.disable_warnings()

# Router details
router_ip = '192.168.0.10'
username = 'cisco'
password = 'cisco'
#interface_name = 'GigabitEthernet=1'
interface_name = 'GigabitEthernet1'

# API endpoint for native interface JSON output
api_endpoint = f"https://{router_ip}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface={interface_name}"

# Request headers
headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
}

# Authentication credentials
auth = (username, password)

# Make the request
response = requests.get(api_endpoint, headers=headers, auth=auth, verify=False)

# Check the response status code
if response.status_code == 200:
    # Print the JSON output
    #print(response.json())
    print(response.text)
else:
    print(f"Request failed with status code {response.status_code}")
