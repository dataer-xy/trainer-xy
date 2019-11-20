
<template>
  <div class="sessiontitle">
    <hr class="sess-hr" />
    <p class="sess-p">{{ this.sessContent }} ({{this.trainNameForWatch}})</p>
  </div>
</template>

<script>
export default {
  name: "SessionTitle",

  props: ["sessContent"],

  data() {
    return {};
  },
  computed: {
    trainNameForWatch: function() {
      return this.$root.GlobalTrainName;
    }
  },
  methods: {}
};
</script>

<style scoped>
.sessiontitle {
  text-align: left;
}
.sess-p {
  text-align: "left";
  font-size: 25px;
  height: 80px;
  line-height: initial;
}
.sess-hr {
  height: 0.5px;
  border: none;
  border-top: 1px solid #555555;
}
</style>

