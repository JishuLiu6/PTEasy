<template>
  <div id="app-view">
    <div id="app-view-router">
      <span style="color:white;font-size:36px;margin-right: 40px;cursor:default;user-select: none;">PtEasy</span>
      <router-link to="/about">压制组</router-link>
      <router-link to="/about">存储设备</router-link>
      <router-link to="/about">保种软件</router-link>
      <router-link to="/about">备份</router-link>
      <router-link to="/about">恢复</router-link>
    </div>
    <div id="server-list">
      <div id="server-list-left" style="display: flex;align-items: center;">
        <!-- <p style="color:white;writing-mode: vertical-lr;text-align: center;">本机</p> -->
        <div class="server-list-item server-list-item-active">
          <el-image :src="$imgUrl('pteasy_logo.png')" class="server-list-img"></el-image>
          <div class="server-list-item-info">
            <div class="connect-icon"></div>
            <span>PtEasy</span>
          </div>
        </div>
      </div>
      <div id="server-list-left" style="display: flex;align-items: center;">
        <p style="color:white;writing-mode: vertical-lr;text-align: center;">存储设备</p>
        <div class="server-list-item">
          <el-image :src="$imgUrl('dsm.png')" class="server-list-img"></el-image>
          <div class="server-list-item-info">
            <div class="connect-icon"></div>
            <span>192.168.195.100</span>
          </div>
        </div>
      </div>
      <div id="server-list-right" style="display: flex;">
        <p style="color:white;writing-mode: vertical-lr;text-align: center;">保种软件</p>
        <div class="server-list-item">
          <el-image :src="$imgUrl('qb.jpeg')" class="server-list-img"></el-image>
          <div class="server-list-item-info">
            <div class="connect-icon"></div>
            <span>下载:1</span>
            <span>保种:100</span>
          </div>
        </div>
        <div class="server-list-item">
          <el-image :src="$imgUrl('utorrent.jpeg')" class="server-list-img"></el-image>
          <div class="server-list-item-info">
            <div class="connect-icon"></div>
            <span>下载:1</span>
            <span>保种:100</span>
          </div>
        </div>
      </div>
    </div>
    <router-view />
  </div>
</template>

<script setup>
import { getCurrentInstance } from 'vue'
const { proxy } = getCurrentInstance();
const { $imgUrl } = proxy;
</script>

<style scoped>
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

#app-view {
  height: 100vh;
}

#server-list {
  /* margin-top: 20px; */
  display: flex;
  width: 1160px;
  margin: 20px auto 0 auto;
}

.server-list-item {
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-right: 50px;
}


.server-list-item-active:after {
  content: "";
  position: absolute;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 20px 20px;
  border-color: transparent transparent white;
  top: 208px;
}

.connect-icon {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #00ff00;
  margin-right: 5px;
}

.server-list-item-info {
  display: flex;
  /* display: inline-block; */
  align-items: center;
  justify-content: center;
  overflow: hidden;
  min-width: 84px;
  padding: 0 10px;
  font-size: 12px;
  height: 24px;
  line-height: 24px;
  margin: 10px auto;
  border-radius: 24px;
  color: white;
  background: #2065ac;
}

.server-list-item-info>span {
  margin-right: 3px;
  opacity: .5;
}

.server-list-item-info>span:hover {
  opacity: 1;
}

.server-list-img {
  width: 100px;
  height: 100px;
  border: 1px dashed #989898;
  box-shadow: 0 0.5625rem 1.5rem 0 rgb(82, 96, 250);
  padding: 5px;
}

.server-list-img:hover {
  background-color: white;
}</style>