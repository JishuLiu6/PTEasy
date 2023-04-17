export const SET_DIRECTORY_FILES = "SET_DIRECTORY_FILES";

export default {
  [SET_DIRECTORY_FILES](state, directoryFiles) {
    state.directoryFiles = directoryFiles;
  },
};
