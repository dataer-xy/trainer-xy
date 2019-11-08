    // TODO 这个地方放到外面算了 并且改成对象数组
    const buttomMap = new Map()
    buttomMap
        .set("stop",0)
        .set("pauseEpoch",2)
        .set("continueEpoch",3)
        .set("pauseBatch",4)
        .set("continueBatch",5)

    const buttomTooltipMap = new Map() // 提示的内容
    buttomTooltipMap
        .set("stop","终止训练")
        .set("pauseEpoch","暂停下一个 epoch")
        .set("continueEpoch","继续 epoch")
        .set("pauseBatch","暂停下一个 batch")
        .set("continueBatch","继续 batch")

    const buttomConfirmMap = new Map() // 弹窗内容
    buttomConfirmMap
        .set("stop","真的要终止训练吗？一般在训练不理想或者已经饱和的时候，才主动终止训练！")
        .set("pauseEpoch","将暂停下一个 epoch，不要多次点击。如果要继续训练，点击 continueEpoch ！")
        .set("continueEpoch","继续 epoch")
        .set("pauseBatch","暂停下一个 batch，不要多次点击。如果要继续训练，点击 continueBatch ！")
        .set("continueBatch","继续 batch")
