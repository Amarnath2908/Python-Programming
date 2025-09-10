def search(a):
    s = "This is a string"
    l = []
    for x in s.split(" "):
        if a in x:
            l.append(x)

    for x in l:
        print(x)
search("is") 
