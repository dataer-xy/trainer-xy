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
      },
      //
      timer: null
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
  methods: {
    // 请求
    request_summary_dynamic_info() {
      this.axios
        .post(bpSummaryDynamicInfo, this.requestJsonData, {
          baseURL: BaseUrl
        })
        .then(()=>{
          window.console.log("summary 请求成功！")
        }
          // resp => {
          // // 接受响应
          // window.console.log(resp.data);
          // }
        )
        .catch(err => {
          window.console.log(
            "消息发送失败:" + err.status + "," + err.statusText
          );
        });
    },

    // 循环请求
    circula_request_summary_dynamic_info() {
      // 清空
      if (this.timer) {
        clearInterval(this.timer);
      }
      // 创建
      if (!DEBUG) {
        this.timer = setInterval(() => {
          this.request_summary_dynamic_info();
        }, circulaTime);
      } else {
        this.timer = setInterval(() => {
          window.console.log(" summary 进入到循环请求！");
        }, circulaTime);
      }
    }
  },
  /***************************************************************/
  mounted() {},
  beforeDestroy() {
    if (this.timer) {
      //如果定时器还在运行 或者直接关闭，不用判断
      clearInterval(this.timer); //关闭
      this.timer = null;
    }
  }
};
</script>

<style scoped>
</style>

