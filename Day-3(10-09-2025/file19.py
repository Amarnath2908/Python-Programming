#Lowest frequency of a character
def co():
    s = "sssssmmmmmswwddddd"
    mc = 100000
    mchar = ""
    for i in s:
        c = s.count(i)
        if c < mc:
            mc = c
            mchar = i
    print(f"The Lowest frequency character is: {mchar} and its count is : {mc}")

co()