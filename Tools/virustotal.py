import requests
import abuseIp

class virustotal_search:
    def __init__(self):
        self.abuseIP = abuseIp.Ips_class()
        self.page_content = self.abuseIP.abuseip_request()
        self.ip_list = self.abuseIP.getting_ip_list(self.page_content)


