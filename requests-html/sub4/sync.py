import time 
from requests_html import HTMLSession 

session = HTMLSession()

t1 = time.perf_counter() # set the timer

# synchronous request
# the server will return the response after time delay you pass into the url
r = session.get('https://httpbin.org/delay/1')
response = r.html.url 
print(response)

r = session.get('https://httpbin.org/delay/2')
response = r.html.url 
print(response)

r = session.get('https://httpbin.org/delay/3')
response = r.html.url 
print(response)

t2 = time.perf_counter() 

# counting time
print(f'Synchronous: {t2 - t1} seconds')
