import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  server:{
    cors: true, // 默认启用并允许任何源
    proxy:{
      '/local': {
        target: 'http://127.0.0.1:9900/',
        changeOrigin: true,
        configure: (proxy, options) => {
          console.log(proxy, options)
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
  }
})
