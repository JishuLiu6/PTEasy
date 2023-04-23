import GET from '@/api/get';
import { inject } from "vue";

export default {
  namespaced: true,
  state: {
    logs: [],
    page: 1,
    size: 10,
    totalCount: 0,
    socketListeners: [
      {
        event: 'log',
        mutation: 'addLog',
      }
    ]
  },
  mutations: {
    addLog(state, log) {
      state.logs.unshift(log);
      state.totalCount += 1;

      if (state.logs.length > state.size) {
        state.logs.pop();
      }
    },
    removeLog(state, logIndex) {
      state.logs.splice(logIndex, 1);
    },
    clearLogs(state) {
      state.logs = [];
    },
    // 添加 setLogs mutation
    setLogs(state, logs) {
      state.logs = logs;
    },
    setTotalCount(state, totalCount) {
      state.totalCount = totalCount;
    },
  },
  actions: {
    initSocket({ commit, state}) {
      const socketManager = inject("socketManager");
      socketManager.initListeners(commit, state.socketListeners);
    },
    closeSocket({ commit, state}) {
      const socketManager = inject("socketManager");
      socketManager.closeListeners(commit, state.socketListeners);
    },
    async fetchData({ commit, state }) {
      GET.logsList({ page: state.page, size: state.size })
        .then((r) => {
          var { data_list, total_count } = r.data.data;
          commit('setLogs', data_list); // 日志数据
          commit('setTotalCount', total_count); // 日志志总数
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  getters: {
    logs: (state) => state.logs,
  },
};
