class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

class Manager(Employee):
    def __init__(self, name, salary,dept):
        super().__init__(name, salary)
        self.dept = dept
    def display(self):
        super().display()
        print("Department:",self.dept)

e1 = Employee("Cepha",50000)
e1.display()
m1 = Manager("Amarnath",60000,"IT")
m1.display()


         