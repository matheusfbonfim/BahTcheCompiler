import graphviz

tree = graphviz.Digraph(comment='Parser Tree')


def plot(node, level, state):
    node.level = level
    name = f'{state} {node.name}'

    tree.node(name, f'{node.name}')

    level += 1

    for child in node.children:
        state += 1
        tree.edge(name, f'{state} {child.name}', constraint='true')
        plot(child, level, state)

    if level - 1 == 0:
        tree.render('tree', view=True)

