// 数据集静态信息 自治

<template>
    <div class="datasetstatic">
        <StaticTable v-bind:partTitle="this.partTitle"></StaticTable>
    </div>
</template>

<script>
import StaticTable from "./StaticTable"

export default {
    name:"DatasetStatic",

    data (){
        return {
            partTitle:"数据集静态信息"
        }
    },

    components :{
        StaticTable,
    }

}
</script>

<style scoped>
</style>