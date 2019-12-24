

# 后后端

## 消息队列
* 组/库/项目的概念 -- 虚拟机/拼接路由 OK
* 删除项目 OK
* 删除队列 OK

## train
* 消息结构整理好 OK
* sysinfo OK
* trainer 调用 sysinfo 子进程 OK
* train stopState 发送到哪里？ 只能在 batch 上停止 OK
* sess summary 还有些问题, summary tfb 写的不是同一个文件！
* train 终止问题 return 0 ? 
* sysinfo 定义成进程或子进程 NO
* 调试时 mq 主动关闭了连接 https://blog.csdn.net/csdn_am/article/details/79894662

* app 从 trainer 拿到下层，引用很耗时 OK

* 速度-- 包装起来
* output 路径要修改 在 config 中
* 显示 GPU 利用率等信息




#-----------------------------------------------------------------------------






# 后端 11-7

* epochState，batchState回传 OK
* sess等什么时候处理？get None，从数据库中读取 config 信息 OK

* 所有trainer 的信息 OK
* 服务配置好 OK
* 测试 request OK

* train 静态属性增加 tag OK
* 有些不要的数据，在后端过滤掉 OK
* ds 等 动态数据没有 step 信息，要在 trainer 中加上 OK

* 后端的初始化是发送一个 index.html (由前端提供)??


* 后端 -- 删除某个trainer -- 后台管理工具
* 后端 -- 清空无用的任务，在 trainListStaticInfo 中进行 
* 后端 -- sql 的存储 用的 pandas ，有些字段无法存储，会报错。使用 table 来存储！
* 后端 -- TF summary 能否写进一个文件 （有一定的可能）
* 后端 -- sanic 如何传递 html 文件 OK 
* 后端 -- 发送的 html 能找到 js 等文件吗？ OK
* 后端 -- utils 整理




#-----------------------------------------------------------------------------


# 前端
* 创建项目 OK
* 设计结构 OK
* 写程序 OK

* 边框 OK
* buttom OK
* 走马灯 箭头 OK
* sess summary 隐藏请求 OK
* 显示 trainer 名称 div OK
* axios 的用法是否正确，响应可能是 data.data.mainData，如果是的话，修改后端，让后端直接返回数据，不管对错！OK
* 循环请求应该放到哪里？OK
* isGetAll 时，echart 要清空 NO
* key 的顺序会不会有问题 OK
* 循环请求 trainList
* stop 发送仍然有问题



* 前端 -- loss acc 分开
* 前端 -- foot -- tfb 集合
* 前端 -- 列表排序
* 前端 -- 设置学习率
* 前端 -- 自动将单图多线展开成多图多线
* 前端 -- 列表 指向时间最大的








# 调试 11-15
* 不可以改变变量的名称，可以增加字典的键（不需要改写后端），可以增加队列（需要改写后端）
* stop 只能发送到 batch 


# 结束 11-21
* 开发任务基本结束 OK
* 进入收尾阶段 OK




#-----------------------------------------------------------------------------


# 打包
* 客户端
* index.html npm run build (vue 如何部署？)
* pypi OK
* doc OK
* test
* readme OK
* readdoc 



#-----------------------------------------------------------------------------

# NEW

* train ds/sys 分开

* 能否深度组合 tfb?
* tfb 读取数据库研究一下
* 后后端 -- sys 780 子进程自动终止了？
* 前端/后端 -- 自动扩展前后端 --> 自动扩展静态信息，动态信息 （这个就和 tfb 的功能一样）

* 继续训练？消息队列继续

* 前端 -- 被迫停止，还是 完成

