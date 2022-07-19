import os
import booking.constants as const # run from the same directory as run.py
from selenium import webdriver

'''
create a booking class define some methods that you will be reuse in the project,
inherited from webdriver.Chrome
'''

class Booking(webdriver.Chrome):   
    
    def __init__(self,driver_path=r"C:/Users/PC/Desktop/crawl_data/selenium/driver",
                 teardown = False,wait_time = 10):
        # self.wait_time = wait_time # the value for implicitly wait
        self.teardown = teardown # bit option to quit the driver after executed 
        self.driver_path = driver_path 
        os.environ['PATH'] = driver_path # when call this class as object, it will be set in os environment variables
        super(Booking,self).__init__() # completely inherit from webdriver.Chrome, you can take the full access of webdriver.Chrome
        self.implicitly_wait(wait_time) # set the implicitly_wait value, no matter what you
        self.maximize_window()
        
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
        
    def change_currency(self, currency="USD"):
        # we can change the current via path-argument https://www.booking.com/?changed_currency=1&selected_currency=USD&top_currency=1
        # data-tooltip-text="Choose your currency",
        currency_element = self.find_element_by_css_selector('button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        # a[data-modal-header-async-url-param="changed_currency=1&selected_currency=USD&top_currency=1"]
        # asterisk equal find an expression that contain subtring.
        option = self.find_element_by_css_selector(f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        option.click()
    
    def select_place_to_go(self,place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear() # clearning text field to avoid auto fill
        search_field.send_keys(place_to_go)
        
    