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
      window.console.log(`sess 检测到改变 ${this.$root.GlobalTrainName}`);
      this.requestJsonData.mainData.trainName = this.$root.GlobalTrainName;
      this.requestJsonData.mainData.isGetAll = true;
      //
      this.circula_request_sess_dynamic_info();
    }
  },
  methods: {
    // 请求
    request_sess_dynamic_info() {
      this.axios
        .post(bpSessDynamicInfo, this.requestJsonData, {
          baseURL: BaseUrl
        })
        .then(()=>{
          window.console.log("sess 请求成功！")
        }
        //   resp => {
        //   // 接受响应
        //   window.console.log(resp.data);
        // }
        )
        .catch(err => {
          window.console.log(
            "消息发送失败:" + err.status + "," + err.statusText
          );
        });
    },

    // 循环请求
    circula_request_sess_dynamic_info() {
      // 清空
      if (this.timer) {
        clearInterval(this.timer);
      }
      // 创建
      if (!DEBUG) {
        this.timer = setInterval(() => {
          this.request_sess_dynamic_info();
        }, circulaTime);
      } else {
        this.timer = setInterval(() => {
          window.console.log("sess 进入到循环请求！");
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

