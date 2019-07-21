import B1_requests
from lxml import etree

def getData(url,xpath):
    #html = B1_requests.Gethtml('http://www.example.com')
    html = B1_requests.Gethtml(url)
    #print(html)
    #res= etree.HTML(html).xpath('/html/body/div[1]/p[2]/a/text()')
    res = etree.HTML(html).xpath(xpath)
    for r in res:
        print(r)

getData('https://www.cnblogs.com/','//*[@id="post_list"]/div/div[2]/h3/a/text()')