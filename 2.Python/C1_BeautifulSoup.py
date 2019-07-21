#fcic:对text做分析处理
import B1_requests
from bs4 import BeautifulSoup
#request = __import__('1_1_requests')

B1_requests.Gethtml('http://www.example.com')

#print(html)


# soup = BeautifulSoup(html,'html.parser').select('body > div:nth-of-type(1) > p')
#print(soup)

# for s in soup:
#     print(s.get_text())