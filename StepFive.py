import requests
from datetime import timedelta
import dateutil.parser

r = requests.post('http://challenge.code2040.org/api/dating', data = {'token': 'e33fa7ab36fcb87205d5f9feb1cad3cb'})

#receiving json info
info = r.json()
datestamp = info['datestamp']
interval = info['interval']

#convert date received from endpoint to different format
dateConv = dateutil.parser.parse(datestamp)
#add the interval to existing date
date = dateConv + timedelta(seconds=interval)
#convert back to ISO format and add trailing Z
myDate = date.isoformat().replace('+00:00', 'Z')

#send dictionary back to server
r = requests.post('http://challenge.code2040.org/api/dating/validate', json = {'token': 'e33fa7ab36fcb87205d5f9feb1cad3cb', 'datestamp': myDate})
print r.text
