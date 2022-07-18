**navigating**

[source](https://selenium-python.readthedocs.io/navigating.html)

this sub execute code line-by-line on terminal

ex:

    C:\Users\PC\Desktop\crawl_data\selenium>python
    Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

    Warning:
    This Python interpreter is in a conda environment, but the environment has
    not been activated.  Libraries may fail to load.  To activate this environment
    please see https://conda.io/activation

    Type "help", "copyright", "credits" or "license" for more information.
    >>> import os
    >>> from selenium import webdriver
    >>> from selenium.webdriver.common.keys import Keys
    >>> from selenium.webdriver.common.by import By


`driver.get("http://www.google.com")`

    element = driver.find_element(By.ID, "passwd-id")
    element = driver.find_element(By.NAME, "passwd")
    element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
    element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")

*Note:*
You can also look for a link by its text, but be careful! The text must be an exact match! You should also be careful when using XPATH in WebDriver. If there’s more than one element that matches the query, then only the first will be returned. If nothing can be found, a `NoSuchElementException` will be raised.

`element.send_keys("some text")`

- you can send your text and press arrow down by `element.send_keys(" and some", Keys.ARROW_DOWN)`
- clear the text in text field `textfield.clear()`

We’ve already seen how to enter text into a textarea or text field, but what about the other elements? You can “toggle” the state of the drop down, and you can use “setSelected” to set something like an OPTION tag selected. Dealing with SELECT tags isn’t too bad:

    element = driver.find_element(By.XPATH, "//select[@name='name']")
    all_options = element.find_elements(By.TAG_NAME, "option")
    for option in all_options:
        print("Value is: %s" % option.get_attribute("value"))
        option.click()

As you can see, this isn’t the most efficient way of dealing with SELECT elements. WebDriver’s support classes include one called a “Select”, which provides useful methods for interacting with these:

from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.NAME, 'name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)

WebDriver also provides features for deselecting all the selected options:

    select = Select(driver.find_element(By.ID, 'id'))
    select.deselect_all()

This will deselect all OPTIONs from that particular SELECT on the page.

Suppose in a test, we need the list of all default selected options, Select class provides a property method that returns a list:

    select = Select(driver.find_element(By.XPATH, "//select[@name='name']"))
    all_selected_options = select.all_selected_options

To get all available options: `options = select.options`

Once you’ve finished filling out the form, you probably want to submit it. One way to do this would be to find the “submit” button and click it:

    # Assume the button has the ID "submit" :)
    driver.find_element_by_id("submit").click()

Alternatively, WebDriver has the convenience method “submit” on every element. If you call this on an element within a form, WebDriver will walk up the DOM until it finds the enclosing form and then calls submit on that. If the element isn’t in a form, then the `NoSuchElementException` will be raised:

    element.submit()

**Drag and drop**

You can use drag and drop, either moving an element by a certain amount, or on to another element

    element = driver.find_element(By.NAME, "source")
    target = driver.find_element(By.NAME, "target")

    from selenium.webdriver import ActionChains
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(element, target).perform()

**Moving between windows and frames**

- switch to another window: `driver.switch_to_window("windowName")`
- find windows name: `<a href="somewhere.html" target="windowName">Click here to open a new window</a>`
- Alternatively, you can pass a “window handle” to the “switch_to_window()” method. Knowing this, it’s possible to iterate over every open window like so:

    for handle in driver.window_handles:
        driver.switch_to_window(handle)

- switch from frame to frame `driver.switch_to_frame("frameName")`

- It’s possible to access subframes by separating the path with a dot, and you can specify the frame by its index too. That is: `driver.switch_to_frame("frameName.0.child")`. Once we are done with working on frames, we will have to come back to the parent frame which can be done using: `driver.switch_to_default_content()`

**popup dialog**

Selenium WebDriver has built-in support for handling popup dialog boxes. After you’ve triggered action that would open a popup, you can access the alert with the following:

    alert = driver.switch_to.alert

This will return the currently open alert object. With this object, you can now accept, dismiss, read its contents or even type into a prompt. This interface works equally well on alerts, confirms, prompts. Refer to the API documentation for more information.

**navigation**

To move backward and forward in your browser’s history:

    driver.forward()
    driver.back()

**cookie**

Before moving to the next section of the tutorial, you may be interested in understanding how to use cookies. First of all, you need to be on the domain that the cookie will be valid for:

    # Go to the correct domain
    driver.get("http://www.example.com")

    # Now set the cookie. This one's valid for the entire domain
    cookie = {‘name’ : ‘foo’, ‘value’ : ‘bar’}
    driver.add_cookie(cookie)

    # And now output all the available cookies for the current URL
    driver.get_cookies()