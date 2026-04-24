def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

s = input()
print(count_vowels(s))

'''output:
Enter a string: Hello World
3
Enter a string: Python Programming
4
'''
