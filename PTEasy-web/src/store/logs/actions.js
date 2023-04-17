import { ADD_LOG, CLEAR_LOGS } from "./mutations";

export default {
  addLog({ commit }, log) {
    commit(ADD_LOG, log);
  },
  clearLogs({ commit }) {
    commit(CLEAR_LOGS);
  },
};
