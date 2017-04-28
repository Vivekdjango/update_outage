#!/usr/bin/python

print ("Content-type: text/html")
print ("")

import cgi
import json
import urllib2


form=cgi.FieldStorage()
colo=form.getvalue('colo')


url="http://ims.corp.inmobi.com/api/search/?itag=.*%s.*&filter=itag,hostname,discovered_data"%(colo)

d=urllib2.urlopen(url).read().decode('utf-8')
f=json.loads(d)


data=f['result']

print " <head>"
print """
<link href="https://fonts.googleapis.com/css?family=Oleo+Script" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
<link href="https://cdn.datatables.net/1.10.12/css/jquery.dataTables.min.css" rel="stylesheet">
<link href="https://cdn.datatables.net/buttons/1.2.2/css/buttons.dataTables.min.css" rel="stylesheet">

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
    <link href="/bootstrap/search_files/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="/bootstrap/css/bootstrap-theme.css" rel="stylesheet">

    <script src="/bootstrap/search_files/ie-emulation-modes-warning.js"></script>

"""

print "</head>"

print """
	<body>
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
            <li class="active"><a href="http://localhost:82/bootstrap/search.html">Search</a></li>
            <li><a href="http://localhost:82/bootstrap/info.html"">Export DC Info</a></li>
            <li><a href="#">About</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container theme-showcase" role="main">


"""



print ("""
	<div style="clear: both;margin-top: 100px;">
	<table class="table table-bordered" id="sample_1">
	     <caption><h3><u><center>Drive Details (per colo):</center></u></h3></caption>
              <thead style="background-color: #003366;">
              <tr style="color: white;">
		  <th>S. No</th>
		  <th>ITAG</th>
		 <th>Hostname</th>
                  <th>Drive details</th>
              </tr>
              </thead>
              <tbody>

	""")

for i in range(len(data)):
	if 'discovered_data' not in data[i] or data[i]['discovered_data'] is None or 'physical_drives' not in data[i]['discovered_data']['storage']:
		c='None'

	else:
		c=data[i]['discovered_data']['storage']['physical_drives']

	print ("""
                                                <tr>    
                                                                  <td>{0}</td>
                                                                  <td >{1}</td>                   
                                                                  <td>{2}</td>
								  <td>{3}</td>
                                                </tr>

             """).format(i,data[i]['itag'],data[i]['hostname'],c)



'''
for i in range(len(data)):
	if 'discovered_data' not in data[i] or data[i]['discovered_data'] is None or 'physical_drives' not in data[i]['discovered_data']['storage']:
		print ("""
						<tr>    
                                                                  <td>{0}</td>
                                                                  <td >{1}</td>                   
  								  <td>{2}</td>
                                                </tr>

                        	""").format(i,data[i]['itag'],data[i]['hostname'])
	else:
		print ("""
                                                <tr>    
                                                                  <td>{0}</td>
                                                                  <td >{1}</td>                   
                                                                  <td>{2}</td>
                                                                  <td>{3}</td>
                                                </tr>

                        """).format(i,data[i]['itag'],data[i]['hostname'],data[i]['discovered_data']['storage']['physical_drives'])

	print '<br />'

'''
print ("""
</div>
</tbody>
</table>
</div>




<script type="text/javascript" src="//code.jquery.com/jquery-1.12.3.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/1.10.12/js/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="https://cdn.datatables.net/buttons/1.2.2/js/dataTables.buttons.min.js"></script>
<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/jszip/2.5.0/jszip.min.js"></script>
<script type="text/javascript" src="//cdn.rawgit.com/bpampuch/pdfmake/0.1.18/build/pdfmake.min.js"></script>
<script type="text/javascript" src="//cdn.rawgit.com/bpampuch/pdfmake/0.1.18/build/vfs_fonts.js"></script>
<script type="text/javascript" src="//cdn.datatables.net/buttons/1.2.2/js/buttons.html5.min.js"></script>
<script type="text/javascript" src="/js/new.js"></script>

</body>""")


