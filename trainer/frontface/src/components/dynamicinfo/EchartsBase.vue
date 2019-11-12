// 折线图
<template>
  <el-card>
    <el-tag>{{this.partTitle}}</el-tag>
    <div class="linechart-nothing">
      <!-- 无内容填充高度 -->
    </div>
    <div class="linechart-fig" v-bind:id="this.lineChartId" style="width: 400px;height: 400px;margin:0 auto"></div>
  </el-card>
</template>

<script>
export default {
  name: "LineChart",

  props: [
    "partTitle", // 主题
    "lineChartId", // id 索引
    "plotData" 
  ],

  // 数据
  data: function() {
    return {};
  },

  // 生命周期函数 表示挂载完毕，html 已经渲染
  mounted() {
    this.drawLine();
  },

  // 方法
  methods: {
    drawLine() {
      // 基于准备好的dom，初始化echarts实例
      let linechart = this.$echarts.init(
        document.getElementById(this.lineChartId)
      );
      // 绘制图表
      linechart.setOption({
        title: {
          text: ""
        },
        tooltip: {
          trigger: "axis"
        },
        legend: {
          data: this.plotData.legend
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: this.plotData.xTicks
        },
        yAxis: {
          type: "value"
        },
        series: this.plotData.data
      });
    }
  }
};
</script>

<style scoped>
.linechart-nothing{
  height: 10px;
}
.el-tag {
  height: 40px;
  padding: 10px;
  line-height: 25px;
  font-size: 16px;
}
</style>