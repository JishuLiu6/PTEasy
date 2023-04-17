export const ADD_NOTIFICATION = "ADD_NOTIFICATION";
export const REMOVE_NOTIFICATION = "REMOVE_NOTIFICATION";

export default {
  [ADD_NOTIFICATION](state, notification) {
    state.notifications.push(notification);
  },
  [REMOVE_NOTIFICATION](state, notificationId) {
    state.notifications = state.notifications.filter(
      notification => notification.id !== notificationId
    );
  },
};
