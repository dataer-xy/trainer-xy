// 静态 session 自治

<template>
  <div class="staticsession">
    <SessionTitle v-bind:sessContent="this.sessionContent"></SessionTitle>
    <div class="staticsession-body">
      <ModelStatic ></ModelStatic>
      <DatasetStatic></DatasetStatic>
      <TrainStatic></TrainStatic>
      <SysStatic></SysStatic>
      <MsmgStatic></MsmgStatic>
    </div>
  </div>
</template>

<script>
import SessionTitle from "./SessionTitle";
import DatasetStatic from "./staticinfo/DatasetStatic";
import TrainStatic from "./staticinfo/TrainStatic";
import SysStatic from "./staticinfo/SysStatic";
import MsmgStatic from "./staticinfo/MsmgStatic";
import ModelStatic from "./staticinfo/ModelStatic";

export default {
  name: "StaticSession",
  data() {
    return {
      sessionContent: "静态信息"
    };
  },

  components: {
    SessionTitle,
    DatasetStatic,
    TrainStatic,
    SysStatic,
    MsmgStatic,
    ModelStatic
  }
};
</script>

<style scoped>
.datasetstatic {
  display: inline-block;
  padding: 8px;
  width: 300px;
}
.trainstatic {
  display: inline-block;
  padding: 8px;
  width: 300px;
}
.sysstatic {
  display: inline-block;
  padding: 8px;
  width: 300px;
}
.msmgstatic {
  display: inline-block;
  padding: 8px;
  width: 300px;
}
.modelstatic {
  display: inline-block;
  padding: 8px;
  width: 300px;
}
</style>
