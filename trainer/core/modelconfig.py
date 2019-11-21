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
                outDict[attrStr] = attr

        return outDict