// summary 只发送请求，不接收数据

<template>
  <div class="summarydynamic">
    <!-- 啥也没有，是个空的 -->
  </div>
</template>

<script>
import { BaseUrl, DEBUG, circulaTime } from "../config";
//
let bpSummaryDynamicInfo = "/bpSummaryDynamicInfo"; // url

export default {
  name: "SummaryDynamic",

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
      window.console.log(`summary 检测到改变 ${this.$root.GlobalTrainName}`);
      this.requestJsonData.mainData.trainName = this.$root.GlobalTrainName;
      this.requestJsonData.mainData.isGetAll = true;

      //
      this.circula_request_summary_dynamic_info();
    }
  },
  mounted() {},
  methods: {
    // 请求
    request_summary_dynamic_info() {
      this.axios
        .post(bpSummaryDynamicInfo, this.requestJsonData, {
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
    circula_request_summary_dynamic_info() {
      if (!DEBUG) {
        setInterval(() => {
          this.request_summary_dynamic_info();
        }, circulaTime);
      } else {
        setInterval(() => {
          window.console.log(" summary 进入到循环请求！");
        }, circulaTime);
      }
    }
  }
};
</script>

<style scoped>
</style>

