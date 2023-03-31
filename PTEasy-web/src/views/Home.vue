<template>
  <div id="home">
    <div id="home-content">
      <div class="home-content-resource">
        <div class="home-content-search">
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
  </div>
</template>

<script setup>
</script>
<style lang="scss" scoped>
#home {
  width: 85vw;

  &-content {
    width: 85vw;
    height: 85vh;
    background: #fff;
    border-radius: 10px;
    padding: 20px;
    margin-top: 5px;

    .home-content-search {
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
    }
  }
}

.search_title {
  font-size: 14px;
  margin-right: 5px;
}

.block_title {
  font-size: 20px;
  font-weight: bolder;
  margin-right: 5px;
  color: #4099ff;
}
</style>