class Main:
    def __init__(self,num,den):
        self.num = num
        self.den = den
    def display(self):
        try:
            num = self.num/self.den
            print(num)
        except:
            print("Found an error")
        finally:
            print("Division is not possible")

d = Main(10,0)
d.display()

        