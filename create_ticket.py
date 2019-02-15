﻿# import requests library
import requests
def getTickets():
#import json library
    import json

# put the ip address or dns of your apic-em controller in this url
#url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    url='https://devnetapi.cisco.com/sandbox/apic_em/api/v1/ticket'



#the username and password to access the APIC-EM Controller
    payload = {"username":"devnetuser","password":"Cisco123!"}


#Content type must be included in the header
    header = {"content-type": "application/json"}

#Performs a POST on the specified url.
    response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

# print the json that is returned
    r_json = response.json()
    return r_json["response"]["serviceTicket"]




