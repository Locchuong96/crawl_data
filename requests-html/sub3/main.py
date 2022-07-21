from requests_html import HTML,HTMLSession
#from prettytable import PrettyTable
import csv

csv_file = open('cm_scrape.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Headline','Date','Author','Summary','youtube_link'])

# get the session for your html session
session = HTMLSession()
response = session.get('https://coreyms.com/')

articles = response.html.find('article')
# print(response.html) # html element

#print(len(articles))
collections = []
for article in articles:
    headline = article.find('a.entry-title-link',first = True).text.strip()
    date = article.find('time.entry-time',first = True).text.strip()
    author = article.find('span.entry-author-name',first = True).text.strip()
    summary= article.find('div.entry-content',first = True).text.strip()
    video_id = None
    # sometime in the article there is no link in the article
    try:
        video_link = article.find('iframe',first = True)
        video_id = video_link.attrs['src'].split('/')[4]
        video_id = video_id.split("?")[0]
        youtube_link = f'https://youtube.com/watch?v={video_id}'
    except Exception as e:
        pass
    collections.append([headline,date,author,video_id])
    csv_writer.writerow([headline,date,author,summary,youtube_link])

csv_file.close()
print('csv exported!')

# table = PrettyTable(field_names = ['Headline','Date','Author','video_id'])
# table.add_rows(collections)
# print(table)
    
