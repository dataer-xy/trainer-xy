# 2、保存模型 OK
saver = tf.train.Saver(max_to_keep=4) 
# 
merged_summary_op = tf.summary.merge_all() # op graph
summaryWriter = tf.summary.FileWriter(modelConfig.tensorboardLogPath) # 实例化一个FileWriter的类对象，并将当前TensoirFlow的计算图写入【日志文件】


summaryWriter.add_graph(sess.graph)

summaryWriter.add_run_metadata(runMetadata, 'step{}'.format(step), global_step=step)



saver.save(
    sess, os.path.join(modelConfig.checkpointPath,modelConfig.checkpointModelName), 
    global_step=step
)



summaryWriter.add_summary(summaryStr, global_step=step) # buffer--as str


