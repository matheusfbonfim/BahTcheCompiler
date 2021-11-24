from Token import Token

class Table:
    def __init__(self, tokens):
        self._table = {}          # Tabela de simbolos - Dicionario
        self._tokens = tokens     # Fluxo de tokens
        self._count = 0           # Indica qual o token da lista está sendo lido  
        self._tipos = [           # Lista com os tokens de tipos
            Token.TK_INT,
            Token.TK_STRING,
            Token.TK_FLOAT
        ]
    
    # ====================
    # CRIA A TABELA DE SIMBOLOS
    def create(self):
        token = self._proximo_tk()      # Ex: ('BAHTCHE', 'TK_MAIN', 1, 1)

        # Verificar se é um token BARBARIDADE
        if token[1] == Token.TK_FUNC:
            token = self._proximo_tk()  # Ex: ('GURI', 'TK_INT', 1, 13)
            
            # Verifica se é um token de tipo
            if token[1] in self._tipos:
                
                retorno = token             # Tipo da funcao - Retorno 
                token = self._proximo_tk()  # Ex: ('uberfuncao', 'TK_IDENT', 1, 18)
                escopo = token              # Escopo do token

                # Adicionando info inicial da funcao
                self._table[escopo] = []             # Ex: table: {('uberfuncao', 'TK_IDENT', 1, 18): []}
                self._table[escopo].append(retorno)  # Ex: table: {('uberfuncao', 'TK_IDENT', 1, 18): [('GURI', 'TK_INT', 1, 13),]}

                token = self._proximo_tk()           # Ex: ('(', 'TK_OP', 1, 28)
                
                tipo = None
                identificador = None
                
                # Varrendo para encontrar tipo e identificador
                while not token[1] in [Token.TK_FUNC, Token.TK_MAIN]:
                    # Verifica se terminou os tokens
                    if token == 'finish':
                        break
                
                    if token[1] in self._tipos:
                        tipo = token           # Atribui tipo
                        token = self._proximo_tk() 
                        
                        # Verifica se o token é identificador
                        if token[1] == Token.TK_IDENT:
                            identificador = token # Atribui identificador
                             # Adiciona na tabela
                            self._table[escopo].append([tipo, identificador])
                            
                    token = self._proximo_tk()   
                    
                # Verifica se o proximo é um TK_FUNC -> Recursao da table
                if token[1] == Token.TK_FUNC:
                    self._count -= 1
                    self.create()
                else:
                    return 
        
        self._count -= 1
        token = self._proximo_tk()


    
    # ====================
    # AVANÇA PARA O PROXIMO TOKEN DA LISTA
    def _proximo_tk(self):
        temp = 'finish'  # De inicio é atribuido temp como 'finish'

        # Caso o count ainda seja menor que a lista de tokens, redefine temp
        if self._count < len(self._tokens):
            temp = self._tokens[self._count]
            self._count += 1  # O count ja fica posicionado para o proximo token
        return temp