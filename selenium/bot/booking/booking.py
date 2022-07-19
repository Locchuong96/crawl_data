import os
import booking.constants as const # run from the same directory as run.py
from selenium import webdriver

'''
create a booking class define some methods that you will be reuse in the project,
inherited from webdriver.Chrome
'''

class Booking(webdriver.Chrome):   
    
    def __init__(self,driver_path=r"C:/Users/PC/Desktop/crawl_data/selenium/driver",
                 teardown = False):
        self.teardown = teardown 
        self.driver_path = driver_path 
        os.environ['PATH'] = driver_path # when call this class as object, it will be set in os environment variables
        super(Booking,self).__init__() # completely inherit from webdriver.Chrome, you can take the full access of webdriver.Chrome
        
    def __exit__(self,exc_type,exc_val,exc_tb):
        if self.teardown:
            self.quit()
        
    def landing_page(self,path = "https://www.booking.com"):
        '''
        go to your specific page
        Arguments:
            path: your url (link)
        Returns:
            None
        '''
        self.get(const.BASE_URL)
    