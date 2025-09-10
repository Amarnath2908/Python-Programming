def c():
    l = [1,3,432,5,4,2,57,2,78]
    c1 = 0
    c2 = 0
    for x in l:
        if x%2==0:
            c1+=1
        else:
            c2+=1
    
    print(f"Even count is {c1} and Odd count is {c2}")

c()