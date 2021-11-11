from Token import Token  # Importando classe de tokens


class Parser:
    def __init__(self, tokens):
        self._table_tokens = tokens     # Lista com todos os tokens [('BAHTCHE', 'TK_MAIN', 1, 1), ...]
        self._error = 'no error'        # Flag de erro
        self._count = 0                 # Indica qual o token da lista está sendo lido
        self._token = self._proximo_tk()  # Variavel que indica o token atual que está sendo lido


    def _mensagem(self, expected_symbol = None, current_symbol = None, line = None, column = None):
        return f'\t"{current_symbol}" is not "{expected_symbol}" | line: {line} | column: {column}'


    def _terminal(self, token = None, description = None):
        current_token = self._token     # ('BAHTCHE', 'TK_MAIN', 1, 1)

        if current_token == 'finish':
            pass
        
        # Verificando se o token atual não corresponde ao token lido
        if not (current_token[1] in token):   
            raise Exception(self._mensagem(description, current_token[0], current_token[2], current_token[3]))
        

        

    def _main(self):
        self._terminal([Token.TK_MAIN], 'BAHTCHE')

    def _code(self):
        # self._funcao()
        self._main()
        #self._openKey()
        #self._content()
        #self._closeKey()


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
