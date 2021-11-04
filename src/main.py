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
    AF = Automaton()            # Instancia o automato AF
    AF.create_automato()        # Instancia o diagrama de estados

    # ====================
    # MOSTRANDO O AUTOMATO
    # AF.show_automaton()
    # print("\n")


    #####################################################
    ############### SCANNER - LEX #######################
    #####################################################

    # Cria o scanner
    scanner = Scanner(AF)               # Parametro sendo o Automato
    lex = scanner.analise_lexica()      # Realiza a análise léxica (True: Sucesso/False: Falhou)

    # Caso o scanner falhe, stop programa
    if not lex:
        return

    # Imprimindo para tabela de tokens gerada
    # print(scanner.getTableTokens())

    #####################################################
    ############### PARSER ##############################
    #####################################################

    
    #####################################################
    ############### SEMANTICO ###########################
    #####################################################


# Executando a função principal
if __name__ == '__main__':
    main()
