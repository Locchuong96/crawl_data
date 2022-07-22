from bs4 import BeautifulSoup
from prettytable import PrettyTable
import requests

scource = requests.get('http://coreyms.com').text # return html string
soup = BeautifulSoup(scource,'lxml')

#print(soup.prettify())

# get all articles
articles = soup.find_all('article')

# extract the information inside article
collections = []
for article in articles:
    #print(article)
    headline = article.find('a',class_ = 'entry-title-link').text
    date = article.find('time',class_ = 'entry-time').text
    author = article.find('span',class_ = 'entry-author-name').text
    summary = article.find('div',class_ = 'entry-content').p.text
    
    try:
        video_link = article.find('iframe')
        video_link = video_link.attrs['src'] # get attribute dictionary inside
        video_link = video_link.split("?")[0]
    except Exception as e:
        video_link = None
    #print(summary)
    collections.append([headline,date,author])

# print(collections)  
table = PrettyTable(field_names = ['Headline','Date','Author'])
table.add_rows(collections)
print(table)
