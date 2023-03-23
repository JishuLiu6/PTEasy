/*
 * @Author: Mike Wen
 * @Date: 2021-01-14 13:22:57
 * @LastEditors: Mike Wen
 * @LastEditTime: 2021-01-19 11:15:28
 */
import axios from 'axios'
// import store from '@/store'
// import { getToken } from '@/utils/auth'
const ERR_OK = 0
// const TOKEN_INVALID = 1
const NOT_AUTH = 4

const service = axios.create({
  baseURL: 'http://127.0.0.1:9900', // api 的 VUE_APP_URL
  timeout: 10000 // 请求超时时间(因为需要调试后台,所以设置得比较大)
})

const pending = [] // 声明一个数组用于存储每个请求的取消函数和axios标识
const CancelToken = axios.CancelToken
const removePending = (config) => {
  for (const p in pending) {
    if (pending[p].u === config.url.split('?')[0] + '&' + config.method) {
      // 当当前请求在数组中存在时执行函数体
      pending[p].f() // 执行取消操作
      pending.splice(p, 1) // 数组移除当前请求
    }
  }
}

service.interceptors.request.use(
  config => {
    removePending(config)
    config.cancelToken = new CancelToken((c) => {
      // pending存放每一次请求的标识，一般是url + 参数名 + 请求方法，当然你可以自己定义
      pending.push({ u: config.url.split('?')[0] + '&' + config.method, f: c })// config.data为请求参数
    })
    // const token = getToken()
    // if (token !== '') {
    //   config.headers.Authorization = 'Bearer ' + token
    // }
    return config
  },
  error => {
    return Promise.reject(error)
  }
)

service.interceptors.response.use(
  response => {
    const { errno, data } = response.data
    // if (errno === NOT_AUTH) {
    //   window.vm.$message('没有权限')
    // }
    // if (errno === ERR_OK) {
    //   if (data.msg) {
    //     window.vm.$message(data.msg)
    //   }
    // }
    return response
  },
  error => {
    return Promise.reject(error)
  }
)

export default service
