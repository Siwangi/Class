""" Super(Inbuilt function in python) is about:
 How to invoke Parent's class methods and constructer from child class methods and constructor"""

""" Just add super with init function in child class and remove self - it will run same as parent class"""

class BMW:
    def __init__(self, brand, year, model):
        self.brand = brand
        self.year = year
        self.model = model

    def start(self):
        print("Start the car")

    def stop(self):
        print("stop the car")

class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled, brand, year, model):
        self.cruiseControlEnabled = cruiseControlEnabled
        super().__init__(brand, model, year)


    def display(self):
        print(self.cruiseControlEnabled)


    def start(self):
        super().start()
        print("Button start")

threeseries = ThreeSeries(True, "BMW", "328i", "2008")
threeseries.start()

threeseries.display()



""" works in child & parent class as well.
 In child class init function : remove parent name & self from init and add super
  In child class method add one more line before print: for super to get both parent & childs output """


""" Runtime polymorphism is same like over riding - we can chnage the object with parent class name"""