# -*- coding: UTF-8 -*-
import requests
import re



def fcic(url):
  #print('hello');
  headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
  'Referer':url};
  data = {'key':'value'};
  #files= {"files":open("test.jpg","rb")}

  #proxies = {    "http": "http://user:password@127.0.0.1:9743/",  }
  #requests.get("http://httpbin.org/get", timeout=0.5)
  
  
  r = requests.post(url, data);
  r.encoding='utf-8';
  #r.status_code
  #r.encoding
  #r.content
  #r.headers
  #r.json()
  #r.raw
  # r.cookies['example_cookie_name']
  return r.text; #str(r.content,'utf-8');

def match(regex,str):
  return re.search(regex , str, re.M|re.I)

# print(fcic("https://www.cnblogs.com"));

regex="<a(.*?)</a>";
matchObj=match(regex,fcic("https://www.cnblogs.com"));  #re.match(regex, str, re.M|re.I);
if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
  #  print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"
