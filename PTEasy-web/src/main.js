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
// 导入表格
import Vue3EasyDataTable from 'vue3-easy-data-table';
import 'vue3-easy-data-table/dist/style.css';
import fm from './store';

const app = createApp(App)

const store = createStore({
    modules: { fm },
});

app.use(store)
app.use(router)
app.component('EasyDataTable', Vue3EasyDataTable);
app.use(ElementPlus)
app.config.globalProperties.$imgUrl = imgUrl
app.mount('#app')
