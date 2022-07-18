import os
from selenium import webdriver
# for web-driver wait explicitly
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# add web-driver into your os-environment, add new value to existing var +=, r for prefix
os.environ['PATH'] = r"C:/Users/PC/Desktop/crawl_data/selenium/driver"

# you can choice many option of web brower ex: Chrome,Edge,FireFox,etc.
driver = webdriver.Chrome() # webdriver.Chrome("./driver/chromedriver.exe")

# define your target page
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")

# wait for your web-driver go to the page 10 seconds, we will get to the target page sooner if your element is already there
driver.implicitly_wait(1) # time.sleep(10)

# find the button element by id ='modaldialog'
my_element = driver.find_element_by_link_text('Team')
# click the button
my_element.click()

# WebDriverWait(driver,30).until(
#     EC.text_to_be_present_in_element(
#         (By.CLASS_NAME,'progress-label'), # element filtration
#         'Complete!' # the expected text
#     )
# )

# explicitly wait 5 second until
w = WebDriverWait(driver,5)
w.until(EC.presence_of_element_located((By.TAG_NAME,'h1')))
s = driver.find_element_by_tag_name('h1')
#obtain text
t = s.text 
print('Text is: ',t)
# quit driver
driver.quit()