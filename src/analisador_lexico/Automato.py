from .State import State    # Importando a class state - objeto estado
import string               # Importando funcoes para loops de caracteres
from Token import Token     # Importando classe de tokens

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
        transitions_state0 = {'B': 1, 'E': 29, 'F': 41, 'G': 49, 'I': 56, 'L': 64, 'P': 74, 'T': 82, '"': 90,
                              '(': 93, ')': 94, '{': 95, '}': 96, ',': 97, '+': 98, '-': 99, '*': 100, '/': 101,
                              '|': 102, '&': 104, '!': 106, '<': 108, '>': 108, '=': 110, ';': 112}
        alphabet_az_state86 = self.loop_az(number_estado=86)  # {'a': 86, 'b': 86 ...}
        loop_09_state87 = self.loop_0_to_9(number_estado=87)  # {'0': 87, '1': 87 ...}

        transitions_state0.update(alphabet_az_state86)
        transitions_state0.update(loop_09_state87)

        self.add_state(0, 'q0', initial=True, end=False, transicoes=transitions_state0)

        # --------------
        # BAHTCHE
        self.add_state(1, 'q1', initial=False, end=False, transicoes={'A': 2, 'E': 21})
        self.add_state(2, 'q2', initial=False, end=False, transicoes={'H': 3, 'R': 8, 'G': 17})
        self.add_state(3, 'q3', initial=False, end=False, transicoes={'T': 4})
        self.add_state(4, 'q4', initial=False, end=False, transicoes={'C': 5})
        self.add_state(5, 'q5', initial=False, end=False, transicoes={'H': 6})
        self.add_state(6, 'q6', initial=False, end=False, transicoes={'E': 7})
        self.add_state(7, 'q7', initial=False, end=True, transicoes={})
        self.automato[7].token = Token.TK_MAIN  # Define Token

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
        self.add_state(16, 'q16', initial=False, end=True, transicoes={})
        self.automato[16].token = Token.TK_FUNC  # Define Token

        for i in range(8, 16):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'BARBARIDADE' né?"

        # --------------
        # BAGUAL
        self.add_state(17, 'q17', initial=False, end=False, transicoes={'U': 18})
        self.add_state(18, 'q18', initial=False, end=False, transicoes={'A': 19})
        self.add_state(19, 'q19', initial=False, end=False, transicoes={'L': 20})
        self.add_state(20, 'q20', initial=False, end=True, transicoes={})
        self.automato[20].token = Token.TK_ELSE  # Define Token

        for i in range(17, 20):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'BAGUAL' né?"

        # --------
        # BEM_CAPAZ
        self.add_state(21, 'q21', initial=False, end=False, transicoes={'M': 22})
        self.add_state(22, 'q22', initial=False, end=False, transicoes={'_': 23})
        self.add_state(23, 'q23', initial=False, end=False, transicoes={'C': 24})
        self.add_state(24, 'q24', initial=False, end=False, transicoes={'A': 25})
        self.add_state(25, 'q25', initial=False, end=False, transicoes={'P': 26})
        self.add_state(26, 'q26', initial=False, end=False, transicoes={'A': 27})
        self.add_state(27, 'q27', initial=False, end=False, transicoes={'Z': 28})
        self.add_state(28, 'q28', initial=False, end=True, transicoes={})
        self.automato[28].token = Token.TK_ELIF # Define Token

        for i in range(21, 28):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'BEM_CAPAZ' né?"

        # --------
        # EMCIMADOLACO
        self.add_state(29, 'q29', initial=False, end=False, transicoes={'M': 30})
        self.add_state(30, 'q30', initial=False, end=False, transicoes={'C': 31})
        self.add_state(31, 'q31', initial=False, end=False, transicoes={'I': 32})
        self.add_state(32, 'q32', initial=False, end=False, transicoes={'M': 33})
        self.add_state(33, 'q33', initial=False, end=False, transicoes={'A': 34})
        self.add_state(34, 'q34', initial=False, end=False, transicoes={'D': 35})
        self.add_state(35, 'q35', initial=False, end=False, transicoes={'O': 36})
        self.add_state(36, 'q36', initial=False, end=False, transicoes={'L': 37})
        self.add_state(37, 'q37', initial=False, end=True, transicoes={'A': 38})
        self.add_state(38, 'q38', initial=False, end=False, transicoes={'C': 39})
        self.add_state(39, 'q39', initial=False, end=False, transicoes={'O': 40})
        self.add_state(40, 'q40', initial=False, end=True, transicoes={})
        self.automato[40].token = Token.TK_WHILE  # Define Token

        for i in range(29, 40):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'EMCIMADOLACO' né?"

        # --------
        # FANDANGO
        self.add_state(41, 'q41', initial=False, end=False, transicoes={'A': 42})
        self.add_state(42, 'q42', initial=False, end=False, transicoes={'N': 43})
        self.add_state(43, 'q43', initial=False, end=False, transicoes={'D': 44})
        self.add_state(44, 'q44', initial=False, end=False, transicoes={'A': 45})
        self.add_state(45, 'q45', initial=False, end=False, transicoes={'N': 46})
        self.add_state(46, 'q46', initial=False, end=False, transicoes={'G': 47})
        self.add_state(47, 'q47', initial=False, end=False, transicoes={'O': 48})
        self.add_state(48, 'q48', initial=False, end=True, transicoes={})
        self.automato[48].token = Token.TK_STRING # Define Token

        for i in range(41, 48):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'FANDANGO' né?"

        # --------
        # GURI
        self.add_state(49, 'q49', initial=False, end=False, transicoes={'U': 50})
        self.add_state(50, 'q50', initial=False, end=False, transicoes={'R': 51})
        self.add_state(51, 'q51', initial=False, end=False, transicoes={'I': 52})
        self.add_state(52, 'q52', initial=False, end=True, transicoes={'Z': 53})
        self.automato[52].token = Token.TK_INT # Define Token

        for i in range(49, 52):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'GURI' né?"

        # --------
        # GURIZAO
        self.add_state(53, 'q53', initial=False, end=False, transicoes={'A': 54})
        self.add_state(54, 'q54', initial=False, end=False, transicoes={'O': 55})
        self.add_state(55, 'q55', initial=False, end=True, transicoes={})
        self.automato[55].token = Token.TK_FLOAT # Define Token

        for i in range(53, 55):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'GURIZAO' né?"

        # --------
        # INPUTCHE
        self.add_state(56, 'q56', initial=False, end=False, transicoes={'N': 57})
        self.add_state(57, 'q57', initial=False, end=False, transicoes={'P': 58})
        self.add_state(58, 'q58', initial=False, end=False, transicoes={'U': 59})
        self.add_state(59, 'q59', initial=False, end=False, transicoes={'T': 60})
        self.add_state(60, 'q60', initial=False, end=False, transicoes={'C': 61})
        self.add_state(61, 'q61', initial=False, end=False, transicoes={'H': 62})
        self.add_state(62, 'q62', initial=False, end=False, transicoes={'E': 63})
        self.add_state(63, 'q63', initial=False, end=True, transicoes={})
        self.automato[63].token = Token.TK_SCANF # Define Token

        for i in range(56, 63):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'INPUTCHE' né?"

        # --------
        # LARGUEIMAO
        self.add_state(64, 'q64', initial=False, end=False, transicoes={'A': 65})
        self.add_state(65, 'q65', initial=False, end=False, transicoes={'R': 66})
        self.add_state(66, 'q66', initial=False, end=False, transicoes={'G': 67})
        self.add_state(67, 'q67', initial=False, end=False, transicoes={'U': 68})
        self.add_state(68, 'q68', initial=False, end=False, transicoes={'E': 69})
        self.add_state(69, 'q69', initial=False, end=False, transicoes={'I': 70})
        self.add_state(70, 'q70', initial=False, end=False, transicoes={'M': 71})
        self.add_state(71, 'q71', initial=False, end=False, transicoes={'A': 72})
        self.add_state(72, 'q72', initial=False, end=False, transicoes={'O': 73})
        self.add_state(73, 'q73', initial=False, end=True, transicoes={})
        self.automato[73].token = Token.TK_RETURN  # Define Token

        for i in range(64, 73):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'LARGUEIMAO' né?"

        # --------
        # PRINTCHE
        self.add_state(74, 'q74', initial=False, end=False, transicoes={'R': 75})
        self.add_state(75, 'q75', initial=False, end=False, transicoes={'I': 76})
        self.add_state(76, 'q76', initial=False, end=False, transicoes={'N': 77})
        self.add_state(77, 'q77', initial=False, end=False, transicoes={'T': 78})
        self.add_state(78, 'q78', initial=False, end=False, transicoes={'C': 79})
        self.add_state(79, 'q79', initial=False, end=False, transicoes={'H': 80})
        self.add_state(80, 'q80', initial=False, end=False, transicoes={'E': 81})
        self.add_state(81, 'q81', initial=False, end=True, transicoes={})
        self.automato[81].token = Token.TK_PRINT # Define Token

        for i in range(74, 81):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'PRINTCHE' né?"

        # --------
        # TRIF
        self.add_state(82, 'q82', initial=False, end=False, transicoes={'R': 83})
        self.add_state(83, 'q83', initial=False, end=False, transicoes={'I': 84})
        self.add_state(84, 'q84', initial=False, end=False, transicoes={'F': 85})
        self.add_state(85, 'q85', initial=False, end=True, transicoes={})
        self.automato[85].token = Token.TK_IF # Define Token

        for i in range(82, 85):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'TRIF' né?"
            
        # --------
        # VARIAVEL
        transitions_state86 = self.loop_az(number_estado=86)  # a..z
        loop_AZ_state86 = self.loop_AZ(number_estado=86)  # A..Z
        numbers_state86 = self.loop_0_to_9(number_estado=86)  # 0..9

        transitions_state86.update(numbers_state86)  # a...z...0...9
        transitions_state86.update(loop_AZ_state86)  # a..z..0..9..A..Z

        self.add_state(86, 'q86', initial=False, end=True, transicoes=transitions_state86)
        self.automato[86].token = Token.TK_IDENT # Define Token

        # --------
        # NUMBER
        transitions_state87 = {'.': 88}
        loop_09_state87 = self.loop_0_to_9(number_estado=87)  # {0: 87, 1: 87, ... }
        transitions_state87.update(loop_09_state87)  # {'.': 88, 0: 87, 1: 87, ... }

        self.add_state(87, 'q87', initial=False, end=True, transicoes=transitions_state87)
        self.automato[87].token = Token.TK_NUMBER  # Define Token
        
        # --------
        # REAL
        loop_09_state88 = self.loop_0_to_9(number_estado=89)  # {0: 89, 1: 89 ...}
        self.add_state(88, 'q88', initial=False, end=False, transicoes=loop_09_state88)
        
        loop_09_state89 = self.loop_0_to_9(number_estado=89)  # 0..9
        self.add_state(89, 'q89', initial=False, end=True, transicoes=loop_09_state89)

        self.automato[89].token = Token.TK_REAL # Define Token

        for i in range(87, 89):
            self.automato[i].mensagemDeErro = "Mas BAH.. Acho que esse numero ta errado né?"

        # --------
        # TEXT
        dict_ascii = self.all_ascii(number_estado=91)   #  Dicionario com todo ASCII
        dict_ascii.pop('"')   # {a:91, b:91, c:91 ..., 0:91,1:91, ..... @:91}

        self.add_state(90, 'q90', initial=False, end=False, transicoes=dict_ascii)

        transitions_state91 = {'"': 92}
        transitions_state91.update(dict_ascii)
        self.add_state(91, 'q91', initial=False, end=False, transicoes=transitions_state91)

        self.add_state(92, 'q92', initial=False, end=True, transicoes={})
        self.automato[92].token = Token.TK_TEXT # Define Token

        for i in range(90, 92):
            self.automato[i].mensagemDeErro = "Mas BAH.. Tentativa de fazer uma string falhou"

        # --------
        # (
        self.add_state(93, 'q93', initial=False, end=True, transicoes={})
        self.automato[93].token = Token.TK_OP # Define Token

        # --------
        # )
        self.add_state(94, 'q94', initial=False, end=True, transicoes={})
        self.automato[94].token = Token.TK_CP # Define Token

        # --------
        # {
        self.add_state(95, 'q95', initial=False, end=True, transicoes={})
        self.automato[95].token = Token.TK_OK # Define Token

        # --------
        # }
        self.add_state(96, 'q96', initial=False, end=True, transicoes={})
        self.automato[96].token = Token.TK_CK # Define Token

        # --------
        # ,
        self.add_state(97, 'q97', initial=False, end=True, transicoes={})
        self.automato[97].token = Token.TK_COMMA # Define Token

        # --------
        # +
        self.add_state(98, 'q98', initial=False, end=True, transicoes={})
        self.automato[98].token = Token.TK_MATH_ADD  # Define Token

        # --------
        # -
        self.add_state(99, 'q99', initial=False, end=True, transicoes={})
        self.automato[99].token = Token.TK_MATH_SUB # Define Token

        # --------
        # *
        self.add_state(100, 'q100', initial=False, end=True, transicoes={})
        self.automato[100].token = Token.TK_MATH_MUL  # Define Token

        # --------
        # /
        self.add_state(101, 'q101', initial=False, end=True, transicoes={})
        self.automato[101].token = Token.TK_MATH_DIV # Define Token

        # --------
        # OR
        self.add_state(102, 'q102', initial=False, end=False, transicoes={'|': 103})
        self.add_state(103, 'q103', initial=False, end=True, transicoes={})
        self.automato[103].token = Token.TK_LOGIC_OR  # Define Token

        for i in range(102, 103):
            self.automato[i].mensagemDeErro = "Mas BAH.. Esse OR ta errado macho"

        # --------
        # AND
        self.add_state(104, 'q104', initial=False, end=False, transicoes={'&': 105})
        self.add_state(105, 'q105', initial=False, end=True, transicoes={})
        self.automato[105].token = Token.TK_LOGIC_AND # Define Token

        for i in range(104, 105):
            self.automato[i].mensagemDeErro = "Mas BAH.. Esse AND ta errado macho"

        # --------
        # !
        self.add_state(106, 'q106', initial=False, end=True, transicoes={'=': 107})
        self.automato[106].token = Token.TK_LOGIC_NOT  # Define Token

        # --------
        # !=
        self.add_state(107, 'q107', initial=False, end=True, transicoes={})
        self.automato[107].token = Token.TK_LOGIC_DIF # Define Token

        # --------
        # <, >
        self.add_state(108, 'q108', initial=False, end=True, transicoes={'=': 109})
        self.automato[108].token = Token.TK_LOGIC_LG # Define Token

        # --------
        # <=, >=
        self.add_state(109, 'q109', initial=False, end=True, transicoes={})
        self.automato[109].token = Token.TK_LOGIC_LE_GE # Define Token

        # --------
        # =
        self.add_state(110, 'q110', initial=False, end=True, transicoes={'=': 111})
        self.automato[110].token = Token.TK_ASSIGNMENT # Define Token

        # --------
        # ==
        self.add_state(111, 'q111', initial=False, end=True, transicoes={})
        self.automato[111].token = Token.TK_LOGIC_EQ # Define Token

        # --------
        # ;
        self.add_state(112, 'q112', initial=False, end=True, transicoes={})
        self.automato[112].token = Token.TK_END # Define Token

        # ==================================================
