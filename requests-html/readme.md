**Angenda**

[1/ instalation & first look](/requests-html/sub1)

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

[2/ crawl data from website with HTMLsession](/requests-html/sub2)

[target-page](https://coreyms.com/)

get response from website

    # get the session for your html session
    session = HTMLSession()
    response = session.get('https://coreyms.com/')
    print(response.html)

[prettify the code](https://codebeautify.org/htmlviewer)
`Corey` say he did not find `prettify-method` when print out html contend in requests-html.

get the attributes of element as a dictionary: `element_attribute = video.attrs`

        {'class': ('youtube-player',),
        'width': '640',
        'height': '360',
        'src': 'https://www.youtube.com/embed/z0gguhEmWiY?version=3&rel=1&showsearch=0&showinfo=1&iv_load_policy=1&fs=1&hl=en-US&autohide=2&wmode=transparent',
        'allowfullscreen': 'true',
        'style': 'border:0;',
        'sandbox': 'allow-scripts allow-same-origin allow-popups allow-presentation'
        }
or 
        video_link = video_link.attr['src']

**Tips**
- This is a litle helpful tip, if you crawl a page and export it into csv file or somekind of table, you should do this tip

1/ get a contain-element (biggest one contain all row-element)
2/ loop over each element in contain-element
3/ give the default value for each ifo
4/ try to get the value, if it crash ignore it, take the default

![img](/requests-html/imgs/useless_infomation.png)