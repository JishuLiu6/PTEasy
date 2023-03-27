import POST from '@/api/post';
export default {
  getLocalList({ commit }, data) {
    POST.localList(data).then(response => {
      // const { data } = response.data
      console.log(response)
      // commit('SET_LOCAL_LIST', data)
    }).catch(error => {
      console.log(error)
    })
  }
}