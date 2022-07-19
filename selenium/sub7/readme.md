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

[1/ locating by id]()

[2/ locating by name]()

[3/ locating by xpath]()

[4/ locating hyperlink by link-text]()

[5/ locating by tag-name]()

[6/ locating by class-name]()

[7/ locating by css-selector]()