import requests
import json
from requests.auth import HTTPBasicAuth

requests.packages.urllib3.disable_warnings()


HOST = '192.168.0.82' #CSR1000v Router IP
PORT = 443 #HTTPS Port
USER = 'cisco' #Username
PASS = 'cisco' #Password


basic = HTTPBasicAuth(USER, PASS) #Basic Authentication
headers = {'Content-type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}


x = requests.get("https://{h}:{p}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1".format(h=HOST, p=PORT), auth=basic, headers=headers, verify=False)

#print(x.status_code)
#print (x.json())
print(x.text)

