from gevent import wsgi
def hello_world(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    yield '<b>Hello world</b>'

server = wsgi.WSGIServer(
    ('0.0.0.0', 8080), hello_world)

server.serve_forever()
