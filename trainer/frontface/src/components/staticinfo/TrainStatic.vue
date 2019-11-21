// 训练静态信息 自治

<template>
  <div class="trainstatic">
    <StaticTable v-bind="this.responseJsonData"></StaticTable>
  </div>
</template>

<script>
import { BaseUrl, DEBUG } from "../config";
import StaticTable from "./StaticTable";

//
let bpTrainStaticInfo = "/bpTrainStaticInfo";

//
let responseJsonData = {};
if (DEBUG) {
  responseJsonData = {
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
  name: "TrainStatic",

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
      // output: 请求得到的数据
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
      window.console.log(`静态 train 检测到改变 ${this.$root.GlobalTrainName}`);
      this.requestJsonData.mainData.trainName = this.$root.GlobalTrainName;
      if (!DEBUG) {
        this.request_train_static_info();
      }
    }
  },

  mounted() {},

  methods: {
    // 处理 响应数据
    _handle_trainStaticInfoDict(trainStaticInfoDict) {
      // {
      //   key: "2016-05-02",
      //   value: "王小虎"
      // },
      let objArray = [];

      for (let [k, v] of Object.entries(trainStaticInfoDict)) {
        objArray.push(
          {
            key: k,
            value: v 
          }
        );
      }

      return objArray;
    },

    request_train_static_info() {
      this.axios
        .post(bpTrainStaticInfo, this.requestJsonData, {
          baseURL: BaseUrl
        })
        .then(resp => {
          // 接受响应
          // window.console.log(resp.data);
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

          // 清空
          this.responseJsonData = {}
        });
    }
  }
};
</script>

<style scoped>
</style>