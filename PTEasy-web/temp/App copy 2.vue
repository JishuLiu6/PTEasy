<template>
  <div class="h-screen flex">

    <div class="flex-grow flex">
      <div class="flex-none w-56 bg-indigo-100 p-4">
        <div class="text-2xl font-bold mb-6 text-indigo-700">PtEasy</div>
        <el-menu :default-openeds="['1']" class="text-indigo-700">
          <el-menu-item index="2" class="my-2">
            <template #title>
              <i class="bi-house-door text-xl"></i>
              <span class="ml-2">站点</span>
            </template>
          </el-menu-item>
          <el-menu-item index="4" class="my-2">
            <template #title>
              <i class="bi-gear text-xl"></i>
              <span class="ml-2">设置</span>
            </template>
          </el-menu-item>
          <el-menu-item index="5" class="my-2">
            <template #title>
              <i class="bi-bell text-xl"></i>
              <span class="ml-2">通知</span>
            </template>
          </el-menu-item>
          <el-menu-item index="6" class="my-2">
            <template #title>
              <i class="bi-cloud-arrow-down text-xl"></i>
              <span class="ml-2">备份</span>
            </template>
          </el-menu-item>
          <el-menu-item index="3" class="my-2">
            <template #title>
              <i class="bi-download text-xl"></i>
              <span class="ml-2">下载器</span>
            </template>
          </el-menu-item>
          <el-menu-item index="1" class="my-2">
            <template #title>
              <i class="bi-bar-chart text-xl"></i>
              <span class="ml-2">数据统计</span>
            </template>
          </el-menu-item>
        </el-menu>
      </div>

      <div class="flex-grow bg-white p-4">
        <!-- 主要内容 -->
        
          <router-view />
        
      </div>
    </div>
  </div>
</template>

<script setup>
// 你的脚本代码
</script>

<style scoped>
.el-menu {
  --el-menu-text-color: #1d273b;
  --el-menu-hover-text-color: #1d273b;
  --el-menu-bg-color: transparent;
  --el-menu-hover-bg-color: rgb(255, 255, 255);
  --el-menu-active-color: black;
  --el-menu-item-font-size: 1.1rem;
  --el-menu-item-height: 45px;
}
</style>

