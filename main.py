from bs4 import BeautifulSoup
import requests
from PIL import Image
import os
import lxml
from lxml import etree
import pandas as pd
import numpy as np
from html.parser import HTMLParser

class properties():

    def __init__(self, mls_link):
        self.mls_link = mls_link
        # self.listing_div = None
        self._collect_listings()


    def _collect_listings(self):
        response = requests.get(self.mls_link)
        html = response.text
        html_soup = BeautifulSoup(html, features='html.parser')
        self.listing_div = html_soup.find_all('div', attrs={'class': 'j-resultsPageAsyncDisplays'})
   
    def convert_to_HTML(self):
        self.p = HTMLParser()
        self.p.feed(str(self.listing_div))
        self.p.close()
        

if __name__ == "__main__":

    mls_link = os.environ['MLS_FEED_URL']

    northern_denver_properties = properties(mls_link)