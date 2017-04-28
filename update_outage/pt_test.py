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
import datetime


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

# Status
ch=ds['Name'].index('%s'%(k[0]))
ds['Status'][ch]=st

#DashBoard Downtime
pe=ds['Time'][ch].split()
dt=datetime.datetime.now().strftime('%H:%M')
FMT='%H:%M'
df=datetime.datetime.strptime(dt,FMT)-datetime.datetime.strptime(pe[0],FMT)
gh=df.seconds/60

ds['Downtime'][ch]=gh


with open('/var/www/cgi-bin/details.json','w') as f:
	json.dump(ds,f)


# Downtime calculation:

ot=open('/var/www/test/updated_outage/files/%s'%(m),'r')
bt=ot.read()
pt=re.search(r'Time(.*)',bt)
qt=re.search(r'\d+(.*)',pt.group())
mt=qt.group().split()
nt=mt[0]


dt=datetime.datetime.now().strftime('%H:%M')
FMT='%H:%M'

df=datetime.datetime.strptime(dt,FMT)-datetime.datetime.strptime(nt,FMT)
jt=df.seconds/60


with open('/var/www/test/updated_outage/files/%s'%(m),'r+') as fn:
        sn=fn.read()
        dn=re.search(r'Downtime</b>:([0-9]+)',sn)
        jn='Downtime</b>:%d'%(jt)
        xn=dn.group()
        sn=re.sub(xn,jn,sn)
        fn.seek(0)
        fn.truncate()

with open('/var/www/test/updated_outage/files/%s'%(m),'a') as gn:
        gn.write(sn)
        gn.close()



## Updating Status 
#with open('/var/www/test/updated_outage/files/%s'%(m)) as f:
#	s=f.readlines()

#with open('/var/www/test/updated_outage/files/%s'%(m),'w') as hj:
#	hj.truncate()

s=open("/var/www/test/updated_outage/files/%s"%(m)).read()
z=re.search('style(.*)',s)
x=z.group()


if st=="amber" and x=="style='color:red'><b><u>Status:</u></b>RED</p>":
        s=s.replace(x,"style='color:orange'><b><u>Status:</u></b>AMBER</p>")
        f=open("/var/www/test/updated_outage/files/%s"%(m),'w')
        f.write(s)
        f.close()
elif st=="amber" and x=="style='color:green'><b><u>Status:</u></b>GREEN</p>":
        s=s.replace(x,"style='color:orange'><b><u>Status:</u></b>AMBER</p>")
        f=open("/var/www/test/updated_outage/files/%s"%(m),'w')
        f.write(s)
        f.close()
elif st=="green" and x=="style='color:red'><b><u>Status:</u></b>RED</p>":
        s=s.replace(x,"style='color:green'><b><u>Status:</u></b>GREEN</p>")
        f=open("/var/www/test/updated_outage/files/%s"%(m),'w')
        f.write(s)
        f.close()

elif st=="green" and x=="style='color:orange'><b><u>Status:</u></b>AMBER</p>":
        s=s.replace(x,"style='color:green'><b><u>Status:</u></b>GREEN</p>")
        f=open("/var/www/test/updated_outage/files/%s"%(m),'w')
        f.write(s)
        f.close()

elif st=="red" and x=="style='color:orange'><b><u>Status:</u></b>AMBER</p>":
        s=s.replace(x,"style='color:red'><b><u>Status:</u></b>RED</p>")
        f=open("/var/www/test/updated_outage/files/%s"%(m),'w')
        f.write(s)
        f.close()
elif st=="red" and x=="style='color:green'><b><u>Status:</u></b>GREEN</p>":
        s=s.replace(x,"style='color:red'><b><u>Status:</u></b>RED</p>")
        f=open("/var/www/test/updated_outage/files/%s"%(m),'w')
        f.write(s)
        f.close()


'''
if st=="amber" and 'RED' in s[121]:
        s[121]="<p style='color:orange'><b>Status:</b>AMBER</p>"
	for i in s:
        	f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()
elif st=="amber" and 'GREEN' in s[121]:
        s[121]="<p style='color:orange'><b>Status:</b>AMBER</p>"
	for i in s:
        	f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()
elif st=="green" and 'RED' in s[121]:
        s[121]="<p style='color:green'><b>Status:</b>GREEN</p>"
	for i in s:
        	f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()

elif st=="green" and 'AMBER' in s[121]:
        s[121]="<p style='color:green'><b>Status:</b>GREEN</p>"
        for i in s:
		f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()

elif st=="red" and 'AMBER' in s[121]:
        s[121]="<p style='color:red'><b>Status:</b>RED</p>"
	for i in s:
        	f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()
elif st=="red" and 'GREEN' in s[121]:
        s[121]="<p style='color:red'><b>Status:</b>RED</p>"
	for i in s:
        	f=open("/var/www/test/updated_outage/files/%s"%(m),'a')
        	f.write(i)
        	f.close()

'''
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
                        <option value="green">GREEN</option>

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
</body>
</html>
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
<!-- saved from url=(0053)http://v4-alpha.getbootstrap.com/examples/dashboard/# -->
<html lang="en" class="gr__v4-alpha_getbootstrap_com"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="Outage Tool">
    <meta name="author" content="Vivek Sinha">

    <title>NOC Outage Tool </title>

<!--New-->

<link href="/css/new/bootstrap.min.css" rel="stylesheet">   
<script src="/css/new/jquery.min.js"></script>
<link rel="stylesheet" 
href="/css/new/jquery.dataTables.min.css"></style>
<script type="text/javascript" 
src="/css/new/jquery.dataTables.min.js"></script>
<script type="text/javascript" 
src="/css/new/bootstrap.min.js"></script>
<link type="text/css" rel="stylesheet" href="/css/press.css">

<style>
.sidebar{

	background-color:black;
	padding-bottom: 100%;
}
a{
color:white;
margin-left:0px;
}
a.hover{
	color:white;
}
li
{
	margin-top:7px;
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
.nb{
	margin-top:70px;
}
.dataTables_wrapper .dataTables_length {
float: right;
}
.dataTables_wrapper .dataTables_filter {
float: left;
text-align: left;
border-radius:12px solid #dbdbdb;
}
.hover{
	background-color:blue;	
}
</style>
 </head>

  <body data-gr-c-s-loaded="true">


<div class="container-fluid">
      <div class="row">
        <div class="col-sm-3 col-md-2 sidebar">
          <ul class="nav nav-sidebar content">
	    <li><a href="#"><img style="width:100%;height: 60px;" src="/css/new/images1.png"></a></li>	
            <li class="active" style="margin-top: 5px;"><a href="http://localhost:82/cgi-bin/updated_outage/new.py">Dashboard <span class="sr-only">(current)</span></a></li>
            <li><a href="http://localhost:82/cgi-bin/updated_outage/new.py">Home</a></li>
            <li><a href="http://localhost:82/test/updated_outage/button.html">Outage Action</a></li>
            <li><a href="http://localhost:82/test/updated_outage/jira_create.html">Jira Action</a></li>
          </ul>
        </div>
	
        <div class="col-sm-9 offset-sm-3 col-md-10 offset-md-2 main">

"""
print"""        
	<div class="container">
        <div class="wrapper">
               <div id="button">
		<a href="http://localhost:82/test/updated_outage/files/%s_update.html" class="button-3d">View Update</a>
		</div>
	</div>
      </div>
    </div>"""%(k[0])

print """
<script>
$(document).ready(function(){
    $('#myTable').dataTable();
});
</script>

</body></html>"""

