def freq():
    l = [1,3,54,223,5,1,12,5,22,54,54,54,54,54,54,54,54,54]
    li = []
    c = 0
    for x in l:
        if l.count(x) > 1 and x not in li:
            li.append(x)
    return f"The count of duplicate elements is {len(li)}"
print(freq())