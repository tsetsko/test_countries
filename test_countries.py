from selenium import webdriver
from sys import platform
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

URL = "https://zzg-demo-varna-returnportal-aps-001.azurewebsites.net/testshop/lite"

path = ""
if platform == "darwin":
    path = '/Applications/chromedriver'
elif platform == "win32":
    path = "C:/Users/tsvetan.donov/Documents/chromedriver.exe"

driver = webdriver.Chrome(executable_path=path)
driver.get(URL)
time.sleep(10)
driver.find_element(By.ID, 'languagesToggle').click()
driver.find_element(By.XPATH, '/html/body/div/div[2]/header/div/div/div/div[2]/div/div/div/a[29]').click()
time.sleep(1)
driver.find_element(By.NAME, 'CountryCode')
page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")

countries = [country.text for country in soup.find('div', {'class': 'dropdown-search-results'}).findChildren('button', {'name': 'CountryCode'})]

df = pd.DataFrame(countries)
df.to_csv('thai.csv')