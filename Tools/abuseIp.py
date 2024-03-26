import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.abuseipdb.com/", headers={"User-agent": "Mozilla/5.0"})

page_content = BeautifulSoup.find_all
print(req.status_code)