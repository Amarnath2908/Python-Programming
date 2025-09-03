cn = input("Enter the name:")
cnum = int(input("Enter the number:"))
pmr = int(input("Enter the present month reading:"))
lmr = int(input("Enter the last month reading:"))

c = (pmr-lmr)*3.80

print(f"Customer name: {cn}\nCustomer number: {cnum}\nPresent month reading: {pmr}\nLast month reading : {lmr}\ntotal no. of units : {pmr-lmr}\ntotal cost : {c}")