# scraper.py

import requests
from bs4 import BeautifulSoup

def get_website_text(url):
    try:
        html = requests.get(url).text

        soup = BeautifulSoup(html, "html.parser")

        text = soup.get_text(separator=" ")

        return text[:15000]

    except Exception as e:
        return str(e) 