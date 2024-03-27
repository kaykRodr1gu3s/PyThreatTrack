import requests
from Tools import abuseIp
from Tools import csv_transformer

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


    def search(self) -> list:

        """
        This function, will do the request to virustotal endpoint, returning a json.This json will be parsed and saved in a list od dict 
          
        """

        list_to_csv = []
       
        for ip in self.ip_list:
            dict_datas = {}
            dict_datas['Ip address'] = ip

            req = requests.get(f"{self.endpoint_v3}{ip}", headers=self.headers)
            response = req.json()
            
            for key in response['data']['attributes']['last_analysis_stats']:

                dict_datas[key] = response['data']['attributes']['last_analysis_stats'][key]
            
            list_to_csv.append(dict_datas)

        return list_to_csv
        

virustotal = virustotal_search()
datas_to_csv = virustotal.search()


csv = csv_transformer.csv_creator()
csv.datas_to_csv(datas_to_csv)
        