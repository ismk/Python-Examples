import sys
import urllib2
from datetime import date
 
if not len(sys.argv) == 3:
    print 'Usage: issuu.py <pub_id> <number_of_pages>'
    print 'Where pub_id is the issuu string identifier, such as'
    print '  081230122554-f76b0df1e7464a149caf5158813252d9'
    print 'Read the source of this script for how to find it.'
    sys.exit()
pub = sys.argv[1]
pages = int(sys.argv[2])
 
for x in range(1, pages+1):
    px = "page_%s.jpg" % x
    padx = "page_%03d.jpg" % x
    print date.today().strftime("%Y-%m-%d") + str(x) + " get " + px + " >> " + padx
    open(padx,'wb').write(urllib2.urlopen('http://image.issuu.com/' + pub + '/jpg/' + px).read())
 
print date.today().strftime('%Y-%m-%d ') + str(pages) + " downloaded. Done!"