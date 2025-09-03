sid = int(input("Enter the roll no:"))
sname = input("Enter the name:")
m = int(input("Enter the maths marks:"))
p = int(input("Enter the physics marks:"))
c = int(input("Enter the chemistry marks:"))
t = m+p+c
print("Total:",t)
print("Average:",t/3)
print(f"Name : {sname}, Roll no: {sid},total marks: {t},average: {t/3}")
