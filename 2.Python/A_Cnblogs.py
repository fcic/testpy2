import B1_requests
from lxml import etree

i=1

def getData(url):
    global i
    #html = B1_requests.Gethtml('http://www.example.com')
    html = B1_requests.Gethtml(url)
    #print(html)
    #res= etree.HTML(html).xpath('/html/body/div[1]/p[2]/a/text()')
    #row = []
    rows= ['ID\tTitle\tAuthor\tView\tComment\tContent']
    obj = etree.HTML(html).xpath('//*[@id="post_list"]/div/div[2]')
    #print(obj)
    # i=1
    for r in obj:
        row = [ str(i),r.xpath('h3/a/text()')[0].replace('\r\n','') , 
            r.xpath('div/a/text()')[0].replace('\r\n','') , 
                    r.xpath('div/span[1]/a/text()')[0].replace('\r\n','').replace('评论(','').replace(')','') , 
                        r.xpath('div/span[2]/a/text()')[0].replace('\r\n','').replace('阅读(','').replace(')','') ,
                            r.xpath('p/text()')[0].replace('\r\n','') ]
        rows.append('\t'.join(row))
        i+=1
        #rows.append(row)
        #rows.append('123')
        #print(','.join(row))
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
#view: 
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

def read(file):
    f=open(file,'r')
    return f.read()

a = read('./fcictest.csv').split('\n')
for r in a:
    #print(r)
    write2('./test.xls', '\r'.join( getData(r)))
    #time.sleep(2)

#write2('./test.xls', '\r'.join( getData('https://www.cnblogs.com/')))
#print(getData('https://www.cnblogs.com/'))
