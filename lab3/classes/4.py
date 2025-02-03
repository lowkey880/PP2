import math

class Point:

    def __init__(self, x, y):

        self.x = x

        self.y = y

    def show(self):

        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):

        self.x = new_x
        
        self.y = new_y

    def dist(self, other_point):

        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

a_1 = int(input("Write x: "))

b_1 = int(input("Write y: "))

p1 = Point(a_1, b_1)

c = int(input("Write another x: "))

d = int(input("Write another y: "))

p2 = Point(c, d)

p1.show()  
p2.show()  

a_2 = int(input("Write new x: "))

b_2 = int(input("Write new y: "))

p1.move(a_2, b_2)
p1.show()

print("Distance between points:", p1.dist(p2)) 