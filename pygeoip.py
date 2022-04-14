import urllib2
import json
from urllib2 import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
print ('\n')
print ('Your IP detail')
print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}\n'.format(org,region,country,city,IP))
