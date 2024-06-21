import logging
import requests
from xml.etree import ElementTree as ET
url = "https://www.w3schools.com/xml/cd_catalog.xml"
response = requests.get(url)
root = ET.fromstring(response.content)
 
logging.basicConfig(level = logging.INFO)
cds = []
 
for cd_info in root.findall("CD"):
    cd_title = cd_info.find("TITLE").text
    cd_artist = cd_info.find("ARTIST").text
    cds.append((cd_title, cd_artist))

logging.info(f"cds: {cds} \n")