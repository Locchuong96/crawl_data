import time 
from booking.booking import Booking

# inst = Booking()
# inst.landing_page()
# time.sleep(5)
# inst.quit() # webdriver.Chrome is already have quit method, don't define this menthod again in the attribute, it making to recursion

# bot is the object created by booking class, but after execute command in with, your object will be activate __exit__ method and close the driver
with Booking(teardown = True) as bot:
    bot.landing_page()
    print('Existing ...')