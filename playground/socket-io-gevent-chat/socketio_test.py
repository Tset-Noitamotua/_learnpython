import os

from socketio import socketio_manage
from socketio.server import SocketIOServer

from socketio.namespace import BaseNamespace

public = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        'public'))

class ChatNamespace(BaseNamespace):
    _registry = {}

    def initialize(self):
        self._registry[id(self)] = self
        self.emit('connect')
        self.nick = None

    def disconnect(self, *args, **kwargs):
        if self.nick:
            self._broadcast('exit', self.nick)
        del self._registry[id(self)]
        super(ChatNamespace, self).disconnect(*args, **kwargs)

    def on_login(self, nick):
        if self.nick:
            self._broadcast('exit', self.nick)
        self.nick = nick
        self._broadcast('enter', nick)
        self.emit('users',
                  [ ns.nick
                    for ns in self._registry.values()
                    if ns.nick is not None ])

    def on_chat(self, message):
        if self.nick:
            self._broadcast('chat', dict(u=self.nick, m=message))
        else:
            self.emit('chat', dict(u='SYSTEM', m='You must first login'))

    def _broadcast(self, event, message):
        for s in self._registry.values():
            s.emit(event, message)


def chat(environ, start_response):
    if environ['PATH_INFO'].startswith('/socket.io'):
        return socketio_manage(environ, { '/chat': ChatNamespace })
    else:
        return serve_file(environ, start_response)

def serve_file(environ, start_response):
    path = os.path.normpath(
        os.path.join(public, environ['PATH_INFO'].lstrip('/')))
    assert path.startswith(public), path
    if os.path.exists(path):
        start_response('200 OK', [('Content-Type', 'text/html')])
        with open(path) as fp:
            while True:
                chunk = fp.read(4096)
                if not chunk: break
                yield chunk
    else:
        start_response('404 NOT FOUND', [])
        yield 'File not found'

sio_server = SocketIOServer(
    ('', 8080), chat, 
    policy_server=False)
sio_server.serve_forever()
