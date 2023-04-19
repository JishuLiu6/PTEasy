<template>
  <div class="site-view">
    <div class="site-view__header flex justify-between items-center mb-6">
      <router-link to="/site/new" class="bg-blue-500 text-white px-4 py-2 rounded-md hover:bg-blue-600">添加站点</router-link>
    </div>
    <div class="site-view__table grid grid-cols-6 gap-4">
      <div class="site-view__table-header col-span-6 grid grid-cols-6 gap-4 font-semibold border-b border-gray-300 py-2">
        <div>网址</div>
        <div>图标</div>
        <div>信息概括</div>
        <div>连通性</div>
        <div>下载量</div>
        <div>操作</div>
      </div>

      <div class="site-view__table-row col-span-6 grid grid-cols-6 gap-4 py-2 text-gray-600 bg-white">
        <div>http://www.google.com</div>
        <div><img src="https://www.google.com/favicon.ico" alt="Google Icon"></div>
        <div>Google Inc.</div>
        <div><i class="bi-check-circle-fill text-green-500"></i> 正常</div>
        <div>100MB</div>
        <div class="site-view__table-row-actions col-span-1 flex items-center justify-end">
          <router-link to="/site/edit/1" class="text-blue-500 hover:underline">编辑</router-link>
          <button class="text-red-500 ml-2 hover:underline">删除</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
};
</script>

<style>
.site-view {
  padding: 16px;
  box-sizing: border-box;
}

.site-view__header {
  margin-bottom: 16px;
}

.site-view__table {
  border-collapse: collapse;
}

.site-view__table-header {
  background-color: var(--primary-color);
  color: white;
  padding: 8px;
}

.site-view__table-row {
  border-bottom: 1px solid var(--accent-color);
  padding: 8px;
}

.site-view__table-row:last-child {
  border-bottom: none;
}

.site-view__table-row-actions button {
  background-color: transparent;
  border: none;
  color: var(--text-color);
  cursor: pointer;
}
</style>
