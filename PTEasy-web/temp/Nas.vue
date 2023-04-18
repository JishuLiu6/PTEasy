<template>
  <div id="home">
    <div id="home-content">
      
    </div>
  </div>
</template>

<script setup>
import {
  onMounted
} from "vue";

onMounted(() => {
  
})

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
</style>