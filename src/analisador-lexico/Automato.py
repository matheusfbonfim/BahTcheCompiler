from State import State  # Importando a class state - objeto estado
import string

class Automaton:

    def __init__(self):
        self.__automato = {}  # Dicionario de estados

    # ====================
    # GETTERS
    @property
    def automato(self):
        return self.__automato

    # ====================
    # INSERINDO ESTADO COM SUAS TRANSICOES NO AUTOMATO
    def add_state(self, number, name, initial = False, end = False, transicoes = None):
        estado = State(name, initial, end)

        # Regras de produção - Ex: {'U': 1, 'T': 2}
        for i in transicoes:
            estado.insere_transicao(i, transicoes[i])
        
        # Adiciona um elemento no dicionario(map), correspondente ao numero de cada estado
            # Cada estado é um class state
        self.__automato[number] = estado
    
    # ====================
    # MOSTRA OS ESTADOS E SUAS TRANSICOES
    def show_automaton(self):
      for i in self.__automato.values():
          print(i.__dict__)
      #print(self.__automato)

    # ====================
    # DICIONARIO DE A..Z PARA UM MESMO ESTADO (LOOP)
    @staticmethod
    def loop_AZ(number_estado):
        dict = {}
        alfabeto_maisculo = list(string.ascii_uppercase)    # ['A', 'B', 'C', 'D', ...

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