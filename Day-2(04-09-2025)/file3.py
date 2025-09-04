def grade(m):
    if m >= 81:
        return "Distinction"
    elif m >= 71 and m <= 80:
        return "A grade"
    elif m >= 61 and m <= 70:
        return "B grade"
    elif m >= 51 and m <= 60:
        return "C grade"
    elif m >= 41 and m <= 50:
        return "pass"
    else:
        return "Fail"

x = int(input("Enter the marks:"))
print(grade(x))


















