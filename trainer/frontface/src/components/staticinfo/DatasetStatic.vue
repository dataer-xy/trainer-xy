// 数据集静态信息 自治
// 获取请求数据，并可视化
// TODO trainName 
// TODO isGetAll
// TODO mounted 正确吗
// TODO response OK

<template>
  <div class="datasetstatic">
    <StaticTable v-bind="this.responseJsonData"></StaticTable>
  </div>
</template>

<script>
import { BaseUrl } from "../config";
import StaticTable from "./StaticTable";

//
let bpDsStaticInfo = "/bpDsStaticInfo";

export default {
  name: "DatasetStatic",

  data() {
    return {
      // input:
      requestJsonData: {
        mainData: {
          trainName: null,
          isGetAll: true
        }
      },
      // output: TODO 请求得到的数据
      responseJsonData: {
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
      }
    };
  },
  computed : {
    trainNameForWatch : function(){
      return this.$root.GlobalTrainName
    },
  },
  watch : {
    trainNameForWatch : function () {
      this.requestJsonData.mainData.trainName=this.$root.GlobalTrainName
    },
  },

  mounted() {
    // this.request_dataset_static_info();
  },

  methods: {
    // 处理 响应数据
    _handle_dsStaticInfoDict(dsStaticInfoDict) {
      let objArray = [];
      let tdsStaticInfoDict = dsStaticInfoDict.tdsStaticInfoDict; // --> obj
      let vdsStaticInfoDict = dsStaticInfoDict.vdsStaticInfoDict;

      for (let [k, v] of Object.entries(tdsStaticInfoDict)) {
        objArray.push({ [k]: `tds_${v}` });
      }

      for (let [k, v] of Object.entries(vdsStaticInfoDict)) {
        objArray.push({ [k]: `vds_${v}` });
      }
      return objArray;
    },

    request_dataset_static_info() {
      this.axios
        .post(bpDsStaticInfo, {
          data: this.requestJsonData,
          baseURL: BaseUrl
        })
        .then(resp => {
          // TODO 接受响应
          window.console.log(resp.data);
          //
          let orginalData = resp.data.mainData;

          let partTitle = orginalData.partTitle; // 标题

          let dsStaticInfoDict = orginalData.dsStaticInfoDict;
          let tableData = this._handle_dsStaticInfoDict(dsStaticInfoDict); // 表数据
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