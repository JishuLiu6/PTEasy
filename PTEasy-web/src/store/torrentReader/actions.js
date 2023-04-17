import { SET_TORRENT_FILES, SET_CURRENT_TORRENT } from "./mutations";

export default {
  async readTorrentFiles({ commit }, files) {
    const torrentFiles = await api.readTorrentFiles(files);
    commit(SET_TORRENT_FILES, torrentFiles);
  },
  setCurrentTorrent({ commit }, torrent) {
    commit(SET_CURRENT_TORRENT, torrent);
  },
};
