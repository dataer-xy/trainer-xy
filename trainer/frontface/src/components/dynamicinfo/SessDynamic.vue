// sess 只发送请求，不接收数据

<template>
  <div class="sessdynamic">
    <!-- 啥也没有，是个空的 -->
  </div>
</template>

<script>
import { BaseUrl } from "../config";
//
let bpSessDynamicInfo = "/bpSessDynamicInfo"; // url
// let circulaTime = 60000; // 循环时间 1000 = 1秒

export default {
  name: "SessDynamic",

  data() {
    return {
      // trainNameForWatch : this.$root.GlobalTrainName, // NOTE data 中不可以引用全局动态变量，也不能引用计算属性
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
      window.console.log(`sess 检测到改变 ${this.$root.GlobalTrainName}`)
      this.requestJsonData.mainData.trainName = this.$root.GlobalTrainName;
      this.requestJsonData.mainData.isGetAll = true;
    }
  },
  mounted() {
    this.circula_request_sess_dynamic_info();
  },
  methods: {
    // 请求
    request_sess_dynamic_info() {
      this.axios
        .post(bpSessDynamicInfo, {
          data: this.requestJsonData,
          baseURL: BaseUrl
        })
        .then(resp => {
          // TODO 接受响应
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
      // setTimeout(this.request_sess_dynamic_info, circulaTime);
      setTimeout(() => {
        window.console.log("进入到循环请求！");
      }, 10000);
    }
  },


};
</script>

<style scoped>
</style>

