import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  build:{
    outDir: '../PTEasy-backend/app/templates', // 输出目录
  },
  base: process.env.VUE_APP_BASE_API,
  server:{
    cors: true, // 默认启用并允许任何源
    proxy:{
      '/v1': {
        target: 'http://127.0.0.1:8999/',
        changeOrigin: true,
        configure: (proxy, options) => {
          // proxy 是 'http-proxy' 的实例
        }
      },
    },
  },
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  css: {
    postcss: {
      plugins: [require("tailwindcss"), require("autoprefixer")]
    }
  }
})
