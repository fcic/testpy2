# pip3 install uwsgi
# uwsgi --http :9090 --wsgi-file F4_WebServer_UWSGI.py

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]