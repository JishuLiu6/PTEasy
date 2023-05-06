<template>
  <div class="flex flex-col p-6 max-h-screen rounded-md bg-white m-6 shadow-md">
    <div class="flex items-center mb-6">
      <el-input class="flex-grow w-full md:w-1/4" placeholder="搜索日志"></el-input>
    </div>

    <div>
    <el-input v-model="path" placeholder="目录"></el-input>
    <el-button type="danger" @click="sendPathTask">发送</el-button>
  </div>
    <div class="l-block-shadow flex-grow rounded-lg p-4" style="height: 65vh">
      <el-table v-if="!isEmpty" :data="logs" max-height="60vh" empty-text="没有日志记录">
        <el-table-column prop="task_type" label="日志类型" max-width="150">
        </el-table-column>
        <el-table-column label="日志等级" max-width="150">
          <template v-slot="{ row }">
            <el-tag :type="tagType(row.level)" class="log-level-tag">{{ tagContent(row.level) }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="日志内容" min-width="300">
          <template v-slot="{ row }">
            <el-tooltip :content="row.message" placement="top">
              <div :style="{
                'color': row.level === 0 ? 'var(--el-color-info)' :
                  row.level === 1 ? 'var(--el-color-warning)' :
                    row.level === 2 ? 'var(--el-color-success)' :
                      row.level === 3 ? 'var(--el-color-danger)' :
                        '',
              }" class="logs-view__table-cell truncate">
                [{{row.task_id}}] <span class="font-black">{{ row.message }}</span>
              </div>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column label="时间" max-width="200">
          <template v-slot="{ row }">
            {{ timestampToDate(row.time) }}
          </template>
        </el-table-column>
      </el-table>
    </div>

    <div class="mt-6">
      <el-pagination background layout="prev, pager, next" :page-size="size" :current-page.sync="page" :total="totalCount"
        @current-change="handlePageChange">
      </el-pagination>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted} from "vue";
import { useStore } from "vuex";
import helper from "@/mixins/helper.js";

export default {
  mixins: [helper],
  setup() {
    const path = ref("");
    const store = useStore();
    const logs = computed(() => store.state.logManagement.logs)
    const size = computed(() => store.state.logManagement.size);
    const totalCount = computed(() => store.state.logManagement.totalCount);
    const page = computed({
      get: () => store.state.logManagement.page,
      set: (value) => (store.state.logManagement.page = value),
    });
    
    const isEmpty = ref(false); // 根据实际数据设置是否为空

    function sendPathTask(){
      store.dispatch("socketManager/sendMessage",{'event':'path', 'payload': path.value});
    }

    function tagType(level) {
      switch (level) {
        case 0:
          return "info";
        case 1:
          return "warning";
        case 2:
          return "success";
        case 3:
          return "danger";
        default:
          return "";
      }
    }

    function tagContent(level) {
      switch (level) {
        case 0:
          return "信息";
        case 1:
          return "警告";
        case 2:
          return "成功";
        case 3:
          return "错误";
        default:
          return "";
      }
    }

    function handlePageChange(newPage) {
      page.value = newPage;
      store.dispatch("logManagement/fetchData");
    }
    onMounted(() => {
      store.dispatch("logManagement/fetchData");
    });

    return {
      path,
      logs,
      page,
      size,
      totalCount,
      isEmpty,
      tagType,
      tagContent,
      handlePageChange,
      timestampToDate: helper.methods.timestampToDate,
      sendPathTask
    };
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
