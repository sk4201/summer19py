'''
Problem 12: 

write a python code to do the following

i)  take input from user and search in google
ii)   pick the first 3 url of google search
iii)  make  QR-code of all 3 url's
iv)   Store all these qr-code in  apache web server in aws cloud
v)   share link of qrcode using aws public IP

Note:   v) option you can do it manually there is no need of programing

  '''

#!/usr/bin/python3

from googlesearch import search
import pyqrcode 



#taking input from user  
web=input("please Enter some topic: ")              
#declaring blank list to store result.
urllist=[]
j=0
#for iteration for searching recursively 
for i in search(web,stop=5):          
     #printing searched web addres
    print(i)  
                   	
	#appending web address in the list url
    urllist.append(i)                           
    	# Generate QR code 
    url = pyqrcode.create(i)
# Create and save the png file  
    url.svg("pqr"+str(j)+".svg", scale=8) 
    j=j+1

