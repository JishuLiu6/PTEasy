<template>
  <div class="h-screen flex overflow-hidden">
    <div class="sidebar">
      <div class="logo mb-6">PtEasy</div>
      <el-menu :default-openeds="['1']" class="menu">
        <el-menu-item v-for="(t_route, index) in sidebarRoutes" :key="index" :index="index" class="my-4"
          :class="{ 'is-active': t_route.path === $route.path }" @click.native="handleRouteClick(t_route.path)">
          <a class="flex items-center">
            <i :class="[t_route.meta.icon, 'text-2xl']"></i>
            <span class="ml-4 inline-block align-middle">{{ t_route.meta.title }}</span>
          </a>
        </el-menu-item>
      </el-menu>
    </div>
    <div class="flex-grow flex flex-col">
      <div class="topbar">
        <div class="topbar-title text-3xl font-bold">{{ $route.meta.title }}</div>
        <div class="flex items-center space-x-8 ml-auto">
          <el-popover placement="bottom" :width="250" trigger="hover" style="--el-popover-padding: 0">
            <template #reference>
              <i class="bi bi-gear-fill mr-4 text-2xl" :class="hasActiveTasks ? 'text-primary' : 'text-default'"
                @click="handleRouteClick('logs')"></i>
            </template>
            <div class="rounded-lg bg-white shadow-md py-3 px-2">
              <div class="text-lg font-semibold text-gray-600 mb-2 border-b border-gray-300 pb-2">活动</div>
              <div v-for="(item, index) in activityList" :key="index"
                class="border-gray-300 cursor-pointer p-4 hover:bg-gray-100">
                <div class="text-xs text-gray-600">{{ item.title }}</div>
                <div class="text-xs text-gray-500">{{ item.path }}</div>
                <div>
                  <el-progress :percentage="item.percentage" :color="item.color"></el-progress>
                </div>
              </div>
            </div>
          </el-popover>

          <el-popover placement="bottom" trigger="hover" :width="200" style="--el-popover-padding: 0">
            <template #reference>
              <i class="bi bi-palette text-3xl text-white ml-8"></i>
            </template>
            <div class="rounded-lg bg-white shadow-md py-3 px-2">
              <div class="text-lg font-semibold text-gray-600 mb-2 border-b border-gray-300 pb-2">选择主题</div>
              <div class="grid grid-cols-1 gap-2">
                <div v-for="(theme, index) in themes" :key="index"
                  class="flex items-center cursor-pointer py-2 px-3 rounded-lg hover:bg-gray-100" :class="[{ 'bg-gray-100': themeClass === theme.name },
                  { 'text-gray-800': themeClass === theme.name },
                  { 'opacity-70': themeClass !== theme.name }]" @click="changeTheme(theme.name)">
                  <div class="w-6 h-6 rounded-full mr-2 border border-gray-400" :class="'bg-' + theme.color"></div>
                  <div class="text-sm font-medium">{{ theme.name.slice(6) }}</div>
                </div>
              </div>
            </div>
          </el-popover>
        </div>
      </div>
      <div class="main-content h-full">
          <transition name="fade" mode="out-in">
            <router-view />
          </transition>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { router } from './router';

const sidebarRoutes = ref([]);

const themeClass = ref(localStorage.getItem('themeClass') || 'theme-red');

const themes = ref([
  { name: 'theme-red', color: 'red' },
  { name: 'theme-orange', color: 'orange' },
  { name: 'theme-green', color: 'green' }
]);

const activityList = ref([
  {
    name: '扫描文件夹',
    path: '/Users/jishuliu/SMSBoom',
    percentage: Math.floor(Math.random() * 101),
    color: 'primary'
  },
  {
    name: '上传文件',
    path: '/Users/jishuliu/Documents/Resume',
    percentage: Math.floor(Math.random() * 101),
    color: 'success'
  },
  {
    name: '下载文件',
    path: '/Users/jishuliu/Documents/Notes',
    percentage: Math.floor(Math.random() * 101),
    color: 'warning'
  }
])

const changeTheme = (newTheme) => {
  document.documentElement.classList.remove(themeClass.value);
  themeClass.value = newTheme;
  document.documentElement.classList.add(themeClass.value);
  localStorage.setItem('themeClass', newTheme); // 保存用户选择的主题到本地存储
};

const handleRouteClick = (path) => {
  router.push(path);
};

onMounted(() => {
  document.documentElement.classList.add(themeClass.value);

  sidebarRoutes.value = router.options.routes.filter(
    (route) => !route.meta.hideSidebar
  );
});

</script>
<style lang="scss">
@import './assets/scss/main.scss';

.sidebar {
  min-width: 18rem;
  background-color: var(--el-color-primary-light-9);
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  z-index: 10;
}

.logo {
  position: relative;
  display: inline-block;
  padding: 5px 10px;
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 2rem;
  color: var(--el-text-color-primary);
  background: var(--logo-bg-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-transform: uppercase;
  letter-spacing: 0.1rem;
  cursor: pointer;
  border-radius: 5px;
}

@keyframes shine {
  0% {
    left: -30%;
  }

  100% {
    left: 50%;
  }
}

.el-menu {
  --el-menu-text-color: var(--el-text-color-primary);
  --el-menu-bg-color: transparent;
  --el-menu-item-font-size: 1.4rem;
  --el-menu-item-height: 60px;
  border: none !important;
  flex-grow: 1;
}

.el-menu-item {
  margin-bottom: 1rem;
  border-radius: 6px;
  user-select: none;
  transition: all 0.3s ease;

  &:hover {
    color: var(--el-color-primary-light-5);
    background-color: var(--el-color-primary-light-8) !important;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  }
}

.el-menu-item.is-active {
  color: var(--el-color-primary) !important;
  background-color: var(--el-color-primary-light-7) !important;
  border-radius: 6px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  font-weight: bold;
}

.topbar {
  min-height: 4rem;
  background-color: var(--el-color-primary);
  color: white;
  border-bottom: none;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  z-index: 11;
  // transition: all 0.3s ease;
  position: sticky
}

.topbar-title {
  margin-right: auto;
  font-size: 1.5rem;
  // transition: color 0.3s ease;
}

.bi-person-circle {
  font-size: 2.5rem;
}

.el-dropdown-menu {
  border-radius: 6px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

.main-content {
  flex-grow: 1;
  font-size: 1.1rem;
  @apply bg-gray-100;
}

.icon {
  padding: 0.5rem;
  border-radius: 6px;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: rgba(255, 255, 255, 0.2);
    cursor: pointer;
  }
}

.el-popover {
  --el-popover-background-color: var(--el-color-primary-light-7) !important;
  --el-popover-border-radius: 0.5rem;
}

.el-popover.el-popper {
  padding: 0 !important;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
.main-content{
  overflow-y: auto;
  scroll-behavior: smooth;
}
</style>