import requests
from Tools.csv_creators import CSVprocessor
from Tools.IPTracker import ips

class abuseipapi:
    def __init__(self, API) -> None:
        self.endpoint = "https://api.abuseipdb.com/api/v2/check"
        self.header = {
                'Accept': 'application/json',
                'Key': API
                        } 
        
    def search(self, ip_list):
        datas_to_csv = []
        for ip in ip_list:
            
            query = {
            'ipAddress': ip,
            'maxAgeInDays': '90'
            }
            req = requests.get(url=self.endpoint, headers=self.header, params=query)
            data = req.json()
            data = data['data']
            datas_to_csv.append(data)
        print(datas_to_csv)
        return datas_to_csv


list_ip = ips.Ips_class()
abuseip_page_content = list_ip.abuseip_request()
all_ips = list_ip.getting_ip_list(abuseip_page_content)


abuseip = abuseipapi("API KEY")
datas_to_csv = abuseip.search(all_ips)

csv = CSVprocessor.abuseip("abuseIP.csv")
dir_name = csv.verifing_directory()
csv.appending_datas(dir_name,datas_to_csv)