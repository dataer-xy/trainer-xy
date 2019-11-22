
# DEBUG 结构

* bug id
* bug 内容
* bug 原因分析
* bug 处理方法简介
* 处理人 id
* 处理结果




# 1
* bug id: 1 
* bug 内容: dataset 的 show() 方法 tableForPrint = pd.DataFrame(outputDict) Data must 1-dim --> 无法拼接矩阵
* bug 处理方法简介：
1：将 np.ndarray tolist , pd.DataFrame 就不会出错。优点是简单，缺点是改变了数据类型，并且list会带来很大的内存消耗，且慢。
2：使用for，将np.ndarray中的元素，一个一个的传递到pd.DataFrame中。优点是保证数据类型，缺点是慢。
3：使用np 的split 方法可能会更快一些！并没有显著的效果。
采用1 NO 改用方法3 !
* 处理人 id：1
* 处理结果 ： OK




# 2
* bug id : 2
* bug 内容：pandas.io.sql.DatabaseError: Execution failed on sql 'select * from tableocrimgtext where id in (19999,)': (1064, "You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near ')' at line 1")

* bug 原因分析：
datamanager sqldatamanager.get_data_by_idxs() 方法的输入 idxs 是一个值，tuple 类型转换的时候，出错了

In [8]: a
Out[8]: array([1])

In [9]: tuple(a)
Out[9]: (1,)

In [10]: b = np.array([1,2,3])

In [11]: tuple(b)
Out[11]: (1, 2, 3)

* bug 处理方法简介：
判断 idxs 的长度，如果是1 ，则
* 处理人 id ；1
* 处理结果：OK




# 3

  File "D:\Program Files\Anaconda2\envs\python35\lib\site-packages\numpydoc\docscrape_sphinx.py", line 396, in __str__
    'methods': self._str_member_list('Methods'),
  File "D:\Program Files\Anaconda2\envs\python35\lib\site-packages\numpydoc\docscrape_sphinx.py", line 268, in _str_member_list
    if param_obj and pydoc.getdoc(param_obj):
  File "D:\Program Files\Anaconda2\envs\python35\lib\site-packages\dask\delayed.py", line 450, in __bool__
    raise TypeError("Truth of Delayed objects is not supported")
TypeError: Truth of Delayed objects is not supported




