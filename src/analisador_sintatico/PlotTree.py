import graphviz

tree = graphviz.Digraph(comment='Parser Tree')


def plot(node, level, state):
    node.level = level              # Armazena o nivel do nó da arvore
    name = f'{state} {node.name}'   # Nome unico para insercao do node

    tree.node(name, f'{node.name}') # Cria o estado no desenho

    level += 1                      # Incrementa o nivel do estado

    # Percorrendo cada filho do node e fazendo os links
    for child in node.children:
        state += 1                  # Incrementando o estado 
        tree.edge(name, f'{state} {child.name}', constraint='true')
        plot(child, level, state)

    print(tree)
    if level - 1 == 0:
        tree.render('tree', view=True)

