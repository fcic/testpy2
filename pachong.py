import requests
from bs4 import BeautifulSoup as bs

r = requests.get("http://www.hao123.com");
r.encoding = r.apparent_encoding

soup = bs(r.text,"lxml")
text = soup.find_all('a')

for i in text:
    print(i.get_text()+' '+i['href'])
