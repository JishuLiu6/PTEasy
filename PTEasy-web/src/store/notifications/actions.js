import { ADD_NOTIFICATION, REMOVE_NOTIFICATION } from "./mutations";

export default {
  addNotification({ commit }, notification) {
    commit(ADD_NOTIFICATION, notification);
  },
  removeNotification({ commit }, notificationId) {
    commit(REMOVE_NOTIFICATION, notificationId);
  },
};
