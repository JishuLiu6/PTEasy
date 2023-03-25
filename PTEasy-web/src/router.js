import { createRouter, createWebHistory } from 'vue-router'

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
    // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
    history: createWebHistory(),
    routes, // `routes: routes` 的缩写
})

// 加载更改标题
router.beforeEach((to, from, next) => {
    const title = to.meta && to.meta.title;
    if (title) {
        document.title = title;
    }
    next();
});

export {
    router
};
