from aiohttp import web
import socketio

from websocket_server.log_init import logger

sio = socketio.AsyncServer(cors_allowed_origins="*")
# app = socketio.WSGIApp(sio, static_files={
#     '/': {'content_type': 'text/html', 'filename': 'index.html'}
# })

app = web.Application()
sio.attach(app)


@sio.event
def connect(sid, environ):
    logger.info("connect %s ", sid)


@sio.event
async def echo(sid, data):
    logger.info("message %s ", sid)


@sio.event
def disconnect(sid):
    logger.info("disconnect %s", sid)


if __name__ == "__main__":
    web.run_app(app)
