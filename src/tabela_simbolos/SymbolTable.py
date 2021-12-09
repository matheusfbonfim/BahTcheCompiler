from .Symbol import Symbol 

class SymbolTable:
    def __init__(self):
        self.__table = {}

    def add(self, symbol: Symbol):
        self.__table[symbol.getName()] = symbol
    
    def exists(self, symbolName):
        return symbolName in self.__table
    
    def get(self, symbolName):
        return self.__table[symbolName]

    def getTable(self):
        return self.__table