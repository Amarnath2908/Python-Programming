def ecomm():
    l = []
    while True:
        x = int(input("Enter an operation:"))
        match(x):
            case 1:
                item = (input("Enter the item to add into the cart:"))
                l.append(item)
                print("Added an item")
            case 2:
                item = (input("Enter an item to remove from the cart:"))
                l.remove(item)
                print("Removed an item")
            case 3:
                item = (input("Enter an element to search:"))
                if item in l:
                    print("Element is found in the cart")
                else:
                    print("ELement is not cart")
            case 4:
                for x in l:
                    print(x)
            case 5:
                print(f"The count of the cart is {len(l)}")
            case 6:
                l.sort()
                print("Sorted cart is",l)
            case 7:
                l.clear()
                print("The cart is cleared")
            case 8:
                print("Exited from the cart")
                break
            case _:
                print("Enter valid operation")
ecomm()



