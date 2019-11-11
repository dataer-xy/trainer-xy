// 静态信息表，每个会有一个标签
// 固定大小，超出大小会有下拉框
// 基础模块，非自治

<template>
  <div class="statictable">
    <el-card class="box-card">
      <div slot="header" class="clearfix">{{this.partTitle}}</div>
      <div class="statictable-table">
        <el-table v-bind:data="this.tableData" style="width: 100%">
          <el-table-column prop="key" label="变量" width="120"></el-table-column>
          <el-table-column prop="value" label="值" width="120"></el-table-column>
        </el-table>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "StaticTable",
  props: [
    "partTitle", // "标题"
    "url"
  ],
  data() {
    return {
      // TODO data 是通过 url 从后端获取的
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
};
</script>

<style scoped>
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.clearfix {
  height: 50px;
  margin: 0px;
  padding: 0px;
  line-height: 4;
}

.box-card {
  width: 300px;
}
</style>
