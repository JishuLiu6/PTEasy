<template>
  <div class="flex flex-col p-6 max-h-screen rounded-md bg-white m-6 shadow-md">
    <div class="l-block-shadow flex-grow rounded-lg p-4" style="height: 65vh">
      <el-table :data="tableData" class="text-sm" max-height="60vh">
        <el-table-column label="站点名" prop="siteName"></el-table-column>
        <el-table-column label="用户名" prop="username"></el-table-column>
        <el-table-column label="等级" prop="level"></el-table-column>
        <el-table-column label="数据量" prop="dataSize"></el-table-column>
        <el-table-column label="分享率" prop="shareRatio"></el-table-column>
        <el-table-column label="做种数" prop="seedingCount"></el-table-column>
        <el-table-column label="做种体积" prop="seedingSize"></el-table-column>
        <el-table-column label="魔力值/积分" prop="magicPoints"></el-table-column>
        <el-table-column label="时魔" prop="timeMagic"></el-table-column>
        <el-table-column label="入会时间" prop="entryTime"></el-table-column>
        <el-table-column label="数据更新时间" prop="updateTime"></el-table-column>
        <el-table-column label="状态" prop="status" min-width="120">
          <template v-slot="{ row }">
            <span class="px-2 py-1 rounded text-white" :style="statusStyle(row.status)">
              {{ row.status }}
            </span>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="180">
          <template v-slot="{ row }">
            <el-button type="text" @click="refresh(row)">刷新</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
  <el-dialog title="添加站点" :visible.sync="addDialogVisible">
    <el-form :model="addFormData" label-width="120px">
      <el-form-item label="站点名">
        <el-input v-model="addFormData.siteName"></el-input>
      </el-form-item>
      <el-form-item label="用户名">
        <el-input v-model="addFormData.username"></el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button @click="addDialogVisible = false">取消</el-button>
      <el-button type="primary" @click="addSite">添加站点</el-button>
    </template>
  </el-dialog>
</template>
<script setup>
import { ref } from 'vue';


const tableData = ref([
  {
    "siteName": "Site C",
    "username": "User3",
    "level": "Gold",
    "dataSize": 94,
    "shareRatio": "0.50",
    "seedingCount": 31,
    "seedingSize": 461,
    "magicPoints": 79,
    "timeMagic": 4,
    "entryTime": "2017-10-09 22:17",
    "updateTime": "2019-11-20 13:06",
    "status": "Active"
  },
  {
    "siteName": "Site D",
    "username": "User7",
    "level": "VIP",
    "dataSize": 17,
    "shareRatio": "0.48",
    "seedingCount": 12,
    "seedingSize": 40,
    "magicPoints": 85,
    "timeMagic": 8,
    "entryTime": "2020-06-14 22:33",
    "updateTime": "2021-03-23 15:05",
    "status": "Active"
  },
  {
    "siteName": "Site E",
    "username": "User5",
    "level": "Bronze",
    "dataSize": 5,
    "shareRatio": "0.35",
    "seedingCount": 7,
    "seedingSize": 103,
    "magicPoints": 24,
    "timeMagic": 6,
    "entryTime": "2019-06-16 15:03",
    "updateTime": "2021-02-10 00:43",
    "status": "Inactive"
  },
  {
    "siteName": "Site C",
    "username": "User6",
    "level": "Gold",
    "dataSize": 58,
    "shareRatio": "0.17",
    "seedingCount": 13,
    "seedingSize": 424,
    "magicPoints": 15,
    "timeMagic": 0,
    "entryTime": "2018-01-26 12:49",
    "updateTime": "2022-02-18 10:29",
    "status": "Inactive"
  },
  {
    "siteName": "Site A",
    "username": "User1",
    "level": "VIP",
    "dataSize": 63,
    "shareRatio": "0.39",
    "seedingCount": 7,
    "seedingSize": 370,
    "magicPoints": 21,
    "timeMagic": 8,
    "entryTime": "2021-02-09 11:02",
    "updateTime": "2022-01-22 20:41",
    "status": "Inactive"
  }]);


const totalRows = ref(0);
const addDialogVisible = ref(false);
const addFormData = ref({
  siteName: '',
  username: '',
});

function openAddDialog() {
  addDialogVisible.value = true;
}

function handlePageChange(page) {
  // Fetch data for the selected page
}

function refresh(row) {
  // Refresh data for the selected row
}

function addSite() {
  // Add a new site with the provided data
  addDialogVisible.value = false;
}
function statusStyle(status) {
  switch (status) {
    case "Active":
      return { backgroundColor: "var(--el-color-success)" };
    case "Inactive":
      return { backgroundColor: "var(--el-color-warning)" };
    default:
      return { backgroundColor: "var(--el-color-info)" };
  }
}

</script>
<style scoped lang="scss">
@import '@/assets/scss/main.scss';
</style>