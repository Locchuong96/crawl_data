from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable

# give response from target page
keyword = input('What is your keyword? ')
keyword = keyword.replace(' ','+')
#print(keyword)
html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keyword}').text

# create soup instance by html_text
soup = BeautifulSoup(html_text,'lxml')
#print(soup.prettify())
# get job-list
job_list = soup.find('ul',class_='new-joblist')
# get job in the job list
jobs = job_list.find_all('li',class_='clearfix job-bx wht-shd-bx')
#print(len(jobs))

collections = []

for job in jobs:
    #extract update-date
    tags = job.find('div',class_ = 'applied-dtl clearfix')
    date = tags.find('span',class_ = 'sim-posted').text.strip()
    #date = date.replace(' ','')
    date = date.replace('\n','')
    date = date.lower()
    #print(date)
    if 'few' not in date:
        continue
    # extract detail link
    detail_link = job.find('header',class_ = 'clearix')
    detail_link = job.find('a').attrs['href']
    # print(detail_link)
    # extract position
    position = job.find('a').text.strip().replace(' ','')
    # extract company
    company = job.find('h3',class_='joblist-comp-name').text.strip()
    #company = company.replace(' ','')
    # extract year exp and location
    tags = job.find('ul',class_='top-jd-dtl clearfix')
    exp_location = tags.find_all('li')
    exp = exp_location[0]
    exp = exp.text.strip()
    exp = exp.replace('card_travel','')
    exp = exp.replace(' ','')
    # extract year exp and location
    location = exp_location[-1]
    location = location.text.strip().split()[-1]
    location = location.replace(' ','')
    # extract year exp and location
    #location = tag.find('span').location.text.strip()
    # print(exp,location)
    # extract descript and skills
    tags = job.find('ul',class_ = 'list-job-dtl clearfix')
    descript = tags.find_all('li')[0]
    descript = descript.text.strip()
    descript = descript.replace('\n','')
    #print(descript)
    skills = tags.find_all('li')[-1]
    skills = skills.text.strip()
    skills = skills.replace(' ','')
    skills = skills.replace('\n','')
    #print(skills)
    collections.append([position,company,exp,location,date])

table = PrettyTable(field_names = ['position','company','exp','location','date'])
table.add_rows(collections)
print(table)    