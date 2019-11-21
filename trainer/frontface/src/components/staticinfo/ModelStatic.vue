// 模型配置静态信息 自治

<template>
  <div class="modelstatic">
    <StaticTable v-bind="this.responseJsonData"></StaticTable>
  </div>
</template>

<script>
import { BaseUrl, DEBUG } from "../config";
import StaticTable from "./StaticTable";

//
let bpModelConfigStaticInfo = "/bpModelConfigStaticInfo";

//
let responseJsonData = {};
if (DEBUG) {
  responseJsonData = {
    partTitle: "模型静态信息", // part title
    tableData: [
      {
        key: "2016-05-02",
        value: "王小虎"
      },
      {
        key: "2016-05-04",
        value: "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
      },
      {
        key: "2016-05-01",
        value: "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
      },
      {
        key: "2016-05-03",
        value: "王小虎"
      },
      {
        key: "2016-05-02",
        value: "王小虎"
      },
      {
        key: "2016-05-04",
        value: "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
      },
      {
        key: "2016-05-01",
        value: "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
      },
      {
        key: "2016-05-03",
        value: "王小虎"
      },
      {
        key: "2016-05-02",
        value: "王小虎"
      },
      {
        key: "2016-05-04",
        value: "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
      },
      {
        key: "2016-05-01",
        value: "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
      },
      {
        key: "2016-05-03",
        value: "王小虎"
      },
      {
        key: "2016-05-02",
        value: "王小虎"
      },
      {
        key: "2016-05-04",
        value: "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
      },
      {
        key: "2016-05-01",
        value: "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
      },
      {
        key: "2016-05-03",
        value: "王小虎"
      }
    ]
  };
}

export default {
  name: "ModelStatic",

  components: {
    StaticTable
  },

  data() {
    return {
      // input:
      requestJsonData: {
        mainData: {
          trainName: null,
          isGetAll: true
        }
      },
      // output:
      responseJsonData: responseJsonData
    };
  },
  computed: {
    trainNameForWatch: function() {
      return this.$root.GlobalTrainName;
    }
  },
  watch: {
    trainNameForWatch: function() {
      window.console.log(`静态 model 检测到改变 ${this.$root.GlobalTrainName}`);
      this.requestJsonData.mainData.trainName = this.$root.GlobalTrainName;
      if (!DEBUG) {
        this.request_modelconfig_static_info();
      }
    }
  },

  mounted() {},

  methods: {
    // 处理响应数据
    _handle_modelconfigStaticInfoDict(modelconfigStaticInfoDict) {
      /**
       * 
       * 输入: modelconfigStaticInfoDict
       * {
       *  k:v
          }
       * 
       * 输出：objArray
       * [
            {
              key: "2016-05-02",
              value: "王小虎"
            },
            {
              key: "2016-05-04",
              value: "王小虎"
            },
          ]
       */
      let objArray = [];

      for (let [k, v] of Object.entries(modelconfigStaticInfoDict)) {
        objArray.push(
          {
            key: k,
            value: v 
          }
        );
      }

      return objArray;
    },

    // 向后端请求数据
    request_modelconfig_static_info() {
      this.axios
        .post(bpModelConfigStaticInfo, this.requestJsonData, {
          baseURL: BaseUrl
        })
        .then(resp => {
          // 接受响应
          // window.console.log(resp.data);
          //
          let orginalData = resp.data.mainData;

          let partTitle = orginalData.partTitle; // 标题

          let modelconfigStaticInfoDict = orginalData.modelconfigStaticInfoDict;
          let tableData = this._handle_modelconfigStaticInfoDict(
            modelconfigStaticInfoDict
          ); // 表数据
          let responseJsonData = { partTitle, tableData };
          this.responseJsonData = responseJsonData;
        })
        .catch(err => {
          window.console.log(
            "消息发送失败:" + err.status + "," + err.statusText
          );

          // 清空
          this.responseJsonData = {}
        });
    }
  }
};
</script>

<style scoped>
</style>