import os, re, uuid, psutil, logging
import socket
import platform
import sys
import urllib
import urllib.request
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)
username=os.getlogin()
nameof=os.environ.get('USERNAME')
hostname=socket.gethostname()
fqdn=socket.getfqdn()
osname=os.name
osplatform=platform.system()
#architecture=platform.architecture()
#machine=platform.machine()
#release=platform.release()
sysplatform=sys.platform
IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
#print ('\nHELLO {0} - {1} - {2} - {3} - {4} - {5} - {6}'.format(username,nameof,hostname,fqdn,osname,osplatform,sysplatform))
#platform.machine()
#platform.release()
#ToDoo
ipaddr=data['ip-address']=socket.gethostbyname(socket.gethostname())
mac=data['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
#osplatform=data['platform']=platform.system()
#release=data['platform-release']=platform.release()
#version=data['platform-version']=platform.version()
#machine=data['architecture']=platform.machine()
#processor=data['processor']=platform.processor()
ram=data['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
hostname=data['hostname']=socket.gethostname()

print ('\n========--| Your system details |-===========================================')
print ('Username: {0}'.format(username))
#print ('-| Your system details |-')
print ('OS: {0}'.format(osplatform))
#print ('{0}\n'.format(release))
#print ('{0}\n'.format(version))
#print ('{0}\n'.format(machine))
#print ('{0}\n'.format(processor))
print ('RAM: {0}'.format(ram))
print ('MAC: {0}'.format(mac))
print ('LAN-IP: {0}'.format(ipaddr))
print ('Hostname: {0}'.format(hostname))
print ('========--| Your location details |--========================================')
#print ('-| Your location details |-')
print ('IP : {4} \nRegion : {1} |\tCity : {3} |\tCountry : {2} \nOrg : {0}\n'.format(org,region,country,city,IP))
#print ('-====================================================================\n')

#print ('-| System overview |-')
#for item in os.environ:
#
#    print(f'{item}{" : "}{os.environ[item]}')
#
#print ('-===========================================\n')