import socketio

sio = socketio.Client()

sio.connect("http://localhost:5000")
sio.emit("echo", {"response": "my response"})
# sio.wait()
