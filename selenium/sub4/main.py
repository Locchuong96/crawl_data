from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

os.environ['PATH'] = r"C:/Users/PC/Desktop/crawl_data/selenium/driver"

driver = webdriver.Chrome()
driver.get('http://www.python.org')

assert "Python" in driver.title # confirm the Python word in driver.title
 
elem = driver.find_element(By.NAME,"q") # find the text field
elem.clear() # clear the text field
elem.send_keys("pycon") # entry your word
elem.send_keys(Keys.RETURN) # press enter

assert "No result found." not in  driver.page_source # if there is no result, assert out
driver.quit()#driver.close()