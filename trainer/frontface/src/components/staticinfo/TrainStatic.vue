// 训练静态信息 自治

<template>
    <div class="trainstatic">
        <StaticTable v-bind:partTitle="this.partTitle"></StaticTable>
    </div>
</template>

<script>
import StaticTable from "./StaticTable"

export default {
    name:"TrainStatic",

    data (){
        return {
            partTitle:"训练静态信息"
        }
    },

    components : {
        StaticTable,
    }

}
</script>

<style scoped>

</style>