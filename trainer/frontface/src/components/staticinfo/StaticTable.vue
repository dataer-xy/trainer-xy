// 静态信息表，每个会有一个标签
// 固定大小，超出大小会有下拉框
// 基础模块，非自治

<template>
  <div class="statictable">
    <el-card class="statictable-card">
      <div slot="header" class="statictable-header">{{this.partTitle}}</div>
      <div class="statictable-table" >
        <el-table v-bind:data="this.tableData" style="width: 100%"  height="350" :fit="false">
          <el-table-column prop="key" label="变量" fixed width="150px"></el-table-column>
          <el-table-column prop="value" label="值" width="500px" ></el-table-column>
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
    "tableData", // 表数据
  ],
  data() {
    return {
      
    };
  }
};
</script>

<style scoped>
.statictable-card {
  width: 400px;
}

/* statictable-table 表的高度 只要在el-table元素中定义了height属性，即可实现固定表头的表格，而不需要额外的代码。*/

.statictable-header:before,
.statictable-header:after {
  display: table;
  content: "";
}
.statictable-header:after {
  clear: both;
}

.statictable-header {
  height: 50px;
  margin: 0px;
  padding: 0px;
  line-height: 4;
}


</style>
