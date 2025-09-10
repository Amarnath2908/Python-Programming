def cou():
    s = "This is a sample101 code."
    c1,c2,c3 = 0,0,0
    for i in s:
        if i.isdigit():
            c1+=1
        elif i.isalpha():
            c2+=1
        else:
            c3+=1
    
    print(f"The no of digits is {c1} , no of alphabets is {c2} and the no of spl characters is {c3}")

cou()