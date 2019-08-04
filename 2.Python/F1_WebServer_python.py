# python2
# python -m SimpleHTTPServer 8000

# python3
# python3 -m http.server 8000          //get
# python3 -m http.server --cgi 8000    //post


import cgi,cgitb
form1=cgi.FieldStorage()
name=form1.getvalue('name')
 
print ('Content-type:text/html \n\n')
print ('Hello'+name)