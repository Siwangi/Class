class Python:
    def __init__(self, id, name):
        self.__id = id            #double underscore make it private
        self.__name = name

    def function(self):
        print(self.__name)

obj = Python(1, 'shivi')

print(obj._Python__id)    #name mangling syntax

