export default {
    serversByType: (state) => (serverType) => {
      return state.servers.filter((server) => server.type === serverType);
    },
  };
  