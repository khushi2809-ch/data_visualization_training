ch = input("Enter a character: ")

if ch.isdigit():
    print("Digit")
elif ch.isalpha():
    print("Alphabet")
else:
    print("Special Character")

'''output:
Enter a character: 5
Digit
Enter a character: a
Alphabet
Enter a character: @
Special Character
'''
