import GET from '@/api/get';

export default {
  namespaced: true,
  state: {
    logs: [],
    page: 1,
    size: 10,
    totalCount: 0
  },
  mutations: {
    addLog(state, log) {
      state.logs.push(log);
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
    receiveLog({ commit }, log) {
      commit('addLog', log);
    },
    deleteLog({ commit }, logIndex) {
      commit('removeLog', logIndex);
    },
    clearLogs({ commit }) {
      commit('clearLogs');
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
