def st_num(n):
    s = 0
    x = n
    while n > 0:
        r = n%10
        f = 1
        while r > 0:
            f = f*r
            r -= 1
        s = s + f
        n = n//10
    if s == x:
        print("Its a strong num")
    else:
        print("Its not a strong num")

n = int(input("Enter a number:"))
st_num(n)


