def pat1(n):
    for i in range(n):
        for j in range(n):
            if (i == j):
                print('$',end = " ")
            elif (i+j == n-1):    
                print('$',end = " ")
            else:
                print('*',end = " ")
        print()

n = int(input("Enter a number:"))
pat1(n)