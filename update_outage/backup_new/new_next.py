#!/usr/bin/python
print "Content-type: text/html"
print ""


import json
import cgi


import os

print """
<!DOCTYPE html>
<!-- saved from url=(0053)http://v4-alpha.getbootstrap.com/examples/dashboard/# -->
<html lang="en" class="gr__v4-alpha_getbootstrap_com"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Dashboard Template for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="/css/Dashboard/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/css/Dashboard/dashboard.css" rel="stylesheet">


	<style>
.sidebar{

	background-color:black;
}
.nav-sidebar a{
color:white;
margin-left:0px;
}
.nav-sidebar li
{
	margin-top:7px;
}
.nav-sidebar{
	margin-top:0px;
}
.navbar {
	background-color:white;
	background-image:none;
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
	margin-top:5px;
	text-align:left;
}
.navbar .navbar-fixed-top .bg-inverse{
        background-color:white;
        background-image:none;
}
button{
	margin-top: 0px;
}

</style>
 
 </head>

  <body data-gr-c-s-loaded="true">

    
  <nav class="navbar  navbar-fixed-top navbar-default">
<a class="navbar-brand" href="#">NOC Outage Tool</a>
<!--	 <h3 class="navbar-text" style="color: blue;margin-left: 350px;">Outage Dashboard</h3>-->
        <div id="navbar" class="navbar-collapse collapse">
        </div>
        <form class="float-xs-right">
          <input type="text" class="form-control" placeholder="Search...">
        </form>
    </nav>

<hr> 

<div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar">
            <li class="active"><a href="#">DashBoard <span class="sr-only">(current)</span></a></li>
            <li><a href="#">Home</a></li>
            <li><a href="#">Outage Action</a></li>
            <li><a href="#">Jira Action</a></li>
          </ul>
        </div>
        <div class="col-sm-9 offset-sm-3 col-md-10 offset-md-2 main">

	<div class="nb">
	 <button type="button" class="btn btn-danger" style="width:50px; height: 40px;margin-right:-5px;"></button>
        <button type="button" class="btn btn-warning" style="width:100px;height: 40px;margin-right: -5px;"></button>
        <button type="button" class="btn btn-success" style="width:120px; height:40px;"></button>



          <div class="table-responsive">
        <table  class="table table-bordered table-hover text-centered" id="sample_1">      
	<thead  style="background-color: #003366;">
              <tr style="color: white;padding: 4px;">

                  <th style="width:340px;">Issue Title</th>
                  <th>Sevirity</th>
                  <th>Status</th>
                  <th>Jira</th>
                  <th>Slack</th>
		<th>OC Time</th>
		<th>Downtime</th>
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
                                                                  <td><a href="/test/updated_outage/files/{0}.html" name='name' target="_blank">{1}</a></td>
                                                                  <td>{2}</td>
                                                                  <td style="font-size: 17px;color: {3};">{4}</td>                                                                  <td><a href="https://jira.corp.inmobi.com:8443/browse/{5}" target="_blank">{6}</a></td>
                                                                  <td><a href="https://inmobi.slack.com/messages/{7}" target="_blank">{8}</a></td>
                                                </tr>
 

		""".format(d['Name'][i],d['Name'][i],d['Severity'][i],dic[g[i]],g[i].upper(),d['Jira'][i],d['Jira'][i],d['Slack'][i],d['Slack'][i],)
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

 <script src="Dashboard/jquery.min.js" integrity="sha384-THPy051/pYDQGanwU6poAc/hOdQxjnOEXzbT+OuUAFqNqFjL+4IGLBgCJC3ZOShY" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="Dashboard/tether.min.js" integrity="sha384-Plbmg8JY28KFelvJVai01l8WyZzrYWG825m+cZ0eDDS1f7d/js6ikvy1+X+guPIB" crossorigin="anonymous"></script>
    <script src="Dashboard/bootstrap.min.js"></script>
    <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
    <script src="Dashboard/holder.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="Dashboard/ie10-viewport-bug-workaround.js"></script>

<script src="da.js"></script>



</body></html>
"""
