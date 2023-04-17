import { SET_DIRECTORY_FILES } from "./mutations";

export default {
  async readDirectoryFiles({ commit }, directoryPath) {
    const directoryFiles = await api.readDirectoryFiles(directoryPath);
    commit(SET_DIRECTORY_FILES, directoryFiles);
  },
};
