**locating elements**

[source](https://selenium-python.readthedocs.io/locating-elements.html)

- for find a single element: `find_element`

- for find multiple element (these menthods will return a list): `find_elements`

The attributes available for the By class are used to locate elements on a page. These are the attributes available for By class:

|By attribute|find element|
|---|---|
|ID = "id"|find_element(By.ID, "id")|
|NAME = "name"|find_element(By.NAME, "name")|
|XPATH = "xpath"|find_element(By.XPATH, "xpath")|
|LINK_TEXT = "link text"|find_element(By.LINK_TEXT, "link text")|
|PARTIAL_LINK_TEXT = "partial link text"|find_element(By.PARTIAL_LINK_TEXT, "partial link text")|
|TAG_NAME = "tag name"|find_element(By.TAG_NAME, "tag name")|
|CLASS_NAME = "class name"|find_element(By.CLASS_NAME, "class name")|
|CSS_SELECTOR = "css selector"|find_element(By.CSS_SELECTOR, "css selector")|

reuse driver from main on the terminal

    C:\Users\PC\Desktop\crawl_data\selenium>python
    Python 3.8.8 (default, Apr 13 2021, 15:08:03) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32

    Warning:
    This Python interpreter is in a conda environment, but the environment has
    not been activated.  Libraries may fail to load.  To activate this environment
    please see https://conda.io/activation

    Type "help", "copyright", "credits" or "license" for more information.
    >>> from sub7.main import driver
    >>>

[1/ locating by id](./page1.html)

    login_form = driver.find_element(By.ID, 'loginForm')

[2/ locating by name](./page2.html)

    username = driver.find_element(By.NAME,'username')
    password = driver.find_element(By.NAME,'password')
    continue = driver.find_element(By.NAME,'continue')

[3/ locating by xpath](./page2.html)

XPath is the language used for locating nodes in an XML document. As HTML can be an implementation of XML (XHTML), Selenium users can leverage this powerful language to target elements in their web applications. XPath supports the simple methods of locating by id or name attributes and extends them by opening up all sorts of new possibilities such as locating the third checkbox on the page.

    login_form = driver.find_element(By.XPATH,"/html/body/form") # Copy Full XPath
    login_form = driver.find_element(By.XPATH,"//*[@id='loginForm']") # Copy XPath
    username = driver.find_element(By.XPATH,"/html/body/form/input[1]")
    username = driver.find_element(By.XPATH,"//*[@id="loginForm"]/input[1]")

[4/ locating hyperlink by link-text](./page3.html)

    continue_link = driver.find_element(By.LINK_TEXT,'Continue')
    continue_link = driver.find_element(By.PARTIAL_LINK_TEXT,'Conti')

[5/ locating by tag-name](./page4.html)

you can locating element by name

    heading1 = driver.find_element(By.TAG_NAME,'h1')


[6/ locating by class-name](./page5.html)

Use this when you want to locate an element by `class name`, when no element has a matching class name attribute, a `NoSuchElementException` will be raised.

    content = driver.find_element(By.CLASS_NAME,'content')

[7/ locating by css-selector](./pag6.html)

Use this when you want to locate an element using [CSS selector](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors) syntax. With this stategy, the first element matching the given CSS selector will be returned. If no element matches the provided CSS selector, a `NoSuchElementException` will be raised.

