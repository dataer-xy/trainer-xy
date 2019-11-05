import os

import tensorflow as tf

from image2latex.models.myim2latex.config.modelconfig import modelConfig

import hiddenlayer as hl 
from image2latex.models.myim2latex.selfutils.modelplot import MyCanvas # 自制画布



def train_im2latexModel(im2latexModel,trainDataSet,validDataSet=None):


    # 3、模型可视化 OK summary summaryWriter tensorboard
    # TensorBoard 默认是不会记录每个节点的用时、耗费的内存大小等这些信息的
    tf.summary.scalar('loss_op', im2latexModel.loss_op) # histogram、image...
    tf.summary.scalar("predict_true_num_op", im2latexModel.predict_true_num_op)
    tf.summary.scalar("count_num_op", im2latexModel.count_num_op)
    tf.summary.scalar("accuracy_op", im2latexModel.accuracy_op)
    tf.summary.scalar("predict_true_num_all_op",im2latexModel.predict_true_num_all_op)
    tf.summary.scalar("count_num_all_op", im2latexModel.count_num_all_op)
    tf.summary.scalar("accuracy_all_op", im2latexModel.accuracy_all_op)


    # 4、模型训练的可视化 hiddenlayer
    myHistory = hl.History() # summary、progress、save、load、steps、get_total_time、formatted_steps、
    myCanvas = MyCanvas(classes=None)

    # 6、使用save_model保存模型用于部署 -- 这种方式不仅保存garph,还有参数
    # NOTE: 这个似乎并不是每一步都保存，而是保存最终的graph和variable 用于部署环境。因为它并没有提供更多的保存步骤等信息
    # 因此，它被用于训练结束之后，保存。这个在https://stackoverflow.com/questions/33759623/tensorflow-how-to-save-restore-a-model 有说明
    # NOTE: 下面的tf2.0中的示例再次说明了其用法
    # x = input_layer.Input((4,), name="x")
    # y = core.Dense(5, name="out")(x)
    # model = training.Model(x, y)
    # tf.saved_model.save(model, '/tmp/saved_model/')
    # The exported SavedModel takes "x" with shape [None, 4] and returns "out"
    # with shape [None, 5]

    # builder = tf.saved_model.builder.SavedModelBuilder(modelConfig.exportPath)  # 构建者模式？？？


    # 训练配置
    tfconfig = tf.ConfigProto(allow_soft_placement=True) # 需要在没有GPU的情况下，转为CPU
    tfconfig.gpu_options.allow_growth = True # 动态申请显存
    # gpu_options.per_process_gpu_memory_fraction = 0.4 # 占用40%显存

    with tf.Session(config=tfconfig) as sess: # graph=trainGraph, 

        init = tf.global_variables_initializer() # 全局变量初始化
        sess.run(init)

        summaryWriter.add_graph(sess.graph)

        step = 0
        predict_true_num_all = 0
        count_num_all = 0
        valid_predict_true_num_all = 0
        valid_count_num_all = 0

        for epoch_i in range(modelConfig.epochs):

            batch_i = 0
            trainDataSet.shuffle_idxs() # 每迭代一次都要 shuffle idxs
            for outputDict in trainDataSet:

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
                else:
                    _, loss, accuracy_all, summary_str = sess.run(
                        [
                            im2latexModel.train_op, 
                            im2latexModel.loss_op, 
                            im2latexModel.accuracy_all_op, 
                            merged_summary_op
                        ], 
                        feed_dict=feed_dict,
                    )

                

                #----------------------------------------------------------------------------
                # 记录结果

                # 计算总的准确率 NOTE 这个应该在 tf 中 OK
                # predict_true_num_all = predict_true_num_all + int(predict_true_num_item)
                # count_num_all = count_num_all + int(count_num_item)
                # accuracy_all = predict_true_num_all / count_num_all

                # 计算平均loss并显示出来
                if step % modelConfig.printStep == 0:
                    print("epoch:{epoch}  batch:{batch}  loss:{loss}  accuracy: {accuracy}".format(
                        epoch=epoch_i,batch=batch_i,loss=loss,accuracy=accuracy_all
                    ))

                # 模型保存 OK
                if step % modelConfig.modelStepSave == 0:
                    saver.save(
                        sess, os.path.join(modelConfig.checkpointPath,modelConfig.checkpointModelName), 
                        global_step=step
                    )

                # 模型可视化 OK - tensorboard
                if step % modelConfig.summaryStepSave == 0:
                    summaryWriter.add_summary(summary_str, global_step=step) # buffer--as str

                # 模型运行时可视化 OK - hiddenlayer
                try:
                    if step % modelConfig.printStep == 0:
                        myHistory.log(step=step, loss=loss, accuracy=accuracy_all) # NOTE 这个地方是用字典存储的
                        # myHistory.progress()

                    if step % modelConfig.hiddenLayerStepSave == 0:
                        myCanvas.draw_plot([myHistory["accuracy"], myHistory["loss"]])
                        # OK save figure
                        myCanvas.save(os.path.join(modelConfig.historyPath, modelConfig.canvasFileName))
                        # OK save history
                        myHistory.save(os.path.join(modelConfig.historyPath, modelConfig.historyFileName)) # 用pickle 保存
                except:
                    pass


                #----------------------------------------------------------------------------
                # 验证集
                if validDataSet is not None:
                    try:
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
                            # 记录结果

                            # 1
                            print(
                                'Epoch {:>3}/{} Batch {:>4} - Training Loss: {:>6.3f}  - Validation loss: {:>6.3f}  - Training Accuracy: {:>6.3f}  - Validation Accuracy: {:>6.3f} '
                                .format(epoch_i, 
                                        modelConfig.epochs, 
                                        batch_i, 
                                        loss,
                                        valid_loss,
                                        accuracy_all,
                                        valid_accuracy_all)
                            )


                            # 2
                            myHistory.log(step=step, loss_val=valid_loss, accuracy_val_=valid_accuracy_all) # NOTE 这个地方是用字典存储的
                            # myHistory.progress()

                            with myCanvas:
                                myCanvas.draw_plot([myHistory["loss"], myHistory["loss_val"]],ylabel="loss")
                                myCanvas.draw_plot([myHistory["accuracy"], myHistory["accuracy_val"]],ylabel="accuracy")

                            # OK save figure
                            myCanvas.save(os.path.join(modelConfig.historyPath, modelConfig.canvasFileName))
                            # OK save history
                            myHistory.save(os.path.join(modelConfig.historyPath, modelConfig.historyFileName))

                    except:
                        pass
                
                step += 1
                batch_i += 1
                
        # 保存最终的模型信息，用于部署环境
        # builder.add_meta_graph_and_variables(sess, [tf.saved_model.tag_constants.TRAINING])

        # OK summary 
        summaryWriter.close()
    
        im2latexModel.sess = sess # NOTE NOTE NOTE TODO 是不是已经关闭了？是的


# tensorboard --logdir="/目录"
