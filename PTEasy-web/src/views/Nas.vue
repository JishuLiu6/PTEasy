<template>
  <div id="home">
    <div id="home-content">
      <div style="margin-bottom: 10px;display: flex;justify-content: space-between;">
        <div style="display:flex">
          <div style="margin-right: 20px;">
            <span class="search_title">保种路径:</span>
            <el-select placeholder="请选择" style="width: 150px;">
              <el-option label="全部" value="all"></el-option>
              <el-option label="E:\\" value="E:\\"></el-option>
              <el-option label="F:\\" value="F:\\"></el-option>
              <el-option label="G:\\" value="G:\\"></el-option>
            </el-select>
          </div>
          <div>
            <span class="search_title">种子路径:</span>
            <el-select placeholder="请选择" style="width: 150px;">
              <el-option label="全部" value="all"></el-option>
              <el-option label="E:\\" value="E:\\"></el-option>
              <el-option label="F:\\" value="F:\\"></el-option>
              <el-option label="G:\\" value="G:\\"></el-option>
            </el-select>
          </div>
        </div>
        <div>
          <span class="search_title">搜索:</span>
          <el-input placeholder="请输入内容" style="width: 200px;"></el-input>
        </div>
      </div>
      <EasyDataTable :headers="resourceHeaders" :items="resourceData" alternating border-cell buttons-pagination
        table-height="462">
        <template #item-yazigroup="item">
          <el-tag>{{ item.yazigroup }}</el-tag>
        </template>
        <template #item-save_software="item">
          <el-checkbox-group>
            <el-checkbox label="QB"></el-checkbox>
            <el-checkbox label="UT"></el-checkbox>
            <el-checkbox label="TR"></el-checkbox>
          </el-checkbox-group>
        </template>
      </EasyDataTable>
    </div>
  </div>
</template>

<script lang="ts" setup>
import type { Header, Item } from "vue3-easy-data-table";

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
  { text: "资源路径", value: "save_path" },
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
#home {
  width: 1160px;
  margin: 0 auto;
}

#home-content {
  width: 1160px;
  height: 70vh;
  background: #fff;
  box-shadow: 0 0.5625rem 1.5rem 0 rgb(0 0 0 / 50%);
  border-radius: 10px;
  padding: 20px;
  margin-top: 5px;
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

.search_title {
  font-size: 14px;
  /* font-weight: bolder; */
  margin-right: 5px;
}
</style>