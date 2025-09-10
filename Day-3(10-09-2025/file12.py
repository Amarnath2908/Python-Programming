def cou():
    l = ['a','e','i','o','u']
    s = "rhinocerous"
    c1,c2 =0, 0
    for i in s:
        if i in l:
            c1+=1
        else:
            c2+=1
    print(f"The no of vowels is {c1} and the consonants is {c2}")

cou()

