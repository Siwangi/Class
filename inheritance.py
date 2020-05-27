class Parent:
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name: ", self.last_name)
        print("Eye Color: ", self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)      #inherit the constructor from parent
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last name: ", self.last_name)
        print("Eye Color: ", self.eye_color)
        print("Number of toys:", str(self.number_of_toys))


" #Instance of Parent class "

billy_cyrus = Parent("cyrus", "blue")

" #def one more function in parent class and call it "
billy_cyrus.show_info()

print(billy_cyrus.last_name)


" #Instance of Child class "

miley_cyrus = Child("cyrus", "blue", 5)

"""Method Overriding"""
# Case 1 - If the show_info method/function is in parent & not child : Child class will call parent other functions(its not in child but can inherit from parent) :
# Case 2 - If the show info method/function is in child with added info, it will call child's info method and not the parent :

miley_cyrus.show_info()

print(miley_cyrus.last_name)

print(miley_cyrus.number_of_toys)


