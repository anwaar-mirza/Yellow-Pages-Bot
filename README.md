# Yellow-Pages-Bot

This documentation covers the methods and functions of the two Python scripts designed for scraping business information from Yellow Pages using Selenium and Geopy. The primary class in focus is `YellowPagesData`, which encapsulates all functionalities related to data extraction.

## Overview

The `YellowPagesData` class is responsible for navigating the Yellow Pages website, extracting detailed information about businesses, and saving that information into a CSV file. The script utilizes Selenium for web automation and Geopy for geocoding addresses.

## Class: `YellowPagesData`

### Attributes
- **data**: A dictionary to store scraped data.
- **nom**: An instance of `ArcGIS` for geocoding (converting addresses to geographical coordinates).
- **opt**: Chrome options for the Selenium WebDriver.
- **ser**: Service for the ChromeDriver.

### Initialization
```python
def __init__(self):
    self.driver = webdriver.Chrome(options=self.opt, service=self.ser)
    self.driver.maximize_window()
```
- Initializes the WebDriver with specified options and maximizes the browser window.

### Methods

#### 1. `land_first_page(url)`
```python
def land_first_page(self, url):
    self.driver.get(url)
    self.driver.implicitly_wait(5)
```
- Navigates to the specified URL and waits implicitly for elements to load.

#### 2. `get_name()`
```python
def get_name(self):
    try:
        name = self.driver.find_element(By.XPATH, '//a[@class="listing-name"]').text
        self.data['Name'] = name
    except:
        self.data['Name'] = 'N/A'
```
- Extracts the business name from the page and stores it in the `data` dictionary.

#### 3. `get_address()`
```python
def get_address(self):
    try:
        address = self.driver.find_element(By.XPATH, '//div[@class="listing-address mappable-address"]').text
        self.data['Address'] = address
        coor = self.nom.geocode(address)
        self.data['Latitude'] = str(coor.latitude)
        self.data['Longitude'] = str(coor.longitude)
        # Further processing to extract street address, city, zip code, and country.
    except:
        # Handle exceptions by setting values to 'N/A'
```
- Scrapes the business address, geocodes it to obtain latitude and longitude, and extracts additional address components like street address, city, zip code, and country.

#### 4. `get_speciality()`
```python
def get_speciality(self):
    try:
        spec = self.driver.find_element(By.XPATH, '//h2[@class="listing-heading"]/a').text
        self.data['Speciality'] = spec
    except:
        self.data['Speciality'] = 'N/A'
```
- Retrieves the specialty of the business.

#### 5. `get_phone()`
```python
def get_phone(self):
    try:
        phone = self.driver.find_element(By.XPATH, '//a[@title="Phone"]').get_attribute('href')
        self.data['Phone'] = phone.replace('tel:', '')
    except:
        self.data['Phone'] = 'N/A'
```
- Extracts the phone number of the business.

#### 6. `get_email()`
```python
def get_email(self):
    try:
        mail = self.driver.find_element(By.XPATH, '//a[@class="contact contact-main contact-email"]').get_attribute('href')
        self.data['E-Mail'] = mail[:mail.index('?')].replace('%40', '@').replace('mailto:', '')
    except:
        self.data['E-Mail'] = 'N/A'
```
- Scrapes the email address of the business.

#### 7. `get_website()`
```python
def get_website(self):
    try:
        web = self.driver.find_element(By.XPATH, '//a[@class="contact contact-main contact-url"]').get_attribute('href')
        self.data['Website'] = web
    except:
        self.data['Website'] = 'N/A'
```
- Extracts the website URL of the business.

#### 8. `get_timings()`
```python
def get_timings(self):
    try:
        time.click()
        timings = self.driver.find_element(By.XPATH, '//div[@class="opening-hours-all-days"]').text
        self.data['Timings'] = timings
    except:
        self.data['Timings'] = 'N/A'
```
- Retrieves the operating hours of the business.

#### 9. `get_other_details()`
```python
def get_other_details(self):
    try:
        staff = self.driver.find_element(By.XPATH, '//dd[@class="number-of-employees"]').text
        self.data['Staff'] = staff
    except:
        self.data['Staff'] = 'N/A'
    
    # Similar blocks for established year and legal ID.
```
- Collects additional details like number of employees, establishment year, and legal ID.

#### 10. `get_about()`
```python
def get_about(self):
    try:
        about = self.driver.find_element(By.XPATH, '//div[@class="listing-descriptors about-us-section"]').text
        self.data['About'] = about
    except:
        self.data['About'] = 'N/A'
```
- Retrieves a description about the business.

#### 11. `get_logo()`
```python
def get_logo(self):
    try:
        logo = self.driver.find_element(By.XPATH, '//img[@class="brand-logo"]').get_attribute('src')
        self.data['Logo URL'] = logo
    except:
        self.data['Logo URL'] = 'N/A'
```
- Extracts the URL of the business logo.

#### 12. `get_ABN()`
```python
def get_ABN(self):
    try:
        abn = self.driver.find_element(By.XPATH, '//dd[@class="abn"]').text
        self.data['ABN'] = abn
    except:
        self.data['ABN'] = '-'
```
- Retrieves the Australian Business Number (ABN).

