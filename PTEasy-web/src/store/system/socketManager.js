// src/store/socket.js
import { reactive } from "vue";

const state = reactive({
  socket: null,
  heartbeatInterval: null,
  listeners: []
});

const actions = {
  connect({ commit }, wsUrl) {
    state.socket = new WebSocket(wsUrl);

    state.socket.addEventListener("open", () => {
      console.log("WebSocket connected");

      state.heartbeatInterval = setInterval(() => {
        state.socket.send(JSON.stringify({ event: "heartbeat" }));
      }, 30000);
    });

    state.socket.addEventListener("close", () => {
      console.log("WebSocket close");
      clearInterval(state.heartbeatInterval);

      // setTimeout(() => {
      //   actions.connect({ commit }, wsUrl);
      // }, 3000);
    });
  },

  initListeners({ commit, dispatch, state}, listeners) {
    if (!Array.isArray(listeners.value)) {
      listeners = [];
    } else {
      listeners = listeners.value;
    }
    
    state.socket.addEventListener("message", (event) => {
      const data = JSON.parse(event.data);
      state.listeners.push(data);
      const listener = listeners.find(
        (listener) => listener.event === data.event
      );
  
      if (listener) {
        const payload = {
          ...data.payload,
          ...listener.data,
        };
  
        if (listener.type === 'mutation') {
          commit(listener.name, payload, {root: true});
        } else if (listener.type === 'action') {
          dispatch(listener.name, payload, {root: true});
        }
      }
    });
  },
  

  sendMessage(_, { event, payload = {} }) {
    state.socket.send(JSON.stringify({ event, payload }));
  },
  closeListeners({state}, listeners=[]) {
    if (!Array.isArray(listeners.value)) {
      listeners = [];
    } else {
      listeners = listeners.value;
    }
  
    listeners.forEach((listener) => {
      console.log(listener)
      state.socket.removeEventListener("message", listener);
    });
  
    clearInterval(state.heartbeatInterval);
  
    if (state.socket.readyState === WebSocket.OPEN) {
      // WebSocket连接状态为 OPEN，立即关闭连接
      state.socket.close();
      console.log("closeSocket OK")
    } else {
      // WebSocket连接可能已经关闭或正在关闭，不需要再次关闭
      return;
    }
  }
  
};

export default {
  namespaced: true,
  state,
  actions,
};
