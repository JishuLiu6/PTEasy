export const ADD_MATCHED_FILE = "ADD_MATCHED_FILE";
export const UPDATE_MATCHED_FILE_STATUS = "UPDATE_MATCHED_FILE_STATUS";

export default {
  [ADD_MATCHED_FILE](state, matchedFile) {
    state.matchedFiles.push(matchedFile);
  },
  [UPDATE_MATCHED_FILE_STATUS](state, { torrentId, fileId, status }) {
    const matchedFileIndex = state.matchedFiles.findIndex(
      (matchedFile) => matchedFile.torrentId === torrentId && matchedFile.fileId === fileId
    );
    if (matchedFileIndex !== -1) {
      state.matchedFiles[matchedFileIndex].status = status;
    }
  },
};
