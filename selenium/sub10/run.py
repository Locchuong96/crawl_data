import time 
from booking.booking import Booking

# inst = Booking()
# inst.landing_page()
# time.sleep(5)
# inst.quit() # webdriver.Chrome is already have quit method, don't define this menthod again in the attribute, it making to recursion

# bot is the object created by booking class, but after execute command in with, your object will be activate __exit__ method and close the driver
with Booking(teardown = True) as bot:
    bot.landing_page()
    #bot.change_currency(currency="GBP")
    bot.select_place_to_go(place_to_go="New York")
    bot.select_dates(checkin_date = "2022-07-20",checkout_date = "2022-07-21")
    bot.select_adults(count = 3)
    bot.submit_search()
    bot.apply_filtrations()
    print('Existing ...')