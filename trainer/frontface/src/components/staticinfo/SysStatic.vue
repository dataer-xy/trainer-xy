// 系统静态信息 自治

<template>
  <div class="sysstatic">
    <StaticTable v-bind="this.responseJsonData"></StaticTable>
  </div>
</template>

<script>
import { BaseUrl, DEBUG } from "../config";
import StaticTable from "./StaticTable";
//
let bpSysStaticInfo = "/bpSysStaticInfo";

//
let responseJsonData = {};
if (DEBUG) {
  responseJsonData = {
    partTitle: "系统静态信息", // part title
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
  name: "SysStatic",

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
      this.requestJsonData.mainData.trainName = this.$root.GlobalTrainName;
      if (!DEBUG) {
        this.request_sys_static_info();
      }
    }
  },
  mounted() {},

  methods: {
    // 处理 响应数据
    _handle_sysStaticInfoDict(sysStaticInfoDict) {
      let objArray = [];

      for (let [k, v] of Object.entries(sysStaticInfoDict)) {
        objArray.push(
          {
            key: k,
            value: v 
          }
        );
      }

      return objArray;
    },

    request_sys_static_info() {
      this.axios
        .post(bpSysStaticInfo, this.requestJsonData, {
          baseURL: BaseUrl
        })
        .then(resp => {
          // 接受响应
          // window.console.log(resp.data);
          //
          let orginalData = resp.data.mainData;

          let partTitle = orginalData.partTitle; // 标题

          let sysStaticInfoDict = orginalData.sysStaticInfoDict;
          let tableData = this._handle_sysStaticInfoDict(sysStaticInfoDict); // 表数据
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