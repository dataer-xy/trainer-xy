// 折线图
<template>
  <div class="linechart">
    <!-- <el-card> -->
      <!-- 卡片显示 -->
      <el-tag>{{this.partTitle}}</el-tag>
      <div class="linechart-nothing">
        <!-- 无内容填充高度 -->
      </div>
      <div
        class="linechart-fig"
        v-bind:id="this.lineChartId"
        style="width: 400px;height: 400px;margin:0 auto"
      ></div>
    <!-- </el-card> -->
  </div>
</template>

<script>
export default {
  name: "LineChart",

  props: [
    "partTitle", // 主题
    "lineChartId", // id 索引
    "plotData", // 原始数据
    "addData" // 新增数据
  ],

  // 数据
  data: function() {
    return {};
  },

  // 生命周期函数 表示挂载完毕，html 已经渲染
  mounted() {
    this.drawLine(this.lineChartId);
    this.linechart.setOption({
      series: this.plotData.data
    });
  },

  // watch
  watch: {
    addData: function(newVal) {
      for (let newData of newVal) {
        this.linechart.appendData(newData); // 有 appendData
      }
      this.linechart.resize();
    },
    plotData : function () {
      this.linechart.setOption({
        series: this.plotData.data
      });
    }
  },
  // 方法
  methods: {
    drawLine(domId) {
      // 基于准备好的dom，初始化echarts实例
      this.linechart = this.$echarts.init(document.getElementById(domId));
      // 绘制图表
      this.linechart.setOption({
        title: {
          text: ""
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            animation: false
          }
        },
        legend: {
          data: this.plotData.legend
        },
        // grid: {
        //   left: "3%",
        //   right: "4%",
        //   bottom: "3%",
        //   containLabel: true
        // },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          type: "value", //"time"
          boundaryGap: false,
          splitLine: {
            show: false
          }
          // data: this.plotData.xTicks
        },
        yAxis: {
          type: "value",
          // boundaryGap: [0, "100%"],
          splitLine: {
            show: false
          }
        },
        animation: false
      });
    }
  }
};
</script>

<style scoped>
.linechart-nothing {
  height: 10px;
}
.el-tag {
  height: 40px;
  padding: 10px;
  line-height: 20px;
  font-size: 16px;
}
</style>