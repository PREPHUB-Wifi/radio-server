from urllib.request import urlopen
from urllib.parse import urlencode 
import http.client 
import time
from datetime import date

url = '127.0.0.1:8081/notes' #node.js server address
#test data 
data = { 
  "newName":"Bridget",
  "needHelp":"food",
  "notes":"quesadilla",
  "time": 12345678923456789
}


data_encoded = urlencode(data) #encode URL for sending
h = http.client.HTTPConnection('127.0.0.1:8081') #connect to server
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"} #set headers
h.request('POST', '/notes', data_encoded, headers) #post to server
r = h.getresponse() #get the response
print(r.read()) #print it out for a sanity check