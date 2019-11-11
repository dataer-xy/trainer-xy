// 消息队列静态信息 自治

<template>
    <div class="msmgstatic">
        <StaticTable v-bind:partTitle="this.partTitle"></StaticTable>
    </div>
</template>

<script>
import StaticTable from "./StaticTable"

export default {
    name:"MsmgStatic",

    data (){
        return {
            partTitle:"MQ静态信息"
        }
    },

    components :{
        StaticTable,
    }

}
</script>

<style scoped>

</style>