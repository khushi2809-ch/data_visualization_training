s1 = input()
s2 = input()

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")

'''output:
Enter first string: listen
Enter second string: silent
Anagram
Enter first string: hello
Enter second string: world
Not Anagram
'''
