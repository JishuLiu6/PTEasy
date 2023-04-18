// 导出 activeTasks 子模块
export default {
    namespaced: true,
    state: {
      tasks: [] // 存储正在运行的任务列表
    },
    mutations: {
      // 添加任务
      addTask(state, task) {
        state.tasks.push(task);
      },
      // 删除任务
      removeTask(state, taskIndex) {
        state.tasks.splice(taskIndex, 1);
      },
      // 更新任务状态
      updateTaskStatus(state, { taskIndex, status }) {
        state.tasks[taskIndex].status = status;
      }
    },
    actions: {
      // 添加任务
      addTask({ commit }, task) {
        commit('addTask', task);
      },
      // 删除任务
      deleteTask({ commit }, taskIndex) {
        commit('removeTask', taskIndex);
      },
      // 更新任务状态
      updateTaskStatus({ commit }, payload) {
        commit('updateTaskStatus', payload);
      },
      // 从后端获取正在运行的任务数据的逻辑
      async fetchData({ commit }) {

        // const response = await axios.get('/api/activeTasks');
        // commit('setTasks', response.data);
  
        // 示例代码
        const tasks = await new Promise((resolve) => {
          setTimeout(() => {
            resolve([{ id: 1, name: 'Sample task', status: 'running' }]);
          }, 1000);
        });
        commit('setTasks', tasks);
      },
    },
    getters: {
      // 获取任务列表
      tasks: (state) => state.tasks
    }
  };
  