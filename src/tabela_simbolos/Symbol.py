class Symbol:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name

    def toString(self):
        return f"Symbol: {self.__name}"
    
