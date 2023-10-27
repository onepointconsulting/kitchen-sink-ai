from websocket_server.log_init import logger
from websocket_server.session import Session, sessions_id
from websocket_server.service import simple_query
import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins="*")

app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    logger.info("connect %s ", sid)


@sio.event
def echo(sid, data):
    """For testing purposes"""
    logger.info("echo %s", data)
    sio.emit("echo", data, room=sid)


@sio.event
def question(sid, data):
    logger.info("question %s: %s", sid, data)
    if sid in sessions_id:
        sessions_id[sid].messages_history.append(data)
    else:
        Session(sid).messages_history.append(data)
    res = simple_query.memory_run(data, sessions_id[sid])
    sio.emit("response", res, room=sid)


@sio.event
def disconnect(sid):
    logger.info("disconnect %s", sid)


if __name__ == "__main__":
    eventlet.wsgi.server(eventlet.listen(("127.0.0.1", 3001)), app)
