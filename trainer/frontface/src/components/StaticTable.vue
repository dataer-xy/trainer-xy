// 静态信息表，每个会有一个标签
// 固定大小，超出大小会有下拉框

<template>
    <div>
        <div class="statictable-tag">
            <el-tag>训练静态信息</el-tag>
        </div>
         
        <div class="statictable-table">
            <el-table :data="tableData" style="width: 100%">
            <el-table-column
                prop="date"
                label="日期"
                width="180">
            </el-table-column>
            <el-table-column
                prop="name"
                label="姓名"
                width="180">
            </el-table-column>
            <el-table-column
                prop="address"
                label="地址">
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
            date: '2016-05-02',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1518 弄'
          }, {
            date: '2016-05-04',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1517 弄'
          }, {
            date: '2016-05-01',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1519 弄'
          }, {
            date: '2016-05-03',
            name: '王小虎',
            address: '上海市普陀区金沙江路 1516 弄'
          }]
        }
      }
    }
</script>

<style scoped>

</style>