#### 13. `get_ACN()`
```python
def get_ACN(self):
    try:
        acn = self.driver.find_element(By.XPATH, '//dd[@class="acn"]').text
        self.data['ACN'] = acn
    except:
        self.data['ACN'] = '-'
```
- Extracts the Australian Company Number (ACN).

#### 14. `get_listed_under()`
```python
def get_listed_under(self):
    try:
        listed = self.driver.find_element(By.XPATH, '//dd[@class="also-listed-under"]').text
        self.data['Listed Under'] = listed
    except:
        self.data['Listed Under'] = '-'
```
- Collects categories under which the business is listed.

#### 15. `trade_as()`
```python
def trade_as(self):
    try:
        trade = self.driver.find_element(By.XPATH, '//dd[@class="trading-aliases"]').text
        self.data['Also Trade As'] = trade
    except:
        self.data['Also Trade As'] = '-'
```
- Retrieves any trading aliases for the business.

#### 16. `get_image()`
```python
def get_image(self):
    img_elements = self.driver.find_elements(By.XPATH, '//img[@class="rsImg rsMainSlideImage"]')
    
    # Attempts to extract multiple image URLs.
```
- Collects URLs of images associated with the business listing.

#### 17. `current_url()`
```python
def current_url(self):
    self.data['Current Url'] = self.driver.current_url
```
- Stores the current URL being processed in the data dictionary.

#### 18. `move_into_file()`
```python
def move_into_file(self):
    p = pd.DataFrame([self.data])
    p.to_csv("C:/imp codes/Ye/data/camden.csv", mode='a', header=not os.path.exists("C:/imp codes/Ye/data/camden.csv"), index=False)
```
- Saves collected data into a CSV file for further analysis or reporting.

### Execution Block

The script includes an execution block that initializes an instance of `YellowPagesData`, reads URLs from a CSV file containing links to businesses, and sequentially calls various data extraction methods for each link:

```python
bot = YellowPagesData()
time.sleep(30)  # Wait for manual setup if needed

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
            bot.move_into_file()  # Save data to CSV
        except Exception as e:
            print(f"Error processing {f}: {e}")
```
#  YellowLinks Web Scraper

## Overview
The **YellowLinks** class is a Python web scraper that utilizes Selenium to navigate through the Yellow Pages website and extract links related to plumbers in Camden Council. The extracted links are saved into a CSV file for further analysis.


### Class Definition
```python
class YellowLinks:
    data = {}
    nom = ArcGIS(timeout=10)
    opt = Options()
    opt.add_extension("path_to_your_extension")
```
- **data**: A dictionary to store extracted link data.
- **nom**: An instance of ArcGIS for geolocation (not utilized in this script).
- **opt**: Chrome options configured to add a specific extension.

### Initialization
```python
def __init__(self):
    self.driver = webdriver.Chrome(options=self.opt)
    self.driver.maximize_window()
```
- Initializes the Chrome WebDriver and maximizes the browser window.

### Landing on First Page
```python
def land_first_page(self, url):
    self.driver.get(url)
    self.driver.implicitly_wait(5)
```
- Navigates to the specified URL and waits for elements to load.

### Extracting Links
```python
def get_links(self):
    links = self.driver.find_elements(By.XPATH, '//div[@class="Box__Div-sc-dws99b-0 fYIHHU"]/a')
    self.driver.implicitly_wait(5)
    for l in links:
        print("Link: "+l.get_attribute('href'))
        self.data['Links'] = l.get_attribute('href')
        p = pd.DataFrame([self.data])
        p.to_csv("path_to_your_csv_file", mode='a', header=not os.path.exists("path_to_your_csv_file"), index=False)
```
- Finds all links matching the specified XPath and saves them into a CSV file.

### Main Execution Loop
```python
bot = YellowLinks()
time.sleep(15)
for i in range(1, 150):
    time.sleep(5)
    bot.land_first_page(f'https://www.yellowpages.com.au/search/listings?clue=Plumbers&locationClue=Camden+Council&pageNumber={i}')
    bot.get_links()
```
- Creates an instance of `YellowLinks`, waits for a few seconds, and iterates through multiple pages to extract links related to plumbers.

## Usage Instructions
1. Run the script using Python:
   ```bash
   python your_script_name.py
   ```
2. The extracted links will be appended to `camden.csv` located at your specified path.

## Important Notes
- Ensure that your Chrome browser version matches the version of ChromeDriver you have installed.
- Adjust wait times (`time.sleep()`) as necessary depending on your internet speed and website response time.
- Respect website terms of service when scraping data.

## Conclusion

The `YellowPagesData` class provides a comprehensive solution for scraping detailed information from Yellow Pages listings using Selenium and Geopy. Each method is designed to handle specific data extraction tasks with appropriate error handling to ensure robustness against missing data or unexpected page structures. The collected data is stored in a structured format (CSV), allowing for easy access and analysis in subsequent processes.

