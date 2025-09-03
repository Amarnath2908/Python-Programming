def conv(d):
    y = (int)(d/365)
    x = d - (y*365)
    m = x/30
    print(f"No of years: {y}\nNo of months: {round(m,2)}")
a = 1232
conv(a)