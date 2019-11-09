<template>
    <div class="traindynamic">
        <el-tag>训练动态信息</el-tag>
        <LineChart></LineChart>
        <ButtomList></ButtomList>
    </div>
</template>

<script>
import LineChart from "./EchartsBase"
import ButtomList from "./ButtomList"

export default {
    name : "TrainDynamic",
    data() {
        return {
            
        }
    },
    props : [],
    components :{
        LineChart,
        ButtomList
    }

}
</script>

<style  scoped>
.traindynamic{
    text-align: center;
}

</style>