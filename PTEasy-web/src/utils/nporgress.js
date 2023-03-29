import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

// 开启进度条
export const start = () => {
    NProgress.start();
};

// 关闭进度条
export const close = () => {
    NProgress.done();
};
