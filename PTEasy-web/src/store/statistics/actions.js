import SocketHandler from "@/socket";

const socketHandler = new SocketHandler("http://your-socket-io-url");

socketHandler.onMessage("message", (data) => {
    if (data.type === "downloadServerStatus") {
        const servers = this.getters["downloadServer/serversByType"](data.serverType);
        if (servers.length) {
            servers.forEach((server) => {
                if (server.name === data.serverName) {
                    commit(SET_DOWNLOAD_SERVER_STATUS, {
                        serverId: server.id,
                        status: data.status,
                    });
                }
            });
        }
    } else if (data.type === "resourceTypes") {
        commit(SET_RESOURCE_TYPES, data.resourceTypes);
    } else if (data.type === "apiStatistics") {
        commit(SET_API_STATISTICS, data.apiStatistics);
    } else if (data.type === "seedRatio") {
        commit(SET_SEED_RATIO, data.seedRatio);
    }
});

export default {
    // 此处可添加与后端 API 交互的 action，如获取 API 统计信息等
};