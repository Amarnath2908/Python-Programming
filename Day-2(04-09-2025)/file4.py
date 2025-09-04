def curr_bill(x):
    if x<=50:
        return x*3.8
    elif x >= 51 or x <=100:
        return (50*3.8)+((x-50)*4.2)
    elif x>=101 or x <= 200:
        return (50*3.8) + (50*4.2) + ((x-100)*5.1)
    elif x>=201 or x<=300:
        return (50*3.8) + (50*4.2) + (100*5.1) + ((x-200)*6.3)
    else:
        return (50*3.8) + (50*4.2) + (100*5.1) + (100*6.3) + ((x-300)*7.5)

x = int(input("Enter the units:"))
print(curr_bill(x))