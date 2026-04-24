s = input()

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)

'''output:
Enter a string: Hello World
Uppercase: 2
Lowercase: 8
Enter a string: Python Programming
Uppercase: 2
Lowercase: 18
'''
