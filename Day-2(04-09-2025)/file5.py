def curr(x):
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    
    c1 = x//100
    x = x%100
    c2 = x//50
    x = x%50
    c3 = x//20
    x = x%20
    c4 = x//10
    x = x%10
    c5 = x//5
    x = x%5
    c6 = x//2
    x = x%2
    c7 = x//1

    c = c1+ c2+ c3+ c4+ c5+ c6+ c7
    print(c)

x = int(input("Enter the amount:"))
curr(x)