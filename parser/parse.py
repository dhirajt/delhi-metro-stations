import urllib2
from BeautifulSoup import BeautifulSoup
import json

req = urllib2.Request(
    "http://en.wikipedia.org/wiki/List_of_Delhi_metro_stations",
    headers={'User-Agent': "Mozilla/5.0"})  
    #fake agent since wiki returns 403 for default requests
source = urllib2.urlopen(req).read()

print '*******Source read*********\n'

soup = BeautifulSoup(source)
rows = soup.findAll('table')[2].findAll('tr')


lst = []
form = '{ "name": "%s",\
          "details": {"layout":"%s",\
                      "line":"%s",\
                      "lattitude":0.0,\
                      "longitude":0.0 }}'

for row in rows[1:]:
    items = row.findAll('td')
    lst.append(form % (
               items[1].findAll('a')[0].contents[0],
               items[5].contents[0],
               items[3].findAll('a')[0].contents[0]))

string = '['+','.join(lst)+']'

data = json.loads(string)

f = open('metro.json', 'w+')
print '***Dumping metro.json****\n'
f.write(json.dumps(data, indent=4))
f.close()

