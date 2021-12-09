from .Symbol import Symbol 

class Variable(Symbol):
    def __init__(self, name, type, value):
        super().__init__(name)
        self.__type = type
        self.__value = value

    def getType(self):
        return self.__type

    def getValue(self):
        return self.__value

    def setType(self, type):
        self.__type = type
    
    def setValue(self, value):
        self.__value = value

    def toString(self):
        return f'Variable: [ name: {self.getName()} | type: {self.__type} | value: {self.__value}]'
