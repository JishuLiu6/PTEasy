<template>
  <div class="backup-page">
    <!-- 选择备份内容 -->
    <div class="backup-page__content">
      <h2 class="backup-page__title">选择备份内容</h2>
      <div class="backup-page__checkbox-group">
        <div class="backup-page__checkbox-item">
          <input id="file-backup" type="checkbox" class="backup-page__checkbox" v-model="backupItems.file" />
          <label for="file-backup">文件备份</label>
        </div>
        <div class="backup-page__checkbox-item">
          <input id="database-backup" type="checkbox" class="backup-page__checkbox" v-model="backupItems.database" />
          <label for="database-backup">数据库备份</label>
        </div>
        <!-- 添加更多备份项 -->
      </div>
    </div>

    <!-- 选择备份方式 -->
    <div class="backup-page__content">
      <h2 class="backup-page__title">选择备份方式</h2>
      <div class="backup-page__radio-group">
        <div class="backup-page__radio-item">
          <input id="manual-backup" type="radio" class="backup-page__radio" value="manual" v-model="backupMode" />
          <label for="manual-backup">手动备份</label>
        </div>
        <div class="backup-page__radio-item">
          <input id="scheduled-backup" type="radio" class="backup-page__radio" value="scheduled" v-model="backupMode" />
          <label for="scheduled-backup">定时备份</label>
        </div>
        <!-- 添加更多备份方式 -->
      </div>

      <!-- 手动备份设置 -->
      <div class="backup-page__manual-container" v-if="backupMode === 'manual'">
        <button class="backup-page__backup-button" @click="backup">备份</button>
      </div>

      <!-- 定时备份设置 -->
      <div class="backup-page__scheduled-container" v-if="backupMode === 'scheduled'">
        <div class="backup-page__form-group">
          <label for="backup-interval">备份周期</label>
          <select id="backup-interval" class="backup-page__form-select" v-model="backupInterval">
            <option value="daily">每天</option>
            <option value="weekly">每周</option>
            <option value="monthly">每月</option>
          </select>
        </div>
        <div class="backup-page__form-group">
          <label for="backup-time">备份时间</label>
          <input id="backup-time" type="time" class="backup-page__form-input" v-model="backupTime" />
        </div>
        <button class="backup-page__backup-button" @click="scheduleBackup">保存</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'BackupView',
  setup() {
    const selectedItems = ref([]);
    const backupType = ref('full');
    const backupDestination = ref('local');

    function handleSelectAll() {
      selectedItems.value = [...backupItems.value];
    }

    function handleDeselectAll() {
      selectedItems.value = [];
    }

    function handleBackup() {
      // 处理备份操作
    }

    const backupItems = ref([
      {
        name: '用户数据',
        type: 'data',
        selected: false,
      },
      {
        name: '系统设置',
        type: 'setting',
        selected: false,
      },
      {
        name: '应用程序',
        type: 'app',
        selected: false,
      },
      {
        name: '日志文件',
        type: 'log',
        selected: false,
      },
    ]);

    return {
      selectedItems,
      backupType,
      backupDestination,
      handleSelectAll,
      handleDeselectAll,
      handleBackup,
      backupItems,
    };
  },
};
</script>

<style lang="scss">
.backup-page {
  display: flex;
  flex-direction: column;
  gap: 40px;
  padding: 20px;
  background-color: var(--background-color);

  &__content {
    display: flex;
    flex-direction: column;
    gap: 20px;
    padding: 20px;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    background-color: white;
  }

  &__title {
    margin: 0;
    font-size: 24px;
    font-weight: bold;
    color: var(--text-color);
  }

  &__checkbox-group {
    display: flex;
    flex-direction: column;
    gap: 10px;

    &__checkbox-item {
      display: flex;
      align-items: center;

      & label {
        margin-left: 10px;
        font-size: 16px;
        color: var(--text-color);
      }
    }
  }

  &__radio-group {
    display: flex;
    flex-direction: column;
    gap: 10px;

    &__radio-item {
      display: flex;
      align-items: center;

      & label {
        margin-left: 10px;
        font-size: 16px;
        color: var(--text-color);
      }
    }
  }

  &__manual-container,
  &__scheduled-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  &__form-group {
    display: flex;
    flex-direction: column;
    gap: 5px;

    & label {
      font-size: 16px;
      color: var(--text-color);
    }

    &__form-input {
      height: 32px;
      padding: 4px;
      border-radius: 4px;
      border: 1px solid #ccc;
      background-color: white;
      color: #333;

      &:focus {
        border-color: var(--accent-color);
      }
    }

    &__form-select {
      height: 32px;
      padding: 4px;
      border-radius: 4px;
      border: 1px solid #ccc;
      background-color: white;
      color: #333;

      &:focus {
        border-color: var(--accent-color);
      }
    }
  }

  &__backup-button {
    width: 120px;
    height: 40px;
    padding: 0 20px;
    border-radius: 4px;
    background-color: var(--accent-color);
    color: white;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    line-height: 40px;
    cursor: pointer;
  }
}
</style>