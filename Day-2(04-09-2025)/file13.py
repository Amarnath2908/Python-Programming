def cou(n):
    c = 0
    while n > 0:
        c+=1
        n = n//10
    print("The count is :",c)
x = int(input("Enter a number:"))
cou(x)