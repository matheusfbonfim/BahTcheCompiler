# IMPORTS
import sys
sys.path.insert(1, './analisador-lexico')

from Automato import Automaton  # Importando a class automato - objeto automato
from Scanner import Scanner     # Importando a class Scanner - Varredor Lexico


# FUNÇÃO PRINCIPAL
def main():
    #####################################################
    ############### AUTOMATO ############################
    #####################################################

    # Construindo o Automato
    AF = Automaton()

    # ==================================================
    # ADICIONANDO ESTADOS AO AUTOMATO
    #   number, name, initial, end, transicoes

    # --------------
    # INICIO - Estado q0
    transitions_state0 = {'B': 1, 'E': 31, 'F': 43, 'G': 51, 'I': 58, 'L': 66, 'P': 76, 'T': 84, '"': 92,
                          '(': 95, ')': 96, '{': 97, '}': 98, ',': 99, '+': 100, '-': 100, '*': 100, '/': 100,
                          '|': 101, '&': 103, '!': 105, '<': 105, '>': 105, '=': 107, ';': 109}
    alphabet_az_state88 = AF.loop_az(number_estado=88)  # {'a': 94, 'b': 94 ...}
    loop_09_state89 = AF.loop_0_to_9(number_estado=89)

    transitions_state0.update(alphabet_az_state88)
    transitions_state0.update(loop_09_state89)

    AF.add_state(0, 'q0', initial=True, end=False, transicoes=transitions_state0)

    # --------------
    # BAHTCHE
    AF.add_state(1, 'q1', initial=False, end=False, transicoes={'A': 2, 'E': 23})
    AF.add_state(2, 'q2', initial=False, end=False, transicoes={'H': 3, 'R': 8, 'G': 19})
    AF.add_state(3, 'q3', initial=False, end=False, transicoes={'T': 4})
    AF.add_state(4, 'q4', initial=False, end=False, transicoes={'C': 5})
    AF.add_state(5, 'q5', initial=False, end=False, transicoes={'H': 6})
    AF.add_state(6, 'q6', initial=False, end=False, transicoes={'E': 7})
    AF.add_state(7, 'q7', initial=False, end=True, transicoes={})
    AF.automato[7].token = 'TK_MAIN'  # Define Token

    for i in range(3, 7):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'BAHTCHE' né?"

    # --------------
    # BARBARIDADE
    AF.add_state(8, 'q8', initial=False, end=False, transicoes={'B': 9})
    AF.add_state(9, 'q9', initial=False, end=False, transicoes={'A': 10})
    AF.add_state(10, 'q10', initial=False, end=False, transicoes={'R': 11})
    AF.add_state(11, 'q11', initial=False, end=False, transicoes={'I': 12})
    AF.add_state(12, 'q12', initial=False, end=False, transicoes={'D': 13})
    AF.add_state(13, 'q13', initial=False, end=False, transicoes={'A': 14})
    AF.add_state(14, 'q14', initial=False, end=False, transicoes={'D': 15})
    AF.add_state(15, 'q15', initial=False, end=False, transicoes={'E': 16})
    AF.add_state(16, 'q16', initial=False, end=False, transicoes={'@': 17})

    transitions_state17 = AF.loop_AZ(number_estado=18)  # A..Z
    AF.add_state(17, 'q17', initial=False, end=False, transicoes=transitions_state17)

    transitions_state18 = AF.loop_AZ(number_estado=18)  # A..Z
    numbers_state18 = AF.loop_0_to_9(number_estado=18)  # 0..9
    transitions_state18.update(numbers_state18)  # A...Z...0...9

    AF.add_state(18, 'q18', initial=False, end=True, transicoes=transitions_state18)
    AF.automato[18].token = 'TK_FUNC'  # Define Token

    for i in range(8, 17):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'BARBARIDADE' né?"
    AF.automato[17].mensagemDeErro = "Mas BAH.. Acho que isso ai ta meio errado"

    # --------------
    # BAGUAL
    AF.add_state(19, 'q19', initial=False, end=False, transicoes={'U': 20})
    AF.add_state(20, 'q20', initial=False, end=False, transicoes={'A': 21})
    AF.add_state(21, 'q21', initial=False, end=False, transicoes={'L': 22})
    AF.add_state(22, 'q22', initial=False, end=True, transicoes={})
    AF.automato[22].token = 'TK_ELSE'  # Define Token

    for i in range(19, 22):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'BAGUAL' né?"

    # --------
    # BEM_CAPAZ
    AF.add_state(23, 'q23', initial=False, end=False, transicoes={'M': 24})
    AF.add_state(24, 'q24', initial=False, end=False, transicoes={'_': 25})
    AF.add_state(25, 'q25', initial=False, end=False, transicoes={'C': 26})
    AF.add_state(26, 'q26', initial=False, end=False, transicoes={'A': 27})
    AF.add_state(27, 'q27', initial=False, end=False, transicoes={'P': 28})
    AF.add_state(28, 'q28', initial=False, end=False, transicoes={'A': 29})
    AF.add_state(29, 'q29', initial=False, end=False, transicoes={'Z': 30})
    AF.add_state(30, 'q30', initial=False, end=True, transicoes={})
    AF.automato[30].token = 'TK_ELIF'  # Define Token

    for i in range(23, 30):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'BEM_CAPAZ' né?"

    # --------
    # EMCIMADOLACO
    AF.add_state(31, 'q31', initial=False, end=False, transicoes={'M': 32})
    AF.add_state(32, 'q32', initial=False, end=False, transicoes={'C': 33})
    AF.add_state(33, 'q33', initial=False, end=False, transicoes={'I': 34})
    AF.add_state(34, 'q34', initial=False, end=False, transicoes={'M': 35})
    AF.add_state(35, 'q35', initial=False, end=False, transicoes={'A': 36})
    AF.add_state(36, 'q36', initial=False, end=False, transicoes={'D': 37})
    AF.add_state(37, 'q37', initial=False, end=False, transicoes={'O': 38})
    AF.add_state(38, 'q38', initial=False, end=False, transicoes={'L': 39})
    AF.add_state(39, 'q39', initial=False, end=True, transicoes={'A': 40})
    AF.add_state(40, 'q40', initial=False, end=False, transicoes={'C': 41})
    AF.add_state(41, 'q41', initial=False, end=False, transicoes={'O': 42})
    AF.add_state(42, 'q42', initial=False, end=True, transicoes={})
    AF.automato[42].token = 'TK_WHILE'  # Define Token

    for i in range(31, 42):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'EMCIMADOLACO' né?"

    # --------
    # FANDANGO
    AF.add_state(43, 'q43', initial=False, end=False, transicoes={'A': 44})
    AF.add_state(44, 'q44', initial=False, end=False, transicoes={'N': 45})
    AF.add_state(45, 'q45', initial=False, end=False, transicoes={'D': 46})
    AF.add_state(46, 'q46', initial=False, end=False, transicoes={'A': 47})
    AF.add_state(47, 'q47', initial=False, end=False, transicoes={'N': 48})
    AF.add_state(48, 'q48', initial=False, end=False, transicoes={'G': 49})
    AF.add_state(49, 'q49', initial=False, end=False, transicoes={'O': 50})
    AF.add_state(50, 'q50', initial=False, end=True, transicoes={})
    AF.automato[50].token = 'TK_STRING'  # Define Token

    for i in range(43, 50):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'FANDANGO' né?"

    # --------
    # GURI
    AF.add_state(51, 'q51', initial=False, end=False, transicoes={'U': 52})
    AF.add_state(52, 'q52', initial=False, end=False, transicoes={'R': 53})
    AF.add_state(53, 'q53', initial=False, end=False, transicoes={'I': 54})
    AF.add_state(54, 'q54', initial=False, end=True, transicoes={'Z': 55})
    AF.automato[54].token = 'TK_INT'  # Define Token

    for i in range(51, 54):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'GURI' né?"

    # --------
    # GURIZAO
    AF.add_state(55, 'q55', initial=False, end=False, transicoes={'A': 56})
    AF.add_state(56, 'q56', initial=False, end=False, transicoes={'O': 57})
    AF.add_state(57, 'q57', initial=False, end=True, transicoes={})
    AF.automato[57].token = 'TK_FLOAT'  # Define Token

    for i in range(55, 57):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'GURIZAO' né?"

    # --------
    # INPUTCHE
    AF.add_state(58, 'q58', initial=False, end=False, transicoes={'N': 59})
    AF.add_state(59, 'q59', initial=False, end=False, transicoes={'P': 60})
    AF.add_state(60, 'q60', initial=False, end=False, transicoes={'U': 61})
    AF.add_state(61, 'q61', initial=False, end=False, transicoes={'T': 62})
    AF.add_state(62, 'q62', initial=False, end=False, transicoes={'C': 63})
    AF.add_state(63, 'q63', initial=False, end=False, transicoes={'H': 64})
    AF.add_state(64, 'q64', initial=False, end=False, transicoes={'E': 65})
    AF.add_state(65, 'q65', initial=False, end=True, transicoes={})
    AF.automato[65].token = 'TK_SCANF'  # Define Token

    for i in range(58, 65):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'INPUTCHE' né?"

    # --------
    # LARGUEIMAO
    AF.add_state(66, 'q66', initial=False, end=False, transicoes={'A': 67})
    AF.add_state(67, 'q67', initial=False, end=False, transicoes={'R': 68})
    AF.add_state(68, 'q68', initial=False, end=False, transicoes={'G': 69})
    AF.add_state(69, 'q69', initial=False, end=False, transicoes={'U': 70})
    AF.add_state(70, 'q70', initial=False, end=False, transicoes={'E': 71})
    AF.add_state(71, 'q71', initial=False, end=False, transicoes={'I': 72})
    AF.add_state(72, 'q72', initial=False, end=False, transicoes={'M': 73})
    AF.add_state(73, 'q73', initial=False, end=False, transicoes={'A': 74})
    AF.add_state(74, 'q74', initial=False, end=False, transicoes={'O': 75})
    AF.add_state(75, 'q75', initial=False, end=True, transicoes={})
    AF.automato[75].token = 'TK_RETURN'  # Define Token

    for i in range(66, 75):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'LARGUEIMAO' né?"

    # --------
    # PRINTCHE
    AF.add_state(76, 'q76', initial=False, end=False, transicoes={'R': 77})
    AF.add_state(77, 'q77', initial=False, end=False, transicoes={'I': 78})
    AF.add_state(78, 'q78', initial=False, end=False, transicoes={'N': 79})
    AF.add_state(79, 'q79', initial=False, end=False, transicoes={'T': 80})
    AF.add_state(80, 'q80', initial=False, end=False, transicoes={'C': 81})
    AF.add_state(81, 'q81', initial=False, end=False, transicoes={'H': 82})
    AF.add_state(82, 'q82', initial=False, end=False, transicoes={'E': 83})
    AF.add_state(83, 'q83', initial=False, end=True, transicoes={})
    AF.automato[83].token = 'TK_PRINT'  # Define Token

    for i in range(76, 83):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'PRINTTCHE' né?"

    # --------
    # TRIF
    AF.add_state(84, 'q84', initial=False, end=False, transicoes={'R': 85})
    AF.add_state(85, 'q85', initial=False, end=False, transicoes={'I': 86})
    AF.add_state(86, 'q86', initial=False, end=False, transicoes={'F': 87})
    AF.add_state(87, 'q87', initial=False, end=True, transicoes={})
    AF.automato[87].token = 'TK_IF'  # Define Token

    for i in range(84, 87):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Acho que quis dizer 'TRIF' né?"

    # --------
    # VARIAVEL
    transitions_state88 = AF.loop_az(number_estado=88)  # a..z
    loop_AZ_state88 = AF.loop_AZ(number_estado=88)  # A..Z
    numbers_state88 = AF.loop_0_to_9(number_estado=88)  # 0..9

    transitions_state88.update(numbers_state88)  # a...z...0...9
    transitions_state88.update(loop_AZ_state88)  # a..z..0..9..A..Z

    AF.add_state(88, 'q88', initial=False, end=True, transicoes=transitions_state88)
    AF.automato[88].token = 'TK_IDENT'  # Define Token

    # --------
    # NUMBER
    transitions_state89 = {'.': 90}
    loop_09_state89 = AF.loop_0_to_9(number_estado=89)  # 0..9

    transitions_state89.update(loop_09_state89)

    AF.add_state(89, 'q89', initial=False, end=True, transicoes=transitions_state89)
    AF.automato[89].token = 'TK_NUMBER'  # Define Token

    # --------
    # DOUBLE
    loop_09_state90 = AF.loop_0_to_9(number_estado=91)  # 0..9
    AF.add_state(90, 'q90', initial=False, end=False, transicoes=loop_09_state90)
    loop_09_state91 = AF.loop_0_to_9(number_estado=91)  # 0..9
    AF.add_state(91, 'q91', initial=False, end=True, transicoes=loop_09_state91)

    AF.automato[91].token = 'TK_DOUBLE'  # Define Token

    # --------
    # TEXT
    dict_ascii = AF.all_ascii(number_estado=93)
    dict_ascii.pop('"')

    AF.add_state(92, 'q92', initial=False, end=False, transicoes=dict_ascii)

    transitions_state93 = {'"': 94}
    transitions_state93.update(dict_ascii)
    AF.add_state(93, 'q93', initial=False, end=False, transicoes=transitions_state93)

    AF.add_state(94, 'q94', initial=False, end=True, transicoes={})
    AF.automato[94].token = 'TK_TEXT'  # Define Token

    for i in range(92, 94):
        AF.automato[i].mensagemDeErro = "Mas BAH.. Tentativa de fazer uma string falhou"

    # --------
    # (
    AF.add_state(95, 'q95', initial=False, end=True, transicoes={})
    AF.automato[95].token = 'TK_OP'  # Define Token

    # --------
    # )
    AF.add_state(96, 'q96', initial=False, end=True, transicoes={})
    AF.automato[96].token = 'TK_CP'  # Define Token

    # --------
    # {
    AF.add_state(97, 'q97', initial=False, end=True, transicoes={})
    AF.automato[97].token = 'TK_OK'  # Define Token

    # --------
    # }
    AF.add_state(98, 'q98', initial=False, end=True, transicoes={})
    AF.automato[98].token = 'TK_CK'  # Define Token

    # --------
    # ,
    AF.add_state(99, 'q99', initial=False, end=True, transicoes={})
    AF.automato[99].token = 'TK_COMMA'  # Define Token

    # --------
    # +,-,*,/
    AF.add_state(100, 'q100', initial=False, end=True, transicoes={})
    AF.automato[100].token = 'TK_MATH_OP'  # Define Token

    # --------
    # OR
    AF.add_state(101, 'q101', initial=False, end=False, transicoes={'|': 102})
    AF.add_state(102, 'q102', initial=False, end=True, transicoes={})
    AF.automato[102].token = 'TK_OR'  # Define Token

    # --------
    # AND
    AF.add_state(103, 'q103', initial=False, end=False, transicoes={'&': 104})
    AF.add_state(104, 'q104', initial=False, end=True, transicoes={})
    AF.automato[104].token = 'TK_AND'  # Define Token

    # --------
    # !, <, >
    AF.add_state(105, 'q105', initial=False, end=True, transicoes={'=': 106})
    AF.automato[105].token = 'TK_OPERATOR'  # Define Token

    # --------
    # !=, <=, >=
    AF.add_state(106, 'q106', initial=False, end=True, transicoes={})
    AF.automato[106].token = 'TK_OPERATOR'  # Define Token

    # --------
    # ==
    AF.add_state(107, 'q107', initial=False, end=True, transicoes={'=': 108})
    AF.automato[107].token = 'TK_ASSIGN'  # Define Token

    # --------
    # ==
    AF.add_state(108, 'q108', initial=False, end=True, transicoes={})
    AF.automato[108].token = 'TK_OPERATOR'  # Define Token

    # --------
    # ;
    AF.add_state(109, 'q109', initial=False, end=True, transicoes={})
    AF.automato[109].token = 'TK_END'  # Define Token

    # ==================================================
    # ==================================================

    # ====================
    # MOSTRANDO O AUTOMATO
    AF.show_automaton()
    print("\n")


    #####################################################
    ############### SCANNER #############################
    #####################################################

    sc = Scanner(AF)
    sc.analise_lexica()


    # print(sc.getTable())


# Executando a função principal
if __name__ == '__main__':
    main()
