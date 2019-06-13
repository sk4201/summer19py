# A Program that takes input as username and greets with GM , GA ,GN as per the system time.

#!/usr/bin/python3
# 0.00 - 12.00 = Good Morning
# 12.00 - 17.00 =Good Afternoon
# 17.00 - 21.00 =Good Evening
# 21.00 - 0.00 =Good Night





import datetime

name =input("Enter your Name : ")
d=datetime.datetime.now()
currenthour=d.hour
currentmin=d.minute
if currenthour<12:
	print("Good Morning",name+"!")
elif currenthour>12 and currenthour<=16:
	print("Good Afternoon",name+"!")
elif currenthour > 16 and currenthour <=19:
	print("Good Evening",name+"!")
else:

	print("Good Night", name+"!")

