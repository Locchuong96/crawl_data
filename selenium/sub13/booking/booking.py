import os
import booking.constants as const # run from the same directory as run.py
from selenium import webdriver
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable

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
        # ignore the warning if exists
        options = webdriver.ChromeOptions() # access class webdriver.ChromeOptions, create instance webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        super(Booking,self).__init__(options= options) # completely inherit from webdriver.Chrome, you can take the full access of webdriver.Chrome
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
        '''
        choice the currency type
        Arguments:
            currency: currency type, default = USD
        Returns:
            None 
        '''
        # we can change the current via path-argument https://www.booking.com/?changed_currency=1&selected_currency=USD&top_currency=1
        # data-tooltip-text="Choose your currency",
        currency_element = self.find_element_by_css_selector('button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        # a[data-modal-header-async-url-param="changed_currency=1&selected_currency=USD&top_currency=1"]
        # asterisk equal find an expression that contain subtring.
        option = self.find_element_by_css_selector(f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        option.click()
    
    def select_place_to_go(self,place_to_go):
        '''
        fill where you want to go
        Arguments:
            place_to_go: where do you want to go
        Returns:
            None 
        '''
        search_field = self.find_element_by_id('ss')
        search_field.clear() # clearning text field to avoid auto fill
        search_field.send_keys(place_to_go)
        # select the first element
        first_option = self.find_element_by_css_selector("li[data-i='0']")
        first_option.click()
        
    def select_dates(self,checkin_date, checkout_date):
        '''
        choice checkin and checkout date
        Arguments:
            - checkin_date: format DD-M-YYYY ex: "20 July 2022"
            - checkout_date: format DD-M-YYYY ex: "2022-07-20"
        '''
        # locating the element
        from_date = self.find_element_by_css_selector(f'td[data-date="{checkin_date}"]') # table data
        to_date = self.find_element_by_css_selector(f'td[data-date="{checkout_date}"]') # table data
        # click them
        from_date.click()
        to_date.click()
        
    # def select_adults(self, count=1):
    #     selection_element = self.find_element_by_id('xp__guests__toggle')
    #     selection_element.click()
    
    def select_adults(self,count=1):
        '''
        choice adult, min =1
        Arguments:
            count: number of adult
        Return:
            None
        '''
        # click to display adult-children-room
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()
        
        # descrease adult number until 1 (hard-min)
        while True:
            adult_descrease_button = self.find_element_by_css_selector('button[aria-label="Decrease number of Adults"]')
            # adult_number = self.find_element_by_css_selector('span[data-bui-ref="input-stepper-value"]')
            adult_number_element = self.find_element_by_id('group_adults')
            adult_number = adult_number_element.get_attribute('value')
            #print(adult_number.text)
            if int(adult_number) == 1:
                break
            else:
                adult_descrease_button.click()
        # increase the adult number as your desired
        adult_inscrease_button = self.find_element_by_css_selector('button[aria-label="Increase number of Adults"]')
        for i in range(count-1): # because adult min = 1
            adult_inscrease_button.click()
    
    def submit_search(self):
        submit_search_element = self.find_element_by_css_selector('button[type="submit"]')
        submit_search_element.click()
        
    def apply_filtrations(self):
        # add your booking filtration, pass your custom web-driver class (a.k.a your bot a.k.a self)
        filtration = BookingFiltration(driver = self) # give the origin webdriver.Chrome into booking
        filtration.apply_star_rating(3) #(1,2,3)
        filtration.sort_price_lowest_first()
        
    def report_results(self):
        results = self.find_elements_by_css_selector('div[data-testid="property-card"]')
        report = BookingReport(results)
        # create table object
        table = PrettyTable(
            field_names=["Hotel Name","Hotel Price","Hotel Score"]
        )
        collections = report.pull_dealbox_attribute() # list[list]
        table.add_rows(collections)
        print(table)
        
        #report.display_table()
        #return results