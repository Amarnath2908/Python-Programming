def prime(n):
    i=1
    c = 0
    while i<=n:
        if(n%i == 0):
            c+=1
        i+=1
    if c == 2:
        print("It is a prime number")
    else:
        print("Not a prime number")


prime(17)