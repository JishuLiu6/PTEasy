export const ADD_DOWNLOAD_SERVER = "ADD_DOWNLOAD_SERVER";
export const REMOVE_DOWNLOAD_SERVER = "REMOVE_DOWNLOAD_SERVER";

export default {
  [ADD_DOWNLOAD_SERVER](state, server) {
    state.servers.push(server);
  },
  [REMOVE_DOWNLOAD_SERVER](state, serverId) {
    state.servers = state.servers.filter((server) => server.id !== serverId);
  },
};
