#!/usr/bin/python
print "Content-Type: text/html"
print ""

from smtplib import SMTP
import smtplib, sys
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import datetime
import cgi, cgitb
from termcolor import colored
import os

cgitb.enable()

__author__="vivek.sinha@inmobi.com"

sender = 'No-reply@inmobi.com'
#recipient = 'vivek.sinha@inmobi.com'
receipents = ['vivek.sinha@inmobi.com']
d=datetime.datetime.now().strftime("%d-%B-%Y")
t=datetime.datetime.now().strftime("%H:%M %p")
form=cgi.FieldStorage()
pr=form.getvalue('priority')
sub=form.getvalue('subject')
jira=form.getvalue('jira')
slack=form.getvalue('slack')
app=form.getvalue('app')
bu=form.getvalue('business')
re=form.getvalue('region')
desc=form.getvalue('desc')
out=form.getvalue('time')
ath=form.getvalue('fileinput')
up=form.getvalue('update')
rep=form.getvalue('reporter')
owner=form.getvalue('owner')


st="""
<p style='color:red'><b>Status:</b>RED</p>
"""
head="""
<b><center><u>%s Outage Communication</u></center></b>
"""%(pr.upper())
j="""
<a href=https://jira.corp.inmobi.com:8443/browse/{0}>{1}</a>
""".format(jira,jira)

slk="""
<a href=https://inmobi.slack.com/messages/{0}>{1}</a>
""".format(slack,slack)

status='RED'

msg = "%s<br><br> <b>Date</b>:%s <br> <br> <strong>Outage Creation Time:</strong>:%s (IST)<br><br> %s <br><b>Downtime</b>:%s (minute)<br><br><b>Issue</b>:%s <br><br> <b>Jira:</b>%s <br><br><b>Slack:</b>%s<br> <br><b>Application Impacted:</b>%s <br> <b>Buisness Impact:</b>%s <br> <b>Region Impacted:</b>%s<br> <b>Reporter:</b>%s<br><b>Incident Owner:</b>%s<br/> <br><b><u>Summary:</b></u><br>"%(head,d,t,st,out,sub,j,slk,app,bu,re,rep,owner)


ab=desc.split('\n')

l=[]
for i in ab:
	val="<ul><li>%s</li></ul>"%(i)
	l.append(val)

de=''.join(l)

upt="<b>Next Update:</b> %s <br>"%(up)

foot="<br>Regards & Thanks<br>NOC"

body=msg+de+upt+foot

subject=status+':'+pr.upper()+' '+'Outage Communication'+' '+sub


messg = MIMEMultipart('alternative')
messg['Subject'] = subject
messg['From'] = sender
#msg['Reply-to'] = 'akarsh.gangadharan@inmobi.com'
messg['To'] = ",".join(receipents)

messg.preamble = 'Multipart massage.\n'

part = MIMEText(body,'html')
messg.attach(part)

#new = MIMEApplication(open('%s'%(ath),'rb').read())
#new.add_header('Content-Disposition', 'attachment', filename="%s"%(ath))
#messg.attach(new)


smtp = SMTP("mrelay.corp.inmobi.com")
smtp.ehlo()

smtp.sendmail(messg['From'], messg['To'], messg.as_string())



q=sub.replace(" ","")

path1='/var/www/test/updated_outage/files/'
os.system('touch /var/www/test/updated_outage/files/{0}.html'.format(q))

path2 = '/var/www/cgi-bin/updated_outage/files/'

isue=pr.upper()+' '+'Outage Communication'+' '+sub

da={'Date':d,'Time':t,'Downtime':st,'Issue':isue,'Jira':j,'Slack':slk,'Application Impacted':app,'Buisness Impacted':bu,'Region Impacted':re,'Summary':l}

import json

with open(path2+q+'.json','w') as f:
	json.dump(da,f)



with open('/var/www/cgi-bin/details.json','r') as k:
	fl=json.load(k)


fl['Name'].insert(0,q)
fl['Status'].insert(0,'Red')
fl['Jira'].insert(0,jira)
fl['Slack'].insert(0,slack)
fl['Severity'].insert(0,pr.upper())
fl['Time'].insert(0,t)
fl['Downtime'].insert(0,out)

try:
	with open('/var/www/cgi-bin/details.json','w') as k:
		json.dump(fl,k)
except Exception as e:
	print (e)

