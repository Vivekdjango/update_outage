#!/usr/bin/python
print ("Content-type: text/html")
print ("")

import cgi

#from urllib.request import urlopen
import urllib2
import json
import types

print ("""
<link type="text/css" rel="stylesheet" href="/css/s1.css">
<link href="https://fonts.googleapis.com/css?family=Oleo+Script" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
<link  type="text/css" href="/css/bootstrap.min.css" rel="stylesheet" />
<link type="text/css" href="/datatable/datatables.min.css" rel="stylesheet">
<script src="/datatable/datatables.min.js"></script>

<meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="http://getbootstrap.com/favicon.ico">

    <title>Infra Harware Info</title>

    <!-- Bootstrap core CSS -->
    <link href="/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <!-- Bootstrap theme -->
    <link href="/bootstrap/css/bootstrap-theme.min.css" rel="stylesheet">
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="./search_files/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/bootstrap/css/theme.css" rel="stylesheet">

    <script src="./search_files/ie-emulation-modes-warning.js"></script>


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

h4
{
	font-family: 'Oleo Script', cursive;
	font-size:25px;
}

p{
	font-size:20px;
	display: inline-block;
}


</style>
""")

print ("</head>")



print """

    <!-- Fixed navbar -->
    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="http://localhost:82/bootstrap/search.html">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container theme-showcase" role="main">


"""

print "<body>"


form=cgi.FieldStorage()

itag=form.getvalue('itag')

url="http://ims.corp.inmobi.com/api/search/?itag=%s&filter=itag,hostname,discovered_data"%(itag)

d=urllib2.urlopen(url).read().decode('utf-8')
f=json.loads(d)

j=0

if f['result'][0]['discovered_data'] is None:
	print ("<h3>No Data Found</h3>")
