#encoding:utf-8
class assetViewModel():
    def __init__(self):
        self.__assetName=None
        self.__assetType=None
        self.__assetTypeCode=None
        self.__local=None
        self.__Factory=None
        self.__UserOrDep=None
        self.__createDate=None
        self.__updateDate=None
    @property
    def AssetName(self):
        return self.__assetName
    @AssetName.setter
    def AssetName(self,value):
        self.__assetName=value
    @AssetName.deleter
    def AssetName(self,value):
        del self.__assetName
    @property
    def assetType(self):
        return self.__assetType
    @assetType.setter
    def assetType(self,value):
        self.__assetType=value
    @assetType.deleter
    def assetType(self):
        del self.__assetType
    @property
    def Local(self):
        return self.__local
    @Local.setter
    def Local(self,value):
        self.__local=value
    @Local.deleter
    def Local(self):
        del self.__local
    @property
    def Factory(self):
        return self.__Factory
    @Factory.setter
    def Factory(self,value):
        self.__Factory=value
    @Factory.deleter
    def Factory(self):
        del self.__Factory
    @property
    def UserOrDep(self):
        return self.__UserOrDep
    @UserOrDep.setter
    def UserOrDep(self,value):
         self.__UserOrDep=value
    @UserOrDep.deleter
    def UserOrDep(self):
        del self.__UserOrDep

