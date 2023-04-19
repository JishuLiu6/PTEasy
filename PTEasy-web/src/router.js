import { createRouter, createWebHistory } from 'vue-router'
// 导入进度条
import { start, close } from "@/utils/nporgress";
import DashboardView from '@/views/DashboardView.vue'
import SiteView from '@/views/SiteView.vue'
import NotificationView from '@/views/NotificationView.vue'
import BackupView from '@/views/BackupView.vue'
import SettingView from '@/views/SettingView.vue'
import LogsView from '@/views/LogsView.vue'

const routes = [
    {
        path: '/',
        redirect: '/dashboard',
        meta: { title: '数据', hideSidebar: true }
    },
    {
        path: '/dashboard',
        name: 'DashboardView',
        component: DashboardView,
        meta: { title: '数据', icon: 'bi-bar-chart', hideSidebar: false }
    },
    {
        path: '/site',
        name: 'SiteView',

        component: SiteView,
        meta: { title: '站点', icon: 'bi-house-door', hideSidebar: false }
    },
    {
        path: '/notification',
        name: 'NotificationView',
        component: NotificationView,
        meta: { title: '通知', icon: 'bi-bell', hideSidebar: false }
    },
    {
        path: '/backup',
        name: 'BackupView',
        component: BackupView,
        meta: { title: '备份', icon: 'bi-cloud-arrow-down', hideSidebar: false }
    },
    {
        path: '/setting',
        name: 'SettingView',
        component: SettingView,
        meta: { title: '设置', icon: 'bi-gear', hideSidebar: false }
    },
    {
        path: '/download_server',
        name: 'DownloadServerView',
        component: SettingView,
        meta: { title: '下载器', icon: 'bi-download', hideSidebar: false }
    },
    {
        path: '/logs',
        name: 'LogsView',
        component: LogsView,
        meta: { title: '日志', icon: 'bi-file-text', hideSidebar: false  }
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
        document.title = `PTEASY-${title}`;
    }
    next();
});

router.afterEach(() => {
    close()
})


export {
    router
};
