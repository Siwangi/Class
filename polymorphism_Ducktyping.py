class Duck:
    def talk(self):
        print("Quack, Quack")


class Human:
    def talk(self):
        print("Hello")

#below function invokes the talk method with whichever object we pass either its human or duck

def calltalk(obj):
    obj.talk()

#object 1

d = Duck()
calltalk(d)

#Object 2

h = Human()
calltalk(h)


""" Same function can do multiple things depending on what we pass in it """