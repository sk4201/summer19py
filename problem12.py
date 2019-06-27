from googlesearch import search
import pyqrcode
from pyqrcode import QRCode
web=input("Enter the search text :")
List = []


j=0

for i in search(web,stop=5):
	List.append(i)
	print(i)

	url = pyqrcode.create(List[j])
	url.svg("qr"+str(j) +"svg",scale=8)
	j=j+1
	print(url.terminal())

