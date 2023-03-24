<template>
  <div id="home">
    <div id="server-list">
      <div id="server-list-left" style="display: flex;align-items: center;">
        <p style="color:white;writing-mode: vertical-lr;text-align: center;">本机</p>
        <div class="server-list-item">
          <el-image :src="$imgUrl('pteasy_logo.png')" class="server-list-img"></el-image>
          <div class="server-list-item-info">
            <div class="connect-icon"></div>
            <span>PtEasy</span>
          </div>
        </div>
      </div>
      <div id="server-list-left" style="display: flex;align-items: center;">
        <p style="color:white;writing-mode: vertical-lr;text-align: center;">NAS</p>
        <div class="server-list-item">
          <el-image :src="$imgUrl('dsm.png')" class="server-list-img"></el-image>
          <div class="server-list-item-info">
            <div class="connect-icon"></div>
            <span>192.168.195.100</span>
          </div>
        </div>
      </div>
      <div id="server-list-right" style="display: flex;">
        <p style="color:white;writing-mode: vertical-lr;text-align: center;">下载器</p>
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
    <div id="home-content">
      <el-tabs type="border-card" tabPosition="left">
        <el-tab-pane label="下载资源汇总">
          <EasyDataTable :headers="resourceHeaders" :items="resourceData" alternating border-cell buttons-pagination />
        </el-tab-pane>
        <el-tab-pane label="种子资源匹配">
          <EasyDataTable :headers="torrentHeaders" :items="torrentData" alternating border-cell buttons-pagination />
        </el-tab-pane>
      </el-tabs>

    </div>
  </div>
</template>

<script lang="ts" setup>
import type { Header, Item } from "vue3-easy-data-table";
import { getCurrentInstance } from 'vue'
const { proxy } = getCurrentInstance();
const { $imgUrl } = proxy;

const torrentHeaders: Header[] = [
  { text: "种子路径", value: "torrent_path" },
  { text: "做种数", value: "torrent_state.save" },
  { text: "种子数", value: "torrent_state.save" },
]

const torrentData: Item[] = [
  {
    torrent_path: 'E:\\',
    torrent_state: {
      save: 1,
      torrent: 2,
    },
    save_file_list: [
      {
        file_path: 'F:\\stata',
        file_state: {
          seed: 1,
          torrent: 1,
        },
        size: '100M'
      },
      {
        file_path: 'D:\\QQQ',
        file_state: {
          seed: 1,
          torrent: 1,
        },
        size: "200M"
      },
    ],
  },
  {
    torrent_path: 'E:\\',
    torrent_state: {
      save: 1,
      torrent: 2,
    },
    save_file_list: [
      {
        file_path: 'F:\\stata',
        file_state: {
          seed: 1,
          torrent: 1,
        },
        size: '100M'
      },
      {
        file_path: 'D:\\QQQ',
        file_state: {
          seed: 1,
          torrent: 1,
        },
        size: "200M"
      },
    ],
  }
]
const resourceHeaders: Header[] = [
  { text: "资源名称", value: "name" },
  { text: "资源类型", value: "type" },
  { text: "资源大小", value: "size" },
  { text: "保种路径", value: "save_path" },
  { text: "压制组", value: "yazigroup" },
  { text: "保种软件", value: "save_software" },
]
const resourceData = [
  {
    name: '苏有朋版倚天屠龙记.40集全.2003.简繁中字￡CMCT暮雨潇潇',
    type: '视频',
    size: '100M',
    save_path: 'F:\\state\mjtt',
    yazigroup: 'CMCT',
    save_software: 'qb',
  },
  {
    name: '苏有朋版倚天屠龙记.40集全.2003.简繁中字￡CMCT暮雨潇潇',
    type: '视频',
    size: '100M',
    save_path: 'F:\\state\mjtt',
    yazigroup: 'CMCT',
    save_software: 'qb',
  },
  {
    name: '苏有朋版倚天屠龙记.40集全.2003.简繁中字￡CMCT暮雨潇潇',
    type: '视频',
    size: '100M',
    save_path: 'F:\\state\mjtt',
    yazigroup: 'CMCT',
    save_software: 'qb',
  },
  {
    name: '苏有朋版倚天屠龙记.40集全.2003.简繁中字￡CMCT暮雨潇潇',
    type: '视频',
    size: '100M',
    save_path: 'F:\\state\mjtt',
    yazigroup: 'CMCT',
    save_software: 'qb',
  },
  {
    name: '苏有朋版倚天屠龙记.40集全.2003.简繁中字￡CMCT暮雨潇潇',
    type: '视频',
    size: '100M',
    save_path: 'F:\\state\mjtt',
    yazigroup: 'CMCT',
    save_software: 'qb',
  },
]
</script>
<style scoped>
#server-list {
  margin-top: 20px;
  display: flex;
}

.server-list-item {
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-right: 50px;
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
  padding: 5px;
}

.server-list-img:hover {
  background-color: white;
}


#home {
  width: 1160px;
  margin: 0 auto;
}

#home-content {
  width: 1160px;
  height: 60vh;
  /*background: #fff;*/
  border-radius: 10px;
  margin-top: 20px;
  padding-top: 20px;
}

#torrent-table {
  width: 80%;
  margin: 0 auto;
}

#server-add {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 100px;
  border: 1px dashed #989898;
  border-radius: 10px;
  margin-right: 50px;
  background: white;
}
</style>