<template>
    <div class="storage-capacity">
      <div class="capacity-bar relative w-64 h-8 rounded-full bg-gray-200">
        <div class="capacity-progress absolute h-full rounded-full" :style="{ width: percentage + '%' }"></div>
        <div class="capacity-text absolute inset-0 flex items-center justify-center text-xs font-bold text-gray-700">
          {{ used }} GB / {{ total }} GB
        </div>
      </div>
    </div>
  </template>
  <script>
  export default {
    props: {
      total: {
        type: Number,
        default: 0,
      },
      used: {
        type: Number,
        default: 0,
      },
    },
    computed: {
      percentage() {
        return Math.round((this.used / this.total) * 100);
      },
    },
  };
  </script>
  <style scoped>
  .storage-capacity {
    @apply flex flex-col items-center;
  }
  
  .capacity-bar {
    @apply relative my-4;
  }
  
  .capacity-progress {
    background-color: var(--el-color-primary);
    @apply absolute top-0 bottom-0 rounded-full ;
  }
  
  .capacity-text {
    @apply absolute inset-0 flex items-center justify-center font-bold text-gray-700;
  }
  </style>