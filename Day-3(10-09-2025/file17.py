def co():
    s = "this is a string"
    s1 = ""
    for i in s.strip():
        if i not in s1:
            s1 = s1 + i + str(s.count(i))

    print(s1)

co() 


