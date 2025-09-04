def prime(n):
    for i in range(2,n):
        c = 0
        for j in range(1,n+1):
            if i%j == 0:
                c += 1 
        if c == 2:
            print(i)

n = int(input("Enter a number:"))
prime(n)