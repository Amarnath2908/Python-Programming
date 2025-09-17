from abc import ABC,abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass

class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        print("The area of the rectangle :",self.l*self.b)

class Circle:
    def __init__(self,r):
        self.r = r
    def area(self):
        print("The area of the circle:",(3.14*self.r*self.r))

r1 = Rectangle(10,20)
r1.area()

c1 = Circle(10)
c1.area()