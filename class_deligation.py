# class 1:


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduceSelf(self):
        print("My name is", self.name, ".")
        print("My color is", self.color, ".")
        print("My weight is", self.weight, ".")


# objects of class 1


r1=Robot("Tom", "Red", 30)

r2=Robot("Jerry", "Blue", 40)


# class 2


class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting

    def sit_down(self):
        self.isSitting  =True
        print(self.name, "is", self.personality)
        print(self.name, "is Sitting")

    def stand_up(self):
        self.isSitting = False
        print(self.name, "is", self.personality)
        print(self.name, "is Standing")


# objects of class 2


p1 = Person("Alice", "aggressive", False)

#using object of class 2 to call function of it


p1.sit_down()


# Case1: p1(object of class 2) owns r2(object of class 1), so that defines a new attribute to object 2 so set it to object 1

p1.robotOwned = r2

# If user want to call object 1 in 2


p1.robotOwned.introduceSelf()


# objects of class 2

p2=Person("Becky", "talkative", True)

#using object of class 2 to call function of it


p2.stand_up()

# Case2: p2(object of class 2) owns r1(object of class 1), so that defines a new attribute to object 2 so set it to object 1


p2.robotOwned = r1

# If user want to call object 1 in 2


p2.robotOwned.introduceSelf()
