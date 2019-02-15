import create_ticket as tk
import requests
import json
ticket = tk.getTickets()


def getNetworkDevicesCount(ticket):
    controller='devnetapi.cisco.com/sandbox/apic_em'
    url = "https://" + controller + "/api/v1/network-device/count"
    header = {"content-type": "application/json", "X-Auth-Token":ticket}
    response = requests.get(url, headers=header, verify=False)
    print ("The number of network devices = ")
    r_json=response.json()
    print(r_json["response"])




getNetworkDevicesCount(ticket)
