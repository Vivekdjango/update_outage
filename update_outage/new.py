#!/usr/bin/python
print "Content-type: text/html"
print ""


import json
import cgi


import os

__author__="vivek.sinha@inmobi.com"

os.chdir('/var/www/cgi-bin')
p=os.getcwd()

with open('details.json','r') as f:
        d=json.load(f)


g=d['Status']


emp={'Red':0,'amber':0,'green':0}
for i in emp.keys():
	if i in g:
		emp[i]=g.count(i)

print """

<!DOCTYPE html>
<!-- saved from url=(0053)http://v4-alpha.getbootstrap.com/examples/dashboard/# -->
<html lang="en" class="gr__v4-alpha_getbootstrap_com"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="Outage Tool">
    <meta name="author" content="Vivek Sinha">

    <title>NOC Outage Tool</title>


<link href="/css/new/bootstrap.min.css" rel="stylesheet">   
<script src="/css/new/jquery.min.js"></script>
<link rel="stylesheet" 
href="/css/new/jquery.dataTables.min.css"></style>
<script type="text/javascript" 
src="/css/new/jquery.dataTables.min.js"></script>
<script type="text/javascript" 
src="/css/new/bootstrap.min.js"></script>

<style>
.sidebar{

	background-color:black;
	padding-bottom: 80%;
}
.sidebar a{
	color:white;
	margin-left:0px;
	text-align:left;

}
.sidebar ul  a:hover{
	background-color: black;
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
.btn-group{
	margin-top:50px;
}

.btn-group .btn {
	padding-right: 30px;
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


<div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar nav-sidebar-fixed affix">
          <ul class="nav nav-sidebar-fixed content text-uppercase">
	<li><a href="#"><img style="width:100%;height: 60px;margin-left: 0px;" src="/css/new/images1.png"></a></li>	
            <li class="active" style="margin-top: 5px;"><a href="http://localhost:82/cgi-bin/updated_outage/new.py">Dashboard <span class="sr-only">(current)</span></a></li>
            <li><a href="http://localhost:82/cgi-bin/updated_outage/new.py">Home</a></li>
            <li><a href="http://localhost:82/test/updated_outage/button.html">Outage Action</a></li>
            <li><a href="http://localhost:82/test/updated_outage/jira_create.html">Jira Action</a></li>
          </ul>
        </div>
	


        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">
	<h3 style="color: blue;"><center><u>NOC Outage Dashboard</u></center></h3>

	 	
	<div class="btn-group">	
"""
print """
	<button type="button" class="btn btn-danger" style="width:%dpx; height: 50px;margin-right: -5px;"><span class="badge">%d</span></button>
"""%(emp['Red']*40,emp['Red'])

print """
	<button type="button" class="btn btn-warning" style="width:%dpx;height: 50px;margin-right: -5px;"><span class="badge">%d</span></button>
"""%(emp['amber']*20,emp['amber'])

print"""	
	<button type="button" class="btn btn-success" style="width:%dpx; height:50px;"><span class="badge">%d</span></button>
	</div>"""%(emp['green']*20,emp['green'])

print """
          <div class="table-responsive">
	<table id="myTable" class="table table-bordered table-condensed" width="100%" >
	<thead  style="background-color: #003366;">
              <tr style="color: white;padding: 4px;">

                  <th>Issue Title</th>
                  <th>Sevirity</th>
                  <th>Status</th>
                  <th>Jira</th>
                  <th>Slack</th>
		<th>Outage Creation Time</th>
		<th>Downtime (in minutes)</th>
              </tr>
		</thead>
		<tbody style="background-color: white;">


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
								<td>{9}</td>
								<td>{10}</td>
                                                </tr>
 

		""".format(d['Name'][i],d['Name'][i],d['Severity'][i],dic[g[i]],g[i].upper(),d['Jira'][i],d['Jira'][i],d['Slack'][i],d['Slack'][i],d['Time'][i],d['Downtime'][i],)
		s+=1
print """
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>

    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->

<script>
$(document).ready(function(){
    $('#myTable').dataTable();
});
</script>

</body></html>
"""
