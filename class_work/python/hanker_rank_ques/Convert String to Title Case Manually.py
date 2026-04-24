s = input()
result = ""
new_word = True

for ch in s:
    if ch == " ":
        result += ch
        new_word = True
    else:
        if new_word:
            result += ch.upper()
            new_word = False
        else:
            result += ch.lower()

print(result)

'''output:
Enter a string: hello world
Hello World
Enter a string: python programming
Python Programming
'''
