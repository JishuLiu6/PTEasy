// store/modules/system/logManagement.js

// 导出 logManagement 子模块
export default {
    namespaced: true,
    state: {
      logs: [] // 存储日志数据
    },
    mutations: {
      // 添加日志
      addLog(state, log) {
        state.logs.push(log);
      },
      // 删除日志
      removeLog(state, logIndex) {
        state.logs.splice(logIndex, 1);
      },
      // 清空日志
      clearLogs(state) {
        state.logs = [];
      }
    },
    actions: {
      // 接收后端发送的日志数据
      receiveLog({ commit }, log) {
        commit('addLog', log);
      },
      // 删除日志
      deleteLog({ commit }, logIndex) {
        commit('removeLog', logIndex);
      },
      // 清空日志
      clearLogs({ commit }) {
        commit('clearLogs');
      },
      // 从后端获取日志数据的逻辑
      async fetchData({ commit }) {
        // const response = await axios.get('/api/logs');
        // commit('setLogs', response.data);
  
        // 示例代码
        const logs = await new Promise((resolve) => {
          setTimeout(() => {
            resolve([{ id: 1, message: 'Sample log message' }]);
          }, 1000);
        });
        commit('setLogs', logs);
      },
    },
    getters: {
      // 获取日志数据
      logs: (state) => state.logs
    }
  };
  