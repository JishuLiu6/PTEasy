<template>
    <el-dialog class="custom-dialog" :title="title" :visible="visible" :width="dialogWidth">
      <div class="content">
        <slot></slot>
      </div>
      <template #footer>
        <div class="flex justify-end">
          <el-button class="cancel-button" @click="onCancel">
            取消
          </el-button>
          <el-button class="confirm-button" type="primary" @click="onConfirm">
            确定
          </el-button>
        </div>
      </template>
    </el-dialog>
  </template>
  
  <script>
  import 'bootstrap-icons/font/bootstrap-icons.css';
  
  export default {
    name: 'CustomDialog',
    props: {
      title: String,
      visible: Boolean,
      dialogWidth: {
        type: String,
        default: '400px',
      },
    },
    methods: {
      onCancel() {
        this.$emit('update:visible', false);
      },
      onConfirm() {
        this.$emit('confirm');
      },
    },
  };
  </script>
  
  <style lang="scss">
  .custom-dialog {
    border-radius: 5px !important;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
  
    .el-dialog__header {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 50px;
      padding: 0 !important;
      margin: 0 !important;
      position: relative;
      border-bottom: 1px solid var(--el-color-primary);
    }
  
    .el-dialog__title {
      font-weight: bold;
      padding: 0 !important;
      color: var(--el-color-primary) !important;
      position: relative;
    }
  
    .el-dialog__body {
      padding: 40px 20px 10px 20px!important;
    }
  
    .el-dialog__footer {
      padding: 20px;
      border-top: 1px solid var(--el-color-border);
      display: flex;
      justify-content: flex-end;
  
      .el-button {
        padding: 6px 12px;
        font-size: 14px;
        line-height: 1.42857143;
        border-radius: 3px;
        transition: all 0.3s;
  
        &:hover {
          opacity: 0.8;
        }
      }
  
      .cancel-button {
        margin-right: 10px;
        color: #666;
      }
  
      .confirm-button {
        background-color: var(--el-color-primary);
        border-color: var(--el-color-primary);
  
        &:hover {
          background-color: var(--el-color-primary-darker);
          border-color: var(--el-color-primary-darker);
        }
      }
    }
  }
  </style>
  