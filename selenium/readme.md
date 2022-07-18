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

- install selenium on Windows `pip install selenium==4.2.0`
- download [web-driver](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) check chrome-version on the browser `chrome://version`
- set the link to web-driver executable-file in `PATH` os-environment variable, printout your os-variables in bash: `printenv`
- test click download-button automaticly [test-button](https://testpages.herokuapp.com/styled/download/download.html), the first of first you have to identify your element, right-click on `inspect` in your browser, each page have unique html architecture and each html element is going to have html-type, we will find target element and by each type and some additional attributes.

driver attributes:

[locating-elements](https://selenium-python.readthedocs.io/locating-elements.html#)

these are some locating-element method in selenium

    Locating Elements
    - Locating by Id
    - Locating by Name
    - Locating by XPath
    - Locating Hyperlinks by Link Text
    - Locating Elements by Tag Name
    - Locating Elements by Class Name
    - Locating Elements by CSS Selectors

[2/Explicit vs Implicit](./sub2)

*Note* when you set `driver.implicitly_wait()` to find your element, it will apply across all elements

[3/Sending Keys & CSS Selector]()

[4/Structure a Bot Project]()

[5/Deal Searching]()

[6/Booking Filtrations]()

[7/Execution from a CLI]()

[8/Deal Reporting]()
