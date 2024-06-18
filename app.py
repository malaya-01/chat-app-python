# from flask import Flask, render_template, request
# from flask_socketio import SocketIO, send

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @socketio.on('connect')
# def handle_connect():
#     print(f"User {request.sid} connected")
#     send(f"User {request.sid} has entered the chat", broadcast=True)

# @socketio.on('disconnect')
# def handle_disconnect():
#     print(f"User {request.sid} disconnected")
#     send(f"User {request.sid} has left the chat", broadcast=True)

# @socketio.on('message')
# def handle_message(data):
#     msg = data['msg']
#     font = data['font']
#     print(f"Message from {request.sid}: {msg} with font {font}")
#     send({'msg': msg, 'font': font, 'sid': request.sid}, broadcast=True)

# if __name__ == '__main__':
#     socketio.run(app, debug=True)

################# second try.

# from flask import Flask, render_template
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# socketio = SocketIO(app)

# # Hardcoded mapping of session IDs to usernames (for demo purposes)
# session_to_username = {}

# @app.route('/')
# def index():
#     return render_template('index.html')

# @socketio.on('connect')
# def handle_connect():
#     session_id = request.sid
#     # For demo, associate session ID with a username
#     session_to_username[session_id] = f'User_{session_id[-5:]}'  # Example username

# @socketio.on('message')
# def handle_message(data):
#     username = session_to_username.get(request.sid, 'Unknown User')
#     emit('message', {'username': username, 'msg': data['msg'], 'font': data['font']}, broadcast=True)

# if __name__ == '__main__':
#     socketio.run(app)


############### Third try

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Dictionary to store usernames mapped to session IDs
usernames = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    session_id = request.sid
    usernames[session_id] = f'user-{len(usernames) + 1}'  # Assign username like user-1, user-2, ...

# @socketio.on('message')
# def handle_message(data):
#     session_id = request.sid
#     username = usernames.get(session_id, 'Unknown User')
#     emit('message', {'username': username, 'msg': data['msg'], 'font': data['font']}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    session_id = request.sid
    username = usernames.get(session_id, 'Unknown User')
    emit('message', {'username': username, 'msg': data['msg'], 'font': data['font']}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)
