# -*- coding: utf-8 -*-
#  网上很多代码出问题就是 在server_handler的return 加上[u'xxx'.encode('utf8')] 就可以连
from wsgiref.simple_server import make_server


def server_handler(env, response):
    inputStr =env.get('PATH_INFO')
    if(inputStr == '/1'):
        response("200 OK", [('Content-Type', 'text/html')])
        return [u'<h1>Hello response in server_handler</h1>'.encode('utf8')]
    else:
        response("200 OK", [('Content-Type', 'text/html')])
        return [u'<h1>Hello fcic</h1>'.encode('utf8')]

def Swcase(var):
    return {
            'a': 1,
            'b': 2,
            'c': 3,
    }.get(var,'error') 

def create_server(server):
    svr = make_server('127.0.0.1', 8000, server)
    print("Serving HTTP on port 8000 ...")
    svr.serve_forever()

def main():
    create_server(server_handler)

if __name__ == "__main__":
    main()
