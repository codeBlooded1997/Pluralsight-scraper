# Importing required libraries
from selenium import webdriver  # for accessing the webpage.
from bs4 import BeautifulSoup   # for scraping data.
import pandas as pd  # for creating dataframe and saving to csv file.
import time   # for creating break between requests to simulate the human user.
from random import randint  # for creating a random time breaks


# These arrays will include all the scraped result
titles = []
all_courses = []
all_hours = []

"""
In this section we want to open a webdriver and get the url to pluralsight paths page.
"""
# Path to chromedriver (You have to specify the directory where you've saved the chromedriver).
path_to_chromedriver = '/Users/arian/WorkSpace/dev/scraper/drivers/chromedriver'
# Opening a dirver.
driver = webdriver.Chrome(executable_path=path_to_chromedriver)
# Simulating human user.
time.sleep(randint(3, 5))
# URL to page.
url = 'https://www.pluralsight.com/product/paths'
# Getting the url
print("Getting URL ...")
# Waiting for webpage to come up.
time.sleep(randint(4, 6))
driver.get(url)
# Creating soup object form page content to start scraping.
soup = BeautifulSoup(driver.page_source, 'html.parser')
print("SOUP object created")

# Selecor of the result section
paths_selector = '#pathContent > div'
# Selecting the result from soup object
paths = soup.select(paths_selector)
# Iterating through the selected result section
for path in paths:
    # Scraping the visual data (data that are being seen) of each path.
    data = path.find('div', class_='item-text')
    # Parsing the scraped text so we can get the title.
    title = data.text.strip().split('\n')[0]
    # Parsing the courses data
    courses = data.text.strip().split('\n')[2]
    # Parsing the hours data
    hours = data.text.strip().split('\n')[3]
    # Printing extracted data in consol
    print("Title: ", title)
    print("Courses: ", courses)
    print("Hours: ", hours)
    print("======"*5)
    # Appending extracted data to our arrays
    titles.append(title)
    all_courses.append(courses)
    all_hours.append(hours)
# Closing the drive
driver.close()
print("Data scraped.")
# Creating pandas dataframe containing all scraped data.
result_df = pd.DataFrame(
    {
        'Title' :titles,
        'Course' :all_courses,
        'Hourse' :all_hours,
    })
print("Dataframe created")
# Creating csv file
result_df.to_csv('result.csv', index=False)
print("CSV file saved.")