#!/usr/bin/python

print "Content-type: text/html"
print ""

import json

import os
__author__="vivek.sinha@inmobi.com"

print " <head>"
print "	<title>Hello OWrld</title>"
print """
<link href="https://fonts.googleapis.com/css?family=Oleo+Script" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
<link href="/css/bootstrap.min.css" rel="stylesheet" />

<!-- saved from url=(0047)http://v4-alpha.getbootstrap.com/examples/blog/ -->
<html lang="en" class="gr__v4-alpha_getbootstrap_com"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="http://v4-alpha.getbootstrap.com/favicon.ico">

    <title>Blog Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="bootstrap/outage/blog/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="bootstrap/outage/blog/blog.css" rel="stylesheet">

<style>
.navbar-form{
	margin-top:9px;
	float:right;
	text-align:right;
}

table tr{
   height: 10px;
}
.dataTables_paginate
{
        display: none;
}


}
.dataTables_filter 
{
        display: none;
}


</style>"""

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

  <body data-gr-c-s-loaded="true">
    <div class="blog-masthead">
      <div class="container">
        <nav class="nav blog-nav ">
          <a class="nav-link active" href="#">Home</a>
          <a class="nav-link" href="#">Outage</a>
          <a class="nav-link" href="#">Create Jira</a>
          <a class="nav-link" href="#">Create Slack </a>
            <form class="navbar-form navbar-right" role="search">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search" name="q">
		</div>
		</form>
	</div>
        </nav>
	</div>
    </div>

                <div class="container">
<div class="wrapper">
<div class="row">
<div class="span12">
<p style="margin-left: 450px;margin-top: 2px; color: #003366;">Welcome to DashBoard</p>

<hr style="height: 12px; box-shadow: inset 0 12px 12px -12px rgba(0, 0, 0, 0.5);margin-left: 90px;">
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


for i in range(len(d['Name'])):
        print"""
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

           			  <script type="text/javascript" src="/js/jquery-1.8.3.min.js"></script>
                                   <script type="text/javascript" src="/js/jquery.dataTables.js"></script>
                                   <script type="text/javascript" src="/js/DT_bootstrap.js"></script>
                                   <script type="text/javascript" src="/js/dynamic-table.js"></script>
				 <script type="text/javascript" src="js/st.js"></script>

  `<script type="text/javascript" src="/js/jquery-1.8.3.min.js"></script>
   <script type="text/javascript" src="/js/jquery.dataTables.js"></script>
   <script type="text/javascript" src="/js/DT_bootstrap.js"></script>
   <script type="text/javascript" src="/js/dynamic-table.js"></script>


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/bootstrap/outage/blog/jquery.min.js" integrity="sha384-THPy051/pYDQGanwU6poAc/hOdQxjnOEXzbT+OuUAFqNqFjL+4IGLBgCJC3ZOShY" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="/bootstrap/outage/jquery.min.js"><\/script>')</script>
    <script src="/bootstrap/outage/blog/tether.min.js" integrity="sha384-Plbmg8JY28KFelvJVai01l8WyZzrYWG825m+cZ0eDDS1f7d/js6ikvy1+X+guPIB" crossorigin="anonymous"></script>
    <script src="/bootstarp/outage/blog/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="bootstrap/outage/blog/ie10-viewport-bug-workaround.js"></script>
  
<script src="/bootstrap/outage/Dashboard/jquery.min.js" integrity="sha384-THPy051/pYDQGanwU6poAc/hOdQxjnOEXzbT+OuUAFqNqFjL+4IGLBgCJC3ZOShY" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="/bootstrap/outage/jquery.min.js"><\/script>')</script>
    <script src="/bootstrap/outage/Dashboard/tether.min.js" integrity="sha384-Plbmg8JY28KFelvJVai01l8WyZzrYWG825m+cZ0eDDS1f7d/js6ikvy1+X+guPIB" crossorigin="anonymous"></script>
    <script src="/bootstrap/outage/Dashboard/bootstrap.min.js"></script>
    <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
    <script src="/bootstrap/outage/Dashboard/holder.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/bootstrap/outage/Dashboard/ie10-viewport-bug-workaround.js"></script>



		</body>
		"""
