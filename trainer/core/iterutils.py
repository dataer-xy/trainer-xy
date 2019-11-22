

def is_continue_in_epochState(msMg):
    """ 

    Parameters
    ----------
    msMg : MessageManager
        MessageManager 实例

    Returns
    -------
    ? : bool
        True 表示继续，False 表示终止 train 
    
    Notes
    -----
    1、由于 stop 消息只能发送到 batchState 队列，所以这里不会有终止，即 epochState 不会等于 0
    2、{
            "pauseEpoch":2,
            "continueEpoch":3,
            "pauseBatch":4,
            "continueBatch":5,
            "stop":0
        }
    """
    
    topic = "epochState"

    epochState = msMg.pull(topic=topic) # --> int
    if epochState == 2:
        # pause 暂停，只能继续消费队列，找到继续/终止命令
        print("在epoch暂停！")
        while epochState != 3 and epochState != 0:
            # NOTE：不断等待新的消息
            epochState = msMg.pull(topic=topic) # --> int
        
        # 2 3 6 None
        if epochState == 0:
            return False
        else:
            print("继续 epoch")
            return True
    elif epochState == 0:
        return False
    else:
        return True  


def is_continue_in_batchState(msMg):
    """ 

    Parameters
    ----------
    msMg : MessageManager
        MessageManager 实例

    Returns
    -------
    ? : bool
        True 表示继续，False 表示终止 train 
    
    Notes
    -----
    1、{
        "pauseEpoch":2,
        "continueEpoch":3,
        "pauseBatch":4,
        "continueBatch":5,
        "stop":0
    }
    
    """
    topic = "batchState"
    batchState = msMg.pull(topic=topic) # --> int
    if batchState == 4:
        # pause 暂停，只能继续消费队列，找到继续/终止命令
        print("在 batch 暂停！")
        while batchState != 5 and batchState != 0:
            batchState = msMg.pull(topic=topic) # --> int
        
        # 2 3  None
        if batchState == 0:
            return False 
        else:
            print("继续 batch")
            return True
    elif batchState == 0:
        return False 
    else: 
        return True

