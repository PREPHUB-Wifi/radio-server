from urllib.request import urlopen
from urllib.parse import urlencode  
import urllib.request
import http.client 
import time
from datetime import date

url = '127.0.0.1:8081/notes'
data = {
  "newName":"Bridget",
  "needHelp":"food",
  "notes":"quesadilla",
  "time": 12345678923456789
}

curr_data = server_connection('GET') 
if(data not in curr_data):
  if the ids are out of sync:
#   figure out which packets are missing
#   send a request to the radio to get the missing packets 
  server_connection('POST') 

def fix_data(data):
    return data 

def server_connection(request_name):
  data_encoded = urlencode(data)
  h = http.client.HTTPConnection('127.0.0.1:8081')
  headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
  h.request(request_name, '/notes', data_encoded, headers)
  r = h.getresponse()
  return r.read()