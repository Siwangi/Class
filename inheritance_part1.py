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
        BMW.__init__(self, brand, model, year)


    def display(self):
        print(self.cruiseControlEnabled)


    def start(self):
        print("Button start")


class FiveSeries(BMW):

    def __init__(self, parkingAssitEnabled, brand, year, model):
        self.parkingAssitEnabled = parkingAssitEnabled
        BMW.__init__(self, brand, year, model)

    def display(self):
        print(self.parkingAssitEnabled)


threeseries = ThreeSeries(True, "BMW", "328i", "2008")
print(threeseries.model)

"""start function is in parent as well as in child so it will run the child's function i.e. Threeseries (overriding) 
but if there was no same function in child class "start method will inherit from parent"""

threeseries.start()
threeseries.display()
