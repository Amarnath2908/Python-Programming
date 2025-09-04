def arms(n):
    for i in range(1,n+1):
        s = 0
        x = i 
        temp = i
        while temp > 0:
            r = temp%10
            s = s + (r**3)
            temp = temp//10
        if s == x:
            print(i)
n = int(input("Enter a number:"))
arms(n)






