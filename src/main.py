# IMPORTS
import sys 
from analisador_lexico.Automato import Automaton  # Importando a class automato - objeto automato
from analisador_lexico.Scanner import Scanner     # Importando a class Scanner - Varredor Lexico


# FUNÇÃO PRINCIPAL
def main():
    #####################################################
    ############### AUTOMATO ############################
    #####################################################

    # Construindo o Automato
    AF = Automaton()            # Instancia o automato
    AF.create_automato()        # Chamada da funcao

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
