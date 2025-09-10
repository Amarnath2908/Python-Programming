def search(n):
    s = "This is a string"
    c = 0
    for i in s:
        if i == n:
            c+=1
    print("The count of occurences of a character is :",c)

search('i')