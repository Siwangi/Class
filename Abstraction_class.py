"""     Abstract is a contract for child class,
    Abstract method will not have any implementation (pass),
    cannot create object for abstract class,
    it exits only for the contract for the child class,
    child class should extend the abstract(contract)interface : drive ,
    should provide drive method using exact parameter
    """

from abc import abstractmethod, ABC


class iOS(ABC):
    def __init__(self, color, model, size):
        self.color = color
        self.model = model
        self.size = size

    @abstractmethod
    def library(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class Mac(iOS):

    def __init__(self, trackpad, color, model, size):
        self.trackpad = trackpad
        iOS.__init__(self, color, model, size)

    def function(self):
        print("Swipe style trackpad")

    def drive(self):
        print("Mac")

    def library(self):
        pass


# we cannot use parent class as its Interface now


version = Mac("touchpad", "black", 2016, 16)
version.function()
print(version.trackpad)
version.function()



""" Abstract method is mandat to create in child class as well """


""" when a class has all the methods as abstract method , we cal that class as interface """