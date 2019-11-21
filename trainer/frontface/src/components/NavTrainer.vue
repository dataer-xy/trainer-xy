// trainer 条目的导航栏，自治
// 获取数据，并填充

<template>
  <div class="navtrainer">
    <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">
      <el-radio-button :label="false">展开</el-radio-button>
      <el-radio-button :label="true">收起</el-radio-button>
    </el-radio-group>
    <el-menu
      default-active="1-1"
      class="el-menu-vertical"
      @open="handleOpen"
      @close="handleClose"
      :collapse="isCollapse"
    >
      <el-submenu
        v-for="(trainList, itemProjName, index) in responseJsonData"
        v-bind:key="trainList.id"
        v-bind:index="`${index+1}`"
      >
        <template slot="title">
          <i class="el-icon-location"></i>
          <span slot="title">{{itemProjName}}</span>
        </template>
        <el-menu-item-group v-for="(trainName, subIndex) in trainList" v-bind:key="trainName.id">
          <el-menu-item v-bind:index="`${index+1}-${subIndex+1}`">
            <TrainButtom v-bind:trainName="trainName"></TrainButtom>
          </el-menu-item>
        </el-menu-item-group>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
import { BaseUrl,DEBUG } from "./config";
import TrainButtom from "./TrainButtom";

//
let bpTrainList = "/bpTrainList";
//
let responseJsonData = {}
if (DEBUG){
  // 测试用的数据
  responseJsonData={
    projectName1: ["201911141211", "201911151211"],
    projectName2: ["201911161211", "201911171211"],
    projectName3: ["201911181211", "201911191211"]
  }
}


export default {
  name: "NavTrainer",

  components: {
    TrainButtom
  },

  data() {
    return {
      isCollapse: true,
      // input:
      requestJsonData: {
        mainData: {}
      },
      // output:
      responseJsonData: responseJsonData
    };
  },

  mounted() {
    if (!DEBUG){
      this.request_trainlist();
    } else {
      this.compute_origianl_trainName();
    }

    
  },

  methods: {

    /************************************************************/

    // 处理后端请求来的数据
    _handle_projectNameList(projectNameList) {
      // 输入 ：projectNameList {trainName:projectName,...}
      // 输出 ：trainListData {projectName:[trainName1,trainName2...]}
      // "projectName1":["trainer1","trainer2"],
      // "projectName2":["trainer1","trainer2"],
      // "projectName3":["trainer1","trainer2"],

      let trainListData = {};

      for (let [trainName, projectName] of Object.entries(projectNameList)) {
        if (trainListData.hasOwnProperty(projectName)) {
          trainListData[projectName].push(trainName);
        } else {
          // 没有该属性
          trainListData[projectName] = [];
          trainListData[projectName].push(trainName);
        }
      }

      return trainListData;
    },


    // 向后端请求数据
    request_trainlist() {
      this.axios
        .post(bpTrainList, this.requestJsonData, {
          baseURL: BaseUrl, // 配置未生效！？
        })
        .then(resp => {
          // 接受响应
          // window.console.log(resp.data);
          //
          let orginalData = resp.data.mainData;

          let projectNameList = orginalData.projectNameList;
          let trainListData = this._handle_projectNameList(projectNameList); // 表数据

          this.responseJsonData = trainListData;

          // 计算初始化的 name
          this.compute_origianl_trainName();
        })
        .catch(err => {
          window.console.log(
            "消息发送失败:" + err.status + "," + err.statusText
          );
        });
    },


    // 计算时间最大的名字作为开始的目录
    compute_origianl_trainName() {
      // 计算时间最大的名字作为开始的目录

      let maxTrainName = 1;
      for (let trainList of Object.values(this.responseJsonData)) {
        for (let trainName of trainList) {
          let itemTrainNameNum = Number(trainName);
          if (itemTrainNameNum > maxTrainName) {
            maxTrainName = itemTrainNameNum;
          }
        }
      }

      window.console.log(`当前最大name 是 ${maxTrainName}`); //OK
      this.$root.GlobalTrainName = maxTrainName.toString();
    },

    /************************************************************/

    handleOpen(key, keyPath) {
      window.console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      window.console.log(key, keyPath);
    },
  }
};
</script>

<style scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
</style>


