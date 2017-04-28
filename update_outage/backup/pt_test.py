#!/usr/bin/python

print "Content-type: text/html"
print ""

import cgi
import cgitb; cgitb.enable()
import requests, re
import os
import json
import codecs
import re

__author__="vivek.sinha@inmobi.com"


form = cgi.FieldStorage()
comm=form.getvalue('comm')
st=form.getvalue('status')
nxt=form.getvalue('next')

p=os.environ['HTTP_REFERER'].split('/')
m= (p.pop())
k=m.split('.')
h='/var/www/cgi-bin/updated_outage/files/%s.json'%(k[0])

#Updating json issue related files for status and comments

with open(h,'r') as f:
        nq=json.load(f)

if 'Summary' in nq:
        nq['Summary'].append("<ul><li>%s</li></ul>"%(comm))

if 'Status' in nq:
	nq['Status']='%s'%(st)
else:
	nq['Status']='%s'%(st)


with open(h,'w') as f:
        json.dump(nq,f)


# Updating Dashboard status


with  open('/var/www/cgi-bin/details.json','r') as f:
	ds=json.load(f)

ch=ds['Name'].index('%s'%(k[0]))
ds['Status'][ch]=st

with open('/var/www/cgi-bin/details.json','w') as f:
	json.dump(ds,f)


## Updating Status 
with open('/var/www/test/updated_outage/files/%s'%(m)) as f:
	s=f.readlines()

with open('/var/www/test/updated_outage/files/%s'%(m),'w') as hj:
	hj.truncate()


if st=="amber" and 'RED' in s[63]:
        s[63]="<p style='color:orange'><b><u>Status:</u></b>AMBER</p>"
	for i in s:
        	f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()
elif st=="amber" and 'GREEN' in s[63]:
        s[63]="<p style='color:orange'><b><u>Status:</u></b>AMBER</p>"
	for i in s:
        	f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()
elif st=="resolved" and 'RED' in s[63]:
        s[63]="<p style='color:green'><b><u>Status:</u></b>GREEN</p>"
	for i in s:
        	f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()

elif st=="resolved" and 'AMBER' in s[63]:
        s[63]="<p style='color:green'><b><u>Status:</u></b>GREEN</p>"
        for i in s:
		f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()

elif st=="red" and 'AMBER' in s[63]:
        s[63]="<p style='color:red'><b><u>Status:</u></b>RED</p>"
	for i in s:
        	f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()
elif st=="red" and 'GREEN' in s[63]:
        s[63]="<p style='color:red'><b><u>Status:</u></b>RED</p>"
	for i in s:
        	f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()


# Inserting New Comments

l=('/var/www/test/updated_outage/files/%s'%(m))


with open(l,'r') as pt:
	rs=pt.readlines()


regex=re.compile(".*(Next Update).*")

df=[mp.group(0) for lp in rs for mp in [regex.search(lp)] if mp]

x=df[0]+'\n'
num=rs.index(x)

del rs[num:]

rs.append('<ul><li>%s</li></ul>'%(comm))

wk=[]
wk.extend(rs)

j= """ 
        <br/>
        <form action="/cgi-bin/updated_outage/pt_test.py" method="get">
        
         <div class="form-row">
                <label>
                    <span>Status:</span>
                    <select name="status" style="width:100px; margin-left: 35px;">
                        <option value="red">RED</option>
                        <option value="amber">AMBER</option>
                        <option value="resolved">GREEN</option>

                   </select>
               </label>
          </div>

        <br/>
        <div>
        <b>Next Update: </b><input type='text' name='next'>

        </div>
        <br />
        <div>
        <b>Comments: </b><br/>
        <textarea name="comm" style="height:100px; width:320px;" required="required"></textarea>
        </div>
        <div>
       <input type="submit" value="submit" style="margin-top: 50px;background-color: #003366;border-radius:5px;color: white;width: 80px;height:40px;">
        </div>
        </form>

</div>
</body>
"""



# Updating next update time

ib="""
<b>Next Update:</b>%s<br>
"""%(nxt)


with open(l,'w') as pt:
	pt.truncate()

with open(l,'w') as pt:
	for i in rs:
		pt.writelines(i)
	pt.write('\n')
	pt.write(ib)
	pt.write('\n')
	pt.write("<hr style='border-top: 2px solid black;'>")
        pt.write('\n')
        pt.write("<h4><center><u> Enter New Updates </u></center></h4>")
        pt.write('\n')
	pt.write(j)

send_btn = """
	<form action="/cgi-bin/updated_outage/pt_mails.py" method="get">
<input type="submit" value="Send Update" style="margin-top: 50px;background-color: #003366;border-radius:5px;color: white;width: 100px;height:40px;">
	</form>
"""


with open('/var/www/test/updated_outage/files/%s_update.html'%(k[0]),'w') as hj:
	for i in wk:
		hj.writelines(i)
	hj.write('\n')
	hj.write(ib)
	hj.write('\n')
	hj.write(send_btn)




print """

<!DOCTYPE html>
<!-- saved from url=(0047)http://v4-alpha.getbootstrap.com/examples/blog/ -->
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
	<link type="text/css" rel="stylesheet" href="/css/press.css">

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
          <a class="nav-link" href="http://localhost:82/test/updated_outage/jira_create.html">Create Jira</a>
          <a class="nav-link" href="http://localhost:82/test/updated_outage/slack_channel.html">Create Slack </a>
            <form class="navbar-form navbar-right" role="search">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search" name="q">
		</div>
		</div>
		</form>
	</div>
        </nav>
	</div>
    </div>

<div class="container">
	<div class="wrapper">

<br>

<div id="button">
<a href="http://localhost:82/test/updated_outage/files/%s_update.html" class="button-3d">View Update</a>
</div>
   <script src="js/jquery-1.8.3.min.js"></script>
   <script type="text/javascript" src="js/jquery.dataTables.js"></script>
   <script type="text/javascript" src="js/DT_bootstrap.js"></script>
   <script src="js/dynamic-table.js"></script>



    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/css/blog/jquery.min.js" integrity="sha384-THPy051/pYDQGanwU6poAc/hOdQxjnOEXzbT+OuUAFqNqFjL+4IGLBgCJC3ZOShY" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="/css/Dashboard/jquery.min.js"><\/script>')</script>
    <script src="/css/blog/tether.min.js" integrity="sha384-Plbmg8JY28KFelvJVai01l8WyZzrYWG825m+cZ0eDDS1f7d/js6ikvy1+X+guPIB" crossorigin="anonymous"></script>
    <script src="/css/blog/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/css/blog/ie10-viewport-bug-workaround.js"></script>
  
<script src="/css/Dashboard/jquery.min.js" integrity="sha384-THPy051/pYDQGanwU6poAc/hOdQxjnOEXzbT+OuUAFqNqFjL+4IGLBgCJC3ZOShY" crossorigin="anonymous"></script>
    <script>window.jQuery || document.write('<script src="/css/Dashboard/jquery.min.js"><\/script>')</script>
    <script src="/css/Dashboard/tether.min.js" integrity="sha384-Plbmg8JY28KFelvJVai01l8WyZzrYWG825m+cZ0eDDS1f7d/js6ikvy1+X+guPIB" crossorigin="anonymous"></script>
    <script src="/css/Dashboard/bootstrap.min.js"></script>
    <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
    <script src="/css/Dashboard/holder.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="/css/Dashboard/ie10-viewport-bug-workaround.js"></script>

</body>
</html>


"""%(k[0])

