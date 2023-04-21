<template>
    <div class="echarts-wrapper" ref="echartsWrapper"></div>
  </template>
  <script>
  import * as echarts from "echarts";
  
  export default {
    props: {
      data: {
        type: Array,
        default: () => [],
      },
    },
    mounted() {
      this.initChart();
    },
    watch: {
      data() {
        this.updateChart();
      },
    },
    methods: {
      initChart() {
        this.chart = echarts.init(this.$refs.echartsWrapper);
        this.updateChart();
      },
      updateChart() {
        const option = {
          tooltip: {
            trigger: "item",
            formatter: "{a} <br/>{b}: {c} ({d}%)",
          },
          legend: {
            orient: "vertical",
            left: "left",
            data: ["视频", "音乐", "文档", "图片", "其他"],
          },
          series: [
            {
              name: "资源分类",
              type: "pie",
              selectedMode: "single",
              radius: [0, "30%"],
  
              label: {
                position: "inner",
              },
              labelLine: {
                show: false,
              },
              data: [
                { value: Math.floor(Math.random() * 1000), name: "做种" },
                { value: Math.floor(Math.random() * 1000), name: "不做种" },
              ],
            },
            {
              name: "资源分类",
              type: "pie",
              radius: ["40%", "55%"],
              label: {
                formatter: "{b}: {c} ({d}%)",
              },
              data: [
                { value: Math.floor(Math.random() * 1000), name: "视频" },
                { value: Math.floor(Math.random() * 1000), name: "音乐" },
                { value: Math.floor(Math.random() * 1000), name: "文档" },
                { value: Math.floor(Math.random() * 1000), name: "图片" },
                { value: Math.floor(Math.random() * 1000), name: "其他" },
              ],
            },
          ],
        };
        this.chart.setOption(option);
      },
    },
  };
  </script>
  <style scoped lang="scss">
  .echarts-wrapper {
    @apply w-full h-80 mt-4;
  }
  </style>