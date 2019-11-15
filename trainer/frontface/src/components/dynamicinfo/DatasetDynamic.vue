// dataset 动态图像 是自治的
// 获取数据
// 绘制数据
// TODO 每隔一段时间向后端发送请求
// TODO echarts 折线图继续绘图 OK

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
// let circulaTime = 60000; // 循环时间 1000 = 1秒

export default {
  name: "DatasetDynamic",

  data() {
    return {
      // trainNameForWatch:this.$root.GlobalTrainName,
      // input:
      requestJsonData: {
        mainData: {
          trainName: null,
          isGetAll: true // TODO this.isGetAll 可以将整个请求 放到里面
        }
      },
      // output: TODO 调用后台时，去掉这部分。请求得到的数据
      responseJsonData: {
        partTitle: "数据集动态信息",
        lineChartId: lineChartId,
        plotData: {
          legend: ["legend1", "legend2", "legend3", "legend4"],
          data: [
            {
              name: "legend1", // 折线名称
              type: "line", // 线形
              showSymbol: false,
              hoverAnimation: false,
              data: [
                [1, 120],
                [2, 132],
                [3, 101],
                [4, 134],
                [5, 90],
                [6, 230],
                [7, 210]
              ] // 数据
            },
            {
              name: "legend2",
              type: "line",
              data: [
                [1, 220],
                [2, 182],
                [3, 191],
                [4, 234],
                [5, 290],
                [6, 330],
                [7, 310]
              ]
            },
            {
              name: "legend3",
              type: "line",
              data: [
                [1, 150],
                [2, 1232],
                [3, 201],
                [4, 154],
                [5, 190],
                [6, 330],
                [7, 410]
              ]
            },
            {
              name: "legend4",
              type: "line",
              data: [
                [1, 320],
                [2, 332],
                [3, 301],
                [4, 334],
                [5, 390],
                [6, 330],
                [7, 320]
              ]
            }
          ]
        },
        addData: []
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
      window.console.log(`${lineChartId}检测到trainname改变 ${this.$root.GlobalTrainName}`)
      this.requestJsonData.mainData.trainName = this.$root.GlobalTrainName
      this.requestJsonData.mainData.isGetAll=true
    },
  },

  mounted() {
    this.circula_request_dataset_dynamic_info();
  },
  methods: {
    // 处理原始数据
    _handle_dsDynamicInfoDict_all(dsDynamicInfoDict) {
      /**
       * @param {Object} dsDynamicInfoDict {col1:[],col2:[],col3:[]}
       * @returns 
       * plotData = {
          legend: ["legend1", "legend2", "legend3", "legend4"],
          data: [
            {
              name: "legend1", // 折线名称
              type: "line", // 线形
              showSymbol: false,
              hoverAnimation: false,
              data: [
                [1, 120],
                [2, 132],
                [3, 101],
                [4, 134],
                [5, 90],
                [6, 230],
                [7, 210]
              ] // 数据
            },
            {}
          ]
        }

       */

      let step = dsDynamicInfoDict.step;

      let plotData = {};
      plotData.legend = [];

      plotData.data = [];

      for (let [k, v] of Object.entries(dsDynamicInfoDict)) {
        // TODO step
        if (k != "step") {
          //
          plotData.legend.push(k); // 第 k 个序列的名称

          //
          let itemSeriesObj = {};

          itemSeriesObj.name = k;
          itemSeriesObj.type = "line";
          itemSeriesObj.showSymbol = false;
          itemSeriesObj.hoverAnimation = false;
          itemSeriesObj.data = [];

          for (let i in v) {
            itemSeriesObj.data.push([step[i], v[i]]);
          }

          //
          plotData.data.push(itemSeriesObj);
        }
      }

      return plotData;
    },

    // 处理新增数据
    _handle_dsDynamicInfoDict_notall(dsDynamicInfoDict) {
      /**
       * @param {Object} dsDynamicInfoDict {col1:[],col2:[],col3:[]}
       addData = [
          {
            seriesIndex: 0,
            data: []
          },
          {}
        ]
       */

      let step = dsDynamicInfoDict.step;
      let addData = [];
      let idx = 0;
      for (let [k, v] of Object.entries(dsDynamicInfoDict)) {
        // TODO step
        if (k != "step") {
          let itemSeriesObj = {};

          itemSeriesObj.seriesIndex = idx; // 第 k 个序列
          itemSeriesObj.data = [];
          for (let i in v) {
            itemSeriesObj.data.push([step[i], v[i]]);
          }
          addData.push(itemSeriesObj);
        }
      }
      return addData;
    },

    // 请求
    request_dataset_dynamic_info() {
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
          //
          if (this.requestJsonData.isGetAll) {
            // 处理原始数据
            let plotData = this._handle_dsDynamicInfoDict_all(
              dsDynamicInfoDict
            ); // 图数据
            this.responseJsonData = {
              partTitle: partTitle,
              lineChartId: this.lineChartId,
              plotData: plotData,
              addData: []
            }; // 数据双向绑定，绘图子组件通过 prop 自动更新
            this.requestJsonData.isGetAll = false
          } else {
            // 处理新增数据
            let addData = this._handle_dsDynamicInfoDict_notall(
              dsDynamicInfoDict
            ); // 图数据
            this.responseJsonData.addData = addData; // 绘图子组件通过 prop 传递数据，并在内部监听 addData 数据，触发 appendData 事件
          }
        })
        .catch(err => {
          window.console.log(
            "消息发送失败:" + err.status + "," + err.statusText
          );
        });
    },

    // 循环请求
    circula_request_dataset_dynamic_info() {
      // setTimeout(this.request_dataset_dynamic_info, circulaTime);
      // window.console.log("进入到循环请求！");
      setTimeout(() => {
        this.responseJsonData.addData = [
          {
            seriesIndex: 0,
            data: []
          },
          {
            seriesIndex: 1,
            data: [[8, 101], [9, 134], [10, 90], [11, 230], [12, 210]]
          },
          {
            seriesIndex: 2,
            data: [[8, 103], [9, 154], [10, 70], [11, 200], [12, 101]]
          },
          {
            seriesIndex: 3,
            data: [[8, 123], [9, 174], [10, 80], [11, 270], [12, 200]]
          }
        ];
      }, 10000);
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
