<template>
  <div class="notification-view">
    <!-- 通知工具表格 -->
    <div class="notification-view__table-container">
      <table class="notification-view__table">
        <thead>
          <tr>
            <th>通知工具</th>
            <th>KEY</th>
            <th>通知定时</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(notification, index) in notifications" :key="index">
            <td>{{ notification.tool }}</td>
            <td>{{ notification.key }}</td>
            <td>{{ notification.schedule }}</td>
            <td>
              <button class="notification-view__edit-button">编辑</button>
              <button class="notification-view__delete-button">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- 添加通知表单 -->
    <div class="notification-view__form-container">
      <form class="notification-view__form">
        <div class="notification-view__form-group">
          <label for="notification-tool">通知工具</label>
          <select id="notification-tool" class="notification-view__form-select" v-model="newNotification.tool">
            <option value="">请选择通知工具</option>
            <option value="telegram">Telegram</option>
            <option value="dingtalk">钉钉</option>
          </select>
        </div>
        <div class="notification-view__form-group">
          <label for="notification-key">KEY</label>
          <input id="notification-key" type="text" class="notification-view__form-input" placeholder="请输入 KEY" v-model="newNotification.key" />
        </div>
        <div class="notification-view__form-group">
          <label for="notification-schedule">通知定时</label>
          <input id="notification-schedule" type="text" class="notification-view__form-input" placeholder="请输入通知定时" v-model="newNotification.schedule" />
        </div>
        <div class="notification-view__form-group">
          <button type="submit" class="notification-view__form-submit" @click.prevent="addNotification">添加通知</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      notifications: [
        { tool: 'Telegram', key: 'xxxxxxxxxxx', schedule: '0 9 * * *' },
        { tool: '钉钉', key: 'xxxxxxxxxxx', schedule: '0 10 * * *' },
      ],
      newNotification: {
        tool: '',
        key: '',
        schedule: '',
      },
    };
  },
  methods: {
    addNotification() {
      // TODO: 添加通知
    },
  },
};
</script>

<style>
.notification-view {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: auto 1fr;
  gap: 20px;
  height: 100%;
  padding: 20px;
}

.notification-view__table-container {
  grid-row: 1 / span 1;
  grid-column: 1 / span 2;
  overflow: auto;
}

.notification-view__table {
  width: 100%;
  border-collapse: collapse;
}

.notification-view__table th,
.notification-view__table td {
  padding: 10px;
  text-align: center;
  vertical-align: middle;
  border: 1px solid #ddd;
}

.notification-view__table th {
  background-color: var(--primary-color);
  color: white;
}

.notification-view__table th:first-child,
.notification-view__table td:first-child {
  text-align: left;
}

.notification-view__form-container {
  grid-row: 2 / span 1;
  grid-column: 1 / span 1;
}

.notification-view__form {
  display: grid;
  gap: 10px;
}

.notification-view__form-group {
  display: flex;
  flex-direction: column;
}

.notification-view__form-group label {
  margin-bottom: 5px;
  font-weight: bold;
}

.notification-view__form-select,
.notification-view__form-input {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  outline: none;
}

.notification-view__form-submit {
  padding: 8px;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.notification-view__form-submit:hover {
  background-color: var(--secondary-color);
}

@media (max-width: 768px) {
  .notification-view {
    display: block;
  }

  .notification-view__table-container {
    overflow: visible;
  }
}

</style>