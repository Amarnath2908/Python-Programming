def fandl(x):
    f = 0
    l = x%10
    while x>9:
        x = x//10
    f = x
    print(f"Sum is : {f+l}")

fandl(234)