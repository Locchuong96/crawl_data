from bs4 import BeautifulSoup 

with open('sub6/home.html','r') as html_file:
    source = html_file.read()
    soup = BeautifulSoup(source,'lxml')

courses = soup.find_all('div',class_='card')

for course in courses:
    title = course.find('h5',class_ = 'card-title').text.strip()
    summary = course.find('p',class_ = 'card-text').text.strip()
    price = course.find('a',class_ = 'btn btn-primary').text.strip()
    price = price.split()[-1]
    
    print(f'{title} - {summary} - {price}')