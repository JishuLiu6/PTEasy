<template>
  <div class="dashboard">
    <div class="dashboard__chart-container">
      <div class="dashboard__chart" ref="chart"></div>
    </div>
    <div class="dashboard__file-list">
      <div class="dashboard__file-list-header">文件目录</div>
      <ul class="dashboard__file-list-items">
        <li v-for="file in filteredFiles" :key="file.name">
          <i :class="getIconClass(file.type)"></i>
          <span>{{ file.name }}</span>
        </li>
      </ul>
    </div>
  </div>
</template>
<script>
import * as echarts from 'echarts';

export default {
  data() {
    return {
      files: [
        { name: 'index.html', type: 'html', count: 120 },
        { name: 'style.css', type: 'css', count: 260 },
        { name: 'app.js', type: 'js', count: 300 },
        { name: 'data.json', type: 'json', count: 80 },
      ],
      activeType: 'all',
    };
  },
  mounted() {
    this.renderChart();
  },
  computed: {
    filteredFiles() {
      if (this.activeType === 'all') {
        return this.files;
      }
      return this.files.filter(file => file.type === this.activeType);
    },
  },
  methods: {
    renderChart() {
      const chartEl = this.$refs.chart;
      const chart = echarts.init(chartEl);
      const option = {
        title: {
          text: '文件类型分布图',
          subtext: '数据纯属虚构',
          x: 'center',
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b}: {c} ({d}%)',
        },
        legend: {
          orient: 'vertical',
          left: 10,
          data: ['html', 'css', 'js', 'json'],
        },
        series: [
          {
            name: '文件类型',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: 'center',
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '30',
                fontWeight: 'bold',
              },
            },
            labelLine: {
              show: false,
            },
            data: [
              { value: 120, name: 'html' },
              { value: 260, name: 'css' },
              { value: 300, name: 'js' },
              { value: 80, name: 'json' },
            ],
          },
        ],
      };
      chart.setOption(option);
      chart.on('click', ({ name }) => {
        this.activeType = name;
      });
    },
    getIconClass(fileType) {
      let iconClass = 'bi-file-earmark-text';
      switch (fileType) {
        case 'html':
          iconClass = 'bi-file-earmark-code';
          break;
        case 'css':
          iconClass = 'bi-file-earmark-css';
          break;
        case 'js':
          iconClass = 'bi-file-earmark-code';
          break;
        case 'json':
          iconClass = 'bi-file-earmark-bar-graph';
          break;
        default:
          break;
      }
      return iconClass;
    },
  },
};
</script>

<style>
.dashboard {
  display: flex;
  justify-content: space-between;
  align-items: stretch;
  height: 100%;
}

.dashboard__chart-container {
  flex-basis: 50%;
  padding: 16px;
  box-sizing: border-box;
}

.dashboard__chart {
  height: 100%;
}

.dashboard__file-list {
  flex-basis: 50%;
  padding: 16px;
  box-sizing: border-box;
  background-color: #f5f5f5;
}

.dashboard__file-list-header {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 16px;
}

.dashboard__file-list-items {
  list-style: none;
  margin: 0;
  padding: 0;
}

.dashboard__file-list-items li {
  display: flex;
  align-items: center;
  margin-bottom: 8px;
  padding: 8px;
  background-color: white;
  border-radius: 4px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.dashboard__file-list-items li i {
  margin-right: 8px;
}

.bi-file-earmark-text:before {
  content: "\f17d";
}
</style>
