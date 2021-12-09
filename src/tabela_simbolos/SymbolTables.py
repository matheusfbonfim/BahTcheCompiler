# ====================
# TABELA DE SIMBOLOS - VARIAVEIS   
class SymbolTable:
    def __init__(self):
        self.__table = {}

    def add(self, escopo, var_name, symbol_dict):
        self.__table[escopo][var_name] = symbol_dict
    
    # ============================================
    # VERIFICA SE A VARIAVEL JA EXISTE NO ESCOPO
    def exists(self, escopo, symbolName):
        return symbolName in self.__table[escopo]
    
    def setKeyDict(self, name):
        self.__table[name] = {}

    def get(self, symbolName):
        return self.__table[symbolName]

    def getTable(self):
        return self.__table

# ====================
# TABELA DE SIMBOLOS FUNCAO
class FunctionSymbolTable:
    def __init__(self):
        self.__table = {}

    def add(self, name_function, info):
        self.__table[name_function] = info
    
    def exists(self, name_function):
        return name_function in self.__table
    
    def get(self, symbolName):
        return self.__table[symbolName]

    def getTable(self):
        return self.__table