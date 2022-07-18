from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import unittest 

os.environ['PATH'] = r"C:/Users/PC/Desktop/crawl_data/selenium/driver"

class python_org_search(unittest.TestCase):
    
    # unittest hard function define
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_search_in_python_org(self):
        driver = self.driver 
        driver.get("http://www.python.org")
        self.assertIn("Python",driver.title)
        elem = driver.find_element(By.NAME,"q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.",driver.page_source)
    
    # unittest hard function define
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()