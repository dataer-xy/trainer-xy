// 动态信息部分 是自治的

<template>
  <div class="dynamicsession">
    <SessionTitle v-bind:sessContent="this.sessContent"></SessionTitle>
    <div class="dynamicsession-body">
      <DatasetDynamic></DatasetDynamic>
      <TrainDynamic></TrainDynamic>
      <SysDynamic></SysDynamic>
    </div>
    <div class="dynamicsession-foot">
      <!-- 无内容扩展高度 -->
    </div>
  </div>
</template>

<script>
import SessionTitle from "./SessionTitle";
import TrainDynamic from "./dynamicinfo/TrainDynamic";
import DatasetDynamic from "./dynamicinfo/DatasetDynamic";
import SysDynamic from "./dynamicinfo/SysDynamic";

export default {
  name: "DynamicSession",

  data() {
    return {
      sessContent: "动态信息"
    };
  },
  components: {
    SessionTitle,
    TrainDynamic,
    DatasetDynamic,
    SysDynamic,
  }
};
</script>

<style scoped>
.datasetdynamic {
  padding: 20px;
  display: inline-block;
}
.traindynamic {
  padding: 20px;
  display: inline-block;
}
.sysdynamic {
  padding: 20px;
  display: inline-block;
}
.dynamicsession-foot{
  height: 30px;
}
</style>



