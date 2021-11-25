import graphviz

tree = graphviz.Digraph(comment='Parser Tree')


class State:
    def __init__(self):
        self._state = 0

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        value += self._state
        self._state = value


def plot(node, stt):
    name = f'{stt.state} {node.name}'   # Nome unico para insercao do node

    tree.node(name, f'{node.name}')     # Cria o estado no desenho

    # Percorrendo cada filho do node e fazendo os links
    for child in node.children:
        stt.state = 1                  # Incrementando o estado
        tree.edge(name, f'{stt.state} {child.name}', constraint='true')
        plot(child, stt)

    print(tree)
    if node.level - 1 == 0:
        tree.render('tree', view=True)

