def sumofd(n):
    s = 0
    for digit in str(n):
        s += int(digit)
    return "Sum is", s

n = int(input("Enter a number:"))
print(sumofd(n))
