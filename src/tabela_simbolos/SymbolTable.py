from os import name
import sys
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
    # GETTER
    @property
    def table(self):
        return self._table

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
                elif token[1] == Token.TK_MAIN:
                    self._count -= 1
                    token = self._proximo_tk()  
        
                    # ====================
                    # ADICIONANDO VARIAVEIS DA MAIN 
                    main = token
                    self._table[main] = []
                    self._table[main].append(main)

                    token = token = self._proximo_tk()  

                    tipo = None
                    identificador = None
                            
                    # Varrendo para encontrar tipo e identificador
                    while token != 'finish':
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
                                self._table[main].append([tipo, identificador])
                                
                        token = self._proximo_tk()
                else:
                    return 
        # Verificar se é um token BARBARIDADE
        elif token[1] == Token.TK_MAIN:
            self._count -= 1
            token = self._proximo_tk()  
            # ====================
            # ADICIONANDO VARIAVEIS DA MAIN 
            main = token
            self._table[main] = []
            self._table[main].append(main)
            token = token = self._proximo_tk()
            tipo = None
            identificador = None
                    
            # Varrendo para encontrar tipo e identificador
            while token != 'finish':
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
                        self._table[main].append([tipo, identificador])
                        
                token = self._proximo_tk()

    # ====================
    # ARMAZENANDO A TABELA DE SIMBOLOS EM ARQUIVO
    def store_file_symbol_table(self):

        # Criando registro (arquivo) para tree
        path_file_tokens = f"{sys.path[0]}/output_symbol_table.txt"
        output_tokens = open(path_file_tokens, 'w')
        
        # Variavel para armazenar o texto a ser escrito no arquivo
        string_table = ''

        for escopo in self._table:
    
            name_scope = escopo[0]
            type_scope = self._table[escopo][0][0]
            
            if name_scope == 'BAHTCHE': 
                string_table += '*'*8 + ' MAIN ' + '*'*8 + '\n'
                string_table += f'{name_scope}\n'
            else:
                string_table += '*'*7 + ' FUNCTION ' + '*'*7 + '\n'
                string_table += f'{type_scope} {name_scope}\n'
            
            count = 0

            for variaveis in self._table[escopo]:
                if count >= 1:
                    type_ident = variaveis[0][0]
                    name_ident = variaveis[1][0]

                    type_name_text = f'\t\t Tipo: {type_ident} | Nome: {name_ident}'
                    string_table += f'{type_name_text}\n'
                count += 1

            string_table += '\n'+ '-'*40 +'\n'

        # Gravando no arquivo
        output_tokens.write(string_table)
    
    # ====================
    # AVANÇA PARA O PROXIMO TOKEN DA LISTA
    def _proximo_tk(self):
        temp = 'finish'  # De inicio é atribuido temp como 'finish'

        # Caso o count ainda seja menor que a lista de tokens, redefine temp
        if self._count < len(self._tokens):
            temp = self._tokens[self._count]
            self._count += 1  # O count ja fica posicionado para o proximo token
        return temp