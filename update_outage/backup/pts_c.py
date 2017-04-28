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
<link href="/css/bootstrap.min.css" rel="stylesheet" />
"""

print "</head>"


os.chdir('/var/www/cgi-bin')
p=os.getcwd()

with open('details.json','r') as f:
	d=json.load(f)


g=d['Status']

print """<body>

<div class="container-fluid dark ">
	<div class="wrapper">
		<div id="logo_left">
			<h3 style="color: white;margin-top: 0px;margin-left: 500px;align: center;font-family: 'Orbitron', sans-serif;"><u>NOC  &nbsp;  Outage &nbsp;  Tool</u></h3>

		</div>
	</div>		
</div>
<div class="container-fluid  dark">
	<div class="wrapper">

		<ul>
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

<div class="container">
<div class="wrapper">
<p style="margin-left: 400px;margin-top: 10px;color: #003366;">Welcome to DashBoard</p>
<hr style="height: 12px; box-shadow: inset 0 12px 12px -12px rgba(0, 0, 0, 0.5);">
<div style="background-color: white;width:900px; margin-left: 10px;" >

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
		  <tr>
                                                                  <td>1</td>
                                                                  <td><a href="/cgi-bin/pt_update.py" target="_blank">{0}</a></td>
                                                                  <td>{1}</td>
                                                                  <td bgcolor={2} style="border-radius: 12px;"></td>
                                                                  <td><a href="https://jira.corp.inmobi.com:8443/browse/{3}" target="_blank">{4}</a></td>
                                                                  <td><a href="https://inmobi.slack.com/messages/{5}" target="_blank">{6}</a></td>
                                                </tr>

                                                          <tr>
                                                                  <td>2</td>
                                                                  <td><a href="/cgi-bin/pt_update.py" target="_blank">{7}</a></td>
                                                                  <td>{8}</td>
                                                                  <td bgcolor={9} style="border-radius: 12px;"</td>
                                                                  <td><a href="https://jira.corp.inmobi.com:8443/browse/{10}" target="_blank">{11}</a></td>
                                                                  <td><a href="https://inmobi.slack.com/messages/{12}" target="_blank">{13}</a></td>
                                                          </tr>
             


 
        
              
              <tr>
                  <td>6</td>
                  <td><a href="http://www.2my4edge.com/2013/07/marquee-tag-style-in-different-manner.html">Marquee style in different manner</a></td>
                  <td>6</td>
                  <td class="center "><a href="http://demos.2my4edge.com/marquee/">Demo </a></td>
                  <td><a href="http://www.2my4edge.com/2013/07/marquee-tag-style-in-different-manner.html"> Tutorial </a></td>
        	<td>Test</td>      
	</tr>
              
              <tr>
                  <td>7</td>
                  <td><a href="http://www.2my4edge.com/2013/07/my-demos-page-design-details-and-all-my.html">My Demos page design</a></td>
                  <td>3</td>
                  <td class="center "><a href="http://demos.2my4edge.com/">Demo </a></td>
                  <td><a href="http://www.2my4edge.com/2013/07/my-demos-page-design-details-and-all-my.html"> Tutorial </a></td>
        	<td>Test</td>      
	</tr>
              
              <tr>
                  <td>8</td>
                  <td><a href="http://www.2my4edge.com/2013/07/file-download-coding-using-php-and-mysql.html">File download coding using PHP and MySql</a></td>
                  <td>8</td>
                  <td class="center "><a href="http://demos.2my4edge.com/file-download-demo/">Demo </a></td>
                  <td><a href="http://www.2my4edge.com/2013/07/file-download-coding-using-php-and-mysql.html"> Tutorial </a></td>
        	<td>Test</td>      
	</tr>
              
              <tr>
                  <td>9</td>
                  <td><a href="http://www.2my4edge.com/2013/07/simple-login-logout-system-using-php.html">Simple login and logout system</a></td>
                  <td>10</td>
                  <td class="center "><a href="http://demos.2my4edge.com/login-system/">Demo </a></td>
                  <td><a href="http://www.2my4edge.com/2013/07/simple-login-logout-system-using-php.html"> Tutorial </a></td>
        	<td>Test</td>      
	</tr>
              
              <tr>
                  <td>10</td>
                  <td><a href="http://www.2my4edge.com/2013/07/username-live-availability-check-using.html">live availability Check using php</a></td>
                  <td>9</td>
                  <td class="center "><a href="http://demos.2my4edge.com/check-availibity/">Demo </a></td>
                  <td><a href="http://www.2my4edge.com/2013/07/username-live-availability-check-using.html"> Tutorial </a></td>
        	<td>Test</td>      
	</tr>
              
              </tbody>
          </table>
</div>
</div>
</div>

   <script src="/js/jquery-1.8.3.min.js"></script>
   <script type="text/javascript" src="/js/jquery.dataTables.js"></script>
   <script type="text/javascript" src="/js/DT_bootstrap.js"></script>
   <script src="/js/dynamic-table.js"></script>



</body>""".format(d['Name'][0],d['Severity'][0],g[0],d['Jira'][0],d['Jira'][0],d['Slack'][0],d['Slack'][0],d['Name'][1],d['Severity'][1],g[1],d['Jira'][1],d['Jira'][1],d['Slack'][1],d['Slack'][1])
