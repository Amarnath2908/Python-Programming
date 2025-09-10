#SECOND LARGEST ELEMENT IN THE LIST

def sec():
    l = [1,53,12,64,237,647,23,1465,23,86]
    l.sort()
    return f"Second largest element in the list is {l[-2]}"

print(sec())