def pal(x):
    n = x
    s = 0
    while x > 0:
        r = x%10
        x = (x)//10
        s = (s*10) + r 
        
    if s == n:
        print("Its a palindrome")
    else:
        print("Its not a palindrome")
n = int(input("Enter a number:"))
pal(n)

