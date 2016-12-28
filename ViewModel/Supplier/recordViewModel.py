#encoding:utf-8
class Record(object):
    def __init__(self):
        self.__supportUser=None
        self.__supportContent=None
        self.__suportType=None
        self.__suportTime=None

    @property
    def SupportUser(self):
        return self.__supportUser
    @SupportUser.setter
    def SupportUser(self,value):
        self.__supportUser=value
    @SupportUser.deleter
    def SupportUser(self):
        del self.__supportUser

    @property
    def SupportContent(self):
        return self.__supportContent
    @SupportContent.setter
    def SupportContent(self,value):
        self.__supportContent=value
    @SupportContent.deleter
    def SupportContent(self):
        del self.__supportContent

    @property
    def SuportType(self):
        return self.__suportType
    @SuportType.setter
    def SuportType(self,value):
        self.__suportType=value
    @SuportType.deleter
    def SuportType(self):
        del self.__suportType

    @property
    def SuportTime(self):
        return self.__suportTime
    @SuportTime.setter
    def SuportTime(self,value):
        self.__suportTime=value
    @SuportTime.deleter
    def SuportTime(self):
        del self.__suportTime

