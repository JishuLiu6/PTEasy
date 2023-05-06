import { createStore } from 'vuex';
import state from '@/store/state';
import mutations from '@/store/mutations';
import getters from '@/store/getters';
import actions from '@/store/actions';
import activeTasks from '@/store/system/activeTasks';
import logManagement from '@/store/system/logManagement';
import socketManager from '@/store/system/socketManager';

export default createStore({
  state,
  mutations,
  actions,
  getters,
  modules: {
    activeTasks,
    logManagement,
    socketManager
  },
});
