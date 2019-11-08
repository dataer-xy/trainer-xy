// 功能：
// 1、鼠标放到按钮上会有提示
// 2、点击时，向后端发送一个消息
// 3、消息发送成功时，会有弹窗

<template>
    <div class="buttom">
        <el-button type="text" @click="this.open2">点击打开 Message Box</el-button>
    </div>
</template>

<script>
    // import {DEBUG,BaseUrl} from "../js/config"

    export default {
        name:"ButtomBase",

        // 组件内的静态量，不应该在组件中改变 TODO 直接传对象
        // 如果你想要将一个对象的所有属性都作为 prop 传入，你可以使用不带参数的 v-bind <blog-post v-bind="object""></blog-post>
        props:[
            "buttomType",// 主要 danger 危险
            "buttomStr", // "按钮的文本内容"
            "confirmStr", // 提示信息
            "stateInt",
            "tooltipContent"
        ],

        data: function () {
            return {
                round : true, // 按钮形状

                jsonData : {
                    "mainData":this.stateInt // 是依据 buttom
                }

            }
        },

        methods : {
            open2() {
                window.console.log(`打印的啥？${this.stateInt}`)
                this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
                }).then(() => {
                this.$message({
                    type: 'success',
                    message: '删除成功!'
                });
                }).catch(() => {
                this.$message({
                    type: 'info',
                    message: '已取消删除'
                });          
                });
            },

            // // 向后端发送信息
            // send_state() {
            //     this.axios.post('',{
            //         data : this.jsonData,
            //         baseURL : BaseUrl,
            //     }).then(resp=>{
            //         // 接受响应
            //         window.console.log(resp.data)
            //         this.$message({
            //             type: 'success',
            //             message: `消息${this.stateInt}发送成功!`
            //         });
            //     }).catch(err=>{
            //         window.console.log('消息发送失败:'+err.status+','+err.statusText);
            //     });
            // },

            // 事件
            on_send_state() {
                this.$confirm("this.confirmStr", '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                    }).then(() => {
                        // if (!DEBUG) {
                        //     // 向后端发送消息
                        //     this.send_state()
                        // } else {

                        this.$message({
                            type: 'success',
                            message: `消息${this.stateInt}发送成功!`
                        });
                        // }
                        
                    }).catch(() => {
                        this.$message({
                            type: 'info',
                            message: '已取消'
                        });          
                    });
            },



        },

    }
    
</script>

<style scoped>
#buttom {
    width: '50px';
    height: '30px';
}
</style>