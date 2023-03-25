<template>
  <div id="home">
    <div id="home-content">
      <div id="echarts2"></div>
    </div>
  </div>
</template>

<script setup>
import {
  onMounted
} from "vue";
import * as echarts from 'echarts'
onMounted(() => {
  draw_echarts2();
})

function draw_echarts2() {
  let myChart = echarts.init(document.getElementById("echarts2"));
  myChart.setOption({
    title: {
      text: '使用70%',
      left: 'center',
      top: 'center'
    },
    tooltip: {
      trigger: 'item'
    },
    emphasis: {
      itemStyle: {
        shadowBlur: 10,
        shadowOffsetX: 0,
        shadowColor: 'rgba(0, 0, 0, 0.5)'
      }
    },
    series: [
      {
        name: 'Access From',
        type: 'pie',
        radius: ['40%', '70%'],
        avoidLabelOverlap: false,
        label: {
          show: false,
          position: 'center'
        },
        labelLine: {
          show: false
        },
        data: [
          { value: 1048, name: 'Search Engine' },
          { value: 735, name: 'Direct' },
          { value: 580, name: 'Email' },
          { value: 484, name: 'Union Ads' },
          { value: 300, name: 'Video Ads' }
        ]
      }
    ]
  });
  window.onresize = function () {
    myChart.resize();
  };
}
</script>
<style scoped>
#home {
  width: 1160px;
  margin: 0 auto;
}

#home-content {
  width: 1160px;
  height: 70vh;
  background: #fff;
  box-shadow: 0 0.5625rem 1.5rem 0 rgb(0 0 0 / 50%);
  border-radius: 10px;
  padding: 20px;
  margin-top: 5px;
  display: flex;
}

#torrent-table {
  width: 80%;
  margin: 0 auto;
}

#server-add {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100px;
  height: 100px;
  border: 1px dashed #989898;
  border-radius: 10px;
  margin-right: 50px;
  background: white;
}

.search_title {
  font-size: 14px;
  /* font-weight: bolder; */
  margin-right: 5px;
}

#echarts1 {
  width: 400px;
  height: 400px;
}

#echarts2 {
  width: 300px;
  height: 300px;
}
</style>