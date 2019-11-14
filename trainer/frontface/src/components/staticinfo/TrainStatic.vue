// 训练静态信息 自治

<template>
  <div class="trainstatic">
    <StaticTable v-bind="this.responseJsonData"></StaticTable>
  </div>
</template>

<script>
import { BaseUrl } from "../config";
import StaticTable from "./StaticTable";

//
let bpTrainStaticInfo = "/bpTrainStaticInfo";

export default {
  name: "TrainStatic",

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
        partTitle: "训练静态信息", // part title
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
    // this.request_train_static_info();
  },

  methods: {
    // 处理 响应数据
    _handle_trainStaticInfoDict(trainStaticInfoDict) {
      let objArray = [];

      for (let [k, v] of Object.entries(trainStaticInfoDict)) {
        objArray.push({ [k]: v });
      }

      return objArray;
    },

    request_train_static_info() {
      this.axios
        .post(bpTrainStaticInfo, {
          data: this.requestJsonData,
          baseURL: BaseUrl
        })
        .then(resp => {
          // TODO 接受响应
          window.console.log(resp.data);
          //
          let orginalData = resp.data.mainData;

          let partTitle = orginalData.partTitle; // 标题

          let trainStaticInfoDict = orginalData.trainStaticInfoDict;
          let tableData = this._handle_trainStaticInfoDict(trainStaticInfoDict); // 表数据
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