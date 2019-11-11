<template>
  <div class="header">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: "Header",

  data() {
    return {
      msg: "Trainer Dashboard"
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  font-size: 25px;
  color: red;
}
</style>
