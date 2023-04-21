<template>
  <div class="container flex flex-col p-6 max-h-screen rounded-md bg-white m-6 shadow-md h-5/6">
    <div class="header py-4 px-8 bg-gray-100 flex items-center justify-between">
      <div class="header-right flex items-center">
        <div class="timestamps text-sm flex">
          <div class="mr-4">最近扫描时间: {{ recentScanTime }}</div>
          <div>上次备份时间: {{ lastBackupTime }}</div>
        </div>
      </div>
    </div>
    <div class="main flex-grow px-8 py-4 flex">
      <div class="main-left flex flex-col w-1/2 mr-8">
        <div class="chart flex-grow">
          <echarts-wrapper :data="chartData"></echarts-wrapper>
        </div>
      </div>
      <div class="main-right flex flex-col w-1/2">
        <div class="table-header flex justify-between items-center mb-2">
          <h3 class="text-lg font-semibold">种子文件夹</h3>
          <el-button @click="importResourceFolder" size="mini">导入</el-button>
        </div>
        <el-table :data="seedFolders" border style="width: 100%;" class="mb-4">
          <el-table-column label="种子文件夹" width="180" prop="name"></el-table-column>
          <el-table-column prop="size" label="大小" width="120"></el-table-column>
          <el-table-column prop="seeding" label="做种体积" width="120"></el-table-column>
          <el-table-column prop="notSeeding" label="未做种体积" width="120"></el-table-column>
          <el-table-column prop="free" label="空闲"></el-table-column>
          <el-table-column label="操作" width="120">
            <template v-slot="scope">
              <el-button @click="editResourceFolder(scope.$index)" size="mini">编辑</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="table-header flex justify-between items-center mb-2">
          <h3 class="text-lg font-semibold">资源文件夹</h3>
          <el-button @click="importResourceFolder" size="mini">导入</el-button>
        </div>
        <el-table :data="resourceFolders" border style="width: 100%;">
          <el-table-column label="资源文件夹" width="180" prop="name"></el-table-column>
          <el-table-column prop="size" label="大小" width="120"></el-table-column>
          <el-table-column prop="seeding" label="做种体积" width="120"></el-table-column>
          <el-table-column prop="notSeeding" label="未做种体积" width="120"></el-table-column>
          <el-table-column prop="free" label="空闲"></el-table-column>
          <el-table-column label="操作" width="120">
            <template v-slot="scope">
              <el-button @click="editResourceFolder(scope.$index)" size="mini">编辑</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>
<script>
import StorageCapacity from "@/components/StorageCapacity.vue";
import EchartsWrapper from "@/components/EchartsWrapper.vue";

export default {
  components: {
    StorageCapacity,
    EchartsWrapper,
  },
  data() {
    return {
      seedFolders: [],
      resourceFolders: [],
      chartData: [],
      recentScanTime: "",
      lastBackupTime: "",
      totalStorage: 200,
      usedStorage: 40
    };
  },
  methods: {
    importResourceFolder() {
      // 导入资源文件夹并解析文件信息
      // 示例数据，实际应用中需要替换为从文件系统获取的数据
      const newResourceFolder = {
        name: "资源文件夹",
        size: "50GB",
        seeding: "25GB",
        notSeeding: "15GB",
        free: "10GB"
      };
      this.resourceFolders.push(newResourceFolder);
    },
    importSeedFolder() {
      // 导入种子文件夹并解析文件信息
      // 示例数据，实际应用中需要替换为从文件系统获取的数据
      const newSeedFolder = {
        name: "种子文件夹",
        size: "80GB",
        seeding: "45GB",
        notSeeding: "25GB",
        free: "10GB"
      };
      this.seedFolders.push(newSeedFolder);
    }
  },
  created() {
    // 在这里填充示例数据
    this.seedFolders = [
      {
        name: "种子文件夹 1",
        size: "80GB",
        seeding: "45GB",
        notSeeding: "25GB",
        free: "10GB"
      },
      {
        name: "种子文件夹 2",
        size: "120GB",
        seeding: "70GB",
        notSeeding: "40GB",
        free: "10GB"
      }
    ];
    this.resourceFolders = [
      {
        name: "资源文件夹 1",
        size: "50GB",
        seeding: "25GB",
        notSeeding: "15GB",
        free: "10GB"
      },
      {
        name: "资源文件夹 2",
        size: "100GB",
        seeding: "60GB",
        notSeeding: "30GB",
        free: "10GB"
      }
    ];
    // 生成随机数据
    const randomTime = () => {
      const hours = Math.floor(Math.random() * 24);
      const minutes = Math.floor(Math.random() * 60);
      return `${hours < 10 ? '0' + hours : hours}:${minutes < 10 ? '0' + minutes : minutes}`;
    };
    this.recentScanTime = randomTime();
    this.lastBackupTime = randomTime();
  }
};
</script>

<style scoped>
</style>