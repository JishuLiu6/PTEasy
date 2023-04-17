export default {
    // ...
    totalApiUploaded: (state) => {
      return state.apiStatistics.reduce((total, stats) => total + stats.uploaded, 0);
    },
    totalApiDownloaded: (state) => {
      return state.apiStatistics.reduce((total, stats) => total + stats.downloaded, 0);
    },
  };
  