from bs4 import BeautifulSoup 

with open('sub6/home.html','r') as html_file:
    source = html_file.read()
    soup = BeautifulSoup(source,'lxml')

#print(soup.prettify())

# find one
# tags = soup.find('h5')
# print(tags)

# find_all
tags = soup.find_all('h5')
print(type(tags))
for tag in tags:
    #print(tag)
    print(tag.text)