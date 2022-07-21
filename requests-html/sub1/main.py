from requests_html import HTML

with open('./sub1/simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

# printout html source
# print(html.html)

# find something with .find()
# match = html.find('title') # return a list of element
# match = html.find('title',first=True) # find the first element only
# match = html.find('#footer',first=True) # find the by id, meaning it unqiue

# article = html.find('div.article',first = True)
# headline = article.find('h2',first = True) #.text
# summary = article.find('p',first = True) #.text

articles = html.find('div.article')

# print(match) # print out a list
# print(match[0]) # print out the first element
# print(dir(match[0])) # print out attribute in the list
# print(match[0].html) # print out html type of the first element
# print(match[0].text) # print out the text attribute of the first element
# print(match.text)

for article in articles:
    # find element in each article
    headline = article.find('h2',first=True).text 
    summary = article.find('p',first=True).text 
    
    print(f'headline: {headline}')
    print(f'summary: {summary} \n')