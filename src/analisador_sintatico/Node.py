class Node:
    def __init__(self, name=None, terminal=False):
        self._name = name
        self._children = []
        self._level = None
        self._terminal = terminal

    # ====================
    # GETTERS E SETTERS
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def terminal(self):
        return self._terminal
    
    @terminal.setter
    def terminal(self, value):
        self._terminal = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    
    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, child):
        self._children.append(child)
    
