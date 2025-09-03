def fande(x):
    if x%5 == 0 and x%11 == 0:
        return "Divisible by both"
    else:
        return "Not divisible by both"

x = int(input("Enter num:"))
print(fande(x))