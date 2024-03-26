import requests
from bs4 import BeautifulSoup
import re

class Ips_class:
    
    def __init__(self) -> None:
        self.base_url = 'https://www.abuseipdb.com/'
        self.header = {"User-agent": "Mozilla/5.0"}
        self.ip_list = []

    
    def abuseip_request(self) -> bytes:
        
        """
        
        This function, do the request to https://www.abuseipdb.com, and return the page content 
        
        """

        req = requests.get(self.base_url, headers=self.header)
        
        return req.content


    def getting_ip_list(self, page_content: bytes) -> list:

        """
        
       This function takes the page content as an argument and parses the HTML from the page. It then uses regex to find the pattern and extract the IP addresses listed under 'Recently Reported IPs'.
        
        """


        bs = BeautifulSoup(page_content, "html.parser")
        ips = bs.find_all("a", href=re.compile(r'https://www.abuseipdb.com/check/(\d.)+'))
        
        for ip in ips:
            self.ip_list.append(ip.text)

        return self.ip_list
    
