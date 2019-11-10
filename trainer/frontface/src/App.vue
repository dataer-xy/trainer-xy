<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <HelloWorld msg=" Trainer Dashboard " />
    <SessionTitle sessContent="静态信息"></SessionTitle>
    <StaticTable></StaticTable>
    <SessionTitle sessContent="动态信息"></SessionTitle>
    <TrainDynamic></TrainDynamic>
    
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld";
import TrainDynamic from "./components/TrainDynamic"
import SessionTitle from "./components/SessionTitle"
import StaticTable from "./components/StaticTable"

export default {
  name: "app",
  data: function() {
    return {
      
    };
  },


  components: {
    HelloWorld,
    TrainDynamic,
    SessionTitle,
    StaticTable,
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
