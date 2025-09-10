def dict_opt():
    d = {}
    while True:
        x = int(input("Enter the operation:"))
        match x:
            case 1:
                x1 = int(input("Enter BOOK-Id:"))
                x2 = input("Enter the book title:")
                d[x1] = x2
                print("The element is added")
            case 2:
                x1 = int(input("Enter the Book-Id to remove:"))
                d.pop(x1)
                print("The item is deleted")
            case 3:
                x1 = int(input("Enter the book-id to search:"))
                print("The book title for the given Id is:",d.get(x1))
            case 4:
                x1 = int(input("Enter a Book-Id to update:"))
                x2 = input("Enter the Book title:")
                d[x1] = x2
                print("The title is updated")
            case 5:
                    for k, v in d.items():
                        print(f"ID: {k} → Title: {v}")
            case 6:
                print("The total no of books in the library are:",len(d))
            case 7:
                x2 = input("Enter the book title to search:").lower()
                if any(x2 == x3.lower() for x3 in d.values()):
                    print("Book exists in the library")
                else:
                    print("Book does not exists in the library")
            case 8:
                print("Exited")
                break
            case _:
                print("Please enter a valid operation")        
dict_opt()




