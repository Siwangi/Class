class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduceSelf(self):
        print("My name is", self.name, ".")
        print("My color is", self.color, ".")
        print("My weight is", self.weight, ".")

r1 = Robot("Tom", "Red", 30)

r2 = Robot("Jerry", "Blue", 40)


class Person(Robot):
    def __init__(self, name1, personality, isSitting, robotOwned, name, color, weight):
        self.name1 = name1
        self.personality = personality
        self.isSitting = isSitting
        self.robotOwned = robotOwned
        Robot.__init__(self, name, color, weight )


    def sit_down(self):
        self.isSitting = True
        print(self.name, "is", self.personality)
        print(self.name, "is Sitting")
        print(self.name, "owns", self.robotOwned)



    def stand_up(self):
        self.isSitting = False
        print(self.name, "is", self.personality)
        print(self.name, "is Standing")
        print(self.name, "owns", self.robotOwned)



p1 = Person("Alice", "aggressive", False, r2)

p1.sit_down()


p2 = Person("Becky", "talkative", True, r1)

p2.stand_up()

