'''

Problem 9:   

write a code that will take user input untill number of character not exceeding
500 chars.

Now do the following  tasks:
i)   print the number of repeated characters in descending order
ii)  print number of repeated words in descending order
iii)  if a word is repeating more than 5 times remove all those words
iv)  if a word is present only one times add the same word in that string but length must not increase more than 500 chars , you can remove any random thing for doing the same 
'''
import numpy as np
chars = input('Enter the string of characters')
if(len(chars)>500):
    chars=chars[:500]
count={}
for char in chars:
    if char in count.keys():
        count[char]+=1
    else:
        count[char]=1
for v in sorted( count.values() ,reverse=True):
    for key in count:
        if count[ key ] == v:
            print(key)

for k,v in count.items():
    if(v>5):
        del(count[k])
chars = list(chars)
for k,v in count.items():
    if(count[k]==1):
        if(len(chars) >499):
            del(np.random(count[k])
        count[k]+=1   
