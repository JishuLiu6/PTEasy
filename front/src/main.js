import { createApp } from 'vue'
import App from './App.vue'

// 导入element-plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
// normalize.css 用于重置浏览器默认样式
import 'normalize.css/normalize.css'
// 导入路由
import {router} from './router'
// 导入图片方法
import {imgUrl} from './utils/imgUrl'

const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.config.globalProperties.$imgUrl = imgUrl
app.mount('#app')
