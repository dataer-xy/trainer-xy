
<template>
  <div class="wapper">
    <el-container>
      <el-aside width="201px">
        <NavTrainer></NavTrainer>
      </el-aside>
      <el-container>
        <el-header>
          <Header></Header>
        </el-header>
        <el-main>
          <StaticSession></StaticSession>
          <DynamicSession></DynamicSession>
        </el-main>
        <el-footer>Footer</el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import NavTrainer from "./NavTrainer";
import Header from "./Header";

import DynamicSession from "./DynamicSession";
import StaticSession from "./StaticSession";


export default {
  name: "Wapper",
  components: {
    Header,
    NavTrainer,
    DynamicSession,
    StaticSession,
  }
};
</script>

<style scoped>

.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-header{
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 40px;
  height: 100px ! important; /* element.style样式如何修改 https://blog.csdn.net/chenguang79/article/details/46721971 */
}

.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 80px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  /* line-height: 500px; */
}
</style>