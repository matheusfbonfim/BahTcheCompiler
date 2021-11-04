import sys
from .Automato import Automaton

"""
CLASS SCANNER
    # Classe com função de fazer a leitura do programa fonte, caractere a caractere, 
      agrupar os caracteres em lexemas e produzir uma sequência de símbolos léxicos conhecidos como tokens.
    # Atributos
         - AF: Variavel do tipo da classe Automato - Automato AF
         - text: Lista com as linhas vindo da leitura do arquivo
         - cadeias: Cadeias formadas com a varredura pelo automato  (Ex: ['BAHTCHE',...])
         - tokens: Respectivos tokens formados em conjunto com as cadeias (Ex: ['TK_MAIN', ...])
         - file_token: Lista com as strings para escrever no arquivo (Ex: ["1:BAHTCHE:TK_MAIN\n", ...])
         - table_tokens: Lista com tuplas, tendo cada (cadeia, token, linha e coluna) 
         - erro_lexico: Lista para armazenar possivel erro lexico
         - comment_mult_lines: Flag para indicar que a varredura está em comentarios de multiplas linhas
         - text_string: Flag para indicar que a varredura está em uma string
    # Classe apresenta métodos getters e setters para manipulações dos atributos descritos
"""


class Scanner:
    def __init__(self, automato: Automaton):
        self._AF = automato     # Automato - Valida palavras
        self._text = []         # Lista - Linhas do arquivo

        self._cadeias = []      # Cadeias (Identificando no codigo)
        self._tokens = []       # Tokens

        self._file_token = []   # Cadeias com os respectivos tokens para escrever no arquivo
        self._table_tokens = [] # Tabela de tokens com o respectivo linha e coluna do token (cadeia, token, lin, col)

        self._erro_lexico = []              # Lista - Erro Lexico
        self._comment_mult_lines = False    # Flag para comentario de multiplas linhas
        self._text_string = False           # Flag para string " bahtche "

    # ====================
    # GETTERS
    def getfileToken(self):
        return self._file_token

    def getCadeias(self):
        return self._cadeias

    def getTokens(self):
        return self._tokens

    def getTableTokens(self):
        return self._table_tokens

    # ====================
    # LENDO E VALIDANDO O ARQUIVO
    def read_file(self):
        # Usuario insere nome do arquivo fonte
        file_name = input("Digite o nome do arquivo (sem extensao): ")
        file_name = f"{sys.path[0]}/{file_name}.bt"

        # O bloco with - Forma flexível de manipular arquivos (abertura e fechamento automático)
        try:
            with open(file_name, 'r') as file:
                text_lines = file.readlines()  # ['BAHTCHE\n', 'BAhTCHE']
                return [True, text_lines]  # Retorna caso valide a leitura
        except:
            return [False, file_name]

    # ====================
    # ANÁLISE LEXICA
    def analise_lexica(self):

        # Criando arquivo para os erros
        path_file_error = f"{sys.path[0]}/output_errors.txt"   # Diretorio para os arquivos de erros
        output_errors = open(path_file_error, 'w')
        string_erro = ''  # Variavel para armazenar os erros a ser gravado em arquivo

        # Lendo e validando o arquivo
        valid_file, valid_text = self.read_file()  # Ex: True, ['BAHTCHE\n', 'BAhTCHE']

        # -----------------------
        # Verifica o arquivo
        if valid_file:
            self._text = valid_text  # Ex: ['BAHTCHE\n', 'BAhTCHE']

            # Criando registro (arquivo) para os tokens
            path_file_tokens = f"{sys.path[0]}/output_tokens.txt"
            output_tokens = open(path_file_tokens, 'w')

            num_linha = 1  # Numero da linha atual do arquivo

            # --------------------------------------------------
            # ---- Varrendo cada linha do arquivo - Scanner ----
            # --------------------------------------------------
            for linha_text in self._text:
                # Atribui os tokens e cadeias, e retorna o primeiro erro lexico (lista) se existir
                erros_lexicos = self.scanner(linha_text, num_linha)

                # Armazenando os erros lexicos - lista
                if len(erros_lexicos) > 0:      # Ex: ["\t Referência indefinida .."]
                    # Insere na casa 0 do vetor de erros
                    erros_lexicos.insert(0, f"[Erro Léxico] | Linha {num_linha} | ->")
                    self._erro_lexico = erros_lexicos  # Atribuindo para variavel de erro da classe
                    break  # Sai do for após encontrar o primeiro erro

                # Incrementa a contagem de linhas
                num_linha += 1

            # ----------------------------------------------------------
            # ---- Procedimento após a formação de possíveis tokens ----
            # ----------------------------------------------------------

            # -----------------------
            # Escrevendo os tokens em arquivo
            string_tokens = ''  # Variavel para armazenar os erros a ser gravado em arquivo
            for token in self._file_token:
                string_tokens = string_tokens + token  # Juntar todos elementos da lista como string

            output_tokens.write(string_tokens)  # Gravando no arquivo

            # -----------------------
            # Caso tenha erro lexicos
            if len(self._erro_lexico) > 0:
                print("Análise Lexica: [Gerando Erro]\n", end='')

                # Percorrendo os erros presentes na lista
                #   Ex: self._erro_lexico -> ['[Erro Léxico] | Linha 1 | ->', '\t Referência ..']
                first_error = f"\t{self._erro_lexico[0]}{self._erro_lexico[1]}"
                print(first_error, end='')  # Printando o primeiro erro de cada linha
                string_erro = string_erro + first_error  # Gerando string para gravar no arquivo

                # Gravando no arquivo
                output_errors.write(string_erro)

                return False  # Retorna - Analise lexica falhou

            # Erro - Comentario multiplas linhas não terminado
            elif self._comment_mult_lines == True:
                print("Análise Lexica: [Gerando Erro]\n", end='')
                string_erro = "\t[Erro Léxico] Mas BAH.. Tu abriu comentarios de multiplas linhas mas nao finalizou\n"
                print(string_erro, end='')
                # Gravando no arquivo
                output_errors.write(string_erro)

                return False    # Retorna - Analise lexica falhou
            else:
                print("Análise Lexica: [Concluido]")
                return True     # Retorna - Analise lexica sucesso

            # Fechando os arquivos
            output_tokens.close()
            output_errors.close()

        else:
            print(f"!! ERRO - O arquivo \"{valid_text}\" não foi encontrado")
            output_errors.write(f"!! ERRO - O arquivo \"{valid_text}\" não foi encontrado")
            output_errors.close()
            return False    # Retorna - Analise lexica falhou

    # ====================
    # SCANNER
    #   Atribui os tokens e cadeias, e retorna os erros lexicos se existir
    def scanner(self, entrada_text, num_linha):
        # Pré-Processamento de dados
        entrada_text = entrada_text.replace('\n', ' ')
        entrada_text = entrada_text.replace('\t', ' ')

        # Estado inicial q0
        estado_atual_transitions = self._AF.get_transitions_state(0)  # Retorna dicionario de transições do estado q0
        estado_atual = 0  # Variavel - State number

        position = 0  # Posicao na cadeia de caracteres
        cadeia = ''  # String para cadeia
        erros_lexicos = []  # Lista com strings de erros por linha

        # Varrendo a linha da entrada
        while position < len(entrada_text):

            caractere = entrada_text[position]  # Caractere (Transicao do AF)

            # Caso seja um string - ignora o elementos dentro da string
            if caractere == '"':
                self._text_string = not self._text_string

            # ------------------------------------------------------
            # ---- Verificando os casos de comentarios primeiro ----
            # ------------------------------------------------------

            # Verifica caracter de comentario de multiplas linhas (Não estando no meio de string)
            if caractere == "#" and not self._text_string:
                # Valida se o estado atual é final (Manteve no estado anterior)
                if self._AF.automato[estado_atual].is_end:
                    token = self._AF.automato[estado_atual].token  # Captura o atributo token do estado

                    self._tokens.append(token)      # Adiciona na lista[i] o token
                    self._cadeias.append(cadeia)    # Adiciona na lista[i] a cadeia
                    string_cadeia_token = f"{num_linha}:{cadeia}:{token}\n"  # String para armazenar como cadeia e token
                    self._file_token.append(string_cadeia_token)    # Adiciona na lista para o arquivo

                    # print(string_cadeia_token, end='')

                    # Adiciona na tabela
                    self._table_tokens.append((cadeia, token, num_linha, position - len(cadeia) + 1))

                    # Reinicia o AF
                    estado_atual_transitions = self._AF.get_transitions_state(0)
                    estado_atual = 0

                else:
                    # FAZER TRATAMENTO CASO NAO SEJA ' '
                    if cadeia != ' ' and len(cadeia) > 0:
                        mensagem_erro_sugestao = self._AF.automato[estado_atual].mensagemDeErro
                        erro = f"\t Referência indefinida para {cadeia} | Coluna: {position} | {mensagem_erro_sugestao}\n"
                        erros_lexicos.append(erro)
                        return erros_lexicos

                    # Reinicia o AF
                    estado_atual_transitions = self._AF.get_transitions_state(0)
                    estado_atual = 0

                # Reseta cadeia
                cadeia = ''

                # Invertendo o valor de comentarios varias linhas
                self._comment_mult_lines = not self._comment_mult_lines  # Ex: True
                position += 1

                continue    # Proximo passo do while (Proximo caractere)

            # Caso o comentario de multiplas linhas esteja ativo
            #   "Ignora" os caracteres se tiver ativo
            if self._comment_mult_lines:
                position += 1
                continue  # Retorna para o proximo passo do while

            # Se ler caractere $, sai do while e vai para proxima linha (Não estando no meio de string)
            if caractere == '$' and not self._text_string:
                break

            # ---------------------------------------------------------
            # ---- Percorrendo o automato para verificar a palavra ----
            # ---------------------------------------------------------

            # Verifica atraves das transicoes do estado atual se existe caminho para o caractere
            #   estado_atual_transitions -> ex: {'B': 1, 'G': 27}
            if caractere in estado_atual_transitions:
                estado_atual = estado_atual_transitions[caractere]  # Ex: 1
                estado_atual_transitions = self._AF.get_transitions_state(estado_atual)  # Ex: {'A': 2, 'E': 19}

                cadeia = cadeia + entrada_text[position]  # Concatenando a palavra - Cadeia
                position += 1
            # Caso não esteja na transição, verifica por exemplo se o proximo é espaço ou outro caractere
            else:
                # Valida se o estado atual é final (Manteve no estado anterior)
                if self._AF.automato[estado_atual].is_end:
                    # Tratando um caso especifico, ex: GURIa
                    if (cadeia in ['GURI', 'GURIZAO', 'FANDANGO']) and (caractere != ' '):
                        erro = f"\t Mas BAH.. Acho que quis dizer '{cadeia}' né? | Coluna: {position + 1}\n"
                        erros_lexicos.append(erro)
                        return erros_lexicos

                    token = self._AF.automato[estado_atual].token  # Captura o atributo token do estado

                    self._tokens.append(token)      # Adiciona na lista[i] o token
                    self._cadeias.append(cadeia)    # Adiciona na lista[i] a cadeia
                    string_cadeia_token = f"{num_linha}:{cadeia}:{token}\n"  # String para armazenar como cadeia e token
                    self._file_token.append(string_cadeia_token)  # "tabela"

                    # print(string_cadeia_token, end='')

                    self._table_tokens.append((cadeia, token, num_linha, position - len(cadeia) + 1))

                    # Reinicia o AF
                    estado_atual_transitions = self._AF.get_transitions_state(0)
                    estado_atual = 0
                # Caso não seja estado final (Ex: Ignorar os espaços)
                else:
                    # Cria uma cadeia com espaco ou caractere incorreto
                    cadeia = cadeia + entrada_text[position]
                    position += 1

                    # FAZER TRATAMENTO CASO NAO SEJA ' '
                    if cadeia != ' ':
                        mensagem_erro_sugestao = self._AF.automato[estado_atual].mensagemDeErro
                        erro = f"\t Referência indefinida para {cadeia} | Coluna: {position} | {mensagem_erro_sugestao}\n"
                        erros_lexicos.append(erro)
                        return erros_lexicos

                    # Reinicia o AF
                    estado_atual_transitions = self._AF.get_transitions_state(0)
                    estado_atual = 0

                cadeia = ''  # Reset da cadeia

        # Valida se o estado atual (depois de ler toda palavra) é final -> Caso nao tenha espaço
        if self._AF.automato[estado_atual].is_end:
            token = self._AF.automato[estado_atual].token  # Captura o atributo token do estado

            self._tokens.append(token)      # Adiciona na lista[i] o token
            self._cadeias.append(cadeia)    # Adiciona na lista[i] a cadeia
            string_cadeia_token = f"{num_linha}:{cadeia}:{token}\n"  # String para armazenar como cadeia e token
            self._file_token.append(string_cadeia_token)

            # print(string_cadeia_token, end='')
            self._table_tokens.append((cadeia, token, num_linha, position - len(cadeia) + 1))

        elif cadeia != ' ' and len(cadeia) > 0:  # Ex: GUR$dsadasdas
            # FAZER TRATAMENTO CASO NAO SEJA ' '
            mensagem_erro_sugestao = self._AF.automato[estado_atual].mensagemDeErro  # Mensagem de erro (estado atual)
            erro = f"\t Referência indefinida para {cadeia} | Coluna: {position} | {mensagem_erro_sugestao}\n"
            erros_lexicos.append(erro)

            return erros_lexicos

        return erros_lexicos
