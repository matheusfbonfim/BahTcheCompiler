import sys
from Token import Token  # Importando classe de tokens
from tabela_simbolos.SymbolTables import SymbolTable, FunctionSymbolTable
from tabela_simbolos.Variable import Variable

class Semantic:
    def __init__(self, tokens):
        # ====================
        # TABELA DE SIMBOLOS - VARIAVEIS
        self.__tipo = None                      # Tipo da variavel a ser armazenada
        self.__varName = None                   # Nome da variavel a ser armazenada
        self.__varValue = None                  # Valor da variavel a ser armazenada
        self.__symbolTable = SymbolTable()
        self.__symbol = None
        
        # ====================
        # TABELA DE SIMBOLOS - FUNÇÃO
        self.__escopo = None
        self.__retorno_func = None
        self.__num_parametros = 0
        self.__functionSymbolTable = FunctionSymbolTable()
        
        # ======================================       
        self._table_tokens = tokens       # Lista com todos os tokens [('BAHTCHE', 'TK_MAIN', 1, 1), ...]
        self._tree = None                 # Armazena Node raiz da arvore armazenada
        self._error = 'no error'          # Flag de erro
        self._count = 0                   # Indica qual o token da lista está sendo lido
        self._token = self._proximo_tk()  # Variavel que indica o token atual que está sendo lido

        self._tipos = [
            Token.TK_INT,
            Token.TK_STRING,
            Token.TK_FLOAT
        ]

        self._operadores_matematicos = [
            Token.TK_MATH_ADD,
            Token.TK_MATH_SUB,
            Token.TK_MATH_MUL,
            Token.TK_MATH_DIV
        ]

        self._operadores_logicos = [
            Token.TK_LOGIC_AND, # &&
            Token.TK_LOGIC_OR,  # ||
            Token.TK_LOGIC_DIF, # !=
            Token.TK_LOGIC_LG,  # <,>
            Token.TK_LOGIC_LE_GE, # <=, >=
            Token.TK_LOGIC_EQ     # ==
        ]

        self._conjunto_operandos = [
            Token.TK_IDENT,
            Token.TK_NUMBER,
            Token.TK_REAL
        ]

        self._conjunto_tokens_content = [
            Token.TK_IDENT,
            Token.TK_WHILE,
            Token.TK_IF,
            Token.TK_SCANF,
            Token.TK_PRINT,
            Token.TK_CK,
            Token.TK_RETURN
        ] + self._tipos

    # ====================
    # DEFINE A MENSAGEM DE ERRO
    def _mensagem(self, expected_symbol=None, current_symbol=None, line=None, column=None):
        if self._error == 'already_declared_variable':
            return f'\t [Erro Semantico] | Mas BAH, variavel {self.__varName} ja foi declarada | line: {line} column: {column}'
        
    # ====================
    # VERIFICA A CORRESPONDENCIA DO TOKEN LIDO COM O ESPERADO   
    def _terminal(self, token=None, description=None):
        # Token atual lido
        current_token = self._token     # ('BAHTCHE', 'TK_MAIN', 1, 1)

        # Caso terminou de ler a lista de tokens, mas a gramatica não finalizou
        if current_token == 'finish':
            self._error = 'finish'
            raise Exception(self._mensagem())

        # Caso tenha sido lancado na flag self._error algum erro
        if self._error != 'no error':
            raise Exception(self._mensagem(description, current_token[0], current_token[2], current_token[3]))

        # Lanca erro - Verificando se o token atual não corresponde ao token lido
        if not (current_token[1] in token):
            raise Exception(self._mensagem(description, current_token[0], current_token[2], current_token[3]))

        # Caso não haja erro de terminal - Proximo token
        self._token = self._proximo_tk()

    #####################################################
    ############### REGRAS SINTATICAS ###################
    #####################################################

    def _if(self):
        self._terminal([Token.TK_IF], 'TRIF')

    def _elif(self):
        self._terminal([Token.TK_ELIF], 'BEM_CAPAZ')

    def _else(self):
        self._terminal([Token.TK_ELSE], 'BAGUAL')

    def _declara_elif(self):
        if self._token[1] == Token.TK_ELIF:
            
            self._elif()
            self._open_p()

            if self._token[1] != Token.TK_CP:
                self._op_logic()
            else:
                self._error = 'expressao_vazia'
                self._terminal()

            self._close_p()
            self._openKey()
            self._content()
            self._closeKey()
            self._declara_elif()

    def _declara_else(self):
        if self._token[1] == Token.TK_ELSE:
        
            self._else()
            self._openKey()
            self._content()
            self._closeKey()

    def _condicional(self):
        self._if()
        self._open_p()

        if self._token[1] != Token.TK_CP:
            self._op_logic()
        else:
            self._error = 'expressao_vazia'
            self._terminal()

        self._close_p()
        self._openKey()
        self._content()
        self._closeKey()
        self._declara_elif()
        self._declara_else()

    def _term(self):

        if self._token[1] == Token.TK_IDENT:
            self._identificador()
        elif self._token[1] == Token.TK_NUMBER:
            self._number()
        elif self._token[1] == Token.TK_REAL:
            self._real()
        else:
            self._error = 'operacao_matematica_invalida'
            self._terminal()

    def _mul_div_add_sub(self):
        if self._token[1] == Token.TK_MATH_MUL:
            self._terminal([Token.TK_MATH_MUL], '*')
        elif self._token[1] == Token.TK_MATH_DIV:
            self._terminal([Token.TK_MATH_DIV], '/')
        elif self._token[1] == Token.TK_MATH_ADD:
            self._terminal([Token.TK_MATH_ADD], '+')
        elif self._token[1] == Token.TK_MATH_SUB:
            self._terminal([Token.TK_MATH_SUB], '-')
        else:
            self._error = 'operacao_matematica_invalida'
            self._terminal()

    def _multiplication_seg(self):
        if self._token[1] in [Token.TK_MATH_MUL, Token.TK_MATH_DIV]:
            self._mul_div_add_sub()
            self._term()
            self._multiplication_seg()

    def _multiplication(self):
        self._term()
        self._multiplication_seg()

    def _add_sub_seg(self):
        if self._token[1] in [Token.TK_MATH_ADD, Token.TK_MATH_SUB]:
            self._mul_div_add_sub()
            self._multiplication()
            self._add_sub_seg()

    def _op_math(self):
        self._multiplication()
        self._add_sub_seg()

    def _chamada_seg(self):
        if self._token[1] == Token.TK_COMMA:
            self._virgula()
            self._identificador()
            self._chamada_seg()
        elif self._token[1] in [Token.TK_IDENT]:
            self._error = 'pontuacao'
            self._terminal(token=[Token.TK_COMMA], description=',')

    def _parametros_chamada_f(self):
        self._identificador()
        self._chamada_seg()

    def _chama_funcao(self):
        self._id_funcao()
        self._identificador()
        self._open_p()
        if self._token[1] != Token.TK_CP:
            self._parametros_chamada_f()
        self._close_p()

    def _atribuicao(self):
        self._terminal([Token.TK_ASSIGNMENT], '=')

    def _not(self):
        self._terminal([Token.TK_LOGIC_NOT], '!')

    def _operador_l(self):  # OR, AND, DIF, LG, LE_GE, EQ
        if self._token[1] == Token.TK_LOGIC_OR:
            self._terminal([Token.TK_LOGIC_OR], '||')
        elif self._token[1] == Token.TK_LOGIC_AND:
            self._terminal([Token.TK_LOGIC_AND], '&&')
        elif self._token[1] == Token.TK_LOGIC_DIF:
            self._terminal([Token.TK_LOGIC_DIF], '!=')
        elif self._token[1] == Token.TK_LOGIC_LG:
            self._terminal([Token.TK_LOGIC_LG], '> ou <')
        elif self._token[1] == Token.TK_LOGIC_LE_GE:
            self._terminal([Token.TK_LOGIC_LE_GE], '<= ou >=')
        elif self._token[1] == Token.TK_LOGIC_EQ:
            self._terminal([Token.TK_LOGIC_EQ], '==')
        else:
            self._error = 'operacao_logica_invalida'
            self._terminal()

    def _op_logic(self):
        if self._token[1] == Token.TK_LOGIC_NOT:
            self._not()

        if self._token[1] == Token.TK_IDENT:
            self._identificador()
        elif self._token[1] == Token.TK_NUMBER:
            self._number()
        elif self._token[1] == Token.TK_REAL:
            self._real()
        else:
            self._error = 'operacao_logica_invalida'
            self._terminal()

        self._operador_l()

        if self._token[1] == Token.TK_LOGIC_NOT:
            self._not()

        if self._token[1] == Token.TK_IDENT:
            self._identificador()
        elif self._token[1] == Token.TK_NUMBER:
            self._number()
        elif self._token[1] == Token.TK_REAL:
            self._real()
        else:
            self._error = 'operacao_logica_invalida'
            self._terminal()

    def _atribui_var(self):  # Exemplo -> a = b + 2  # self._token = b
  
        self._identificador()   # a
        self._atribuicao()      # =

        # Token que auxilia para qual metodo irá - Ve caractere futuro
        token_aux = self._proximo_tk()  # + 
        self._count -= 1                # Decrementa para voltar no token atual

        # Verifica se o caractere é NOT
        if self._token[1] == Token.TK_LOGIC_NOT:
            self._op_logic()
        # Valida se é operacao matematica
        elif token_aux[1] in self._operadores_matematicos:
            self._op_math()
        # Valida se é operacao logica
        elif token_aux[1] in self._operadores_logicos:
            self._op_logic()
        # Valida se é identificador/number/text/ident
        elif token_aux[1] == Token.TK_END:
            if self._token[1] == Token.TK_TEXT:
                self._texto()
            elif self._token[1] == Token.TK_NUMBER:
                self._number()
            elif self._token[1] == Token.TK_REAL:
                self._real()
            elif self._token[1] == Token.TK_IDENT:
                self._identificador()
            else:
                self._error = "atribuicao_invalida"
                self._terminal()
        # Valida se é chamada de funcao
        elif self._token[1] == Token.TK_FUNC:
            self._chama_funcao()
        else:
            self._error = "atribuicao_invalida"
            self._terminal()

        self._ponto_virgula()

    def _declara_var(self):
        self._parametros()
        self._ponto_virgula()

    def _retorno(self):
        # Token corrente é diferente de TK_RETURN
        if self._token[1] != Token.TK_RETURN:
            self._error = 'no return'

        self._terminal([Token.TK_RETURN], 'LARGUEIMAO')

    def _real(self):
        self._terminal([Token.TK_REAL], 'REAL')

    def _number(self):
        self._terminal([Token.TK_NUMBER], 'NUMBER')

    def _texto(self):
        self._terminal([Token.TK_TEXT], 'TEXT')

    def _ponto_virgula(self):
        if self._token[1] != Token.TK_END:
            self._error = 'pontuacao'

        self._terminal([Token.TK_END], ';')

    def _tipos_retorno(self):
        if self._token[1] == Token.TK_IDENT:
            self._identificador()
        elif self._token[1] == Token.TK_REAL:
            self._real()
        elif self._token[1] == Token.TK_NUMBER:
            self._number()
        elif self._token[1] == Token.TK_TEXT:
            self._texto()
        else:
            self._error = 'retorno_vazio'
            self._terminal()

    def _retorno_f(self):
        self._retorno()
        self._tipos_retorno()
        self._ponto_virgula()

    def _id_funcao(self):
        self._terminal([Token.TK_FUNC], 'BARBARIDADE')

    def _tipo(self):
        # Determinando o tipo da variavel
        self.__tipo = self._token[1]

        self._terminal(self._tipos, 'GURI ou GURIZAO ou FANDANGO')

    def _identificador(self):
        # Inicializa caracteristica do identificador
        self.__varName = self._token[0]
        self.__varValue = None
        # Cria um simbolo/variavel
        self.__symbol = Variable(self.__varName, self.__tipo, self.__varValue)
        
        self._terminal([Token.TK_IDENT], 'IDENTIFICADOR')

    def _open_p(self):
        # Token corrente é diferente de TK_OP
        if self._token[1] != Token.TK_OP:
            self._error = 'error_ok_op'

        self._terminal([Token.TK_OP], '(')

    def _declara_par(self):
        self._tipo()
        self._identificador()

        self.__num_parametros += 1

        # Verifica se a variavel ja existe no escopo
        if not self.__symbolTable.exists(self.__escopo, self.__varName):    
            # Adiciona na tabela
            self.__symbolTable.add(self.__escopo, self.__varName, self.__symbol)
        else:
            self._error = 'already_declared_variable'
            self._terminal()


        print(f"Simbolo adicionado: {self.__symbol.toString()}")

    def _virgula(self):
        self._terminal([Token.TK_COMMA], ',')

    def _parametro_seg(self):
        if self._token[1] == Token.TK_COMMA:
            self._virgula()
            self._declara_par()
            self._parametro_seg()
        
    def _parametros(self):
        # Verifica se o proximo caractere não é CP
        if not(self._token[1] == Token.TK_CP):
            self._declara_par()
            self._parametro_seg()

    def _close_p(self):
        # Token corrente é diferente de TK_CP
        if self._token[1] != Token.TK_CP:
            self._error = 'error_ok_op'

        self._terminal([Token.TK_CP], ')')

    def _while(self):
        self._terminal([Token.TK_WHILE], 'EMCIMADOLACO')

    def _laco(self):
        self._while()
        self._open_p()
        if self._token[1] != Token.TK_CP:
            self._op_logic()
        else:
            self._error = 'expressao_vazia'
            self._terminal()

        self._close_p()
        self._openKey()
        self._content()
        self._closeKey()

    def _print(self):
        self._terminal([Token.TK_PRINT], 'PRINTCHE')

    def _declara_print(self):
        self._print()
        self._open_p()

        if self._token[1] == Token.TK_TEXT:
            self._texto()
        elif self._token[1] == Token.TK_IDENT:
            self._identificador()
        else:
            self._error = 'print_invalido'
            self._terminal()

        self._close_p()
        self._ponto_virgula()

    def _scanf(self):
        self._terminal([Token.TK_SCANF], 'INPUTCHE')

    def _declara_scanf(self):
        self._scanf()
        self._open_p()
        self._identificador()
        self._close_p()
        self._ponto_virgula()

    def _content(self):
        # Verifica se existe content no escopo
        if self._token[1] != Token.TK_CK:
            if self._token[1] in self._tipos:
                self._declara_var()
            elif self._token[1] == Token.TK_IDENT:
                self._atribui_var()
            elif self._token[1] == Token.TK_IF:
                self._condicional()
            elif self._token[1] == Token.TK_WHILE:
                self._laco()
            elif self._token[1] == Token.TK_PRINT:
                self._declara_print()
            elif self._token[1] == Token.TK_SCANF:
                self._declara_scanf()
            elif self._token == 'finish':
                self._terminal()
            elif not self._token[1] in self._conjunto_tokens_content:
                self._error = 'estado_invalido'
                self._terminal()

            if not self._token[1] in [Token.TK_CK, Token.TK_RETURN]:
                self._content()

    def _funcao(self):
        # ('BARBARIDADE', 'TK_FUNC', 1, 1)
        if self._token[1] != Token.TK_MAIN:
            self.__num_parametros = 0   # Reseta o numero de parametros

            self._id_funcao()
            
            # Inicializando o tipo da funcao
            self.__retorno_func = self._token[1]

            self._tipo()
            
            # Inicializando o name_function
            self.__escopo = self._token[0]
            # Insere a chave da funcao no dicionario 
            self.__symbolTable.setKeyDict(self.__escopo) 

    
            self._identificador()
            self._open_p()
            self._parametros()

            # {'uberfunction': [retorno_func, num_parametros]}
            self.__functionSymbolTable.add(name_function=self.__escopo, info = [self.__retorno_func, self.__num_parametros])

            self._close_p()
            self._openKey()
            if self._token[1] != Token.TK_RETURN:
                self._content()
            self._retorno_f()
            self._closeKey()

            # Verifica se existem tokens para serem lidos
            if self._token != 'finish':
                self._funcao()

    def _openKey(self):
        # Token corrente é diferente de TK_OK
        if self._token[1] != Token.TK_OK:
            self._error = 'error_ok_op'

        self._terminal([Token.TK_OK], '{')

    def _closeKey(self):
        # Token corrente é diferente de TK_CK
        if self._token[1] != Token.TK_CK:
            self._error = 'error_ok_op'

        self._terminal([Token.TK_CK], '}')

    def _main(self):

        if self._token[1] == Token.TK_MAIN: # verificar se o token atual e o TK_MAIN
            # Inicializando o name_function
            self.__escopo = self._token[0]
            # Insere a chave da funcao no dicionario 
            self.__symbolTable.setKeyDict(self.__escopo)

        self._terminal([Token.TK_MAIN], 'BAHTCHE')

    # ====================
    # MÉTODO PRINCIPAL - INICIO DA RECURSSÃO
    def _code(self):
        self._funcao()
        self._main()
        self._openKey()
        self._content()
        self._closeKey()

    #####################################################
    ############### METODOS DA CLASSE ###################
    #####################################################

    # ====================
    # INICIALIZACAO DA ANALISE SEMANTICA
    def analise_semantico(self):
        # Tente começar a analise, mas caso haja erro, lance uma exceção
        try:
            self._code()        # Inicia-se pelo code (raiz)
            print("Análise Semantica: [Concluido]")
            return True         # Retorna True - Analise sintatica sucesso
        except Exception as error:
            print("Análise Semantica: [Gerando Erro]\n", end='')
            print(error)
            
            # Criando arquivo para os erros
            path_file_error = f"{sys.path[0]}/output_errors.txt"   # Diretorio para os arquivos de erros
            output_errors = open(path_file_error, 'w')
            
            # Gravando no arquivo
            output_errors.write(f'{error}')

            return False        # Retorna False - Analise sintatica falhou

    # ====================
    # ATRIBUI A SELF._TOKEN O PROXIMO TOKEN
    def _proximo_tk(self):
        temp = 'finish'  # De inicio é atribuido temp como 'finish'

        # Caso o count ainda seja menor que a lista de tokens, redefine temp
        if self._count < len(self._table_tokens):
            temp = self._table_tokens[self._count]
            self._count += 1  # O count ja fica posicionado para o proximo token
        return temp

    # ====================
    # GET DA TABELA DE SIMBOLOS
    def getSymbolTable(self):
        return self.__symbolTable

    #####################################################
    ############### METODOS DA ARVORE ###################
    #####################################################
    
    # ====================
    # Retorna a tree
    def tree(self):
        return self._tree

    # ====================
    # Mostra a arvore em profundidade DFS
    @staticmethod
    def dfs_tree(root):
        stack = [root]
        while stack:
            node = stack.pop(0)
            print(f'{node.name}')
            # print(f'Level: {node.level} Name: {node.name}')
            stack = node.children+stack