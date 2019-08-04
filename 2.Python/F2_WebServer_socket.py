import socket
'''生成socket 对象'''
sk = socket.socket()
''' 绑定IP和端口 '''
sk.bind(("127.0.0.1",8080))
''' 启用监听 '''
sk.listen()
''' 定义不同Url的处理函数 '''
def func1():
 str_html = "";
 with open("1.html","r",encoding="utf-8") as f:
    str_html = f.read()
 return bytes(str_html,encoding="utf-8")
def func2():
 return bytes("你好 2",encoding="utf-8")
def funcErro():
 return bytes("你好 404",encoding="utf-8")
dic={"/1":func1,"/2":func2}
''' 等待客户端链接 '''
while True:
 conn,_ = sk.accept()
 data = conn.recv(8096)
 print('data:')
 print(data)
 item = str(data,encoding="utf-8").split("\r")
 print('item:')
 print(item)
 url = str(item[0]).split(" ")[1]
 print('url:')
 print(url)
 conn.send(b'http/1.1 200 ok\r\nContent-Type:text/html; charset=utf-8\r\n\r\n')
 
 for item in dic.keys():
    if url == item:
        func = dic[item]
        break
    else:
        func = funcErro()
        try:
            response = func()
            conn.send(response)
            conn.close()
        except:
            conn.close()
sk.close()


#original:fcic:can run 
# import socket
# '''生成socket 对象'''
# sk = socket.socket()
# ''' 绑定IP和端口 '''
# sk.bind(("127.0.0.1",8080))
# ''' 启用监听 '''
# sk.listen()
# ''' 等待客户端链接 '''
# while True:
#  conn,_ = sk.accept()
#  data = conn.recv(8096)
#  print(data)
#  item = str(data,encoding="utf-8").split("\r")
#  url = str(item[0]).split(" ")[1]
#  print(url)
#  conn.send(b'http/1.1 200 ok \r\n Content-Type:text/html;charset=utf-8\r\n\r\n')
#  if url == "/1":
#     conn.send(b'HelloWorld 1')
#  elif url == "/2":
#     conn.send(b'HelloWorld 2')
#  else:
#     conn.send(b'404 NotFound')
#     conn.close()
# sk.close()