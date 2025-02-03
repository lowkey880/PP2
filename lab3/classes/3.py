class Shape:

    def __init__(self):

        pass

    def area(self):

        return 0

class Rectangle(Shape):

    def __init__(self, length, width):  

        self.length = length

        self.width = width

    def area(self):

        return self.length * self.width 

a = int(input("Write a length of rectangle: "))

b = int(input("Write a width of rectangle: "))

rectangle = Rectangle(a, b)

print("Rectangle area is:", rectangle.area())  