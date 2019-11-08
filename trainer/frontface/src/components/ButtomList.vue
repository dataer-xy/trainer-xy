// 将多个按钮放在一起

<template>
    <div >

    </div>
</template>

<script>
// TODO 这个地方放到外面算了 并且改成对象数组
const buttomMap = new Map()
buttomMap
    .set("pauseBatch",4)
    .set("continueBatch",5)

buttomTooltipMap
    .set("pauseBatch","暂停下一个 batch")
    .set("continueBatch","继续 batch")

buttomConfirmMap
    .set("continueBatch","继续 batch")


export default {

    data() {
        return {
            // stop, pauseEpoch,continueEpoch pauseBatch,continueBatch
            buttomInfoList : [
                {
                    buttomStr :"stop",
                    buttomType : "warning",
                    confirmStr : "真的要终止训练吗？一般在训练不理想或者已经饱和的时候，才主动终止训练！",
                    tooltipContent:"终止训练",
                    stateInt:0
                },
                {
                    buttomStr :"pauseEpoch",
                    buttomType : "warning",
                    confirmStr : "将在下一个 epoch 暂停，不要多次点击。如果要继续训练，点击 continueEpoch ！",
                    tooltipContent:"在下一个 epoch 暂停",
                    stateInt:2
                },
                {
                    buttomStr :"continueEpoch",
                    buttomType : "info",
                    confirmStr : "继续 epoch",
                    tooltipContent:"继续 epoch",
                    stateInt:3
                },
                {
                    buttomStr :"continueEpoch",
                    buttomType : "info",
                    confirmStr : "将在下一个 batch zha，不要多次点击。如果要继续训练，点击 continueBatch ！",
                    tooltipContent:"继续 epoch",
                    stateInt:3
                },
            ]
        }
    },

    props : [],

    methods: {
        
    },
    
}
</script>

<style scoped>

</style>