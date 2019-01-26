from bs4 import BeautifulSoup 
import urllib 
import urllib.parse 
import urllib.request 
url = "http://srh.bankofchina.com/search/whpj/search.jsp"
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36" #将user_agent写入头信息 
values = {"erectDate":"2018-08-01","nothing":"2018-08-03", "pjname":"1316", "page":"2"} 
headers = { "User-Agent" : user_agent } 
data =urllib.parse.urlencode(values).encode(encoding="UTF8") 
req = urllib.request.Request(url, data, headers) #headers不能通过urllib.request.urlopen()发送，要通过urllib.request.Request()发送 
response = urllib.request.urlopen(req) 
the_page = response.read().decode() 
soup = BeautifulSoup(the_page,"lxml") 
results1=soup.find_all(attrs={"class":"BOC_main publish"})

f=open(r"Getcurrentcy.txt", "a+") 
for i1 in results1[0].table.find_all("tr"): 
    item=[] 
    for i2 in i1.find_all("td"): 
        item.append(i2.string) 
        if len(item)>2: 
            f.write(str(item))

        f.close