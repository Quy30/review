import json
import requests

def get_org_inven():
    organizationId = '681155'
    url= f'https://api.meraki.com/api/v1/organizations/{organizationId}/inventory/devices'

    header = {
        'X-Cisco-Meraki-API-Key':'6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
    }
    resp= requests.get(url, headers= header )
    data= resp.json()
    # print(data)
    # print(json.dumps(data, indent=4))
    num=len(data)
    # print(num)
    for i in range(num):
        network= data[i]['networkId']
        if network == None:
            print(json.dumps(data[i],indent=4))
get_org_inven()