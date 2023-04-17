export const SET_USER = "SET_USER";
export const SET_AUTHENTICATED = "SET_AUTHENTICATED";

export default {
  [SET_USER](state, user) {
    state.user = user;
  },
  [SET_AUTHENTICATED](state, isAuthenticated) {
    state.isAuthenticated = isAuthenticated;
  },
};
