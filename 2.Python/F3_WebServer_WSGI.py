# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server


def server_handler(env, response):
    response("200 OK", [('Content-Type', 'text/html')])
    return '<h1>Hello response in server_handler</h1>'

def create_server(server):
    svr = make_server('127.0.0.1', 8000, server)
    print("Serving HTTP on port 8000 ...")
    svr.serve_forever()

def main():
    create_server(server_handler)

if __name__ == "__main__":
    main()
