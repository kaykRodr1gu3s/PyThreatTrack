import requests
import abuseIp

class virustotal_search:
    def __init__(self):
        self.endpoint_v3 = "https://www.virustotal.com/api/v3/ip_addresses/"
        self.headers = headers = {
    "accept": "application/json",
    "x-apikey": "api"
}
        
        self.abuseIP = abuseIp.Ips_class()
        self.page_content = self.abuseIP.abuseip_request()
        self.ip_list = self.abuseIP.getting_ip_list(self.page_content)


    def test(self):
        for c in self.ip_list:
            req = requests.get(f"{self.endpoint_v3}{c}", headers=self.headers)
            print(req.text)
        
