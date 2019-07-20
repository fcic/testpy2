#fcic:对text做分析处理
#import B1_requests
request = __import__('1_1_requests')

html =  request.Gethtml('http://www.example.com')
print(html)