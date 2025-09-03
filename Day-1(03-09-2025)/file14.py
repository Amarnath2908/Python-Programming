def check(x):
    if x > 0:
        return "Positive num"
    else:
        return "Negative num"
    
x = int(input("Enter num:"))
print(check(x))