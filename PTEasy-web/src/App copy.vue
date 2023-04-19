<template>
  <div class="h-screen flex" :class="themeClass">
    <div class="sidebar">
      <div class="logo mb-6">PtEasy</div>
      <el-menu :default-openeds="['1']" class="menu">
        <el-menu-item v-for="(t_route, index) in sidebarRoutes" :key="index" :index="index" class="my-4"
          @click.native="handleRouteClick(t_route.path)">
          <a href="javascript:void(0)" class="flex items-center">
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
          <i class="icon bi-file-text text-3xl text-white" @click="handleRouteClick('logs')"></i>
          <el-popover placement="bottom" :width="250" trigger="hover" style="--el-popover-padding: 0">
            <template #reference>
              <i class="bi bi-gear-fill mr-8 text-3xl text-white"
                :class="hasActiveTasks ? 'text-blue-500' : 'text-gray-600'"></i>
            </template>
            <div class="rounded-lg bg-white shadow-md pt-3 pb-5">
              <div class="text-lg font-semibold text-gray-700 px-3 mb-2">活动</div>
              <div v-for="index in 3" :key="index"
                class="border-gray-300 border-b-2 border-dashed hover:bg-violet-100 cursor-pointer p-3">
                <div class="text-xs text-gray-600">扫描文件夹</div>
                <div class="text-xs text-gray-500">/Users/jishuliu/SMSBoom</div>
                <div>
                  <el-progress :percentage="percentage2" :color="colors"></el-progress>
                </div>
              </div>
            </div>
          </el-popover>
          <i class="bi bi-palette text-3xl text-white ml-8" @click="toggleTheme"></i>
        </div>
      </div>
      <div class="main-content">
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
const themeClass = ref('theme-light');

onMounted(() => {
  document.documentElement.classList.add(themeClass.value);

  sidebarRoutes.value = router.options.routes.filter(
    (route) => !route.meta.hideSidebar
  );
});

onUnmounted(() => {
  document.documentElement.classList.remove(themeClass.value);
});



const toggleTheme = () => {
  document.documentElement.classList.remove(themeClass.value);
  themeClass.value = themeClass.value === 'theme-light' ? 'theme-dark' : 'theme-light';
  document.documentElement.classList.add(themeClass.value);
};

const handleRouteClick = (path) => {
  router.push(path);
};
</script>


<style lang="scss">
@import './assets/scss/main.scss';

.sidebar {
  width: 18rem;
  background-color: var(--sidebar-bg-color);
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
  color: var(--logo-text-color);
  background: var(--logo-bg-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-transform: uppercase;
  letter-spacing: 0.1rem;
  cursor: pointer;
  border-radius: 5px;
  // background-color: rgba(0, 0, 0, 0.1);

  &:hover::before {
    animation: shine 1.5s linear infinite;
  }

  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 30%;
    height: 100%;
    background-image: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.8) 50%, rgba(255, 255, 255, 0) 100%);
    transform: skewX(-25deg);
    opacity: 0.5;
    pointer-events: none;
  }
}

.theme-dark .logo::before {
  background-image: linear-gradient(90deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 50%, rgba(0, 0, 0, 0) 100%);
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
  --el-menu-text-color: var(--text-color);
  --el-menu-bg-color: transparent;
  --el-menu-item-font-size: 1.4rem;
  --el-menu-item-height: 60px;
  border: none !important;
  flex-grow: 1;
}

.el-menu-item {
  margin-bottom: 1rem; // 增加菜单项之间的间距
  border-radius: 6px;
  user-select: none;
  transition: all 0.3s ease; // 添加过渡效果

  &:hover {
    color: var(--accent-color);
    background-color: var(--menu-item-hover-color) !important;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  }
}


.el-menu-item.is-active {
  color: var(--primary-color) !important;
  background-color: var(--menu-item-active-color) !important;
  border-radius: 6px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  font-weight: bold; // 使激活状态下的菜单项加粗
}

.topbar {
  height: 4rem; // 增加顶部栏高度
  background-color: var(--topbar-bg-color);
  color: white;
  border-bottom: none;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  z-index: 11;
  transition: all 0.3s ease; // 添加过渡效果
}

.topbar-title {
  margin-right: auto;
  font-size: 1.5rem;
  transition: color 0.3s ease; // 添加过渡效果
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
  --el-popover-background-color: rgba(109, 40, 217, 0.15) !important;
  ;
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
</style>
