import graphviz

tree = graphviz.Digraph(comment='Parser Tree')


def plot(node, state):
    name = f'{state} {node.name}'   # Nome unico para insercao do node

    tree.node(name, f'{node.name}') # Cria o estado no desenho

    # Percorrendo cada filho do node e fazendo os links
    for child in node.children:
        state += 1                  # Incrementando o estado 
        tree.edge(name, f'{state} {child.name}', constraint='true')
        plot(child, state)

    # print(tree)
    if node.level - 1 == 0:
        tree.render('tree', view=True)

