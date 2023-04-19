<template>
  <div class="logs-view flex flex-col p-6 max-h-screen rounded-md bg-white m-6">
    <div class="logs-view__filter flex items-center mb-6">
      <el-input class="logs-view__filter-input flex-grow mr-2 w-full md:w-1/4" placeholder="搜索日志"></el-input>
      <el-button class="logs-view__filter-button" type="primary">搜索</el-button>
    </div>

    <div class="logs-view__table-container flex-grow bg-white shadow-md rounded-lg p-4" style="height: 60vh">
      <div v-if="!isEmpty" class="logs-view__table w-full border-collapse">
        <div class="logs-view__table-header grid grid-cols-1 md:grid-cols-4 gap-4 font-semibold border-b border-gray-300 py-2">
          <div>日志类型</div>
          <div>日志等级</div>
          <div>日志内容</div>
          <div>时间</div>
        </div>
        <!-- 以下内容重复生成多行 -->
        <div v-for="(row, index) in 10" :key="index"
          class="logs-view__table-row grid grid-cols-1 md:grid-cols-4 gap-4 py-2 text-gray-600"
          :class="{ 'bg-gray-100': index % 2 === 1 }">
          <div>类型1</div>
          <div>等级1</div>
          <div>日志内容示例</div>
          <div>2023-04-18 14:30:00</div>
        </div>
      </div>
      <div v-else class="text-center text-gray-500 font-semibold">
        没有日志记录
      </div>
    </div>

    <div class="logs-view__pagination mt-6">
      <el-pagination background layout="prev, pager, next" :total="100">
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isEmpty: false // 根据实际数据设置是否为空
    };
  }
};
</script>

<style lang="scss" scoped>
.logs-view__table-row {
  --row-bg-color: #fff;
  /* 定义一个变量 */
  background-color: var(--row-bg-color);
  /* 使用变量 */
}

.theme-dark .logs-view__table-row {
  --row-bg-color: #2c1f49;
  /* 修改变量的值 */
  color: #f1eaff;
  /* 修改文本颜色 */
}

</style>
