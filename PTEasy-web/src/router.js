import { createRouter, createWebHistory } from 'vue-router'
// 导入进度条
import { start, close } from "@/utils/nporgress";

const routes = [
    {
        path: '/',
        name: 'home',
        component: () => import('./views/Home.vue'),
        meta: {
            title: '首页'
        }
    },
    {
        path: '/nas',
        name: 'nas',
        component: () => import('./views/Nas.vue'),
        meta: {
            title: 'NAS'
        }
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes // `routes: routes` 的缩写
})

// 加载更改标题
router.beforeEach((to, from, next) => {
    start();
    const title = to.meta && to.meta.title;
    if (title) {
        document.title = title;
    }
    next();
});

router.afterEach(() => {
    close()
})


export {
    router
};
