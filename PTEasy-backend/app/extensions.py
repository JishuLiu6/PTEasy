from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins='*', async_mode='gevent', ping_timeout=120, ping_interval=60)

