<template>
  <div id="app-view">
    <div id="app-view-router">
      <router-link to="/">PtEasy</router-link>
      <!-- <router-link to="/">种子管理</router-link> -->
      <!-- <router-link to="/about">统计分析</router-link> -->
      <router-link to="/about">添加服务器</router-link>
    </div>
    <router-view />
  </div>
</template>

<script lang="ts" setup>
</script>

<style scoped>
#app-view-router{
  width: 1160px;
  margin: auto;
  height: 52px;
  display: flex;
  align-items: center;
}
#app-view-router a{
    opacity: .5;
    filter: alpha(opacity=50);
    color: #fff;
    text-decoration: none;
    font-size: 18px;
    line-height: 1.2;
    text-shadow: 1px 1px 1px rgba(0,0,0,0.3);
    margin-right: 20px;
}
#app-view-router a:hover{
    opacity: 1;
}
#app-view{
  height: 100vh;
}
</style>