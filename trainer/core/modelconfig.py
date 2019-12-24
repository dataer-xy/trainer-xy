class ModelConfigBase(object):
    """
    配置类的基类

    """
    def to_dict(self):
        """类属性转化为字典"""
        outDict = {}
        attrList = dir(self)
        for attrStr in attrList:
            attr = getattr(self, attrStr)
            if not attrStr.endswith("__") and not callable(attr):
                if isinstance(attr,list): # NOTE: sql 无法存储的数据
                    attr = str(attr)
                outDict[attrStr] = attr

        return outDict




def __test1():
    import os  
    high = 100
    wide = "str"
    channel = os.path.abspath(os.path.dirname(__file__))
    
    class ModelConfig(ModelConfigBase):
            
        def __init__(self):  

            #---------------------------------------------------  
            # 网络配置

            self.high = high # OK

            self.wide = wide # OK

            self.channel = channel # OK

            self.a = self.high * 100


    modelConfig = ModelConfig()

    modelConfigDict = modelConfig.to_dict()

    print(modelConfigDict)

    print("end")


def __main():
    __test1()

if __name__ == "__main__":
    __main()