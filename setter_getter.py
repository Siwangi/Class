class Programmer:
    def setName(self, shivi):
        self.name = shivi

    def getName(self):
        return self.name

    def setSalary(self, amt):
        self.salary = amt

    def getSalary(self):
        return self.salary


p1 = Programmer()

p1.setName("shivi")    #setter or mutator method
p1.setSalary(1000)

print(p1.getName())       #getter or accessor method
print(p1.getSalary())



