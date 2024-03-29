import requests
from Tools.IPTracker import ips
from Tools.csv_creators import CSVprocessor

class virustotal_search:
    def __init__(self, API_KEY):

        self.endpoint_v3 = "https://www.virustotal.com/api/v3/ip_addresses/"
        self.headers = {
    "accept": "application/json",
    "x-apikey": API_KEY
                        }
        
        self.abuseIP = ips.Ips_class()
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
        

virustotal = virustotal_search(API_KEY="API KEY")
datas_to_csv = virustotal.search()

csv = CSVprocessor.abuseip("virustotal_result_ips.csv")
dir_name = csv.verifing_directory()
csv.appending_datas(dir_name,datas_to_csv)
        