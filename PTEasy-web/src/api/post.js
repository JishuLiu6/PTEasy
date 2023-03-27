import HTTP from '@/utils/request'

export default {
  /**
   * Get configuration data from server
   * @returns {*}
   */
  localList(data) {
    return HTTP.post('/local/list', data);
  },
}