else:
	l=f['result'][0]['discovered_data']['network']['interfaces'][0]


	print  "<h4 style='display: inline-block;margin-top: 80px;'><b><u>Hostname :</u></b></h4>",'<p>%s</p>'%(f['result'][0]['discovered_data']['hostname'])

	print "<br />"

	if 'firmware_version' in l.keys():
		print "<h4 style='display: inline-block;'><u>Firmware Version :</u></h4>",'<p>%s</p>'%(l['firmware_version'])
	else:
		print "<h4>Firnmware Details not found</h4>"

	print "<br />"



	print ('<h4><u>Chassis Details :</u></h4>')

        q=f['result'][0]['discovered_data']['chassis']

        print "<b></u>Serial Number :</u></b>",'<p>%s</p>'%(q['serial'])
	print "<br/>"
        print "<b><u>Model :</b></u>",'<p>%s</p>'%(q['model'])

	print "<br />"

	t=f['result'][0]['discovered_data']['host_type']

	print ("<h4 style='display: inline-block;'><u>Host Type :</u></h4>"),'<p>%s</p>'%(t['type'].capitalize())


	p=f['result'][0]['discovered_data']['storage']['physical_drives']

	print ("""
	<table class="table table-responsive table-hover" id="sample_1">
	     <caption><h4><u>Drive Details:</u></h4></caption>
              <thead style="background-color: #003366;">
              <tr class="clickable" data-toggle="collapse" id="row1" data-target=".row1"  style="color: white;">
                  <th><i class="glyphicon glyphicon-plus"></i></th>
                  <th>Slot Nunber</th>
                  <th>Device-Type</th>
                  <th>Size (in GB)</th>
		<th>Faulty Disk</th>
              </tr>
              </thead>
              <tbody>

	""")

	for i in range(len(p)):

		print ("""
						<tr  class="collapse row1" >    
								  <td></td>	
                                                                  <td>{0}</td>
                                                                  <td >{1}</td>                   
  								  <td>{2}</td>
								  <td>{3}</td>
                                                </tr>

                        """).format(p[i]['device_id'],p[i]['media_type'],p[i]['size']/(10**9),p[i]['smart_alert'])

	print '<br />'


	raid=f['result'][0]['discovered_data']['raid']['adapters'][0]['virtual_disks']

        print ("""
        <table class="table table-responsive table-hover" id="sample_1">
             <caption><h4><u>RAID Details:</u></h4></caption>
              <thead style="background-color: #003366;">
              <tr class="clickable" data-toggle="collapse" id="row5" data-target=".row5"  style="color: white;">
                  <th><i class="glyphicon glyphicon-plus"></i></th>
                  <th>ID</th>
                  <th>Number of PD</th>
                  <th>Size</th>
              </tr>
              </thead>
              <tbody>

        """)

        for i in range(len(raid)):

                print ("""
                                                <tr  class="collapse row5" >    
                                                                  <td></td>     
                                                                  <td>{0}</td>
                                                                  <td >{1}</td>                   
                                                                  <td>{2}</td>
                                                </tr>

                        """).format(raid[i]['id'],len(raid[i]['physical_drives']),raid[i]['size_verbose'])

	print '<br />'


	if 'units'  not in f['result'][0]['discovered_data']['memory'].keys():
		print "<h4 style='display: inline-block;'><u>Memory Details:</u></h4>",'<p>%s</p>'%(f['result'][0]['discovered_data']['memory']['size']/10**9)+' gb'

	else:
		w=f['result'][0]['discovered_data']['memory']['units'][0]['banks']

		unuse=[]

		print ("<br />")

		print ("""
        	<table class="table table-responsive table-hover" id="sample_1">
	     	<caption><h4><u>Memory Details:</u></h4></caption>
              	<thead style="background-color: #003366;">
              	<tr class="clickable" data-toggle="collapse" id="row2" data-target=".row2" style="color: white;">
                <th><i class="glyphicon glyphicon-plus"></i></th>
		  <th>Slot Nunber</th>
                  <th>Size</th>
                  <th>Type</th>
              </tr>
              </thead>
              <tbody>

        	""")

		for i in range(len(w)):
			if 'size_verbose' in w[i].keys():
				print ("""             <tr class="collapse row2">    
                                                                   <td></td>     
                                                                  <td>{0}</td>
                                                                  <td >{1}</td>                   
                                                                  <td>{2}</td>
                                	                </tr>

                        	""").format(w[i]['slot'],w[i]['size_verbose'],w[i]['type'])
			elif 'type' in w[i].keys():
                		unuse.append((w[i]['slot'],w[i]['type']))
        		else:
                		unuse.append((w[i]['slot'],'Information Not Available'))


		print ("""
        		<table class="table table-responsive table-hover" id="sample_1">
             		<caption><h4><u>Available Slots:</u></h4></caption>
              		<thead style="background-color: #003366;">
              		<tr class="clickable" data-toggle="collapse" id="row3" data-target=".row3" style="color: white;">
			<th><i class="glyphicon glyphicon-plus"></i></th>
                  	<th>Slot Nunber</th>
                  	<th>Type</th>
             	 </tr>
              	</thead>
              	<tbody>

        		""")

		for i in range(len(unuse)-1):

			print ("""             <tr class="collapse row3">    
                                                                   <td></td>     
                                                                  <td>{0}</td>
                                                                  <td >{1}</td>                   
                                                        </tr>

                         """).format(unuse[i][0],unuse[i][1])


	
	if 'disks' not in f['result'][0]['discovered_data']['storage'].keys():
	
		print "<h4>Disk Details not found</h4>"
	else:

		disk=f['result'][0]['discovered_data']['storage']['disks'][0]['volumes']
		
		print ("""
                        	<table class="table table-responsive table-hover" id="sample_1">
                        	<caption><h4><u>Disk Details:</u></h4></caption>
                        	<thead style="background-color: #003366;">
                        	<tr class="clickable" data-toggle="collapse" id="row4" data-target=".row4" style="color: white;">
				<th><i class="glyphicon glyphicon-plus"></i></th>
                        	<th>Logical Name</th>
                        	<th>Size</th>
                 	</tr>
                	</thead>
                	<tbody>

                       	""")


		for i in range(len(disk)-1):
		
			print ("""      <tr class="collapse row4">    
                                                    <td></td>                    
                                                   <td>{0}</td>
                                                   <td >{1}</td>                   
                                            </tr>

                  	""").format(disk[i]['logicalname'],disk[i]['size'])
		


print ("""
</tbody>
</table>
</div>

   <script type="text/javascript" src="/js/jquery-1.8.3.min.js"></script>
   <script type="text/javascript" src="/js/jquery.dataTables.js"></script>
   <script type="text/javascript" src="/js/DT_bootstrap.js"></script>
   <script type="text/javascript" src="/js/dynamic-table.js"></script>



</body>""")

