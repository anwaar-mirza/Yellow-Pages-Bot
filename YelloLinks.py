from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from geopy.geocoders import ArcGIS
import pandas as pd
import time
import os


class YellowLinks:
    data = {}
    nom = ArcGIS(timeout=10)
    opt = Options()
    opt.add_extension("C:/Users/anwaa/AppData/Local/Google/Chrome/User Data/extensions_crx_cache/eppiocemhmnlbhjplcgkofciiegomcon_1.4390997f076e5e5f9fcbd37b7d785126cd96043daf2c12ac6bfbe7de5a28c962")

    def __init__(self):
        self.driver = webdriver.Chrome(options=self.opt)
        self.driver.maximize_window()

    def land_first_page(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    def get_links(self):
        links = self.driver.find_elements(By.XPATH, '//div[@class="Box__Div-sc-dws99b-0 fYIHHU"]/a')
        self.driver.implicitly_wait(5)
        for l in links:
            print("Link: "+l.get_attribute('href'))
            self.data['Links'] = l.get_attribute('href')
            p = pd.DataFrame([self.data])
            p.to_csv("C:/imp codes/Ye/link/camden.csv", mode='a', header=not os.path.exists("C:/imp codes/Ye/link/camden.csv"), index=False)


bot = YellowLinks()
time.sleep(15)
for i in range(1, 150):
    time.sleep(5)
    bot.land_first_page(f'https://www.yellowpages.com.au/search/listings?clue=Plumbers&locationClue=Camden+Council&pageNumber={i}')
    bot.get_links()
