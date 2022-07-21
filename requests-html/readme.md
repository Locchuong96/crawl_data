**Angenda**

[1/ instalation](/sub1)

There are 2 library `requests` and `requests-html`

- install requests: `pip install requests`
- install requests-html: `pip install requests-html`

you can view contain in html with python script:

>>> python
>>> from requests_html import HTML
>>> with open('sub1/simple.html') as html_file:
...    source = html_file.read()
...    # print(source)
...    html = HTML(source)

`HTML` instance example:

    absolute_links
    add_next_symbol
    arender
    base_url
    default_encoding
    element
    encoding
    find
    full_text
    html
    links
    lxml
    next
    next_symbol
    page
    pq
    raw_html
    render
    search
    search_all
    session
    skip_anchors
    text
    url
    xpath