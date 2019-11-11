// dataset 动态图像 是自治的

<template>
  <div class="datasetdynamic">
    <el-tag>{{tag}}</el-tag>
    
      <LineChart v-bind:lineChartId="this.lineChartId"></LineChart>

  </div>
</template>

<script>
import LineChart from "./EchartsBase";
export default {
  name: "DatasetDynamic",

  data() {
    return {
      tag: "数据集动态信息",
      lineChartId: "datasetdyid"
    };
  },

  components: {
    LineChart
  }
};
</script>

<style scoped>
</style>

