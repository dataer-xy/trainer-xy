<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <HelloWorld msg=" python 项目结构规划 " />
    <myChart></myChart>
    <ButtomBase v-bind="this.propObj"></ButtomBase>

  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import myChart from "./components/EchartsTest.vue";
import ButtomBase from "./components/ButtomBase"

export default {
  name: "app",
  data: function() {
    return {
      propObj: {
        buttomType: "warning",
        buttomStr: "pauseEpoch",
        confirmStr:
          "将暂停下一个 epoch，不要多次点击。如果要继续训练，点击 continueEpoch ！",
        stateInt: 2,
        tooltipContent : "暂停下一个 epoch"
      }
    };
  },


  components: {
    HelloWorld,
    myChart,
    ButtomBase
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
