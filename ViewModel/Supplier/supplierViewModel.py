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
    @property
    def Enginner(self):
        return self.__enginner
    @Enginner.setter
    def Enginner(self,value):
        self.__enginner=value

    @property
    def EnginnerPhone(self):
        return self.EnginnerPhone
    @EnginnerPhone.setter
    def EnginnerPhone(self,value):
        self.__enginnerPhone=value

    @property
    def SupplierName(self):
        return self.__supplierName
    @SupplierName.setter
    def SupplierName(self,value):
        self.__supplierName=value

    @property
    def SysType(self):
        return self.__sysType
    @SysType.setter
    def SysType(self,value):
        self.__sysType=value

    @property
    def Address(self):
        return self.__address
    @Address.setter
    def Address(self,value):
        self.__address=value

    @property
    def SupplierManager(self):
        return self.__supplierManager
    @SupplierManager.setter
    def SupplierManager(self,value):
        self.__supplierManager=value

    @property
    def Supplier_phone(self):
        return self.__Supplier_phone
    @Supplier_phone.setter
    def Supplier_phone(self,value):
        self.__Supplier_phone=value

    @property
    def ZipCode(self):
        return self.__zipCode
    @ZipCode.setter
    def ZipCode(self,value):
        self.__zipCode=value