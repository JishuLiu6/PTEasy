<template>
  <div class="flex flex-col p-6 max-h-screen rounded-md bg-white m-6 shadow-md">
    <div class="flex items-center mb-6">
      <el-input class="flex-grow w-full md:w-1/4" placeholder="搜索日志"></el-input>
    </div>

    <div class="l-block-shadow flex-grow rounded-lg p-4" style="height: 65vh">
      <el-table v-if="!isEmpty" :data="tableData" max-height="60vh" empty-text="没有日志记录">
        <el-table-column prop="type" label="日志类型" max-width="150">
        </el-table-column>
        <el-table-column label="日志等级" max-width="150">
          <template v-slot="{ row }">
            <el-tag :type="tagType(row.level)" class="log-level-tag">{{ row.level }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="content" label="日志内容" min-width="300">
          <template v-slot="{ row }">
            <el-tooltip :content="row.content" placement="top">
              <div class="logs-view__table-cell truncate">{{ row.content }}</div>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column prop="time" label="时间" max-width="200">
        </el-table-column>
      </el-table>
    </div>

    <div class="mt-6">
      <el-pagination background layout="prev, pager, next" :total="100">
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isEmpty: false, // 根据实际数据设置是否为空
      tableData: [
        {
          "type": "下载",
          "level": "ERROR",
          "content": "下载tJcYtNmpjp.txt，大小为962字节，开始时间为2023-04-12 09:43:02，结束时间为2023-04-12 09:46:05，持续时间为0:03:03",
          "time": "2023-04-17 06:48:35"
        },
        {
          "type": "上传",
          "level": "INFO",
          "content": "上传hEmSSDJXRf.txt，大小为926字节，开始时间为2023-04-04 02:54:10，结束时间为2023-04-04 02:56:16，持续时间为0:02:06",
          "time": "2023-04-11 19:37:56"
        },
        {
          "type": "上传",
          "level": "INFO",
          "content": "上传jNJlHvVTtW.txt，大小为274字节，开始时间为2023-04-07 12:15:03，结束时间为2023-04-07 12:18:56，持续时间为0:03:53",
          "time": "2023-04-06 08:08:58"
        },
        {
          "type": "上传",
          "level": "WARN",
          "content": "上传fZKUbJXOgV.txt，大小为826字节，开始时间为2023-04-02 14:35:05，结束时间为2023-04-02 14:38:17，持续时间为0:03:12",
          "time": "2023-04-06 17:11:17"
        },
        {
          "type": "上传",
          "level": "ERROR",
          "content": "上传zvyjBhqBXq.txt，大小为194字节，开始时间为2023-04-18 01:10:07，结束时间为2023-04-18 01:12:31，持续时间为0:02:24",
          "time": "2023-04-18 05:13:34"
        },
        {
          "type": "下载",
          "level": "WARN",
          "content": "下载sBgKjJLsGd.txt，大小为347字节，开始时间为2023-04-02 18:53:20，结束时间为2023-04-02 18:55:32，持续时间为0:02:12",
          "time": "2023-04-09 01:34:10"
        },
        {
          "type": "上传",
          "level": "WARN",
          "content": "上传zOHVczxyfS.txt，大小为202字节，开始时间为2023-04-11 00:30:02，结束时间为2023-04-11 00:31:45，持续时间为0:01:43",
          "time": "2023-04-19 13:08:19"
        },
        {
          "type": "下载",
          "level": "ERROR",
          "content": "下载tJcYtNmpjp.txt，大小为962字节，开始时间为2023-04-12 09:43:02，结束时间为2023-04-12 09:46:05，持续时间为0:03:03",
          "time": "2023-04-17 06:48:35"
        },
        {
          "type": "上传",
          "level": "INFO",
          "content": "上传hEmSSDJXRf.txt，大小为926字节，开始时间为2023-04-04 02:54:10，结束时间为2023-04-04 02:56:16，持续时间为0:02:06",
          "time": "2023-04-11 19:37:56"
        },
        {
          "type": "上传",
          "level": "INFO",
          "content": "上传jNJlHvVTtW.txt，大小为274字节，开始时间为2023-04-07 12:15:03，结束时间为2023-04-07 12:18:56，持续时间为0:03:53",
          "time": "2023-04-06 08:08:58"
        },
        {
          "type": "上传",
          "level": "WARN",
          "content": "上传fZKUbJXOgV.txt，大小为826字节，开始时间为2023-04-02 14:35:05，结束时间为2023-04-02 14:38:17，持续时间为0:03:12",
          "time": "2023-04-06 17:11:17"
        },
        {
          "type": "上传",
          "level": "ERROR",
          "content": "上传zvyjBhqBXq.txt，大小为194字节，开始时间为2023-04-18 01:10:07，结束时间为2023-04-18 01:12:31，持续时间为0:02:24",
          "time": "2023-04-18 05:13:34"
        },
        {
          "type": "下载",
          "level": "WARN",
          "content": "下载sBgKjJLsGd.txt，大小为347字节，开始时间为2023-04-02 18:53:20，结束时间为2023-04-02 18:55:32，持续时间为0:02:12",
          "time": "2023-04-09 01:34:10"
        },
        {
          "type": "上传",
          "level": "WARN",
          "content": "上传zOHVczxyfS.txt，大小为202字节，开始时间为2023-04-11 00:30:02，结束时间为2023-04-11 00:31:45，持续时间为0:01:43",
          "time": "2023-04-19 13:08:19"
        }
      ]
    };
  },
  methods: {
    tagType(level) {
      if (!level) return '';

      switch (level) {
        case 'INFO':
          return 'success';
        case 'WARN':
          return 'warning';
        case 'ERROR':
          return 'danger';
        default:
          return '';
      }
    }
  },
};
</script>

<style scoped>
.log-level-tag {
  font-weight: bold;
}

.logs-view__table-cell {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  position: relative;
}
</style>
