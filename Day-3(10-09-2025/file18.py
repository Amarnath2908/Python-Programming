#Highest frequency of a character
def co():
    s = "amarnath"
    mc = 0
    mchar = ""
    for i in s:
        c = s.count(i)
        if c > mc:
            mc = c
            mchar = i
    print(f"The highest frequency character is: {mchar} and its count is : {mc}")

co() 