#print 5 url

import re
import linkGrabber

links = linkGrabber.Links('https://google.com')
gb = links.find(limit=4,duplicates=False,preety=false)

print(gb)
