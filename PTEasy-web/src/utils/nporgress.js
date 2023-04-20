import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

// 开启进度条
export function start(color = 'var(--el-color-primary-light-3)') {
    NProgress.configure({
        showSpinner: false,
        minimum: 0.1,
        easing: 'ease',
        speed: 500,
        trickleRate: 0.02,
        trickleSpeed: 200,
        parent: '#app'
    })
    
    // 修改进度条颜色
    const css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = `#nprogress .bar { background: ${color}; }`;
    document.head.appendChild(css);

    NProgress.start()
}

// 关闭进度条
export const close = () => {
    NProgress.done()
};
