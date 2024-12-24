from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from geopy.geocoders import ArcGIS
import pandas as pd
import time
import os


class YellowPagesData:
    data = {}
    nom = ArcGIS(timeout=10)
    opt = Options()
    opt.add_extension("C:/eppiocemhmnlbhjplcgkofciiegomcon_1.4390997f076e5e5f9fcbd37b7d785126cd96043daf2c12ac6bfbe7de5a28c962")
    ser = Service("C:/chromedriver.exe")
    def __init__(self):
        self.driver = webdriver.Chrome(options=self.opt, service=self.ser)
        self.driver.maximize_window()

    def land_first_page(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(5)

    def get_name(self):
        try:
            name = self.driver.find_element(By.XPATH, '//a[@class="listing-name"]').text
            self.driver.implicitly_wait(5)
            print("Name: "+name)
            self.data['Name'] = name

        except:
            self.data['Name'] = 'N/A'

    def get_address(self):
        try:
            address = self.driver.find_element(By.XPATH, '//div[@class="listing-address mappable-address mappable-address-with-poi" or @class="listing-address mappable-address"]').text
            self.driver.implicitly_wait(5)
            print("Address: "+address)
            self.data['Address'] = address
            coor = self.nom.geocode(address)
            print("Latitude: "+str(coor.latitude))
            self.data['Latitude'] = str(coor.latitude)
            print("Longitude: "+str(coor.longitude))
            self.data['Longitude'] = str(coor.longitude)
            if address.find(',') != -1:
                split_address = address.split(',')
                street_address = split_address[0]
                self.data['Street Address'] = street_address
                print("Street Address: "+street_address)
                split_zip = split_address[-1].split(' ')
                if len(split_zip) == 4:
                    zip_code = split_zip[-2]+" "+split_zip[-1]
                    city = split_zip[0]+" "+split_zip[1]
                    print("City: "+city)
                    self.data['City'] = city
                    print("Zip Code: "+zip_code)
                    self.data['Zip Code'] = zip_code
                elif len(split_zip) == 3:
                    zip_code = split_zip[-2] + " " + split_zip[-1]
                    city = split_zip[-3]
                    print("City: " + city)
                    self.data['City'] = city
                    print("Zip Code: " + zip_code)
                    self.data['Zip Code'] = zip_code
                country = 'Australia'
                self.data['Country'] = country
                print("Country: "+country)
            else:
                street_address = 'N/A'
                split_zip = address.split(' ')
                zip_code = split_zip[-2] + " " + split_zip[-1]
                if len(split_zip) == 4:
                    city = split_zip[-4]+" "+split_zip[-3]
                    print("Street Address: " + street_address)
                    self.data['Street Address'] = street_address
                    print("City: " + city)
                    self.data['City'] = city
                    print("Zip Code: " + zip_code)
                    self.data['Zip Code'] = zip_code
                    country = 'Australia'
                    self.data['Country'] = country
                    print("Country: " + country)
                elif len(split_zip) == 3:
                    city = split_zip[-3]
                    print("Street Address: " + street_address)
                    self.data['Street Address'] = street_address
                    print("City: " + city)
                    self.data['City'] = city
                    print("Zip Code: " + zip_code)
                    self.data['Zip Code'] = zip_code
                    country = 'Australia'
                    self.data['Country'] = country
                    print("Country: " + country)

                    print("Street Address: "+street_address)
                    self.data['Street Address'] = street_address
                    print("City: " + city)
                    self.data['City'] = city
                    print("Zip Code: " + zip_code)
                    self.data['Zip Code'] = zip_code
                    country = 'Australia'
                    self.data['Country'] = country
                    print("Country: " + country)
                else:
                    city = 'N/A'
                    print("Street Address: " + street_address)
                    self.data['Street Address'] = street_address
                    print("City: " + city)
                    self.data['City'] = city
                    print("Zip Code: " + zip_code)
                    self.data['Zip Code'] = zip_code
                    country = 'Australia'
                    self.data['Country'] = country
                    print("Country: " + country)

        except:
            self.data['Address'] = 'N/A'
            self.data['Latitude'] = 'N/A'
            self.data['Longitude'] = 'N/A'
            self.data['Street Address'] = 'N/A'
            self.data['City'] = 'N/A'
            self.data['Zip Code'] = 'N/A'
            self.data['Country'] = 'N/A'

    def get_speciality(self):
        try:
            spec = self.driver.find_element(By.XPATH, '//h2[@class="listing-heading"]/a').text
            self.driver.implicitly_wait(2)
            print("Speciality: "+spec)
            self.data['Speciality'] = spec
        except:
            self.data['Speciality'] = 'N/A'

    def get_phone(self):
        try:
            phone = self.driver.find_element(By.XPATH, '//a[@title="Phone"]').get_attribute('href')
            self.driver.implicitly_wait(2)
            print("Phone: "+phone.replace('tel:', ''))
            self.data['Phone'] = phone.replace('tel:', '')
        except:
            self.data['Phone'] = 'N/A'

    def get_email(self):
        try:
            mail = self.driver.find_element(By.XPATH, '//a[@class="contact contact-main contact-email"]').get_attribute('href')
            self.driver.implicitly_wait(2)
            print("E-Mail: "+mail[:mail.index('?')].replace('%40', '@').replace('mailto:', ''))
            self.data['E-Mail'] = mail[:mail.index('?')].replace('%40', '@').replace('mailto:', '')
        except:
            self.data['E-Mail'] = 'N/A'

    def get_website(self):
        try:
            web = self.driver.find_element(By.XPATH, '//a[@class="contact contact-main contact-url"]').get_attribute('href')
            self.driver.implicitly_wait(2)
            print("Website: "+web)
            self.data['Website'] = web
        except:
            self.data['Website'] = 'N/A'

    def get_timings(self):
        try:
            time = self.driver.find_element(By.XPATH, '//div[@class="text-and-image inside-gap inside-gap-medium"]')
            self.driver.implicitly_wait(2)
            time.click()
            timings = self.driver.find_element(By.XPATH, '//div[@class="opening-hours-all-days"]').text
            self.driver.implicitly_wait(1.5)
            print("Timings: "+timings)
            self.data['Timings'] = timings
        except:
            self.data['Timings'] = 'N/A'

    def get_other_details(self):
        try:
            staff = self.driver.find_element(By.XPATH, '//dd[@class="number-of-employees"]').text
            self.driver.implicitly_wait(2)
            print("Staff: "+staff)
            self.data['Staff'] = staff
        except:
            self.data['Staff'] = 'N/A'

        try:
            estab = self.driver.find_element(By.XPATH, '//dd[@class="established"]').text
            self.driver.implicitly_wait(1.5)
            print("Established: "+estab)
            self.data['Established'] = estab
        except:
            self.data['Established'] = 'N/A'

        try:
            legal = self.driver.find_element(By.XPATH, '//dd[@class="legal-id"]').text
            self.driver.implicitly_wait(1.5)
            leg = legal.split(" ")
            print("Legal ID: "+leg[-1])
            self.data['Legal ID'] = leg[-1]
        except:
            self.data['Legal ID'] = 'N/A'

    def get_about(self):
        try:
            about = self.driver.find_element(By.XPATH, '//div[@class="listing-descriptors about-us-section"]').text
            self.driver.implicitly_wait(1.5)
            print("About: "+str(about))
            self.data['About'] = about
        except:
            self.data['About'] = 'N/A'

    def get_logo(self):
        try:
            logo = self.driver.find_element(By.XPATH, '//img[@class="brand-logo"]').get_attribute('src')
            self.driver.implicitly_wait(1.5)
            print("Logo Url: "+logo)
            self.data['Logo URL'] = logo
        except:
            self.data['Logo URL'] = 'N/A'

    def get_ABN(self):
        try:
            abn = self.driver.find_element(By.XPATH, '//dd[@class="abn"]').text
            self.driver.implicitly_wait(2)
            print("ABN: "+abn)
            self.data['ABN'] = abn
        except:
            self.data['ABN'] = '-'

    def get_ACN(self):
        try:
            acn = self.driver.find_element(By.XPATH, '//dd[@class="acn"]').text
            self.driver.implicitly_wait(2)
            print("ACN: "+acn)
            self.data['ACN'] = acn
        except:
            self.data['ACN'] = '-'

    def get_listed_under(self):
        try:
            listed = self.driver.find_element(By.XPATH, '//dd[@class="also-listed-under"]').text
            self.driver.implicitly_wait(2)
            print("Listed Under: "+listed)
            self.data['Listed Under'] = listed
        except:
            self.data['Listed Under'] = '-'

    def trade_as(self):
        try:
            trade = self.driver.find_element(By.XPATH, '//dd[@class="trading-aliases"]').text
            self.driver.implicitly_wait(2)
            print("Also Trade As: "+trade)
            self.data['Also Trade As'] = trade

        except:
            self.data['Also Trade As'] = '-'

    def get_image(self):
        img = self.driver.find_elements(By.XPATH, '//img[@class="rsImg rsMainSlideImage"]')
        self.driver.implicitly_wait(1.5)
        try:
            print("Image Url 1: "+str(img[0].get_attribute('src')))
            self.data['Image URL 1'] = img[0].get_attribute('src')
        except:
            self.data['Image URL 1'] = 'N/A'

        try:
            print("Image Url 2: " + str(img[1].get_attribute('src')))
            self.data['Image URL 2'] = img[1].get_attribute('src')
        except:
            self.data['Image URL 2'] = 'N/A'

        try:
            print("Image Url 3: " + str(img[2].get_attribute('src')))
            self.data['Image URL 3'] = img[2].get_attribute('src')
        except:
            self.data['Image URL 3'] = 'N/A'

    def current_url(self):
        self.data['Current Url'] = self.driver.current_url





    def move_into_file(self):
        p = pd.DataFrame([self.data])
        p.to_csv("C:/imp codes/Ye/data/camden.csv", mode='a', header=not os.path.exists("C:/imp codes/Ye/data/camden.csv"),
                 index=False)




bot = YellowPagesData()
time.sleep(30)
with open("C:/imp codes/Ye/link/camden.csv") as file:
    for f in file:
        try:
            bot.land_first_page(f)
            bot.get_name()
            bot.get_address()
            bot.get_speciality()
            bot.get_phone()
            bot.get_email()
            bot.get_website()
            bot.get_timings()
            bot.get_other_details()
            bot.get_about()
            bot.get_logo()
            bot.get_image()
            bot.get_ABN()
            bot.get_ACN()
            bot.get_listed_under()
            bot.trade_as()
            bot.current_url()
            bot.move_into_file()
        except:
            pass
