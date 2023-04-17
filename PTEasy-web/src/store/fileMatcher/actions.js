import { ADD_MATCHED_FILE, UPDATE_MATCHED_FILE_STATUS } from "./mutations";

export const MATCH_TORRENTS_WITH_DIRECTORY = "MATCH_TORRENTS_WITH_DIRECTORY";

export default {
  async [MATCH_TORRENTS_WITH_DIRECTORY]({ commit, rootState }, directory) {
    // 1. 获取种子文件列表和目录文件列表
    const torrents = rootState.torrentReader.torrents;
    const directoryFiles = rootState.directoryReader.directoryFiles;

    // 2. 遍历种子文件列表，将每个种子文件与目录文件列表进行匹配
    torrents.forEach((torrent) => {
      torrent.files.forEach((torrentFile) => {
        const matchedDirectoryFile = directoryFiles.find(
          (dirFile) => dirFile.name === torrentFile.path.split("/").pop()
        );

        if (matchedDirectoryFile) {
          // 匹配成功
          commit(ADD_MATCHED_FILE, {
            torrentId: torrent.id,
            fileId: torrentFile.id,
            status: "matched",
          });
        } else {
          // 匹配失败
          commit(ADD_MATCHED_FILE, {
            torrentId: torrent.id,
            fileId: torrentFile.id,
            status: "unmatched",
          });
        }
      });
    });

    // 3. 可以在此处添加与后端 API 交互的逻辑，例如将匹配结果发送给后端服务器
    // ...
  },

  async updateMatchedFileStatus({ commit }, { torrentId, fileId, status }) {
    commit(UPDATE_MATCHED_FILE_STATUS, { torrentId, fileId, status });

    // 可以在此处添加与后端 API 交互的逻辑，例如更新匹配文件状态
    // ...
  },
};
