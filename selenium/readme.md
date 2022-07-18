### selenium

[course_link](https://www.youtube.com/watch?v=j7VZsCCnptM)

[official-document](https://www.selenium.dev/documentation/)

practice on the [testpages](https://testpages.herokuapp.com/styled/index.html)

there are the big change in selenium ver=4.3.0 and ver=4.2.0

    Selenium 4.3.0
    * Deprecated find_element_by_* and find_elements_by_* are now removed (#10712)
    * Deprecated Opera support has been removed (#10630)
    * Fully upgraded from python 2x to 3.7 syntax and features (#10647)
    * Added a devtools version fallback mechanism to look for an older version when mismatch occurs (#10749)
    * Better support for co-operative multi inheritance by utilising super() throughout
    * Improved type hints throughout

    Selenium 4.2.0
    * Fix bug preventing Firefox from setting accept_insecure_certs to False (#10442)
    * Deprecated opera classes as not w3c compatible (#10379)
    * Fix SecurityError: Invalid Domain problem (#10653)
    * Implement convenience methods for scrolling

please refer this [link](https://github.com/SeleniumHQ/selenium/blob/a4995e2c096239b42c373f26498a6c9bb4f2b3e7/py/CHANGES)

⭐️ Course Contents ⭐️

[1/Getting Started with the basics](./sub1)

[target_page](https://testpages.herokuapp.com/styled/download/download.html)

- install selenium on Windows `pip install selenium==4.2.0`
- you can combine selenium to auto testing with unittest `pip install unittest2` 
- download [web-driver](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) check chrome-version on the browser `chrome://version`
- set the link to web-driver executable-file in `PATH` os-environment variable, printout your os-variables in bash: `printenv`
- test click download-button automaticly, the first of first you have to identify your element, right-click on `inspect` in your browser, each page have unique html architecture and each html element is going to have html-type, we will find target element and by each type and some additional attributes.

driver attributes:

[locating-elements](https://selenium-python.readthedocs.io/locating-elements.html#)

these are some locating-element method in selenium

    Locating Elements
    - [Locating by Id]()
    - [Locating by Name]()
    - Locating by XPath
    - Locating Hyperlinks by Link Text
    - Locating Elements by Tag Name
    - Locating Elements by Class Name
    - [Locating Elements by CSS Selectors]()

default:

    import os 
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # add web-driver into your os-environment, add new value to existing var +=, r for prefix
    os.environ['PATH'] = r"C:/Users/PC/Desktop/crawl_data/selenium/driver"

    # you can choice many option of web brower ex: Chrome,Edge,FireFox,etc.
    driver = webdriver.Chrome() # webdriver.Chrome("./driver/chromedriver.exe")

    # quit
    driver.quit()

*Note:* Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely loaded

[2/Explicit vs Implicit](./sub2)

[target_page](https://www.tutorialspoint.com/about/about_careers.htm)

- implicit_wait : for the element
- explicit_wait : more custom, for waitting a execution until some condition achives

*Note* when you set `driver.implicitly_wait()` to find your element, it will apply across all elements

[3/Sending Keys & CSS Selector](./sub3)

[target_page](https://testpages.herokuapp.com/styled/calculator)

You want to  `sending keys` for register,login or authentication function. you can send-key a `string` or `number`
if you find a multi class you can locating element by last word. You can send even more then value like `Enter`,`Shift`,`Ctrl + C`,etc. by import `Keys`: `from selenium.webdriver.common.keys import Keys`, inside `Keys` is some option of your key-command.

You can locating the element by css styling

    btn = driver.find_element_by_css_selector('button[onclick="return total"])

- `driver.quit()` will close the browser and the executable terminal
- `driver.close()` will only closr the browser

[5/Locating element]()

[6/Structure a Bot Project]()

[7/Deal Searching]()

[8/Booking Filtrations]()

[9/Execution from a CLI]()

[10/Deal Reporting]()

### references

[Top 7 Websites to Practice Selenium Webdriver Online](https://www.techbeamers.com/websites-to-practice-selenium-webdriver-online/#1httpsphptravelscomdemo)

[css_selectors](https://www.w3schools.com/cssref/css_selectors.asp)

[Selenium with Python](https://selenium-python.readthedocs.io/index.html)