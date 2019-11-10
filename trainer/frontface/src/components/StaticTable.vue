// 静态信息表，每个会有一个标签
// 固定大小，超出大小会有下拉框

<template>
    <div class="statictable">
        <div class="statictable-tag">
            <el-tag>训练静态信息</el-tag>
        </div>
         
        <div class="statictable-table">
            <el-table :data="tableData" style="width: 100%">
            <el-table-column
                prop="key"
                label="变量"
                width="180">
            </el-table-column>
            <el-table-column
                prop="value"
                label="值"
                width="180">
            </el-table-column>
            </el-table>
        </div>

    </div>
</template>

<script>
export default {

    name : "StaticTable",
    data() {
        return {
          tableData: [{
            key: '2016-05-02',
            value: '王小虎',
          }, {
            key: '2016-05-04',
            value: '王小虎',
          }, {
            key: '2016-05-01',
            value: '王小虎',
          }, {
            key: '2016-05-03',
            value: '王小虎',
          }]
        }
      }
    }
</script>

<style scoped>

</style>
