# IMPORTS
import sys
from analisador_lexico.Automato import Automaton       # Importando a class automato - objeto automato
from analisador_lexico.Scanner import Scanner          # Importando a class Scanner - Varredor Lexico
from analisador_sintatico.Parser import Parser         # Importando a class Scanner - Varredor Lexico
from analisador_sintatico.PlotTree import plot, State  # Importando a funcao para plot da Tree
from tabela_simbolos.SymbolTable import Table          # Importando class TableSymbol - Tabela de simbolos


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
    parser = Parser(fluxo_tokens)          # Parametro sendo o fluxo_tokens
    sint = parser.analise_sintatica()      # Realiza a análise sintatica (True: Sucesso/False: Falhou)
    
    # Caso o parser falhe, stop programa
    if not sint:
        return

    # Retorno do node raiz da tree
    node_root_tree = parser.tree()

    # Atribuindo niveis aos nodes
    parser.assign_levels(node=node_root_tree, level=0)

    # Plotando a arvore - PlotTree
    plot(node=node_root_tree, stt=State())

    # Armazenar a arvore em profundidade no arquivo
    parser.store_file_dfs_tree()

    #####################################################
    ########### TABELA DE SIMBOLOS ######################
    #####################################################

    # Cria a instancia da tabela de simbolos
    symbol_table = Table(fluxo_tokens)

    # Executa a criacao da tabela com base no fluxo de tokens
    symbol_table.create()

    #print(symbol_table.table)

    symbol_table.store_file_symbol_table()

    #####################################################
    ############### SEMANTICO ###########################
    #####################################################

# Executando a função principal
if __name__ == '__main__':
    main()
