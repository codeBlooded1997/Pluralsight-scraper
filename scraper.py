# Importing required libraries
from selenium import webdriver  # for accessing the webpage.
from bs4 import BeautifulSoup   # for scraping data.
import pandas as pd  # for creating dataframe and saving to csv file.

"""
In this section we want to open a webdriver and get the url to pluralsight paths page.
"""
# Path to chromedriver (Change it if you've forked the script).
path_to_chromedriver = '/Users/arian/WorkSpace/dev/scraper/drivers/chromedriver'
# Opening a dirver.
driver = webdriver.Chrome(executable_path=path_to_chromedriver)
# Simulating human user.
#time.sleep(randint(3, 5))
# URL to page.
url = 'https://www.pluralsight.com/product/paths'
# Getting the url
print("Getting URL ...")
driver.get(url)