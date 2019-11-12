// dataset 动态图像 是自治的
// 获取数据
// 绘制数据
// TODO 每隔一段时间向后端发送请求
// TODO echarts 折线图继续绘图

<template>
  <div class="datasetdynamic">
    <LineChart v-bind="this.responseJsonData"></LineChart>
  </div>
</template>

<script>
import { BaseUrl } from "../config";
import LineChart from "./EchartsBase";

// 
let bpDsDynamicInfo = "/bpDsDynamicInfo"; // url
let lineChartId = "datasetdyid"; // dom id
let circulaTime = 60000; // 循环时间 1000 = 1秒

export default {
  name: "DatasetDynamic",

  data() {
    return {
      lineChartId: "datasetdyid",
      // input:
      requestJsonData: {
        mainData: {
          trainName: "test",
          isGetAll: true // TODO this.isGetAll 可以将整个请求 放到里面
        }
      },
      // output: TODO 请求得到的数据
      responseJsonData: {
        partTitle: "数据集动态信息",
        lineChartId: lineChartId,
        plotData: {
          legend: ["邮件营销", "联盟广告", "视频广告", "直接访问", "搜索引擎"],
          xTicks: ["周一", "周二", "周三", "周四", "周五", "周六", "周日"],
          data: [
            {
              name: "邮件营销", // 折线名称
              type: "line", // 线形
              // stack: "总量",
              data: [120, 132, 101, 134, 90, 230, 210, 101, 134, 90, 230, 210] // 数据
            },
            {
              name: "联盟广告",
              type: "line",
              stack: "总量",
              data: [220, 182, 191, 234, 290, 330, 310, 101, 134, 90, 230, 210]
            },
            {
              name: "视频广告",
              type: "line",
              stack: "总量",
              data: [150, 232, 201, 154, 190, 330, 410, 101, 134, 90, 230, 210]
            },
            {
              name: "直接访问",
              type: "line",
              stack: "总量",
              data: [320, 332, 301, 334, 390, 330, 320, 101, 134, 90, 230, 210]
            },
            {
              name: "搜索引擎",
              type: "line",
              stack: "总量",
              data: [
                820,
                932,
                901,
                934,
                1290,
                1330,
                1320,
                101,
                134,
                90,
                230,
                210
              ]
            }
          ]
        }
      }
    };
  },
  computed: {
    isGetAll: function() {
      // TODO 静态方法，始终是 true，非静态方法要判断 null
      if (this.responseJsonData.plotData.data[0].data.length > 0) {
        return false;
      } else {
        return true;
      }
    }
  },
  mounted() {
    // this.request_dataset_dynamic_info();
  },
  methods: {
    // TODO 处理图数据 追加到原始数据中 append
    _handle_dsDynamicInfoDict(dsDynamicInfoDict) {
      /**
       *
       */
      let objArray = [];

      for (let [k, v] of Object.entries(dsDynamicInfoDict)) {
        objArray.push({ [k]: `tds_${v}` });
      }

      return objArray;
    },

    _request_dataset_dynamic_info() {
      this.axios
        .post(bpDsDynamicInfo, {
          data: this.requestJsonData,
          baseURL: BaseUrl
        })
        .then(resp => {
          // TODO 接受响应
          window.console.log(resp.data);
          //
          let orginalData = resp.data.mainData;

          let partTitle = orginalData.partTitle; // 标题

          let dsDynamicInfoDict = orginalData.dsDynamicInfoDict;
          let plotData = this._handle_dsDynamicInfoDict(dsDynamicInfoDict); // 图数据

          let responseJsonData = {
            partTitle: partTitle,
            lineChartId: this.lineChartId,
            plotData: plotData
          };
          this.responseJsonData = responseJsonData;
        })
        .catch(err => {
          window.console.log(
            "消息发送失败:" + err.status + "," + err.statusText
          );
        });
    },
    
    requset_dataset_dynamic_info() {
      window.setTimeout(
        this._request_dataset_dynamic_info,
        circulaTime
        )

    }
  },


  components: {
    LineChart
  }
};
</script>

<style scoped>
</style>


// setInterval(function(){ alert("Hello"); }, 3000);
