s = input("Enter a string: ").lower()
count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print(count)
'''output:
Enter a string: Hello World
3
Enter a string: Python Programming
4
'''