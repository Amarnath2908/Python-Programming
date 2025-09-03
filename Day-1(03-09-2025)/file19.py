def greater(a,b,c):
    if a>b:
        if a>c:
            return "a is bigger"
        else:
            return "c is bigger"
    else:
        return "b is bigger"

print(greater(50,40,60))