// 模型配置静态信息 自治

<template>
  <div class="modelstatic">
    <StaticTable v-bind="this.responseJsonData"></StaticTable>
  </div>
</template>

<script>
import { BaseUrl } from "../config";
import StaticTable from "./StaticTable";

//
let bpModelConfigStaticInfo = "/bpModelConfigStaticInfo";

export default {
  name: "ModelStatic",

  data() {
    return {
      // input:
      requestJsonData: {
        mainData: {
          trainName: "test",
          isGetAll: true
        }
      },
      // output: TODO 请求得到的数据
      responseJsonData: {
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
            value:
              "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
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
            value:
              "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
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
            value:
              "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
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
            value:
              "王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎王小虎"
          },
          {
            key: "2016-05-03",
            value: "王小虎"
          }
        ]
      }
    };
  },
  computed: {
    isGetAll: function() {
      // TODO 静态方法，始终是 true，非静态方法要判断 null
      if (this.responseJsonData.tableData.length > 0) {
        return false;
      } else {
        return true;
      }
    }
  },

  mounted() {
    // this.request_modelconfig_static_info();
  },

  methods: {
    // 处理 响应数据
    _handle_modelconfigStaticInfoDict(modelconfigStaticInfoDict) {
      let objArray = [];

      for (let [k, v] of Object.entries(modelconfigStaticInfoDict)) {
        objArray.push({ [k]: v });
      }

      return objArray;
    },

    request_modelconfig_static_info() {
      this.axios
        .post(bpModelConfigStaticInfo, {
          data: this.requestJsonData,
          baseURL: BaseUrl
        })
        .then(resp => {
          // TODO 接受响应
          window.console.log(resp.data);
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
        });
    }
  },

  components: {
    StaticTable
  }
};
</script>

<style scoped>
</style>