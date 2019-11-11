// 模型配置静态信息 自治

<template>
    <div class="modelstatic">
        <StaticTable v-bind:partTitle="this.partTitle"></StaticTable>
    </div>
</template>

<script>
import StaticTable from "./StaticTable"

export default {
    name:"ModelStatic",

    data (){
        return {
            partTitle:"模型静态信息"
        }
    },

    components :{
        StaticTable,
    }

}
</script>

<style scoped>

</style>