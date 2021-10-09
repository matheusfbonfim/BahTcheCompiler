from .State import State    # Importando a class state - objeto estado
import string               # Importando funcoes para loops de caracteres

"""
CLASS AUTOMATO
    # Classe para representar um automato deterministico, tendo por atributos:
         - automato: Dicionario contendo cada estado com suas devidas transicoes 
                     Ex: {0: class State 0, 1: class State 1 ....}
                     
    # Classe apresenta métodos getters e setters para manipulações dos atributos descritos
    # Utiliza metodos da classe State para inserir estados ao automato
"""


class Automaton:

    def __init__(self):
        self.__automato = {}  # Dicionario de estados {}

    # ====================
    # GETTERS
    @property
    def automato(self):
        return self.__automato

    # ====================
    # INSERINDO ESTADO COM SUAS TRANSICOES NO AUTOMATO
    def add_state(self, number, name, initial=False, end=False, transicoes=None):
        estado = State(name, initial, end)  # Cria um estado

        # Regras de produção - Ex: {'U': 1, 'T': 2}
        for i in transicoes:
            estado.insere_transicao(i, transicoes[i])

        # Adiciona um elemento no dicionario(map), correspondente ao numero de cada estado
        # Cada estado é um class state
        self.__automato[number] = estado  # {1: class State 1, 2: class State 2}

    # ====================
    # MOSTRA OS ESTADOS E SUAS TRANSICOES
    def show_automaton(self):
        for i in self.__automato.values():
            print(i.__dict__)
        # print(self.__automato)

    # ====================
    # DICIONARIO DE A..Z PARA UM MESMO ESTADO (LOOP)
    @staticmethod
    def loop_AZ(number_estado):
        dict = {}
        alfabeto_maisculo = list(string.ascii_uppercase)  # ['A', 'B', 'C', 'D', ...

        for i in alfabeto_maisculo:
            dict[i] = number_estado

        return dict

    # ====================
    # DICIONARIO DE a..z PARA UM MESMO ESTADO (LOOP)
    @staticmethod
    def loop_az(number_estado):
        dict = {}
        alfabeto_minusculo = list(string.ascii_lowercase)  # ['a', 'b', 'c', 'd', ...

        for i in alfabeto_minusculo:
            dict[i] = number_estado

        return dict

    # ====================
    # DICIONARIO DE 0..9 PARA UM MESMO ESTADO (LOOP)
    @staticmethod
    def loop_0_to_9(number_estado):
        dict = {}

        for i in range(0, 10):
            dict[f'{i}'] = number_estado

        return dict

    # ====================
    # DICIONARIO DE 0..9 PARA UM MESMO ESTADO (LOOP)
    @staticmethod
    def all_ascii(number_estado):
        dict = {}

        for i in range(0, 256):
            dict[f'{chr(i)}'] = number_estado

        return dict

    # ====================
    # RETORNA AS TRANSICOES DO ESTADO
    def get_transitions_state(self, estado):
        return self.__automato[estado].transicoes

    # ====================
    # CRIANDO O AUTOMATO
    def create_automato(self):

        # ==================================================
        # ADICIONANDO ESTADOS AO AUTOMATO
        #   number, name, initial, end, transicoes

        # --------------
        # INICIO - Estado q0
        transitions_state0 = {'B': 1, 'E': 31, 'F': 43, 'G': 51, 'I': 58, 'L': 66, 'P': 76, 'T': 84, '"': 92,
                              '(': 95, ')': 96, '{': 97, '}': 98, ',': 99, '+': 100, '-': 100, '*': 100, '/': 100,
                              '|': 101, '&': 103, '!': 105, '<': 105, '>': 105, '=': 107, ';': 109}
        alphabet_az_state88 = self.loop_az(number_estado=88)  # {'a': 94, 'b': 94 ...}
        loop_09_state89 = self.loop_0_to_9(number_estado=89)

        transitions_state0.update(alphabet_az_state88)
        transitions_state0.update(loop_09_state89)

        self.add_state(0, 'q0', initial=True, end=False, transicoes=transitions_state0)

        # --------------
        # BAHTCHE
        self.add_state(1, 'q1', initial=False, end=False, transicoes={'A': 2, 'E': 23})
        self.add_state(2, 'q2', initial=False, end=False, transicoes={'H': 3, 'R': 8, 'G': 19})
        self.add_state(3, 'q3', initial=False, end=False, transicoes={'T': 4})
        self.add_state(4, 'q4', initial=False, end=False, transicoes={'C': 5})
        self.add_state(5, 'q5', initial=False, end=False, transicoes={'H': 6})
        self.add_state(6, 'q6', initial=False, end=False, transicoes={'E': 7})
        self.add_state(7, 'q7', initial=False, end=True, transicoes={})
        self.automato[7].token = 'TK_MAIN'  # Define Token

        for i in range(3, 7):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'BAHTCHE' né?"

        # --------------
        # BARBARIDADE
        self.add_state(8, 'q8', initial=False, end=False, transicoes={'B': 9})
        self.add_state(9, 'q9', initial=False, end=False, transicoes={'A': 10})
        self.add_state(10, 'q10', initial=False, end=False, transicoes={'R': 11})
        self.add_state(11, 'q11', initial=False, end=False, transicoes={'I': 12})
        self.add_state(12, 'q12', initial=False, end=False, transicoes={'D': 13})
        self.add_state(13, 'q13', initial=False, end=False, transicoes={'A': 14})
        self.add_state(14, 'q14', initial=False, end=False, transicoes={'D': 15})
        self.add_state(15, 'q15', initial=False, end=False, transicoes={'E': 16})
        self.add_state(16, 'q16', initial=False, end=False, transicoes={'@': 17})

        transitions_state17 = self.loop_AZ(number_estado=18)  # A..Z
        self.add_state(17, 'q17', initial=False, end=False, transicoes=transitions_state17)

        transitions_state18 = self.loop_AZ(number_estado=18)  # A..Z
        numbers_state18 = self.loop_0_to_9(number_estado=18)  # 0..9
        transitions_state18.update(numbers_state18)  # A...Z...0...9

        self.add_state(18, 'q18', initial=False, end=True, transicoes=transitions_state18)
        self.automato[18].token = 'TK_FUNC'  # Define Token

        for i in range(8, 17):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'BARBARIDADE' né?"
        self.automato[17].mensagemDeErro = "Mas BAH.. Acho que isso ai ta meio errado"

        # --------------
        # BAGUAL
        self.add_state(19, 'q19', initial=False, end=False, transicoes={'U': 20})
        self.add_state(20, 'q20', initial=False, end=False, transicoes={'A': 21})
        self.add_state(21, 'q21', initial=False, end=False, transicoes={'L': 22})
        self.add_state(22, 'q22', initial=False, end=True, transicoes={})
        self.automato[22].token = 'TK_ELSE'  # Define Token

        for i in range(19, 22):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'BAGUAL' né?"

        # --------
        # BEM_CAPAZ
        self.add_state(23, 'q23', initial=False, end=False, transicoes={'M': 24})
        self.add_state(24, 'q24', initial=False, end=False, transicoes={'_': 25})
        self.add_state(25, 'q25', initial=False, end=False, transicoes={'C': 26})
        self.add_state(26, 'q26', initial=False, end=False, transicoes={'A': 27})
        self.add_state(27, 'q27', initial=False, end=False, transicoes={'P': 28})
        self.add_state(28, 'q28', initial=False, end=False, transicoes={'A': 29})
        self.add_state(29, 'q29', initial=False, end=False, transicoes={'Z': 30})
        self.add_state(30, 'q30', initial=False, end=True, transicoes={})
        self.automato[30].token = 'TK_ELIF'  # Define Token

        for i in range(23, 30):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'BEM_CAPAZ' né?"

        # --------
        # EMCIMADOLACO
        self.add_state(31, 'q31', initial=False, end=False, transicoes={'M': 32})
        self.add_state(32, 'q32', initial=False, end=False, transicoes={'C': 33})
        self.add_state(33, 'q33', initial=False, end=False, transicoes={'I': 34})
        self.add_state(34, 'q34', initial=False, end=False, transicoes={'M': 35})
        self.add_state(35, 'q35', initial=False, end=False, transicoes={'A': 36})
        self.add_state(36, 'q36', initial=False, end=False, transicoes={'D': 37})
        self.add_state(37, 'q37', initial=False, end=False, transicoes={'O': 38})
        self.add_state(38, 'q38', initial=False, end=False, transicoes={'L': 39})
        self.add_state(39, 'q39', initial=False, end=True, transicoes={'A': 40})
        self.add_state(40, 'q40', initial=False, end=False, transicoes={'C': 41})
        self.add_state(41, 'q41', initial=False, end=False, transicoes={'O': 42})
        self.add_state(42, 'q42', initial=False, end=True, transicoes={})
        self.automato[42].token = 'TK_WHILE'  # Define Token

        for i in range(31, 42):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'EMCIMADOLACO' né?"

        # --------
        # FANDANGO
        self.add_state(43, 'q43', initial=False, end=False, transicoes={'A': 44})
        self.add_state(44, 'q44', initial=False, end=False, transicoes={'N': 45})
        self.add_state(45, 'q45', initial=False, end=False, transicoes={'D': 46})
        self.add_state(46, 'q46', initial=False, end=False, transicoes={'A': 47})
        self.add_state(47, 'q47', initial=False, end=False, transicoes={'N': 48})
        self.add_state(48, 'q48', initial=False, end=False, transicoes={'G': 49})
        self.add_state(49, 'q49', initial=False, end=False, transicoes={'O': 50})
        self.add_state(50, 'q50', initial=False, end=True, transicoes={})
        self.automato[50].token = 'TK_STRING'  # Define Token

        for i in range(43, 50):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'FANDANGO' né?"

        # --------
        # GURI
        self.add_state(51, 'q51', initial=False, end=False, transicoes={'U': 52})
        self.add_state(52, 'q52', initial=False, end=False, transicoes={'R': 53})
        self.add_state(53, 'q53', initial=False, end=False, transicoes={'I': 54})
        self.add_state(54, 'q54', initial=False, end=True, transicoes={'Z': 55})
        self.automato[54].token = 'TK_INT'  # Define Token

        for i in range(51, 54):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'GURI' né?"

        # --------
        # GURIZAO
        self.add_state(55, 'q55', initial=False, end=False, transicoes={'A': 56})
        self.add_state(56, 'q56', initial=False, end=False, transicoes={'O': 57})
        self.add_state(57, 'q57', initial=False, end=True, transicoes={})
        self.automato[57].token = 'TK_FLOAT'  # Define Token

        for i in range(55, 57):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'GURIZAO' né?"

        # --------
        # INPUTCHE
        self.add_state(58, 'q58', initial=False, end=False, transicoes={'N': 59})
        self.add_state(59, 'q59', initial=False, end=False, transicoes={'P': 60})
        self.add_state(60, 'q60', initial=False, end=False, transicoes={'U': 61})
        self.add_state(61, 'q61', initial=False, end=False, transicoes={'T': 62})
        self.add_state(62, 'q62', initial=False, end=False, transicoes={'C': 63})
        self.add_state(63, 'q63', initial=False, end=False, transicoes={'H': 64})
        self.add_state(64, 'q64', initial=False, end=False, transicoes={'E': 65})
        self.add_state(65, 'q65', initial=False, end=True, transicoes={})
        self.automato[65].token = 'TK_SCANF'  # Define Token

        for i in range(58, 65):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'INPUTCHE' né?"

        # --------
        # LARGUEIMAO
        self.add_state(66, 'q66', initial=False, end=False, transicoes={'A': 67})
        self.add_state(67, 'q67', initial=False, end=False, transicoes={'R': 68})
        self.add_state(68, 'q68', initial=False, end=False, transicoes={'G': 69})
        self.add_state(69, 'q69', initial=False, end=False, transicoes={'U': 70})
        self.add_state(70, 'q70', initial=False, end=False, transicoes={'E': 71})
        self.add_state(71, 'q71', initial=False, end=False, transicoes={'I': 72})
        self.add_state(72, 'q72', initial=False, end=False, transicoes={'M': 73})
        self.add_state(73, 'q73', initial=False, end=False, transicoes={'A': 74})
        self.add_state(74, 'q74', initial=False, end=False, transicoes={'O': 75})
        self.add_state(75, 'q75', initial=False, end=True, transicoes={})
        self.automato[75].token = 'TK_RETURN'  # Define Token

        for i in range(66, 75):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'LARGUEIMAO' né?"

        # --------
        # PRINTCHE
        self.add_state(76, 'q76', initial=False, end=False, transicoes={'R': 77})
        self.add_state(77, 'q77', initial=False, end=False, transicoes={'I': 78})
        self.add_state(78, 'q78', initial=False, end=False, transicoes={'N': 79})
        self.add_state(79, 'q79', initial=False, end=False, transicoes={'T': 80})
        self.add_state(80, 'q80', initial=False, end=False, transicoes={'C': 81})
        self.add_state(81, 'q81', initial=False, end=False, transicoes={'H': 82})
        self.add_state(82, 'q82', initial=False, end=False, transicoes={'E': 83})
        self.add_state(83, 'q83', initial=False, end=True, transicoes={})
        self.automato[83].token = 'TK_PRINT'  # Define Token

        for i in range(76, 83):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'PRINTTCHE' né?"

        # --------
        # TRIF
        self.add_state(84, 'q84', initial=False, end=False, transicoes={'R': 85})
        self.add_state(85, 'q85', initial=False, end=False, transicoes={'I': 86})
        self.add_state(86, 'q86', initial=False, end=False, transicoes={'F': 87})
        self.add_state(87, 'q87', initial=False, end=True, transicoes={})
        self.automato[87].token = 'TK_IF'  # Define Token

        for i in range(84, 87):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'TRIF' né?"

        # --------
        # VARIAVEL
        transitions_state88 = self.loop_az(number_estado=88)  # a..z
        loop_AZ_state88 = self.loop_AZ(number_estado=88)  # A..Z
        numbers_state88 = self.loop_0_to_9(number_estado=88)  # 0..9

        transitions_state88.update(numbers_state88)  # a...z...0...9
        transitions_state88.update(loop_AZ_state88)  # a..z..0..9..A..Z

        self.add_state(88, 'q88', initial=False, end=True, transicoes=transitions_state88)
        self.automato[88].token = 'TK_IDENT'  # Define Token

        # --------
        # NUMBER
        transitions_state89 = {'.': 90}
        loop_09_state89 = self.loop_0_to_9(number_estado=89)  # 0..9

        transitions_state89.update(loop_09_state89)

        self.add_state(89, 'q89', initial=False, end=True, transicoes=transitions_state89)
        self.automato[89].token = 'TK_NUMBER'  # Define Token

        # --------
        # REAL
        loop_09_state90 = self.loop_0_to_9(number_estado=91)  # 0..9
        self.add_state(90, 'q90', initial=False, end=False, transicoes=loop_09_state90)
        loop_09_state91 = self.loop_0_to_9(number_estado=91)  # 0..9
        self.add_state(91, 'q91', initial=False, end=True, transicoes=loop_09_state91)

        self.automato[91].token = 'TK_REAL'  # Define Token

        # --------
        # TEXT
        dict_ascii = self.all_ascii(number_estado=93)
        dict_ascii.pop('"')

        self.add_state(92, 'q92', initial=False, end=False, transicoes=dict_ascii)

        transitions_state93 = {'"': 94}
        transitions_state93.update(dict_ascii)
        self.add_state(93, 'q93', initial=False, end=False, transicoes=transitions_state93)

        self.add_state(94, 'q94', initial=False, end=True, transicoes={})
        self.automato[94].token = 'TK_TEXT'  # Define Token

        for i in range(92, 94):
            self.automato[i].mensagemDeErro = "Mas BAH.. Tentativa de fazer uma string falhou"

        # --------
        # (
        self.add_state(95, 'q95', initial=False, end=True, transicoes={})
        self.automato[95].token = 'TK_OP'  # Define Token

        # --------
        # )
        self.add_state(96, 'q96', initial=False, end=True, transicoes={})
        self.automato[96].token = 'TK_CP'  # Define Token

        # --------
        # {
        self.add_state(97, 'q97', initial=False, end=True, transicoes={})
        self.automato[97].token = 'TK_OK'  # Define Token

        # --------
        # }
        self.add_state(98, 'q98', initial=False, end=True, transicoes={})
        self.automato[98].token = 'TK_CK'  # Define Token

        # --------
        # ,
        self.add_state(99, 'q99', initial=False, end=True, transicoes={})
        self.automato[99].token = 'TK_COMMA'  # Define Token

        # --------
        # +,-,*,/
        self.add_state(100, 'q100', initial=False, end=True, transicoes={})
        self.automato[100].token = 'TK_MATH_OP'  # Define Token

        # --------
        # OR
        self.add_state(101, 'q101', initial=False, end=False, transicoes={'|': 102})
        self.add_state(102, 'q102', initial=False, end=True, transicoes={})
        self.automato[102].token = 'TK_OR'  # Define Token

        # --------
        # AND
        self.add_state(103, 'q103', initial=False, end=False, transicoes={'&': 104})
        self.add_state(104, 'q104', initial=False, end=True, transicoes={})
        self.automato[104].token = 'TK_AND'  # Define Token

        # --------
        # !, <, >
        self.add_state(105, 'q105', initial=False, end=True, transicoes={'=': 106})
        self.automato[105].token = 'TK_OPERATOR'  # Define Token

        # --------
        # !=, <=, >=
        self.add_state(106, 'q106', initial=False, end=True, transicoes={})
        self.automato[106].token = 'TK_OPERATOR'  # Define Token

        # --------
        # ==
        self.add_state(107, 'q107', initial=False, end=True, transicoes={'=': 108})
        self.automato[107].token = 'TK_ASSIGN'  # Define Token

        # --------
        # ==
        self.add_state(108, 'q108', initial=False, end=True, transicoes={})
        self.automato[108].token = 'TK_OPERATOR'  # Define Token

        # --------
        # ;
        self.add_state(109, 'q109', initial=False, end=True, transicoes={})
        self.automato[109].token = 'TK_END'  # Define Token

        # ==================================================
