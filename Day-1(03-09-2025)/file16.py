def leap(y):
    if y%4 == 0 or y%100==0 or y%400 ==0:
        return "Leap year"
    else:
        return "Not a leap year"

y = int(input("Enter the year:"))
print(leap(y))