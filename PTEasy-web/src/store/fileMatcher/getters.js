export default {
    matchedFilesByTorrentId: (state) => (torrentId) => {
      return state.matchedFiles.filter((matchedFile) => matchedFile.torrentId === torrentId);
    },
  };
  