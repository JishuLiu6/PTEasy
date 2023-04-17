export const ADD_LOG = "ADD_LOG";
export const CLEAR_LOGS = "CLEAR_LOGS";

export default {
  [ADD_LOG](state, log) {
    state.logs.push(log);
  },
  [CLEAR_LOGS](state) {
    state.logs = [];
  },
};
