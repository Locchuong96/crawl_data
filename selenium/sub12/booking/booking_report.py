'''
This file is going to include method that will parse
The specific data that we nedd from each one of the deal boxes.
'''
from selenium.webdriver.remote.webelement import WebElement
class BookingReport:
    
    def __init__(self,raw:WebElement):
        self.raw = raw
        
    def pull_dealbox_attribute(self):
        collections = []
        for deal_box in self.raw:
            # title
            title = deal_box.find_element_by_css_selector('div[data-testid="title"]').text.strip()#.get_attribute('innerHTML').strip()
            # price
            price = deal_box.find_element_by_css_selector('div[data-testid="price-and-discounted-price"]').text.strip()#.get_attribute('innerHTML').strip()
            #print(price)
            # score
            score = deal_box.find_element_by_css_selector('div[data-testid="review-score"]').text.strip()#.get_attribute('innerHTML').strip()
            #print(score.text)
            collections.append([title,price,score])
        return collections
    
    # def pull_deal_boxes(self):
    #     return self.boxes_section_element.find_elements_by_class_name(
    #         'sr_property_block'
    #     )
        