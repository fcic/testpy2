import requests
from bs4 import BeautifulSoup as bs

r = requests.get("http://www.hao123.com");
r.encoding = r.apparent_encoding

soup = bs(r.text,"lxml")
text = soup.find_all('a')

for i in text:
    print(i.get_text()+' '+i['href'])

#apt install python3-pip   
#pip3 install requests  #提示要升级，升级后就出问题，不要升级
#pip3 install beautifulsoup
#pip3 install bs4
#pip3 install xml