import requests
from Tools import abuseIp


class virustotal_search:
    def __init__(self):
        self.endpoint_v3 = "https://www.virustotal.com/api/v3/ip_addresses/"
        self.headers = {
    "accept": "application/json",
    "x-apikey": "api"
}
        
        self.abuseIP = abuseIp.Ips_class()
        self.page_content = self.abuseIP.abuseip_request()
        self.ip_list = self.abuseIP.getting_ip_list(self.page_content)


    def search(self):
        list_to_csv = []
        for ip in self.ip_list:
            req = requests.get(f"{self.endpoint_v3}{ip}", headers=self.headers)
            response = req.json()


            list_to_csv.append(response['data']['attributes']['last_analysis_stats'])
        return list_to_csv
        

    def datas_csv(self, json):
        print(json)



a = virustotal_search()

datas = a.search()
b = a.datas_csv(datas)