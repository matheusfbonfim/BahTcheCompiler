from Token import Token  # Importando classe de tokens


class Parser:
    def __init__(self, tokens):
        self._table_tokens = tokens     # Lista com todos os tokens [('BAHTCHE', 'TK_MAIN', 1, 1), ...]
        self._error = 'no error'        # Flag de erro
        self._count = 0                 # Indica qual o token da lista está sendo lido
        self._token = self._proximo_tk()  # Variavel que indica o token atual que está sendo lido
        
        self._tipos = [
            Token.TK_INT,
            Token.TK_STRING,
            Token.TK_FLOAT
        ]


    def _mensagem(self, expected_symbol = None, current_symbol = None, line = None, column = None):
        if self._error == 'finish':
            return f'\033[1;31m \t Mas BAH, acho que faltou um pedaco do codigo'
        elif self._error == 'error_ok_op':
            return f'\033[1;31m \t Mas BAH, acho que faltou um "{expected_symbol}" antes do "{current_symbol}" | line: {line} | column: {column}'
        elif self._error == 'no return':
            return f'\033[1;31m \t Mas BAH, funcao com retorno incorreto ou sem retorno | line: {line} | column: {column}'
        elif self._error == 'retorno_vazio':
            return f'\033[1;31m \t Mas BAH, isso "{current_symbol}" nao eh um tipo de retorno | line: {line} column: {column}'
        elif self._error == 'ponto_virgula':
            return f'\033[1;31m \t Mas BAH, esperado "{expected_symbol}" antes do "{current_symbol}" | line: {line} column: {column}'
        else:
            return f'\033[1;31m \t Mas BAH, esse o simbolo "{current_symbol}" nao eh "{expected_symbol}" | line: {line} | column: {column}'
            


    def _terminal(self, token = None, description = None):
        # Token atual lido
        current_token = self._token     # ('BAHTCHE', 'TK_MAIN', 1, 1)

        if current_token == 'finish':
            self._error = 'finish'
            raise Exception(self._mensagem())
        
        if self._error != 'no error':
            raise Exception(self._mensagem(description, current_token[0], current_token[2], current_token[3]))

        # Lanca erro - Verificando se o token atual não corresponde ao token lido
        if not (current_token[1] in token): 
            raise Exception(self._mensagem(description, current_token[0], current_token[2], current_token[3]))
        
        
        # Caso não haja erro de terminal
        print(f"Descrição: {description}, Current_Token: {current_token[0]}")
        self._token = self._proximo_tk()    # Proximo do token


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

    def _ponto_virgula(self):
        if self._token[1] != Token.TK_END:
            self._error = 'ponto_virgula'
        self._terminal([Token.TK_END], ';')


    def _retorno_f(self):
        self._retorno()
        self._tipos_retorno()
        self._ponto_virgula()

    def _id_funcao(self):
        self._terminal([Token.TK_FUNC], 'BARBARIDADE')
    
    def _tipo(self):
        self._terminal(self._tipos, 'GURI ou GURIZAO ou FANDANGO')

    def _identificador(self):
        self._terminal([Token.TK_IDENT], 'IDENTIFICADOR')

    def _open_p(self):
        # Token corrente é diferente de TK_OP
        if self._token[1] != Token.TK_OP:
            self._error = 'error_ok_op'
        self._terminal([Token.TK_OP], '(')
    
    def _parametros(self):
        pass

    def _close_p(self):
        # Token corrente é diferente de TK_CP
        if self._token[1] != Token.TK_CP:
            self._error = 'error_ok_op'
        self._terminal([Token.TK_CP], ')')

    
    def _content(self):
        pass
        

    def _funcao(self):
        # ('BARBARIDADE', 'TK_FUNC', 1, 1)
        if self._token[1] != Token.TK_MAIN:
            self._id_funcao()
            self._tipo()
            self._identificador()
            self._open_p()
            #self._parametros()
            self._close_p()
            self._openKey()
            #self._content()
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
        self._terminal([Token.TK_MAIN], 'BAHTCHE')

    def _code(self):
        self._funcao()
        self._main()
        self._openKey()
        #self._content()
        self._closeKey()

    def analise_sintatica(self):
        # Tente começar a analise, mas caso haja erro, lance uma exceção
        try:
            self._code()
            print("Análise Sintatica: [Concluido]")
            return True  # Retorna - Analise sintatica sucesso
        except Exception as error:
            print("Análise Sintatica: [Gerando Erro]\n", end='')
            print(error)
            return False

    # Atribui a self._token o proximo token
    def _proximo_tk(self):
        temp = 'finish'  # De inicio é atribuido temp como 'finish'

        # Caso o count ainda seja menor que a lista de tokens, redefine temp
        if self._count < len(self._table_tokens):
            temp = self._table_tokens[self._count]
            self._count += 1  # O count ja fica posicionado para o proximo token
        return temp


