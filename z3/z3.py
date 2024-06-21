import logging
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
 
logging.basicConfig(level = logging.INFO)
titles_lock = threading.Lock()

countries = ["poland", "spain", "morocco", "bolivia", "syria", "canada", "france", "latavia", "turkey", "algier", "china", "italy", "indonesia", "yemen", "peru"];
links = []
universities = []
 
def download_site(url):
    ctr = url.split("=")[-2:]
    country = ctr[1]
    with requests.get(url) as response:
        unis = response.json()
        for uni in unis:
            name = uni.get('name')
            universities.append(name)
    logging.info(f" country: {country},  universities: {universities}")

 
def download_all_sites(url):
    with ThreadPoolExecutor() as executor:
        for country in countries:
            link = url + country
            links.append(link)    
        executor.map(download_site, links)

url = "http://universities.hipolabs.com/search?country="


download_all_sites(url)