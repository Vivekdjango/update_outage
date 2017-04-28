#!/usr/bin/python

print "Context-Type: text/html"
print ""

from jira.client import JIRA
import cgi, cgitb

__author__="vivek.sinha@inmobi.com"


form=cgi.FieldStorage()
sub=form.getvalue('sub')
comm=form.getvalue('comm')

def jira_create():
	jira = JIRA('http://jira.corp.inmobi.com',basic_auth=('vivek.sinha','Inmobi@123'))
	root_dict={
          'project':{'key':'NOC'},
          'issuetype':{'name':'Epic'},
	  'customfield_11311':{'value':'S1'},
           'customfield_11601':'%s'%(sub),
	   'summary':'%s'%(sub),
           'description':'%s'%(comm),
           'components':[{'name': 'NOC'},],    
	}

	my_issue=jira.create_issue(fields=root_dict)
	print "<b>Jira ticket ID:</b>%s"%(my_issue.key)

jira_create()
print "<br/>"
print "<br />"
print "Jira Ticket created successfully"
print "<br />"
print """
<a href ='http://localhost:82/cgi-bin/updated_outage/new.py'>Back to home....</a>

"""
