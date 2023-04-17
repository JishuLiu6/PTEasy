export default {
    totalServerStatusByType: (state, getters, rootState, rootGetters) => (serverType) => {
        let totalStatus = {
            downloading: 0,
            seeding: 0,
            paused: 0,
            error: 0,
        };

        const servers = rootGetters["downloadServer/serversByType"](serverType);
        const serverStatusList = state.downloadServerStatus.filter((status) =>
            servers.some((server) => server.id === status.serverId)
        );

        serverStatusList.forEach((status) => {
            totalStatus.downloading += status.downloading;
            totalStatus.seeding += status.seeding;
            totalStatus.paused += status.paused;
            totalStatus.error += status.error;
        });

        return totalStatus;
    },
    totalApiStatistics(state) {
        return state.apiStatistics.reduce(
            (total, site) => {
                total.uploaded += site.uploaded;
                total.downloaded += site.downloaded;
                return total;
            },
            { uploaded: 0, downloaded: 0 }
        );
    },
};