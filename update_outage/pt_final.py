#!/usr/bin/python

print "Content-type: text/html"
print ""

import cgi
import json

__author__="vivek.sinha@inmobi.com"

form=cgi.FieldStorage()

comm = form.getvalue('comm')

h='TestingOutage.json'

#comm = raw_input("Enter comment:")
with open(h,'r') as f:
	d=json.load(f)

if 'Summary' in d:
	d['Summary'].append("<ul><li>%s</li></ul>"%(comm))

with open(h,'w') as f:
	json.dump(d,f)

print ('Success')
