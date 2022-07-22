from bs4 import BeautifulSoup
import requests
import time
import csv

# give response from target page
keyword = input('What is your keyword? ')
keyword = keyword.replace(' ','+')
unfamiliar_skills = input("What is your unfamiliar skills (split it out by ',')? ")
unfamiliar_skills = unfamiliar_skills.lower()
unfamiliar_skills = unfamiliar_skills.split(',')
print(f'Seaching: [{keyword}] filtering out: [{unfamiliar_skills}]')

html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={keyword}').text

# wrap your processing into a function
def find_jobs():
    # create soup instance by html_text
    soup = BeautifulSoup(html_text,'lxml')
    # get job-list
    job_list = soup.find('ul',class_='new-joblist')
    # get job in the job list
    jobs = job_list.find_all('li',class_='clearfix job-bx wht-shd-bx')

    collections = []

    for job in jobs:
        #extract update-date
        tags = job.find('div',class_ = 'applied-dtl clearfix')
        date = tags.find('span',class_ = 'sim-posted').text.strip()
        #date = date.replace(' ','')
        date = date.replace('\n','')
        date = date.lower()
        # check new condition
        if 'few' not in date:
            continue
        # extract year exp and location
        # extract descript and skills
        tags = job.find('ul',class_ = 'list-job-dtl clearfix')
        descript = tags.find_all('li')[0]
        descript = descript.text.strip()
        descript = descript.replace('\n','')
        # extract skills
        skills = tags.find_all('li')[-1]
        skills = skills.text.strip()
        skills = skills.lower()
        skills = skills.replace(' ','')
        skills = skills.replace('\n','') # string
        # check unfamiliar sill
        cond = False
        for skill in unfamiliar_skills:
            if skill in skills.split(','):
                #print("YESSS")
                cond =True
                break # break for
        if cond == True:
            continue   
        # extract detail link
        detail_link = job.find('header',class_ = 'clearix')
        detail_link = job.find('a').attrs['href']
        # print(detail_link)
        # extract position
        position = job.find('a').text.strip().replace(' ','')
        # extract company
        company = job.find('h3',class_='joblist-comp-name').text.strip()
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
        # collect data
        collections.append([position,company,exp,date,skills,detail_link])
        # print it out
        print(f'Company Name: {company}')
        print(f'Position: {position} Exeperiences: {exp}')
        print(f'Skills: {skills}')
        print(f'Detail: {detail_link}')
        print()
    return collections
        
if __name__ == "__main__":
    count = 1
    while True:
        # create csv file
        csv_file = open(f'./sub14/s{count}.csv','w')
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['position','company','exp','date','skills','detail']) 
        # scrape
        collections = find_jobs()
        # write down
        csv_writer.writerows(collections)
        csv_file.close()
        print('Exported csv')
        # wait
        time_wait = 1
        print(f'Waiting {time_wait} mins.')
        time.sleep(time_wait * 60)
        count+=1