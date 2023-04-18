<template>
  <div class="h-screen flex">
    <div class="sidebar">
      <div class="logo mb-6">PtEasy</div>
      <el-menu :default-openeds="['1']" class="menu">
          <el-menu-item index="2" class="my-4">
            <template #title>
              <i class="bi-house-door text-2xl"></i>
              <span class="ml-4">站点</span>
            </template>
          </el-menu-item>
          <el-menu-item index="4" class="my-4">
            <template #title>
              <i class="bi-gear text-2xl"></i>
              <span class="ml-4">设置</span>
            </template>
          </el-menu-item>
          <el-menu-item index="5" class="my-4">
            <template #title>
              <i class="bi-bell text-2xl"></i>
              <span class="ml-4">通知</span>
            </template>
          </el-menu-item>
          <el-menu-item index="6" class="my-4">
            <template #title>
              <i class="bi-cloud-arrow-down text-2xl"></i>
              <span class="ml-4">备份</span>
            </template>
          </el-menu-item>
          <el-menu-item index="3" class="my-4">
            <template #title>
              <i class="bi-download text-2xl"></i>
              <span class="ml-4">下载器</span>
            </template>
          </el-menu-item>
          <el-menu-item index="1" class="my-4">
            <template #title>
              <i class="bi-bar-chart text-2xl"></i>
              <span class="ml-4">数据统计</span>
            </template>
          </el-menu-item>
        </el-menu>
    </div>
    <div class="flex-grow flex flex-col">
      <div class="topbar">
        <div class="topbar-title text-3xl font-bold">设置</div>
        <div class="flex items-center space-x-8 ml-auto">
          <i class="bi-file-text text-3xl text-white"></i>
          <i class="bi-gear-fill text-3xl text-white"></i>
          <el-dropdown class="mr-4">
            <span class="el-dropdown-link">
              <i class="bi-person-circle text-3xl text-white"></i>
            </span>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>个人信息</el-dropdown-item>
              <el-dropdown-item>退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
        <!-- 添加搜索框、用户信息等元素 -->
      </div>
      <div class="main-content bg-white p-8">
        <!-- 主要内容 -->
        <router-view />
      </div>
    </div>
  </div>
</template>

<script setup>
// 你的脚本代码
</script>
<style scoped lang="scss">
@import './assets/scss/variables.scss';

.sidebar {
  width: 25rem;
  background-color: $sidebar-bg-color;
  padding: $sidebar-padding;
  display: flex;
  flex-direction: column;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}


.logo {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
  color: $logo-text-color;
  background: $logo-bg-gradient;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-transform: uppercase;
  letter-spacing: 0.1rem;
}


.el-menu {
  --el-menu-text-color: #3c2f5b;
  --el-menu-hover-text-color: #6d28d9;
  --el-menu-bg-color: transparent;
  --el-menu-hover-bg-color: rgba(109, 40, 217, 0.1);
  --el-menu-active-color: #3c2f5b;
  --el-menu-item-font-size: 1.4rem;
  --el-menu-item-height: 55px;
  border: none;
  color: #ffffff;
  flex-grow: 1;

  &__item {
    font-size: var(--el-menu-item-font-size);
    height: var(--el-menu-item-height);
  }
  
  &__item--active {
    color: var(--el-menu-active-color);
  }
  
  &__item:hover {
    color: var(--el-menu-hover-text-color);
    background-color: var(--el-menu-hover-bg-color);
  }
  
  &__item.is-active {
    color: var(--el-menu-active-color);
  }
  
  &__item.is-disabled {
    color: #ccc;
  }
  
  &__background {
    background-color: var(--el-menu-bg-color);
  }
}


.topbar {
  background-color: $topbar-bg-color;
  color: white;
  border-bottom: none;
  padding: 1.5rem 3rem;
  display: flex;
  align-items: center;
}

.topbar-title {
  margin-right: auto;
  font-size: 1.5rem;
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
  background-color: #f5f7fa;
  padding: 2rem;
}
</style>
