
from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):
    def __init__(self):

        @abstractmethod
        def scroll(self):
            pass

    # @abstractmethod
    # def click(self):
    #     pass



class HP(TouchScreenLaptop):

    def __init__(self, HPNotebook):
        super().__init__()
        self.HPNotebook = HPNotebook


    def scroll(self):
        super().scroll()
        print("scroll for HP")

    def display(self):
        print(self.HPNotebook)



class DELL(TouchScreenLaptop):

    def __init__(self, DELLNotebook):
        super().__init__()
        self.DELLNotebook = DELLNotebook

    def scroll(self):
        super().scroll()
        print("scroll for DELL")

    def display(self):
        print(self.DELLNotebook)





hp = HP("HPNotebook" )
print(hp.HPNotebook)
hp.scroll()
hp.display()


Dell = DELL("DELLNotebook")
print(Dell.DELLNotebook)
Dell.scroll()
Dell.display()