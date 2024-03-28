import requests
from Tools.csv_creators import abuseip_csv_creator

url = 'https://api.abuseipdb.com/api/v2/check'

headers = {
    'Accept': 'application/json',
    'Key': 'api'
}
querystring = {
    'ipAddress': '95.214.53.99',
    'maxAgeInDays': '90'
}

req = requests.request(method="GET" , url=url, headers=headers, params=querystring)
test = req.json()
test = test['data']


a = abuseip_csv_creator.abuseip()
a.data([test])

