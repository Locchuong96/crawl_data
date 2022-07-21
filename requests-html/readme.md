**Angenda**

[1/ instalation & first look](/sub1)

There are 2 library `requests` and `requests-html`

- install requests: `pip install requests`
- install requests-html: `pip install requests-html`

you can view contain in html with python script:

    from requests_html import HTML

    with open('simple.html') as html_file:
        source = html_file.read()
        html = HTML(html=source)

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

- we can parse out the information inside html instance like

    print(html.html)
    print(html.text)
    print(html.url)

- find element with `.find()` method `match = html.find('title')`
    match = html.find('title') # tag
    match = html.find('#footer') # id
    match = html.find('div.article') # tag with specific class bt css selector

[2/ sub2](/sub2)
