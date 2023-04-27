from flask_socketio import SocketIO

# socketio 注册
socketio = SocketIO(cors_allowed_origins='*', async_mode='gevent')
