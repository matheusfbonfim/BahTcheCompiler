class Table:
    def __init__(self, tokens):
        self._table = {}          # Tabela de simbolos - Dicionario
        self._tokens = tokens     # Fluxo de tokens
        self._count = 0

    def table(self):
        pass
    

    def _proximo_tk(self):
        temp = 'finish'  # De inicio é atribuido temp como 'finish'

        # Caso o count ainda seja menor que a lista de tokens, redefine temp
        if self._count < len(self._table_tokens):
            temp = self._table_tokens[self._count]
            self._count += 1  # O count ja fica posicionado para o proximo token
        return temp