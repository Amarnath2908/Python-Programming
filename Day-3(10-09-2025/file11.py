def st():
    s = "AMARNATH"
    c = 0
    for i in s:
        c+=1
    print("The length of the string is",c)

    s1 = "amarnath"
    if s1 == s:
        print("Both are equal")
    else:
        print("Not equal")
    
    s2 = s + s1
    print(s2)
st()