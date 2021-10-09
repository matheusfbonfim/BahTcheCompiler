"""
CLASS STATE
    # Classe para representar um estado da máquina, tendo por atributos:
         - name: indica o nome do estado (ex = q0,q1...)
         - initial: indica se refere-se ao estado inicial da máquina
         - end: indica se é um estado final da máquina
         - transições: um dicionário com as possíveis transições a partir do objeto atual
         - token: caso seja final, é atribuido com um token
         - mensagemDeErro: Caso ocorra erro neste estado, lança uma determinada mensagem

    # Classe apresenta métodos getters e setters para manipulações dos atributos descritos
"""


class State:

    # Método construtor
    def __init__(self, name, initial=False, end=False):
        self.__name = name          # Nome dos estados - 0 a 9
        self.__initial = initial    # Indica se o estado é inicial
        self.__end = end            # Indica se o estado é final
        self.__transicoes = {}      # Transições
        self.__token = None         # Caso seja final, definir token
        self.__mensagemDeErro = ''  # Colocar mensagem de erro

    # GETTERS
    @property
    def name_state(self):
        return self.__name

    @property
    def is_initial(self):
        return self.__initial

    @property
    def is_end(self):
        return self.__end

    @property
    def transicoes(self):
        return self.__transicoes

    @property
    def token(self):
        return self.__token

    @property
    def mensagemDeErro(self):
        return self.__mensagemDeErro

    # SETTERS
    @name_state.setter
    def name_state(self, name):
        self.__name = name

    @is_initial.setter
    def is_initial(self, is_initial):
        self.__initial = is_initial

    @is_end.setter
    def is_end(self, is_end):
        self.__end = is_end

    @token.setter
    def token(self, token):
        self.__token = token

    @mensagemDeErro.setter
    def mensagemDeErro(self, mensagem):
        self.__mensagemDeErro = mensagem

    # MÉTODOS PÚBLICOS

    # ====================
    # Insere transicao ao dicionario do estado
    def insere_transicao(self, aresta, prox_estado):
        self.__transicoes[aresta] = prox_estado
