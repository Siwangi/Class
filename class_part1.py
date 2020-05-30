class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduceSelf(self):
        print("My name is", self.name, ".", "My color is", self.color, ".", "My weight is", self.weight, ".")



r1 = Robot("Tom", "Red", 30)

r1.introduceSelf()

r2 = Robot("Jerry", "Blue", 40)

r2.introduceSelf()


