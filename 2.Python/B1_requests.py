#get, post url and response html
import requests

def Gethtml(url):
  #print('hello');
  headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
  'Referer':url};

  #ParaGet = {'key':'value'};
  #r = requests.post(url, ParaGet);
  #files= {"files":open("test.jpg","rb")}

  #proxies = {    "http": "http://user:password@127.0.0.1:9743/",  }
  #requests.get("http://httpbin.org/get", timeout=0.5)

  r = requests.get(url,headers=headers);

  #r.status_code
  #r.encoding
  #r.content
  #r.headers
  #r.json()
  #r.raw
  # r.cookies['example_cookie_name']
  return r.text;

def Posthtml(url):
  #print('hello');
  headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
  'Referer':url};

  #ParaGet = {'key':'value'};
  #r = requests.post(url, ParaGet);
  #files= {"files":open("test.jpg","rb")}

  #proxies = {    "http": "http://user:password@127.0.0.1:9743/",  }
  #requests.get("http://httpbin.org/get", timeout=0.5)

  r = requests.post(url,headers=headers);

  #r.status_code
  #r.encoding
  #r.content
  #r.headers
  #r.json()
  #r.raw
  # r.cookies['example_cookie_name']
  return r.text;

def readCookie():
  response = requests.get('https://www.baidu.com')
  print(response.cookies)
  for key,value in response.cookies.items():
    print(key,'==',value)

#fcic();
#print(Gethtml('http://www.example.com'));

#print(readCookie());
#readCookie();

