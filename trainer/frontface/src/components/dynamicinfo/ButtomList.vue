// 将多个按钮放在一起
// 在组件上使用 v-for https://cn.vuejs.org/v2/guide/list.html#%E5%9C%A8-v-for-%E9%87%8C%E4%BD%BF%E7%94%A8%E5%80%BC%E8%8C%83%E5%9B%B4

<template>
  <div class="buttomlist">
    <ButtomBase v-for="buttomInfo in this.buttomInfoList" :key="buttomInfo.id" v-bind="buttomInfo"></ButtomBase>
  </div>
</template>

<script>
import ButtomBase from "./ButtomBase";

export default {
  name: "ButtomList",

  data() {
    return {
      // stop, pauseEpoch,continueEpoch pauseBatch,continueBatch
      buttomInfoList: [
        {
          buttomStr: "pauseEpoch",
          buttomType: "warning",
          confirmStr:
            "将在下一个 epoch 暂停，不要多次点击。如果要继续训练，点击 continueEpoch ！",
          tooltipContent: "在下一个 epoch 暂停",
          stateInt: 2,
          bpRoute : "/bpEpochState"
        },
        {
          buttomStr: "continueEpoch",
          buttomType: "info",
          confirmStr: "继续 epoch",
          tooltipContent: "继续 epoch",
          stateInt: 3,
          bpRoute : "/bpEpochState"
        },
        {
          buttomStr: "pauseBatch",
          buttomType: "warning",
          confirmStr:
            "将在下一个 batch 暂停，不要多次点击。如果要继续训练，点击 continueBatch ！",
          tooltipContent: "在下一个 batch 暂停",
          stateInt: 4,
          bpRoute : "/bpBatchState"
        },
        {
          buttomStr: "continueBatch",
          buttomType: "info",
          confirmStr: "继续 batch",
          tooltipContent: "继续 batch",
          stateInt: 5,
          bpRoute:"/bpBatchState"
        },
        {
          buttomStr: "stop",
          buttomType: "warning",
          confirmStr:
            "真的要终止训练吗？一般在训练不理想或者已经饱和的时候，才主动终止训练！",
          tooltipContent: "终止训练",
          stateInt: 0,
          bpRoute:"/bpBatchState"
        }
      ]
    };
  },

  props: [],

  methods: {},
  components: {
    ButtomBase
  }
};
</script>

<style scoped>
.buttombase {
   display: inline;
   padding-left: 3px;
   padding-right: 3px;
}
.buttomlist {
    padding-top: 10px;
}

</style>