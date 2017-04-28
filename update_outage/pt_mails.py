#!/usr/bin/python

print "Content-type: text/html"
print ""

import cgi
import json
from smtplib import SMTP
import smtplib, sys
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
import codecs
import json

__author__="vivek.sinha@inmobi.com"


p=os.environ['HTTP_REFERER'].split('/')
m=p.pop()
j=m.split('_')

with open('/var/www/cgi-bin/updated_outage/files/%s.json'%j[0]) as js:
	fg=json.load(js)
	
st=fg['Status']
sb=fg['Issue']

sub=st.upper()+':'+sb


ab=codecs.open('/var/www/test/updated_outage/files/%s_update.html'%j[0])
bc=ab.readlines()
ab.close()

hq='<b><center><u>S0 Outage Communication</u></center></b>\n'
mq='<b><center><u>S1 Outage Communication</u></center></b>\n'

if hq in bc:
	nu=bc.index(hq) 
else:
	nu=bc.index(mq)

del bc[:nu]

ur=bc.index('\t<form action="/cgi-bin/updated_outage/pt_mails.py" method="get">\n')

del bc[ur:]

ki=''.join(bc)

foot="<br>Regards & Thanks<br>NOC"

nl=ki+foot

receipents = ['vivek.sinha@inmobi.com']

def py_mail(SUBJECT, BODY, TO, FROM):
	MESSAGE = MIMEMultipart('alternative')
        MESSAGE['subject'] = SUBJECT
        MESSAGE['To'] = ",".join(receipents)
        MESSAGE['From'] = FROM
        HTML_BODY = MIMEText(BODY, 'html')
        MESSAGE.attach(HTML_BODY)
        server = smtplib.SMTP('mrelay.corp.inmobi.com')
        server.sendmail(FROM, TO, MESSAGE.as_string())
        server.quit()
if __name__ == "__main__":
	"""Executes if the script is run as main script (for testing purposes)"""
	email_content =nl
	FROM = 'No-reply@inmobi.com'
	py_mail(sub, email_content, receipents, FROM)


print "Update sent successfully"

print "<br />"

print """
<a href ='http://localhost:82/cgi-bin/updated_outage/new.py'>Back to home....</a>

"""

