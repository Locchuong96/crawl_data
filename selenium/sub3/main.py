import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# key option
from selenium.webdriver.common.keys import Keys

# add web-driver into your os-environment, add new value to existing var +=, r for prefix
os.environ['PATH'] = r"C:/Users/PC/Desktop/crawl_data/selenium/driver"

# you can choice many option of web brower ex: Chrome,Edge,FireFox,etc.
driver = webdriver.Chrome() # webdriver.Chrome("./driver/chromedriver.exe")
driver.implicitly_wait(5)

# go to your target link
driver.get("https://testpages.herokuapp.com/styled/calculator")

number1 = driver.find_element_by_id('number1')
number2 = driver.find_element_by_id('number2')
button = driver.find_element_by_id('calculate')

# send value
number1.send_keys(12) # string or number
number2.send_keys(Keys.NUMPAD1,Keys.NUMPAD3) # 3
# click the button
button.click()

# wait explicitly
w = WebDriverWait(driver,timeout=3).until(
    EC.presence_of_element_located((By.ID,"answer"))    
)

answer = driver.find_element_by_id('answer')
print('The answer is: ',answer.text)

# quit
driver.quit()