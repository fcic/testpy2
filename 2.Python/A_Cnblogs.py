import B1_requests
from lxml import etree

def getData(url,xpath):
    #html = B1_requests.Gethtml('http://www.example.com')
    html = B1_requests.Gethtml(url)
    #print(html)
    #res= etree.HTML(html).xpath('/html/body/div[1]/p[2]/a/text()')
    #row = []
    rows= []
    obj = etree.HTML(html).xpath('//*[@id="post_list"]/div/div[2]')
    for r in obj:
        row = [r.xpath('h3/a/text()'),r.xpath('div/a/text()'),r.xpath('p/text()'),r.xpath('div/span[1]/a/text()'),r.xpath('div/span[2]/a/text()')]
        rows.append(row)
    #print(rows)
    return rows
#title: 
# //*[@id="post_list"]/div[1]/div[2]/h3/a
#author: 
# //*[@id="post_list"]/div[1]/div[2]/div/a
#content: 
# //*[@id="post_list"]/div[1]/div[2]/p/text()
#comment: 
# //*[@id="post_list"]/div[1]/div[2]/div/span[1]/a
#read: 
# //*[@id="post_list"]/div[1]/div[2]/div/span[2]/a
#datetime: 
# //*[@id="post_list"]/div[1]/div[2]/div/text()
#recommand: 
# //*[@id="digg_count_11223205"]

#getData('https://www.cnblogs.com/','//*[@id="post_list"]/div/div[2]/h3/a/text()')

def write2(file,content):  
    f=open(file,'a')
    f.write(content)
    f.close()

write2('./test.txt', ''.join( getData('https://www.cnblogs.com/','//*[@id="post_list"]/div/div[2]/h3/a/text()')))