import os
from selenium import webdriver

# add web-driver into your os-environment, add new value to existing var +=, r for prefix
os.environ['PATH'] = r"C:/Users/PC/Desktop/crawl_data/selenium/driver"

# you can choice many option of web brower ex: Chrome,Edge,FireFox,etc.
driver = webdriver.Chrome() # webdriver.Chrome("./driver/chromedriver.exe")

# define your target page
driver.get("https://testpages.herokuapp.com/styled/download/download.html")

# find the button
my_element = driver.find_element_by_id('direct_download')
my_element.click()

