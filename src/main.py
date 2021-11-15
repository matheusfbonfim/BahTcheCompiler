# IMPORTS
import sys
from analisador_lexico.Automato import Automaton  # Importando a class automato - objeto automato
from analisador_lexico.Scanner import Scanner  # Importando a class Scanner - Varredor Lexico
from analisador_sintatico.Parser import Parser  # Importando a class Scanner - Varredor Lexico


# FUNÇÃO PRINCIPAL
def main():
    #####################################################
    ############### AUTOMATO ############################
    #####################################################

    # Construindo o Automato
    AF = Automaton()  # Instancia o automato AF
    AF.create_automato()  # Instancia o diagrama de estados

    # ====================
    # MOSTRANDO O AUTOMATO
    # AF.show_automaton()
    # print("\n")

    #####################################################
    ############### SCANNER - LEX #######################
    #####################################################

    # Cria o scanner
    scanner = Scanner(AF)           # Parametro sendo o Automato
    lex = scanner.analise_lexica()  # Realiza a análise léxica (True: Sucesso/False: Falhou)

    # Caso o scanner falhe, stop programa
    if not lex:
        return

    # Fluxo de tokens gerados
    fluxo_tokens = scanner.getTableTokens()  # [('BAHTCHE', 'TK_MAIN', 1, 1), ...]

    #####################################################
    ############### PARSER ##############################
    #####################################################

    # Cria o parser
    parser = Parser(fluxo_tokens)   # Parametro sendo o fluxo_tokens
    parser.analise_sintatica()      # Realiza a análise sintatica (True: Sucesso/False: Falhou)
    
    # Retorno do node raiz da tree
    node_root_tree = parser.tree()

    # Mostra a arvore em profundidade
    parser.show_dfs_tree(node_root_tree)
    
    #####################################################
    ############### SEMANTICO ###########################
    #####################################################

# Executando a função principal
if __name__ == '__main__':
    main()
