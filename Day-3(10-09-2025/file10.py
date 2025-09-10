def tup():
    t = ()
    s1 = [503,"Amar",95]
    s2 = [501,"Cepha",98]
    s3 = [543,"Siddhu",96]
    s4 = [511,"Dhanush",97]
    s5 = [506,"Baba",94]
    t = (s1,s2,s3,s4,s5)
    st = tuple(sorted(t, key=lambda x: x[2]))
    print(f"Name of the student who secured highest marks is {st[-1][1]}")

    for x in t:
        print(f"The name of the student {x[1]}, Roll no : {x[0]}, Marks secured: {x[2]}")
tup()