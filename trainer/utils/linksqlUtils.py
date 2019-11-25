"""link my_sql"""

import pymysql

from ._errors import UtilsException

from ..core.config import MYSqlHost
from ..core.config import MYSqlUser
from ..core.config import MYSqlPassword
from ..core.config import MYSqlPort


class PySqlLinkException(UtilsException):
    """pymysql连接数据库错误"""



# 连接数据库
def link_mysql(database):
    """连接数据库

    TASK:
        连接mysql
    NOTE:
        host为数据库的主机IP地址，
        port为MySQL的默认端口号，
        user为数据的用户名，
        password为数据库的登录密码，
        db为数据库的名称。
    INPUT:
        database:str:数据库名
    OUTPUT:
        con : 

    """
    try:
        con = pymysql.connect(host=MYSqlHost,
                            user=MYSqlUser,
                            password=MYSqlPassword,
                            database=database, 
                            charset='utf8', 
                            port=MYSqlPort,
                            use_unicode=True) # , charset='latin1'
    except pymysql.err.InternalError as e:
        # 不对此异常重命名，直接抛出
        raise e
    except Exception:
        raise PySqlLinkException("数据库连接异常！")
    
    return con


# 连接数据库，如果数据库不存在，则创建数据库
def link_mysql_ifnotexit_creat(database):
    """连接数据库，如果数据库不存在，则创建数据库"""
    try:
        con = link_mysql(database=database) # 会抛出 nameerror 和 pysqllinkexception两种异常
    except pymysql.err.InternalError as e:

        # 创建数据库
        conBase = link_mysql(database=None)
        curBase = conBase.cursor()
        querySql = "Create Database If Not Exists `{database}` Character Set UTF8".format(
            database=database
        )
        curBase.execute(query=querySql)
        con = link_mysql(database=database)
        curBase.close()
        conBase.close()
    except Exception as otherE:
        raise otherE

    return con 


#----------------------------------------------------------------------------------


# 创建引擎 -- pandas to_sql 有时候写不进去，需要用engine
# 语法 ：mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
from sqlalchemy import create_engine


# 创建mysql engine
def create_engine_mysql(database):
    """创建mysql engine"""

    host = "{MYSqlHost}:{MYSqlPort}".format(
        MYSqlHost=MYSqlHost,
        MYSqlPort=MYSqlPort
    )

    engine = create_engine(
        "mysql+pymysql://{user}:{password}@{host}/{database}".format(
            user=MYSqlUser,
            password=MYSqlPassword,
            host=host,
            database=database
        ), 
        encoding="utf-8", # 'latin1'
        max_overflow=5, 
        echo=False
    ) # echo=True =>把所有的信息都打印出来
    return engine






