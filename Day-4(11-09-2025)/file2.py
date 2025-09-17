class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def display(self):
        print("Name:",self.name)
        print("Roll no:",self.roll_no)
        print("Marks:",self.marks)

s1 = Student("Cepha",501,98)
s2 = Student("Amarnath",503,99)
s1.display()
s2.display()
