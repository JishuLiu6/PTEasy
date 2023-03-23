import HTTP from '@/utils/request'

export default {
  /**
   * Get configuration data from server
   * @returns {*}
   */
  localList() {
    return HTTP.get('/local/list');
  },
}