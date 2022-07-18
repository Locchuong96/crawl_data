import os
from selenium import webdriver

# add web-driver into your os-environment, add new value to existing var +=, r for prefix
os.environ['PATH'] = r"C:/Users/PC/Desktop/crawl_data/selenium/driver"

# you can choice many option of web brower ex: Chrome,Edge,FireFox,etc.
driver = webdriver.Chrome() # webdriver.Chrome("./driver/chromedriver.exe")

# define your target page
driver.get("https://testpages.herokuapp.com/styled/download/download.html")

# wait for your web-driver go to the page 10 seconds, we will get to the target page sooner if your element is already there
#driver.implicitly_wait(10) # time.sleep(10)

# find the button
my_element = driver.find_element_by_id('direct-download')

#print(my_element)
my_element.click()

