<template>
  <div class="trainbuttom" v-on:click="this.on_change_global_trainName">{{this.trainName}}</div>
</template>

<script>
export default {
  name: "TrainButtom",
  props: ["trainName"],
  methods: {
    on_change_global_trainName() {
      window.console.log(`改变：当前的train name 是 ${this.trainName}`);
      this.$root.GlobalTrainName = this.trainName;
    }
  }
};
</script>

<style scoped>
</style>