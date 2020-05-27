class my_first_class:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def square(self):
        prod = 1
        count = 0
        while count < self.num2:
            prod = prod * self.num1
            count = count +1
        print(prod)
        return prod



number = my_first_class(6, 2)

number.square()

