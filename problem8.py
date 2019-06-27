'''
Problem 8: 

write a code that will take input from a user and check that if it is a command
then execute it with following  conditions :

 i)  all the commands given by user either wrong or right must be store in a file
ii)   output of success command will be shown to monitor
iii)  if the input command is repeated by user give him voice note not to do this again


'''

import os
from shutil import which
#all the commands given by user either wrong or right must be store in a file
location=input('Enter the location of file in which data must be stored')
file=open(location,"a")
command=input('Enter the command')
file.write(command)
# output of success command will be shown to monitor
if(which(command)):
    print('sucsess')
    os.system(command)
file.close()
fr=open(location,'r')
print(fr.read())
fr.close()

