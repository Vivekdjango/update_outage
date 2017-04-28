#!/usr/bin/python

print "Context-Type: text/html"
print ""

from jira.client import JIRA


def jira_create():
	jira = JIRA('http://jira.corp.inmobi.com',basic_auth=('vivek.sinha','Inmobi@123'))
	root_dict={
          'project':{'key':'NOC'},
          'issuetype':{'name':'Epic'},
           'customfield_11601':'test',
	   'summary':'test',
           'description':'test',
           'components':[{'name': 'NOC'},],    
	}

	my_issue=jira.create_issue(fields=root_dict)
	return my_issue.key

jira_create()
