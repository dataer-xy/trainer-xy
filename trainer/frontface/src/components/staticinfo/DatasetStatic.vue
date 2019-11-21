// 数据集静态信息 自治
// 获取请求数据，并可视化

<template>
  <div class="datasetstatic">
    <StaticTable v-bind="this.responseJsonData"></StaticTable>
  </div>
</template>

<script>
import { BaseUrl, DEBUG } from "../config";
import StaticTable from "./StaticTable";

//
let bpDsStaticInfo = "/bpDsStaticInfo";

//
let responseJsonData = {};
if (DEBUG) {
  responseJsonData = {
    partTitle: "数据集静态信息", // part title
    tableData: [
      {
        key: "2016-05-02",
        value: "王小虎"
      },
      {
        key: "2016-05-04",
        value: "王小虎"
      },
      {
        key: "2016-05-01",
        value: "王小虎"
      },
      {
        key: "2016-05-03",
        value: "王小虎"
      }
    ]
  };
}

export default {
  name: "DatasetStatic",

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
      window.console.log(`静态 ds 检测到改变 ${this.$root.GlobalTrainName}`);
      this.requestJsonData.mainData.trainName = this.$root.GlobalTrainName;
      if (!DEBUG) {
        this.request_dataset_static_info();
      }
    }
  },

  mounted() {},

  methods: {
    /******************************************************************************/

    // 处理 响应数据
    _handle_dsStaticInfoDict(dsStaticInfoDict) {
      /**
       * 
       * 输入: dsStaticInfoDict
       * {
            tdsStaticInfoDict:{

            },
            vdsStaticInfoDict:{

            }
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
      let tdsStaticInfoDict = dsStaticInfoDict.tdsStaticInfoDict; // --> obj
      let vdsStaticInfoDict = dsStaticInfoDict.vdsStaticInfoDict;

      for (let [k, v] of Object.entries(tdsStaticInfoDict)) {
        objArray.push(
          {
            key: `训练集_${k}` ,
            value: v
          }
        );
      }

      for (let [k, v] of Object.entries(vdsStaticInfoDict)) {
        objArray.push(
          {
            key: `测试集_${k}`,
            value :  v
          }
        );
      }
      return objArray;
    },

    // 向后端请求数据
    request_dataset_static_info() {
      this.axios
        .post(bpDsStaticInfo, this.requestJsonData, {
          baseURL: BaseUrl
        })
        .then(resp => {
          // 接受响应
          // window.console.log(resp.data);
          //
          let orginalData = resp.data.mainData;

          let partTitle = orginalData.partTitle; // 标题

          let dsStaticInfoDict = orginalData.dsStaticInfoDict;
          let tableData = this._handle_dsStaticInfoDict(dsStaticInfoDict); // 表数据
          let responseJsonData = { partTitle, tableData };
          this.responseJsonData = responseJsonData;
        })
        .catch(err => {
          window.console.log("消息发送失败:" + err.status + "," + err.statusText);

          // 清空
          this.responseJsonData = {}
        });
    }
  }
};
</script>

<style scoped>
</style>