
class Variable():
    def __init__(self, name, type, value):
        # Informacoes da variavel
        self.__name = name    # Nome da variavel
        self.__type = type    # Tipo da variavel
        self.__value = value  # Valor da variavel
        self.__used = None    # Indica se a variavel ja foi utilizada
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def getType(self):
        return self.__type

    def getValue(self):
        return self.__value

    def getUsed(self):
        return self.used

    def setType(self, type):
        self.__type = type
    
    def setValue(self, value):
        self.__value = value
        
    def setUsed(self, used):
        self.used = used

    def toString(self):
        return f'Variable: [ name: {self.getName()} | type: {self.__type} | value: {self.__value}]'
