from bs4 import BeautifulSoup 
import requests

with open('./sub1/simple.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml') # xml and html

# for i in dir(soup):
#     print(i)

# print html content
# print(soup)
# print(soup.prettify())

# find tag in html
# match = soup.title # find the first element match condition tag = title
# print(match)
# print(match.text)

# find tag div
# match = soup.find('div') # the first one
# print(match)

# find class, we use class_ to avoid python syntax class
# article = soup.find(class_ = 'article') # the first one
# print(type(article))
# print(article)

# find tag with specific class
# article = soup.find('div',class_='article')
# headline = article.h2.a.text
# summary = article.p.text
# print(headline)
# print(summary)

# find_all or findAll tag with specific class
articles = soup.findAll('div',class_ = 'article') # return a list of bs4 element tag
# print(articles)
for article in articles:
    headline = article.h2.a.text
    summary = article.p.text 
    print(f'{headline}: {summary}')

# find a id
# headline = soup.find(id = 'site_title')
# print(type(headline))
# print(headline)
# print(headline.text)


