'''
this file will be automaticly run when you call it in terminal
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os 

os.environ['PATH'] = r"C:/Users/PC/Desktop/crawl_data/selenium/driver"

# create driver object to reuse it on terminal
driver = webdriver.Chrome()