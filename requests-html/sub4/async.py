import time 
from requests_html import AsyncHTMLSession 

asession = AsyncHTMLSession() # a asynchronous session can run multi asynchronous function

# async function
async def get_delay1():
    r = await asession.get('https://httpbin.org/delay/1')
    return r

async def get_delay2():
    r = await asession.get('https://httpbin.org/delay/2')
    return r

async def get_delay3():
    r = await asession.get('https://httpbin.org/delay/3')
    return r

t1 = time.perf_counter()

# return a list of responses
results = asession.run(get_delay1,get_delay2,get_delay3) # while waiting, the assesion try to execute the function

# each iteam in the results list is a response object and can be interacted with as such
for result in results:
    response = result.html.url
    print(response)

t2 = time.perf_counter()

print(f'Asynchronous: {t2 - t1} seconds')