#write a code using  that will take user input from and search on google and store top 10 url in the list.

import time
from googlesearch import search
web=input("please enter some topic:-")


url=[]

for i in search(web,stop=10):

    print(i)
    time.sleep(1)
    url.append(i)



print(url)
