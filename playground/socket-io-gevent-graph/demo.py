
import os
import time
import math
import json
import webbrowser

import paste.urlparser

import gevent
from socketio import SocketIOServer
from gevent_zeromq import zmq

def main():
    '''Set up zmq context and greenlets for all the servers, then launch the web
    browser and run the data producer'''
    context = zmq.Context()

    # zeromq: tcp to inproc gateway
    gevent.spawn(zmq_server, context)
    # WSGI server: copies inproc zmq messages to websocket
    sio_server = SocketIOServer(
        ('', 8000), SocketIOApp(context),
        resource="socket.io")
    # Start the server greenlets
    sio_server.start()
    # Open a couple of webbrowsers
    # webbrowser.open('http://localhost:8000/graph.html')
    # webbrowser.open('http://localhost:8000/graph.html')
    # Kick off the producer
    zmq_producer(context)
    
def zmq_server(context):
    '''Funnel messages coming from the external tcp socket to an inproc socket'''
    sock_incoming = context.socket(zmq.SUB)
    sock_outgoing = context.socket(zmq.PUB)
    sock_incoming.bind('tcp://*:5000')
    sock_outgoing.bind('inproc://queue')
    sock_incoming.setsockopt(zmq.SUBSCRIBE, "")
    while True:
        msg = sock_incoming.recv()
        sock_outgoing.send(msg)

class SocketIOApp(object):
    '''Funnel messages coming from an inproc zmq socket to the socket.io'''

    def __init__(self, context):
        self.context = context
        self.static_app = paste.urlparser.StaticURLParser(
            os.path.dirname(__file__))
        
    def __call__(self, environ, start_response):
        if not environ['PATH_INFO'].startswith('/socket.io'):
            return self.static_app(environ, start_response)
        socketio = environ['socketio']
        sock = self.context.socket(zmq.SUB)
        sock.setsockopt(zmq.SUBSCRIBE, "")
        sock.connect('inproc://queue')
        while True:
            msg = sock.recv()
            socketio.send(msg)

def zmq_producer(context):
    '''Produce a nice time series sine wave'''
    socket = context.socket(zmq.PUB)
    socket.connect('tcp://127.0.0.1:5000')

    SCALE=500
    ts = SCALE / 10000.
    print ts
    while True:
        x = time.time() * 1000
        y = 2.5 * (1 + math.sin(x / SCALE))
        socket.send(json.dumps(dict(x=x, y=y)))
        gevent.sleep(ts)
        # gevent.sleep(0.5)

if __name__ == '__main__':
    main()