par="""
<!DOCTYPE html>
<!-- saved from url=(0053)http://v4-alpha.getbootstrap.com/examples/dashboard/# -->
<html lang="en" class="gr__v4-alpha_getbootstrap_com"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="Outage Tool">
    <meta name="author" content="Vivek Sinha">

    <title>NOC Outage Tool</title>


<link href="../css/new/bootstrap.min.css" rel="stylesheet">   
<script src="../css/new/jquery.min.js"></script>
<link rel="stylesheet" 
href="../css/new/jquery.dataTables.min.css"></style>
<script type="text/javascript" 
src="../css/new/jquery.dataTables.min.js"></script>
<script type="text/javascript" 
src="../css/new/bootstrap.min.js"></script>

<style>
.sidebar{

	background-color:black;
	height:100%;
	padding-bottom: 100%;
}
.sidebar a{
	color:white;
	margin-left:0px;
	text-align:left;
}
.sidebar a:hover{
	color:blue;
}
.sidebar li
{
	margin-top:7px;
	text-align:center;
}
.nav-sidebar{
	margin-top:0px;
}


.navbar-brand{
	color:blue;
}

.table thead tr th
{
	padding:4px;
	text-align:center;
}
.table-responsive  tr td { 
	padding:4px;
} 

.table-responsive{
	margin-top:20px;
	text-align:left;
	padding-left:0px;
	margin-left:0px;
}
.navbar .navbar-fixed-top .bg-inverse{
	background-color:white;
	background-image:none;
}
.wrapper{
	padding-left:0px;
	margin-left:0px;
}
.nb{
	margin-top:50px;
}
.dataTables_wrapper .dataTables_length {
float: right;
}
.dataTables_wrapper .dataTables_filter {
float: left;
text-align: left;
border-radius:12px solid #dbdbdb;
}
</style>
 </head>

  <body data-gr-c-s-loaded="true">

<!--    <nav class="navbar navbar-fixed-top navbar-default">
<a class="navbar-brand" href="#">NOC Outage Tool</a>
	<div id="navbar" class="navbar-collapse collapse">
	</div>	
</nav>

        <form class="float-xs-right">
          <input type="text" class="form-control" placeholder="Search...">
        </form>
    
  </div>-->

<div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar content">
	<li><a href="#"><img style="width:100%;height: 60px;margin-left: 0px;" src="../css/new/images1.png"></a></li>	
            <li class="active" style="margin-top: 5px;"><a href="http://localhost:82/cgi-bin/updated_outage/new.py">Dashboard <span class="sr-only">(current)</span></a></li>
            <li><a href="http://localhost:82/cgi-bin/updated_outage/new.py">Home</a></li>
            <li><a href="http://localhost:82/test/updated_outage/button.html">Outage Action</a></li>
            <li><a href="http://localhost:82/test/updated_outage/jira_create.html">Jira Action</a></li>
          </ul>
        </div>

"""

frm= """ 
        <br/>
       <form action="/cgi-bin/updated_outage/pt_test.py" style="margin-left:50px;" method="get">

         <div class="form-group">
                <label class="control-label col-sm-2" for="status">Status:</label>
                    <div class="col-sm-2">
                    <select id="status" name="status" style="width:100px; margin-left: 65px;">
                        <option value="red">RED</option>
                        <option value="amber">AMBER</option>
                        <option value="green">GREEN</option>
                   </select>
                </div>
                <br/>
          </div>
        <div class="form-group">
        <label class="control-label col-sm-2" for="next">Next Update: </label>
        <div class="col-sm-6">
        <input class="form-control" type='text' name='next' id="next">
        </div>
        <br>
        </div>
        <div class="form-group">
        <label class="control-label col-sm-2" for="comm">Comments: </label><br/>
        <div class="col-sm-6">
        <textarea id="comm" name="comm" style="height:100px; width:320px;" row="7" required="required"></textarea>
        </div>
        <br/>
        </div>
        <div class="form-group">
        <div class="col-sm-offset-2 col-sm-6">
        <button type="submit" class="btn btn-default">Submit</button>
        </div>
        </div>
        </form>
</div>
</div>
</div>
</body>

"""



with open(path1+q+'.html','w') as f:
	f.write(par)
	f.write("\n")
	f.write("<div style='margin-left: 280px;margin-right: 100px; padding: auto; margin-top: 10px;'>")
	f.write("\n")
	f.write(msg)
	f.write("\n")
	f.write(de)
	f.write("\n")
	f.write(upt)
	f.write("\n")
	f.write("<hr style='border-top: 2px solid black;'>")
	f.write('\n')
	f.write("<h4><center><u> Enter New Updates </u></center></h4>")
	f.write('\n')
	f.write(frm)
	f.write('\n')
	f.close()


print "Outage Mail created and sent successfully"
print "<br />"
print """
<a href ='http://localhost:82/cgi-bin/updated_outage/new.py'>Back to home....</a>

"""
