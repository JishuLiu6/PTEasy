import { createApp } from 'vue'
import App from './App.vue'

// 导入tailwindcss
import "tailwindcss/tailwind.css"

// 导入element-plus
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
// normalize.css 用于重置浏览器默认样式
import 'normalize.css/normalize.css'

// 导入路由
import {router} from './router'
// 导入图片方法
import {imgUrl} from './utils/imgUrl'
// 导入图标
import "bootstrap-icons/font/bootstrap-icons.css";


const app = createApp(App)

// 导入自定义弹框
import CustomeDialog from "./components/CustomeDialog.vue";

app.component("pt-dialog", CustomeDialog);
import store from './store'; // 导入 store
app.use(store)
app.use(router)
// app.component('EasyDataTable', Vue3EasyDataTable);
app.use(ElementPlus)
app.config.globalProperties.$imgUrl = imgUrl
app.mount('#app')
