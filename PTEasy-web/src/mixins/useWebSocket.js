import { useStore } from "vuex";
import { computed } from "vue";
export function useWebSocket() {
  const store = useStore();
  const logSocketListeners = computed(() => store.state.logManagement.socketListeners);
  const taskSocketListeners = computed(() => store.state.activeTasks.socketListeners);

  const combinedSocketListeners = computed(() => {
    return [...logSocketListeners.value, ...taskSocketListeners.value];
  });

  function initSocket() {
    store.dispatch("socketManager/connect", "ws://127.0.0.1:8999/v1/task/ws");
    store.dispatch("socketManager/initListeners", combinedSocketListeners.value);
  }

  function closeSocket() {
    store.dispatch("socketManager/closeListeners", combinedSocketListeners.value);
  }

  return {
    initSocket,
    closeSocket,
  };
}
