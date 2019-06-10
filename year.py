#Create a program that asks the user to enter their name and their age.
 #Print out a message that will tell them the year that they will turn 95 years old

import datetime
name=input("Enter Your Name :")
age=int(input("Enter your age :"))
now = datetime.datetime.now()
print(name," Will turn 95 in ",(95-age)+now.year)
