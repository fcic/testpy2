#fcic:对text做分析处理


import B1_requests
from bs4 import BeautifulSoup
#request = __import__('1_1_requests')

html = B1_requests.Gethtml('http://www.example.com')

#print(html)

#原版的nth-child(1) 改成 nth-of-type(1)
# soup = BeautifulSoup(html,'html.parser').select('body > div:nth-of-type(1) > p')
#print(soup)

# for s in soup:
#     print(s.get_text()) #去掉html标签