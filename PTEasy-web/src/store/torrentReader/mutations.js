export const ADD_TORRENT = "ADD_TORRENT";
export const REMOVE_TORRENT = "REMOVE_TORRENT";

export default {
  [ADD_TORRENT](state, torrent) {
    state.torrents.push(torrent);
  },
  [REMOVE_TORRENT](state, torrentId) {
    state.torrents = state.torrents.filter((torrent) => torrent.id !== torrentId);
  },
};
