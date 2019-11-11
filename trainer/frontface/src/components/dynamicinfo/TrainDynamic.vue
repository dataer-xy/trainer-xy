// 训练动态信息，是自治的
<template>
  <div class="traindynamic">
    <el-tag>{{tag}}</el-tag>

      <LineChart v-bind:lineChartId="this.lineChartId"></LineChart>

    <ButtomList></ButtomList>
  </div>
</template>

<script>
import LineChart from "./EchartsBase";
import ButtomList from "./ButtomList";

export default {
  name: "TrainDynamic",
  data() {
    return {
      tag: "训练动态信息",
      lineChartId: "traindyid"
    };
  },
  props: [],
  components: {
    LineChart,
    ButtomList
  }
};
</script>

<style scoped>
/* .traindynamic{
    text-align: center;
    float:left;
} */
</style>