from os import name
from Token import Token
import sys

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
        if symbolName in self.__table[escopo]:
            # Caso esteja tentanto utilizar, marcar variavel como usada
            self.setVariableUsed(escopo, symbolName)

        return symbolName in self.__table[escopo]
    
    # ============================================
    # SETA VALOR INICIAL PARA VARIAVEL
    def setKeyDict(self, name):
        self.__table[name] = {}
    
    # ============================================
    # RETORNA O TIPO DA VARIAVEL
    def returnsTypeVariable(self, escopo, identificador):
        return self.__table[escopo][identificador].getType()

    # ============================================
    # COMPARA O TIPO DA FUNCAO COM SEU RETORNO  
    def typeComparison(self, tipo_func, tipo_var):
        # Verifica se o token é GURIZAO
        if (tipo_func == Token.TK_FLOAT) and (tipo_var == Token.TK_REAL):
            return True
        # Verifica se o token é GURI
        elif (tipo_func == Token.TK_INT) and (tipo_var == Token.TK_NUMBER):
            return True
        # Verifica se o token é FANDANGO
        elif (tipo_func == Token.TK_STRING) and (tipo_var == Token.TK_TEXT):
            return True
        # Verifica se o identificador é do mesmo tipo - String
        elif (tipo_func == Token.TK_STRING) and (tipo_var == Token.TK_STRING):
            return True
        # Verifica se o identificador é do mesmo tipo - Int
        elif (tipo_func == Token.TK_INT) and (tipo_var == Token.TK_INT):
            return True
        # Verifica se o identificador é do mesmo tipo - float
        elif (tipo_func == Token.TK_FLOAT) and (tipo_var == Token.TK_FLOAT):
            return True
        else:
            return False 

    # ============================================
    # DEFINI UMA VARIAVEL ESP. COMO USADA 
    def setVariableUsed(self, escopo, name_var):
        self.__table[escopo][name_var].setUsed(True)


    # ============================================
    # VERIFICA SE EXISTE ALGUMA VARIAVEL NAO UTILIZADA
    def checkUsedVariables(self):
        dicionario = self.getTable()
        variable_not_used = []
        
        for i in dicionario.values():
            for j in i.values():
                if j.getUsed() == False:
                    variable_not_used.append(j.getName())

        # Caso tenha variaveis nao utilizadas, notifica o Warning
        if len(variable_not_used) != 0:
            # Criando arquivo para os warnings
            path_file_warning = f"{sys.path[0]}/output_warning.txt"   # Diretorio para os arquivos de erros
            output_warnings = open(path_file_warning, 'w')

            # Gravando no arquivo de warning
            for atribute in variable_not_used:
                output_warnings.write(f'\t [Warning] - variavel {atribute} declarada mas nao utilizada\n')
                print(f'\t [Warning] - variavel {atribute} declarada mas não utilizada')

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
    
    # ============================================
    # COMPARA O TIPO DA FUNCAO COM SEU RETORNO  
    def checkNumberParameters(self, escopo, quant):
        return self.__table[escopo][1] == quant

    def get(self, symbolName):
        return self.__table[symbolName]

    def getTable(self):
        return self.__table