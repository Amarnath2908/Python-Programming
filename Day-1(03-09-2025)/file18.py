def vandc(x):
    y = ['a','e','i','o','u']
    if x in y:
        return "Vowel"
    else:
        return "Consonant"

x = input("Enter the alphabet:")
print(vandc(x))