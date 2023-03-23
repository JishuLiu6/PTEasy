import GET from '@/api/get';
export default {
  getLocalList({ commit }) {
    GET.localList().then(response => {
      const { data } = response.data
      console.log(data)
      // commit('SET_LOCAL_LIST', data)
    }).catch(error => {
      console.log(error)
    })
  }
}