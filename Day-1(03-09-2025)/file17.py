def checkalpha(a):
    if 'a' <= a and a <= 'z':
        return "Alphabet"
    else:
        return "Not a alphabet"

a = input("Enter the alphabet:")
print(checkalpha(a))
