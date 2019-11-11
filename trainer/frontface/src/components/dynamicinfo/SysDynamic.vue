// 机器 动态图像 是自治的

<template>
  <div class="sysdynamic">
    <el-tag>{{tag}}</el-tag>

      <LineChart v-bind:lineChartId="this.lineChartId"></LineChart>

  </div>
</template>

<script>
import LineChart from "./EchartsBase";
export default {
  name: "SysDynamic",

  data() {
    return {
      tag: "机器动态信息",
      lineChartId: "sysdyid"
    };
  },

  components: {
    LineChart
  }
};
</script>

<style scoped>
</style>

