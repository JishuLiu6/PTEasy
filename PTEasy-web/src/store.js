import state from '@/store/state';
import mutations from '@/store/mutations';
import getters from '@/store/getters';
import actions from '@/store/actions';
import activeTasks from '@/store/system/activeTasks';
import logManagement from '@/store/system/logManagement';
export default {
    namespaced: true,
    modules: {
        activeTasks, logManagement
    },
    state,
    mutations,
    actions,
    getters,
};
