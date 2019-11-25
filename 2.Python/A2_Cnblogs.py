# import B1_requests
from lxml import etree
import requests

#fcic
#1. no  No.21 row
#2. page 2  coming is page 1

i=1


def getData(url,id):
    global i
    # global rows
    # rows.clear()
    row=[]
    rows=[]
    #html = B1_requests.Gethtml('http://www.example.com')
    html = Posthtml(url,id)#B1_requests.Gethtml(url)
    #print(html)
    #res= etree.HTML(html).xpath('/html/body/div[1]/p[2]/a/text()')
    #row = []
    
    obj = etree.HTML(html).xpath('/html/body/div')
    #print(obj)
    # i=1
    for r in obj:
        row = [ str(i),
        r.xpath('div[2]/h3/a/text()')[0].replace('\r\n','') ,
            r.xpath('div[2]/div/a/text()')[0].replace('\r\n','') , 
               # r.xpath('div[2]/div/text()')[0].replace('\r\n','') , 
                    r.xpath('div[2]/div/span[1]/a/text()')[0].replace('\r\n','').replace('评论(','').replace(')','') , 
                        r.xpath('div[2]/div/span[2]/a/text()')[0].replace('\r\n','').replace('阅读(','').replace(')','') ,
                            r.xpath('div[2]/h3/a/@href')[0].replace('\r\n','') ,
                            r.xpath('div[2]/p/text()')[0].replace('\r\n','') ]
        rows.append('\t'.join(row))
        i+=1
        #new version

#title: 
# /html/body/div[1]/div[2]/h3/a
#author: 
# /html/body/div[1]/div[2]/div/a
#content: 
# /html/body/div[1]/div[2]/p/text()
#comment: 
# /html/body/div[1]/div[2]/div/span[1]/a
#view: 
# /html/body/div[1]/div[2]/div/span[2]/a
#datetime: 
# /html/body/div[1]/div[2]/div/text()
#recommand: 
# //*[@id="digg_count_11254208"]

        #rows.append(row)
        #rows.append('123')
        #print(','.join(row))
    #print(rows)
    return rows

def Posthtml(url,id):
  #print('hello');

  headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/75.0.3770.90 Chrome/75.0.3770.90 Safari/537.36',
  'Referer':'https://www.cnblogs.com/',
   'CategoryType':'SiteHome','ParentCategoryId':0,'CategoryId':808,'PageIndex':id,'TotalPostCount':4000,'ItemListActionName':'PostList'};
  #ParaGet = {'key':'value'};
  #r = requests.post(url, ParaGet);
  #files= {"files":open("test.jpg","rb")}
  #ParaGet = {'CategoryType':'SiteHome','ParentCategoryId':0,'CategoryId':808,'PageIndex':2,'TotalPostCount':4000,'ItemListActionName':'PostList'};
  #proxies = {    "http": "http://user:password@127.0.0.1:9743/",  }
  #requests.get("http://httpbin.org/get", timeout=0.5)

  r = requests.post(url,headers);

  #r.status_code
  #r.encoding
  #r.content
  #r.headers
  #r.json()
  #r.raw
  # r.cookies['example_cookie_name']
  return r.text;


#getData('https://www.cnblogs.com/','//*[@id="post_list"]/div/div[2]/h3/a/text()')

def write2(file,content):  
    f=open(file,'a')
    f.write(content)
    f.close()

def read(file):
    f=open(file,'r')
    return f.read() 

 
#print( Posthtml('https://www.cnblogs.com/mvc/AggSite/PostList.aspx'))

#print(getData('https://www.cnblogs.com/mvc/AggSite/PostList.aspx'))

write2('./test.xls','ID\tTitle\tAuthor\tView\tComment\tLink\tContent\n')
for k in range(1,201):
    write2('./test.xls', '\r'.join( getData('https://www.cnblogs.com/mvc/AggSite/PostList.aspx',k))+'\r')

