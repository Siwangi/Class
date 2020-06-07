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



class FiveSeries(BMW):

    def __init__(self, parkingAssitEnabled, brand, year, model):
        self.parkingAssitEnabled = parkingAssitEnabled
        BMW.__init__(self, brand, year, model)


threeseries = ThreeSeries(True, "BMW", "328i", "2008")
print(threeseries.model)