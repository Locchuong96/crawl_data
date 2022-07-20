'''
this file will include the class with instance methods
that will be responsible to interact with our website
after we have some results. to apply filtrations.
selenium give you a type driver to define class's argument is a driver's type
'''
#from typing import List define  argument's type of the class
from selenium.webdriver.remote.webdriver import WebDriver # driver type
class BookingFiltration:
    
    def __init__(self,driver:WebDriver):
        self.driver = driver
    
    # accept many value in star_value, click many star option
    def apply_star_rating(self,*star_values): # star_value
        #print("I'm in the apply_star_rating")
        star_filtration_box = self.driver.find_element_by_css_selector('div[data-filters-group="class"]')
        # star_child_elements = self.driver.find_elements_by_css_selector('div[data-filters-item="class:class=1"]') # find star in whole page => WRONG
        # star_child_element = star_filtration_box.find_elements_by_css_selector(f'div[data-filters-item="class:class={star_value}"]')
        # star_child_element[0].click()
        for star_value in star_values:
            star_child_element = star_filtration_box.find_elements_by_css_selector(f'div[data-filters-item="class:class={star_value}"]')
            star_child_element[0].click()
    
    def sort_price_lowest_first(self):
        # there are 2 gui for sort now 2022-07-20
        print('SORT_PRICE_LOWEST!')
        try:
            list_option_element = self.driver.find_element_by_css_selector('button[data-testid="sorters-dropdown-trigger"]')
            print("List option")
            list_option_element.click()
            lowest_price_first = self.driver.find_element_by_css_selector('button[data-id="price"]')
            lowest_price_first.click()
        except:
            print("Button option")
            lowest_price_first=self.driver.find_element_by_css_selector('li[data-id="price"]')
            lowest_price_first.click()
        