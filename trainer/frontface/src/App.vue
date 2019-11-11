<template>
  <div id="app">
    <Wapper></Wapper>
  </div>
</template>

<script>
import Wapper from "./components/Wapper"


export default {
  name: "app",
  data: function() {
    return {
      
    };
  },


  components: {
    Wapper,
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
  /* margin-top: 60px; */
}
</style>
