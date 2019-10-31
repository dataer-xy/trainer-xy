
msMg = MessageManager()

ds = DataSet()

model = Module()


train(model,tds,vds,msMg) # NOTE 是一个解

from modelconfig import modelConfig 



def train(model,trainDataSet,validDataSet,msMg):

    # 创建 trainName
    # startTime

    trainStaticInfoDict = {
        "trainName":trainName,
        "startTime":startTime,
        "totalStep":??,
        "allEpoch":??
        "allBatch":??
    }

    msMg.push(trainStaticInfoDict,"trainStaticInfoDict")


    #----固定消息--------------------------------------------

    modelConfigStaticInfoDict = modelConfig.to_dict()
    msMg.push(modelConfigStaticInfoDict,"modelConfigStaticInfoDict")

    tdsStaticInfoDict,_ = trainDataSet.describe()
    vdsStaticInfoDict,_ = validDataSet.describe()

    msMg.push(tdsStaticInfoDict,"tdsStaticInfoDict")
    msMg.push(vdsStaticInfoDict,"vdsStaticInfoDict")

    

    # 数据集信息1
    # 模型信息1
    # 训练信息
    # 消息队列信息
    # 机器信息1

    for epoch_i in range(epochs):
        epochState = msMg.pull(topic="epochState") # --> int
        if epochState == 2:
            # pause 暂停，只能继续消费队列，找到继续/终止命令
            while epochState != 3 or epochState != 0:
                epochState = msMg.pull(topic="epochState") # --> int
            
            # 2 3 6 None
            if epochState == 0:
                return 0 # TODO 终止
        elif epochState == 0:
            return 0 # TODO 终止
        else:
            pass
     
        batch_i = 0
        trainDataSet.shuffle_idxs() # 每迭代一次都要 shuffle idxs
        
        for outputDict in trainDataSet:

            batchState = msMg.pull(topic="batchState") # --> int
            if batchState == 4:
                # pause 暂停，只能继续消费队列，找到继续/终止命令
                while batchState != 3 or batchState != 0:
                    batchState = msMg.pull(topic="batchState") # --> int
                
                # 2 3 6 None
                if batchState == 0:
                    return 0 # TODO 终止
            elif batchState == 0:
                return 0 # TODO 终止
            else: # 3 4 5 None
                pass
            
            #----------------------------------------------------------------------------
            # NOTE 尽量保持同名
            
            x_batch = outputDict["inputImage"]
            y_batch = outputDict["outputFormula"]
            z_batch = outputDict["inputFormulaLen"]
            a_batch = len(z_batch)
        
            feed_dict = {
                im2latexModel.batchSize : a_batch,
                im2latexModel.inputImage: x_batch, 
                im2latexModel.outputFormula: y_batch,
                im2latexModel.inputFormulaLen: z_batch
            }

            if step % int(modelConfig.runMetaDataFrequency * modelConfig.nSteps) == 0:
                # NOTE: 每次都新定义一个
                runOptions = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE) # 配置运行时需要记录的信息的protocolmessage
                runMetadata = tf.RunMetadata() # 运行时记录运行信息的protocol message 
                _, loss, accuracy_all, summary_str = sess.run(
                    [
                        im2latexModel.train_op, 
                        im2latexModel.loss_op, 
                        im2latexModel.accuracy_all_op, 
                        merged_summary_op
                    ], 
                    feed_dict=feed_dict,
                    options=runOptions,
                    run_metadata=runMetadata
                )
                summaryWriter.add_run_metadata(runMetadata, 'step{}'.format(step), global_step=step)

            # 数据集信息
            dsIterInfo = outputDict["_info"]
            msMg.push(dsIterInfo,topic="dsIterInfo")

            #----------------------------------------------------------------------------
            # 训练信息

            # 计算平均loss并显示出来
            if step % modelConfig.printStep == 0:
                trainIterInfoDict = {
                    "step":step,
                    "epoch":epoch_i,
                    "batch":batch_i,
                    "loss":loss,
                    "acc":accuracy_all,
                    "loss_val":None,
                    "acc_val":None
                }

                msMg.push(trainIterInfoDict,topic="trainIterInfoDict")


            # 模型保存 OK
            if step % modelConfig.modelStepSave == 0:
                msMg.push(sess,topic="sess")
                # saver.save(
                #     sess, os.path.join(modelConfig.checkpointPath,modelConfig.checkpointModelName), 
                #     global_step=step
                # )

            # 模型可视化 OK - tensorboard
            if step % modelConfig.summaryStepSave == 0:
                msMg.push(summaryStr,topic="summaryStr")
                # summaryWriter.add_summary(summaryStr, global_step=step) # buffer--as str



            #----------------------------------------------------------------------------
            # 验证集
            if validDataSet is not None:

                if step % int(modelConfig.nSteps / modelConfig.validFrequency) == 0:
                    
                    #----------------------------------------------------------------
                    # 计算 validation loss

                    for xy_batch in validDataSet:
                        x_batch = xy_batch["inputImage"]
                        y_batch = xy_batch["outputFormula"]
                        z_batch = xy_batch["inputFormulaLen"]
                        a_batch = len(z_batch)
                
                        feed_dict = {
                            im2latexModel.batchSize : a_batch,
                            im2latexModel.inputImage: x_batch, 
                            im2latexModel.outputFormula: y_batch,
                            im2latexModel.inputFormulaLen: z_batch
                        }
                        valid_loss, valid_predict_true_num_item, valid_count_num_item = sess.run(
                            [im2latexModel.loss_op, im2latexModel.predict_true_num_op, im2latexModel.count_num_op], 
                            feed_dict=feed_dict
                        )
                        
                        # 
                        valid_predict_true_num_all = valid_predict_true_num_all + int(valid_predict_true_num_item)
                        valid_count_num_all = valid_count_num_all + int(valid_count_num_item)
                        valid_accuracy_all = valid_predict_true_num_all / valid_count_num_all

                        # break
                    
                    #----------------------------------------------------------------
                    trainIterInfoDict = {
                        "step":step,
                        "epoch":epoch_i,
                        "batch":batch_i,
                        "loss":loss,
                        "acc":accuracy_all,
                        "loss_val":valid_loss,
                        "acc_val":valid_accuracy_all
                    }



            step += 1
            batch_i += 1
