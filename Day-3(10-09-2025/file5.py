def freq():
    l = [1,3,54,223,5,1,12,5,22,54]

    for x in l:
        c = 0
        for y in l:
            if x == y:
                c+=1
        print(f"The count of the {x} is {c}")
freq()