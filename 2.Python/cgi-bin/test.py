#!/usr/bin/python3
# -*- coding: utf-8 -*-　　

import cgi,cgitb
form1=cgi.FieldStorage()
name=form1.getvalue('name')
 
print ('Content-type:text/html \n\n')
print ('Hello'+name)
