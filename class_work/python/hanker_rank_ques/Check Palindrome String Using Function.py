def is_palindrome(s):
    return s == s[::-1]

s = input()

if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")

'''output:
Enter a string: madam
Palindrome
Enter a string: hello
Not Palindrome
'''
