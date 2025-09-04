def arms(x):
    n = x
    s = 0
    while x > 0:
        r = x%10
        s = s + (r**3)
        x = x//10
    if s == n:
        print("Its an armstrong number")
    else:
        print("Not an armstrong number")

n = int(input("Enter a number:"))
arms(n)