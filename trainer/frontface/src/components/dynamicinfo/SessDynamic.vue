// sess 只发送请求，不接收数据

<template>
  <div class="sessdynamic">
    <!-- 啥也没有，是个空的 -->
  </div>
</template>

<script>
import { BaseUrl, DEBUG, circulaTime } from "../config";
//
let bpSessDynamicInfo = "/bpSessDynamicInfo"; // url

export default {
  name: "SessDynamic",

  data() {
    return {
      // input:
      requestJsonData: {
        mainData: {
          trainName: null,
          isGetAll: true
        }
      }
    };
  },
  computed: {
    trainNameForWatch: function() {
      return this.$root.GlobalTrainName;
    }
  },
  watch: {
    trainNameForWatch: function() {
      window.console.log(`sess 检测到改变 ${this.$root.GlobalTrainName}`);
      this.requestJsonData.mainData.trainName = this.$root.GlobalTrainName;
      this.requestJsonData.mainData.isGetAll = true;
      //
      this.circula_request_sess_dynamic_info();
    }
  },
  mounted() {},
  methods: {
    // 请求
    request_sess_dynamic_info() {
      this.axios
        .post(bpSessDynamicInfo, this.requestJsonData, {
          baseURL: BaseUrl
        })
        .then(resp => {
          // 接受响应
          window.console.log(resp.data);
        })
        .catch(err => {
          window.console.log(
            "消息发送失败:" + err.status + "," + err.statusText
          );
        });
    },

    // 循环请求
    circula_request_sess_dynamic_info() {
      if (!DEBUG) {
        setInterval(() => {
          this.request_sess_dynamic_info();
        }, circulaTime);
      } else {
        setInterval(() => {
          window.console.log("sess 进入到循环请求！");
        }, circulaTime);
      }
    }
  }
};
</script>

<style scoped>
</style>

