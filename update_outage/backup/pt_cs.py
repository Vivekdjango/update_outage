#!/usr/bin/python

print "Content-type: text/html"
print ""

import json

import os

print " <head>"
print "	<title>Hello OWrld</title>"
print """
<link type="text/css" rel="stylesheet" href="/css/style1.css">
<link href="https://fonts.googleapis.com/css?family=Oleo+Script" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
	<link href="/css/bootstrap.min.css" rel="stylesheet" />
	"""

print "</head>"

os.chdir('/var/www/cgi-bin')

r=os.getcwd()
'''
l=[0,1,2,3,4,5,6,7,8,9,10]
k=list(filter((lambda i:'.json' in i),os.listdir(r)))

w=dict(zip(l,k))



for i in os.listdir(r):
	if '.json' in i:
		g=i
		m=g.split('.')
		with open(g,'r') as f:
			d=json.load(f)
'''
with open('details.json','r') as f:
	d=json.load(f)

g=d['Status']


print """<body>


                                   <script type="text/javascript" src="/js/jquery-1.8.3.min.js"></script>
                                   <script type="text/javascript" src="/js/jquery.dataTables.js"></script>
                                   <script type="text/javascript" src="/js/DT_bootstrap.js"></script>
                                   <script type="text/javascript" src="/js/dynamic-table.js"></script>
<div class="container-fluid dark">
<div class="wrapper">
                                                        <div id="logo_left">
                                                                <h2 style="color: white;margin-top: 0px;margin-left: 500px;align: center;">NOC  &nbsp;  Outage &nbsp;  Tool</h2>
                                                        </div>
                                                </div>
                                        </div>

                                        <div class="container-fluid  dark">
                                                <div class="wrapper">

                                                        <ul >
                                                                <li><a href="/cgi-bin/pt_cs.py">Home</a></li>

<li><a href="/test/updated_outage/button.html">Outage Function</a></li>
                                <li><a href="/test/updated_outage/jira_create.html">Jira Action</a>
                                        <ul>
                                                <li><a href="jira_create.html">Create</a></li>
                                                <li><a href="#">Update</a></li>
                                        </ul>
                                </li>
                                <li><a href="slack_channel.html">Slack Action</a>
                                        <ul>
                                                <li><a href="slack_channel.html">Channel Creation</a></li>
                                                <li><a href="slack_message.html">Message</a></li>
                                        </ul>
                                </li>
                        </ul>
                </div>
        </div>



		<div class="container-fluid ">
		<div class="wrapper">

	<div style="background-color: white;width:900px; margin-top:0px ; margin-left: 200px; padding: 52px;" >

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


for i in range(len(d['Name'])):
        print"""
				        <div style="background-color: white;width:900px; margin-top:0px ; margin-left: 200px; padding: auto;" >
	
						  <tr>
								  <td>1</td>
								  <td><a href="/cgi-bin/pt_update.py" target="_blank">{0}</a></td>
								  <td>{1}</td>
								  <td bgcolor={2} style="border-radius: 12px;"></td>
								  <td>{3}</td>
								  <td>{4}</td>
						</tr>
		""".format(d['Name'][i],d['Severity'][i],g[i],d['Jira'][i],d['Slack'][i])

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
