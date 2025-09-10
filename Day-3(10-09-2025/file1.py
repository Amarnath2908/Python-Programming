#CREATE AN EMPTY LIST
l = []

#ADD ELEMENTS INTO THE LIST
l.append(1)
l.append(2)
l.append(3)
l.insert(0,9)

#REMOVE ELEMENTS BASED ON INDEX AND VALUE
l.remove(9)
l.pop(2)

#SEARCH OPERATION
l.index(2)


l.append(4)
l.append(5)
l.append(6)

#UPDATION
l[2] = 3
l[4] = 7

#DELETE 
del l[0]

#SLICING
print(l)
print(l[0:2])

#ADDING -VE ELEMENTS INTO THE LIST
l.append(-1)
l.append(-2)
l.append(-5)

#DISPLAY NEGATIVE ELEMENTS IN THE LIST
for x in l:
    if x<0:
        print(x)

