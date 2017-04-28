#!/usr/bin/python

print "Content-type: text/html"
print ""

import json

with open('TestingOutage.json','r') as f:
	d=json.load(f)


print " <head>"

print "	<title>NOC Outage Tool</title>"
print """
<link type="text/css" rel="stylesheet" href="/css/style1.css">
<link href="https://fonts.googleapis.com/css?family=Oleo+Script" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
<link href="/css/bootstrap.min.css" rel="stylesheet" />
"""

print "</head>"

print """
<body>

<div class="container-fluid dark ">
        <div class="wrapper">
                <div id="logo_left">
                        <h3 style="color: white;margin-top: 0px;margin-left: 500px;align: center;font-family: 'Orbitron', sans-serif;"><u>NOC  &nbsp;  Outage &nbsp;  Tool</u></h3>

                </div>
        </div>          
</div>
<div class="container-fluid  dark">
        <div class="wrapper">

                <ul >
                        <li><a href="/cgi-bin/pts_c.py">Home</a></li>
                        <li><a href="http://localhost:82/test/updated_outage/button.html">Outage Function</a></li>
                        <li><a href="http://localhost:82/test/updated_outage/jira_create.html">Jira Action</a>
                                <ul>
                                        <li><a href="http://localhost:82/test/updated_outage/jira_create.html">Create</a></li>
                                        <li><a href="#">Update</a></li>
                                </ul>
                        </li>
                        <li><a href="http://localhost:82/test/updated_outage/slack_channel.html">Slack Action</a>
                                <ul>
                                        <li><a href="http://localhost:82/test/updated_outage/slack_channel.html">Channel Creation</a></li>
                                        <li><a href="http://localhost:82/test/updated_outage/slack_message.html">Message</a></li>
                                </ul>
                        </li>
                </ul>
        </div>
</div>

"""

print """<div style="margin-left:200px;background-color: white;margin-top: 10px;padding: 50px;">"""
print "Date :" + d['Date']+"<br/> <br/>"
print "Issue :" + d['Issue']+"<br /> <br />"
print "Buisness Impacted :" + d['Buisness Impacted']+ '<br /> <br />'
print d['Downtime'] + '<br /> '
print "Region Impacted :" + d['Region Impacted'] + '<br /> <br />'
print "Application Impacted :" + d['Application Impacted'] + '<br /> <br />'

print "Jira :" +  d['Jira'] + '<br /> <br />'
print "Slack :" + d['Slack']+'<br /> <br />'
print "Time :"  + d['Time'] +'<br /> <br />'

print "Summary :"

for i in d['Summary']:
	 print (i) + '</ br>'

print "</br>"

print """<form action="/cgi-bin/pt_final.py" method="get">

	New Comment: <br/>
	<textarea name="comm" style="height:100px; width:320px;" required="required"></textarea>
       <input type="submit" value="submit" style="margin-top: 50px;background-color: #003366;border-radius:5px;color: white;width: 80px;height:40px;">
	</form>
"""
print """</div>"""

print "</body>"
print "</html>"
