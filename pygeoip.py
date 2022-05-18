import os
import socket
import platform
import sys
import urllib2
import json
from urllib2 import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
username=os.getlogin()
nameof=os.environ.get('USERNAME')
hostname=socket.gethostname()
fqdn=socket.getfqdn()
osname=os.name
platform=platform.system()
#architecture=platform.architecture()
#machine=platform.machine()
#release=platform.release()
sysplatform=sys.platform
IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
print ('\nHELLO {0} - {1} - {2} - {3} - {4} - {5} - {6}'.format(username,nameof,hostname,fqdn,osname,platform,sysplatform))
#platform.machine()
#platform.release()
#ToDoo
print ('\n-===========================================')
print ('- Your IP detail')
print ('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))
print ('-===========================================\n')
