from bs4 import BeautifulSoup
from prettytable import PrettyTable
import requests
from tqdm import tqdm

url = 'http://coreyms.com'
pages = int(input("How many page do you want to scrape? "))

# extract the information inside article
collections = []

def extract_info(articles):
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
        collections.append([headline,date,author])

for i in tqdm(range(2,2+pages+1)):
    #print(url+f'/page/{i}')
    # get soup
    scource = requests.get(url+f'/page/{i}').text # return html string
    soup = BeautifulSoup(scource,'lxml')
    # get all articles
    articles = soup.find_all('article')
    extract_info(articles=articles)

# print(collections)  
table = PrettyTable(field_names = ['Headline','Date','Author'])
table.add_rows(collections)
print(table)
