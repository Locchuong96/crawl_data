from bs4 import BeautifulSoup 

with open('sub6/home.html','r') as html_file:
    source = html_file.read()
    soup = BeautifulSoup(source,'lxml')
print(soup.prettify())