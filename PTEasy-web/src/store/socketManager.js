// src/store/socketManager.js
export default function socketManager(socket) {
  let heartbeatInterval;

  const socketManager = {
    socket: socket,
    initListeners(commit, listeners) {
      listeners.forEach((listener) => {
        socket.on(listener.event, (data) => {
          const payload = {
            ...data,
            ...listener.data,
          };

          commit(listener.mutation, payload);
          // console.log(`${listener.event}: ${JSON.stringify(payload)}`);
        });
      });

      // Start sending heartbeat messages every 30 seconds
      heartbeatInterval = setInterval(() => {
        socket.emit('heartbeat');
      }, 30000);
    },
    closeListeners(commit, listeners) {
      listeners.forEach((listener) => {
        socket.off(listener.event);
      });

      // Stop sending heartbeat messages
      clearInterval(heartbeatInterval);
    },
  };

  return socketManager;
}
