
import GET from '@/api/get';
import { inject } from "vue";

export default {
    namespaced: true,
    state: {
      tasks: [], // 存储正在运行的任务列表
      page: 1,
      size: 10,
      totalCount: 0,
      socketListeners: [
        {
          event: 'task:add',
          type: 'mutation', // 'mutation' or 'action'
          name: 'activeTasks/addTask',
        },
        {
          event: 'task:update',
          type: 'mutation', // 'mutation' or 'action'
          name: 'activeTasks/updateTaskStatus',
        }
      ]
    },
    mutations: {
      // 添加任务
      addTask(state, task) {
        state.tasks.unshift(task);
        state.totalCount += 1;
  
        if (state.tasks.length > state.size) {
          state.tasks.pop();
        }
      },
      // 删除任务
      removeTask(state, taskIndex) {
        state.tasks.splice(taskIndex, 1);
      },
      // 更新任务状态
      updateTaskStatus(state, updatedTask) {
        const taskIndex = state.tasks.findIndex(task => task.task_id === updatedTask.task_id);
        if (taskIndex !== -1) {
          Object.assign(state.tasks[taskIndex], updatedTask);
        }
      },
      setTasks(state, tasks) {
        state.tasks = tasks;
      },
      setTotalCount(state, totalCount) {
        state.totalCount = totalCount;
      }
    },
    actions: {
      // 从后端获取正在运行的任务数据的逻辑
      async fetchData({ commit, state }) { 
        GET.taskList({ page: state.page, size: state.size }) 
          .then((r) => {
            var { data_list, total_count } = r.data.data;
            commit('setTasks', data_list);
            commit('setTotalCount', total_count);
          })
          .catch((error) => {
            console.log(error);
          });
      },
    },
    getters: {
      // 获取任务列表
      tasks: (state) => state.tasks,
      hasActiveTasks: (state) => state.tasks.some(task => task.progress / task.task_len !== 1)
    }
  };
  