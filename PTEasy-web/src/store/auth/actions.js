import { SET_USER, SET_AUTHENTICATED } from "./mutations";

export default {
  async login({ commit }, credentials) {
    const user = await api.login(credentials);
    commit(SET_USER, user);
    commit(SET_AUTHENTICATED, true);
  },
  logout({ commit }) {
    commit(SET_USER, null);
    commit(SET_AUTHENTICATED, false);
  },
};
