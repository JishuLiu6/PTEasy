import { createApp } from 'vue'
import { createStore } from 'vuex'
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
// store
import fm from './store';

const app = createApp(App)
const store = createStore({
    modules: { fm },
});
app.use(router)
app.use(store)
app.use(ElementPlus)
app.config.globalProperties.$imgUrl = imgUrl
app.mount('#app')
