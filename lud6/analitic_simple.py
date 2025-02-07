import requests
from bs4 import BeautifulSoup
import json

url = "http://main-server:8080/simple/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

packages = [a.text.strip("/") for a in soup.find_all("a")]
print(json.dumps(packages, indent=2))

