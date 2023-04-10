<template>
  <div id="app-view">
    <el-container style="height: 100vh">
      <el-aside width="230px" style="background-color: rgb(231, 235, 239);">
        <el-scrollbar>
          <div id="logo">PtEasy</div>
          <el-menu :default-openeds="['1']" style="
                    --el-menu-text-color: #1d273b;
                    --el-menu-hover-text-color: #1d273b;
                    --el-menu-bg-color: transparent;
                    --el-menu-hover-bg-color: rgb(255, 255, 255);
                    --el-menu-active-color: black;
                    --el-menu-item-font-size: 1.1rem;
                    --el-menu-item-height: 45px;
                    ">
            <el-menu-item index="2">
              <template #title>
                站点
              </template>
            </el-menu-item>
            <el-menu-item index="4">
              <template #title>
                设置
              </template>
            </el-menu-item>
            <el-menu-item index="5">
              <template #title>
                通知
              </template>
            </el-menu-item>
            <el-menu-item index="6">
              <template #title>
                备份
              </template>
            </el-menu-item>
            <el-menu-item index="3">
              <template #title>
                下载器
              </template>
            </el-menu-item>
            <el-menu-item index="1">
              <template #title>
                数据统计
              </template>
            </el-menu-item>
          </el-menu>
        </el-scrollbar>
      </el-aside>
      <el-container>
        <el-header class="app-header">
          <div class="app-header-title">设置</div>
          <div class="app-header-setting">
            <!-- <el-icon size="2em" class="mr-8"><notification/></el-icon> -->
            
            <i class="bi bi-card-checklist text-3xl mr-8"></i>
            <img class="header-image" src="https://avatars.githubusercontent.com/u/32886897?s=40&v=4"
              @click="showHeaderSetting" />
            <el-dropdown ref="headerSetting" trigger="contextmenu">
              <el-icon class="el-icon--right">
                <i class="bi bi-caret-down-fill text-sm" @click="showHeaderSetting"></i>
              </el-icon>
              <template #dropdown>
                <el-dropdown-menu>
                  <el-dropdown-item>设置</el-dropdown-item>
                  <el-dropdown-item>登出</el-dropdown-item>
                </el-dropdown-menu>
              </template>
            </el-dropdown>
          </div>
        </el-header>
        <el-main>
          <el-scrollbar>
            <router-view />
          </el-scrollbar>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup>
import { ref } from 'vue'
// import { io } from 'socket.io-client';
// import { ref, onMounted, onActivated } from "vue"
// const socket = io('http://127.0.0.1:8999');
// socket.emit('startFileTask', '/Users/jishuliu/Desktop/PTEasy/PTEasy-backend')
// socket.on("start_file_task", (data) => {
//   console.log(data)
// });
// socket.on("step_error", (data) => {
//   console.log(data)
// });
// socket.on("step_file_task", (data) => {
//   console.log(data)
// });
const headerSetting = ref()
function showHeaderSetting() {
  console.log(headerSetting)
  headerSetting.value.handleOpen()
}
</script>

<style scoped lang="scss">
#logo {
  color: #034783;
  font-size: 36px;
  cursor: default;
  user-select: none;
  text-align: center;
  margin: 20px 0;
}

.el-menu-item {
  margin: 0 10px;
  border-radius: 8px;
}

.el-menu-item.is-active {
  background-color: rgba(123, 178, 233, 0.5) !important;
}

#app-view {
  height: 100vh;

  #app-view-router {
    width: 1160px;
    margin: auto;
    height: 52px;
    display: flex;
    align-items: center;
  }

  #app-view-router a {
    opacity: .5;
    filter: alpha(opacity=50);
    color: #fff;
    text-decoration: none;
    font-size: 18px;
    line-height: 1.2;
    text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.3);
    margin-right: 20px;
  }

  #app-view-router a:hover {
    opacity: 1;
  }
}

.app-header {
  border-bottom: 1px solid rgba(0, 0, 0, 0.06);
  margin: 0 10px;
  display: flex;
  align-items: center;
  justify-content: space-between;

  &-title {
    font-size: 20px;
    font-weight: bolder;
    // margin-right: 5px;
    color: #034783;
    display: flex;
    line-height: 60px;
  }

  &-setting {
    display: flex;
    align-items: center;
    .header-image {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      cursor: pointer;
    }
  }
}
</style>