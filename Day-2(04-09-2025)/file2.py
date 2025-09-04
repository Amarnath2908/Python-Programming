def check(x):
    if x >='a' and x <= 'z' or x<='A' and x>='Z':
        return "It is a alphabet"
    elif x >= '0' and x <= '9':
        return "It is a digit"
    else:
        return "It is a special character"
    
y = (input("Enter the input:"))
print(check(y))