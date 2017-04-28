#!/usr/bin/python
print "Content-type: text/html"
print ""


import json
import cgi


import os

print """<!-- saved from url=(0047)http://v4-alpha.getbootstrap.com/examples/blog/ -->
<html lang="en" class="gr__v4-alpha_getbootstrap_com"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">

    <title>NOC Outage Tool</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/blog/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/css/blog/blog.css" rel="stylesheet">

<style>
.navbar-form{
	margin-top:9px;
	float:right;
	text-align:right;
}

table tr{
   height: 10px;
}

.navbar {
        background-color: #3399ff;
        background-image: none;
    }


</style>
  </head>

  <body data-gr-c-s-loaded="true">
    <div class="blog-masthead">
      <div class="container">
        <nav class="navbar navbar-inverse navbar-fixed-top ">
	<div class="container">
          <a class="nav-link active" href="http://localhost:82/cgi-bin/updated_outage/new.py">Home</a>
          <a class="nav-link" href="http://localhost:82/test/updated_outage/button.html">Outage</a>
          <a class="nav-link" href="href="http://localhost:82/test/updated_outage/jira_create.html">Create Jira</a>
          <a class="nav-link" href="http://localhost:82/test/updated_outage/slack_channel.html">Create Slack </a>
		<form class="navbar-form navbar-right" role="search">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search" name="q">
		</div>
		</form>
	</div>
	</div>
        </nav>
	</div>
    </div>

                <div class="container-fluid">
<div class="wrapper">
<div class="row">
<div class="span12">
<p style="margin-left: 500px;margin-top: 95px; color: #003366;">Welcome to DashBoard</p>

<hr style="height: 12px; box-shadow: inset 0 12px 12px -12px rgba(0, 0, 0, 0.5);margin-left: 0px;">
</div>
</div>
  <div style="background-color: white;width:900px;margin: 0px auto; padding: 15px;border-radius: 2px;" >

<table class="table table-bordered table-hover" id="sample_1">
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
print "</head>"


os.chdir('/var/www/cgi-bin')
p=os.getcwd()

with open('details.json','r') as f:
        d=json.load(f)


g=d['Status']

dic={'red':'red','amber':'orange','green':'green','Red':'red','Green':'green','resolved':'green'}

l=range(len(d['Name']))

s=1
while s<=len(d['Name']):
        for i in range(len(d['Name'])):
		print"""
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



    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/js/blog/jquery.min.js" integrity="sha384-THPy051/pYDQGanwU6poAc/hOdQxjnOEXzbT+OuUAFqNqFjL+4IGLBgCJC3ZOShY" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="/js/jquery.min.js"><\/script>')</script>
    <script src="/js/blog/tether.min.js" integrity="sha384-Plbmg8JY28KFelvJVai01l8WyZzrYWG825m+cZ0eDDS1f7d/js6ikvy1+X+guPIB" crossorigin="anonymous"></script>
    <script src="/js/blog/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/js/blog/ie10-viewport-bug-workaround.js"></script>
  
<script src="/js/Dashboard/jquery.min.js" integrity="sha384-THPy051/pYDQGanwU6poAc/hOdQxjnOEXzbT+OuUAFqNqFjL+4IGLBgCJC3ZOShY" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="/js/jquery.min.js"><\/script>')</script>
    <script src="/js/Dashboard/tether.min.js" integrity="sha384-Plbmg8JY28KFelvJVai01l8WyZzrYWG825m+cZ0eDDS1f7d/js6ikvy1+X+guPIB" crossorigin="anonymous"></script>
    <script src="/js/Dashboard/bootstrap.min.js"></script>
    <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
    <script src="/js/Dashboard/holder.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/js/Dashboard/ie10-viewport-bug-workaround.js"></script>




</body></html>
"""
