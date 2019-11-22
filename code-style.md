# 代码规范

# 包开发要求
* 客户端的易用性
* 文档的齐全
* 数据结构变换的多样性

# 文档要求
* what
* installation
* getting started
* user guide
* api (pandas koalas pyspark 使用的好特别 )
* news
* todo
* development
* release note

# git 要求


# 命名规范
* 函数 a_b_c
* 类 AbCd
* 变量 abCd （不可以有下划线）
* 接口 IGetData
* 模块 尽可能短小（一个单词），不能包含大写字母，不能有空格等分割符
* 包 abc （全小写）

# 
* 如果模块主要是动作/函数，应该用动词命名模块，比如 buildds，主要是类等静态，则使用 静态词
* 函数/方法本应该有参数类型和参数个数检验，但不做！
* 不许使用语法糖。
* exception 要求严格的继承层次结构，并且在合适的地方使用，如果不能保证合理使用exception，则不适用自定义exception
* 临时变量用temp开头 tempTable1
* 尽可能的使用类型注释
* 布尔变量 用 isReturn 的格式
* 变量注释 --> int
* 函数/方法/类 的说明 在外面简单注释一下，用 #
```python

# 该函数的作用
def a_b(a):
    """该函数的作用

    :parm a:

    :return: 
    
    """

```
* #用于步骤注释，# NOTE: 单行的注释应该放在行后面，而不是行上面
```python
#
a = 1 # this is the line note

# 
b = 2 # NOTE: 这个地方有什么特点
```



# 引用
* 先引用外部包
* 再用相对路径引用内部模块



# 程序标识(dataset 所有模块中 通用的标识)：
* 方法上标识的OK123： 1 表示编写完成，2表示流通测试，3表示test
* impliment 标识实现接口，无论是抽象类，还是1级实现类，2级实现类
* important 标识方法重要性，1 非常重要（经常使用），2 一般（default），3 不重要

* 第1开发阶段不做标记，第二开发阶段添加的方法 用 stage 2 注释
* pyspark 有一个@since(1.3) 装饰器

# 
* 抽象类可以有实例化方法__init__ 会被子类自动继承
* 抽象类之间的关联1:n很难在实际的code中体现！
* 抽象方法中的依赖是无法描述的，因为只有具体实现方法内容时，才能弄好

# 
vscode - jupyter 真的很烂，还丢数据，mmb.