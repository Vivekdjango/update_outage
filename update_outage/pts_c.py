#!/usr/bin/python
print "Content-Type: text/html"
print ""


import json
import cgi


import os



print " <head>"
print " <title>NOC Outage Tool</title>"
print """
<link type="text/css" rel="stylesheet" href="/css/style1.css">
<link href="https://fonts.googleapis.com/css?family=Oleo+Script" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
<link  type="text/css" href="/css/bootstrap.min.css" rel="stylesheet" />

<link href="https://fonts.googleapis.com/css?family=Lobster+Two" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Aref+Ruqaa" rel="stylesheet">


<style> 

.dataTables_paginate
{
        display: none;
}


}
.dataTables_filter 
{
        display: none;
}

ul li{
	font-family: "Lobster Two', cursive;"
	font-size: 20px;	
}

ul li li

{
	font-family: "Lobster Two', cursive;"
	font-size:20px;
}
</style>

"""

print "</head>"


os.chdir('/var/www/cgi-bin')
p=os.getcwd()

with open('details.json','r') as f:
	d=json.load(f)


g=d['Status']

dic={'red':'red','amber':'orange','green':'green','Red':'red','Green':'green','resolved':'green'}


print """<body>

<div class="container-fluid dark ">
	<div class="wrapper">
		<div id="logo_left">
			<h2 style="color: white;margin-top: 5px;margin-left: 500px;align: center;font-family: 'Lobster Two', cursive;"><u>NOC  &nbsp;  Outage &nbsp;  Tool</u></h2>

		</div>
	</div>		
</div>
<div class="container-fluid  dark">
	<div class="wrapper">

		<ul style="font-family: 'Lobster Two', cursive;">
			<li><a href="/cgi-bin/updated_outage/pts_c.py">Home</a></li>
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

<div class="container">
<div class="wrapper">
<div class="row">
<div class="span12">
<p style="margin-left: 500px;margin-top: 10px;color: #003366;">Welcome to DashBoard</p>

<hr style="height: 12px; box-shadow: inset 0 12px 12px -12px rgba(0, 0, 0, 0.5);margin-left: 200px;">
</div>
</div>
  <div style="background-color: white;width:900px;margin-left: 100px; padding: 15px;border-radius: 2px;" >

<table class="table table-bordered" id="sample_1">
              <thead style="background-color: #003366;">
              <tr style="color: white;">
                  
                  <th>S No</th>
                  <th>Issue Title</th>
                  <th>Sevirity</th>
                  <th>Status</th>
                  <th>Jira</th>
		  <th>Slack</th>
              </tr>
              </thead>
              <tbody>

"""
l=range(len(d['Name']))

s=1
while s<=len(d['Name']):
	for i in range(len(d['Name'])):
		print """
		                <div style="background-color: white;width:900px;  margin-left: 100px; padding: auto;border-radius: 10px;" >

<tr>	
                                                                  <td>{0}</td>
                                                                  <td><a href="/test/updated_outage/files/{1}.html" name='name' target="_blank">{2}</a></td>
                                                                  <td>{3}</td>
                                                                  <td style="font-size: 17px;color: {4};">{5}</td>                                                                  <td><a href="https://jira.corp.inmobi.com:8443/browse/{6}" target="_blank">{7}</a></td>
                                                                  <td><a href="https://inmobi.slack.com/messages/{8}" target="_blank">{9}</a></td>
                                                </tr>

			""".format(s,d['Name'][i],d['Name'][i],d['Severity'][i],dic[g[i]],g[i].upper(),d['Jira'][i],d['Jira'][i],d['Slack'][i],d['Slack'][i])
		s+=1
     
        
print """
</tbody>
</table>
</div>
</div>
</div>

   <script type="text/javascript" src="/js/jquery-1.8.3.min.js"></script>
   <script type="text/javascript" src="/js/jquery.dataTables.js"></script>
   <script type="text/javascript" src="/js/DT_bootstrap.js"></script>
   <script type="text/javascript" src="/js/dynamic-table.js"></script>



</body>"""
