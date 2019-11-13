// 功能：
// 1、鼠标放到按钮上会有提示
// 2、点击时，向后端发送一个消息
// 3、消息发送成功时，会有弹窗

<template>
    <div class="buttombase">
        <el-tooltip v-bind:content="this.tooltipContent" placement="top">
            <el-button v-bind:type="this.buttomType" @click="this.on_send_state" v-bind:roundButton="this.round">
                {{this.buttomStr}}
            </el-button>
        </el-tooltip>
    </div>
</template>

<script>

import {DEBUG,BaseUrl} from "../config"

export default {
    name:"ButtomBase",

    // 组件内的静态量，不应该在组件中改变 TODO 直接传对象
    // 如果你想要将一个对象的所有属性都作为 prop 传入，你可以使用不带参数的 v-bind <blog-post v-bind="object""></blog-post>
    props:[
        "buttomType",//  success / info / warning / error
        "buttomStr", // "按钮的文本内容"
        "confirmStr", // 弹窗内容
        "stateInt",
        "tooltipContent" // 提示的内容
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

        // 向后端发送信息
        send_state() {
            this.axios.post('',{
                data : this.jsonData,
                baseURL : BaseUrl,
            }).then(resp=>{
                // 接受响应
                window.console.log(resp.data)
                this.$message({
                    type: 'success',
                    message: `消息${this.stateInt}发送成功!`
                });
            }).catch(err=>{
                window.console.log('消息发送失败:'+err.status+','+err.statusText);
            });
        },

        // 事件
        on_send_state() {
            // window.console.log(`here${this.buttomType}`)
            // window.console.log(`here${this.tooltipContent}`)
            // window.console.log(`here${this.stateInt}`)
            this.$confirm(`${this.confirmStr}`, '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: this.buttomType
                }).then(() => {
                    if (!DEBUG) {
                        // 向后端发送消息
                        this.send_state()
                    } else {
                        this.$message({
                            type: 'success',
                            message: `消息${this.stateInt}发送成功!`
                        });
                    }
                    
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

</style>