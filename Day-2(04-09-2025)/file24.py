def per(n):
    s = 0
    for i in range(1,n):
        if n%i == 0:
            s = s + i
    if s == n:
        print("Its a perfect number")
    else:
        print("Its not a perfect number")
n = int(input("Enter a number:"))
per(n)