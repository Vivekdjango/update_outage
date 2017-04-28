#!/usr/bin/python

#from urllib.request import urlopen
print "Content-type: text/html"
print ""

import json
import urllib2

#itag=raw_input('Enter colo value:')


#print ('\n')
#url="http://ims.corp.inmobi.com/api/search/?itag=.*%s.*&filter=itag,hostname,discovered_data"%(itag)

url="http://ims.corp.inmobi.com/api/search/?itag=.*dfw1.*&filter=itag,hostname,discovered_data"

d=urllib2.urlopen(url).read().decode('utf-8')
f=json.loads(d)


data=f['result']

for i in range(len(data)):
	print "Serial Number :", i
	if 'discovered_data' not in data[i] or data[i]['discovered_data'] is None or 'physical_drives' not in data[i]['discovered_data']['storage']:
		print "itag :",data[i]['itag'] + '\n'
		print "Hostname: ",data[i]['hostname'] + '\n'
		print "No Hardware informations found" + '\n'
	else:
		print "itag :",data[i]['itag'] + '\n'
		print "Hostname: ",data[i]['hostname'] + '\n'
		print data[i]['discovered_data']['storage']['physical_drives'] 
		
		



















'''

l=f['result'][0]['discovered_data']['network']['interfaces'][0]

if 'firmware_version' in l.keys():
	print ("Firmware Version :",l['firmware_version'])
else:
	print ("Firnmware Details not found")


print ('\n')

p=f['result'][0]['discovered_data']['storage']['physical_drives']

print ('Drive Details:')

for i in range(len(p)):
	print('Slot Number:',p[i]['device_id'])
	print('Device-Type: ',p[i]['media_type'])
	print('Size: ',p[i]['size'])
	print ('Smart Alet',p[i]['smart_alert'])

print ('\n')


w=f['result'][0]['discovered_data']['memory']['units'][0]['banks']


unuse=[]

for i in range(len(w)):
	if 'size_verbose' in w[i].keys():
		print (w[i]['slot'])
		print (w[i]['size_verbose'])
		print (w[i]['type'])
	elif 'type' in w[i].keys():
		unuse.append((w[i]['slot'],w[i]['type']))
	else:
		unuse.append((w[i]['slot'],'Data Not available'))

print ("Unused-Slots:")

print (unuse)

#for i in unuse:
#	print (i)


print ('Chassis Details')

q=f['result'][0]['discovered_data']['chassis']

print ("Serial Number :",q['serial'])
print ("Model :",q['model'])


disk=f['result'][0]['discovered_data']['storage']['disks'][0]['volumes']

for i in range(len(disk)):
	print ("Logical Name :",disk[i]['logicalname'])
	print ("Size :",disk[i]['size'])


'''
