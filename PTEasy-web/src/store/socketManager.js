// src/store/socketManager.js
export default function socketManager(wsUrl) {
  let socket;
  let heartbeatInterval;

  function connect() {
    socket = new WebSocket(wsUrl);

    socket.addEventListener("open", () => {
      console.log("WebSocket connected");

      // Start sending heartbeat messages
      heartbeatInterval = setInterval(() => {
        socket.send(JSON.stringify({ event: "heartbeat" }));
      }, 30000);
    });

    socket.addEventListener("close", (event) => {
      console.log("WebSocket disconnected, trying to reconnect...");

      // Stop sending heartbeat messages
      clearInterval(heartbeatInterval);

      // Try to reconnect after a delay
      setTimeout(() => {
        connect();
      }, 3000);
    });
  }

  connect();

  const socketManager = {
    get socket() {
      return socket;
    },
    initListeners(commit, listeners) {
      socket.addEventListener("message", (event) => {
        const data = JSON.parse(event.data);
        console.log(data, listeners);
        const listener = listeners.find(
          (listener) => listener.event === data.event
        );

        if (listener) {
          const payload = {
            ...data.payload,
            ...listener.data,
          };
          console.log(listener.mutation, payload);
          commit(listener.mutation, payload);
          // console.log(`${listener.event}: ${JSON.stringify(payload)}`);
        }
      });
    },
    sendMessage(event, payload = {}) {
      socket.send(JSON.stringify({ event, payload }));
    },
    closeListeners(commit, listeners) {
      listeners.forEach((listener) => {
        socket.removeEventListener("message", listener);
      });

      // Stop sending heartbeat messages
      clearInterval(heartbeatInterval);

      // Close WebSocket connection
      socket.close();
    },
  };

  return socketManager;
}
