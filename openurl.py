# Store top 5 url in a list and then open those url in browser. (Python)

import time
from googlesearch import search
import webbrowser
web=input("please enter some topic:-")


url=[]

for i in search(web,stop=10):

    print(i)
    webbrowser.open_new_tab(i)
    time.sleep(1)
    url.append(i)



print(url)
