def delete(n):
    l = [1,431,21,54,4,31,34,12,54]

    if l[n] == l[0]:
        l[0] = l[1]
    elif n+1 == len(l):
        l[n] = l[len(l)-1]
    if l[n] in l:
        l[n-1] = l[n+1]
    
    print(l)

delete(8)





def delete(n):
    l = [1, 431, 21, 54, 4, 31, 34, 12, 54]
    if 0 <= n < len(l):
        del l[n]
    print(l)

delete(8)