class supplierViewMode:
    def __init__(self):
        self.__id=-1
        self.__sales=None
        self.__salesPhone=None
        self.__enginner=None
        self.__enginnerPhone=None
        self.__supplierName=None
        self.__sysType=None
        self.__address=None
        self.__supplierManager=None
        self.__Supplier_phone=None
        self.__zipCode=None

    @property
    def Id(self):
        return self.__id

    @property
    def Sales(self):
       return self.__sales
    @Sales.setter
    def Sales(self,sales):
        self.__sales=sales

    @property
    def SalesPhone(self):
        return self.__salesPhone
    @SalesPhone.setter
    def salesPhone(self,phone):
        self.__salesPhone=phone
