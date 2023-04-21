<template>
  <div class="file-browser">
    <div class="header">
      <div class="breadcrumb">
        <el-breadcrumb separator-class="el-icon-arrow-right">
          <el-breadcrumb-item v-for="folder in breadcrumb" :key="folder.id">
            <span>{{ folder.label }}</span>
          </el-breadcrumb-item>
        </el-breadcrumb>
      </div>
    </div>
    <div class="main">
      <div class="tree">
        <el-tree :data="files" node-key="id" :default-expand-all="true" :highlight-current="true"
          @node-click="handleNodeClick">
          <template #default="{ node }">
            <i :class="node.icon"></i>
            <span>{{ node.label }}</span>
          </template>
        </el-tree>
      </div>
      <div class="content">
        <div class="files">
          <div v-for="file in currentFolder.children" :key="file.id" class="file">
            <i :class="file.icon"></i>
            <span>{{ file.label }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue';

export default {
  props: {
    files: {
      type: Array,
      default: () => [],
    },
  },
  setup(props) {
    const currentFolder = ref(null);
    const breadcrumb = ref([]);

    watch(
      () => props.files,
      (newVal) => {
        if (!currentFolder.value && newVal.length) {
          currentFolder.value = newVal[0];
          breadcrumb.value.push(newVal[0]);
        }
      },
      { immediate: true }
    );

    watch(currentFolder, (newVal) => {
      breadcrumb.value = breadcrumb.value.filter((folder) => folder.id === newVal.id);
    });

    function handleNodeClick(node) {
      if (node.children) {
        currentFolder.value = node;
        breadcrumb.value.push(node);
      }
    }

    return {
      currentFolder,
      breadcrumb,
      handleNodeClick,
    };
  },
};
</script>

<style scoped lang="scss">
.file-browser {
  @apply flex flex-col h-full;
}

.header {
  @apply p-4 bg-gray-100;
}

.breadcrumb {
  @apply text-sm;
}

.main {
  @apply flex flex-grow;
}

.tree {
  @apply w-1/4 p-4 border-r border-gray-300;
}

.content {
  @apply flex-grow p-4;
}

.files {
  @apply flex flex-wrap -mx-2;
}

.file {
  @apply flex items-center m-2 p-2 bg-white border border-gray-300 rounded-lg;
  cursor: pointer;
}

.file i {
  @apply text-2xl mr-2;
}
</style>
