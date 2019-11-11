// 系统静态信息 自治

<template>
    <div class="sysstatic">
        <StaticTable v-bind:partTitle="this.partTitle"></StaticTable>
    </div>
</template>

<script>
import StaticTable from "./StaticTable"

export default {
    name:"SysStatic",

    data (){
        return {
            partTitle:"系统静态信息"
        }
    },

    components :{
        StaticTable,
    }

}
</script>

<style scoped>

</style>