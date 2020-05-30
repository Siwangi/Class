class Prime:
    def __init__(self, num):
        self.num=num

    def function(self):
        sum=0
        count=1
        while count <= self.num:
            if self.num % count == 0:
                sum=sum + 1
            count=count + 1
        if sum == 2:
            print("prime")
        else:
            print("not prime")


prime = Prime(5)

prime.function()
